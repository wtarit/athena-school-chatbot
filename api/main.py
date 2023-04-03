from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from genflex import *
from dotenv import load_dotenv
import json
import os

load_dotenv()

# Use a service account
service_acc = json.loads(os.environ.get("FIREBASE_SERVICE_ACCOUNT_KEY"))
cred = credentials.Certificate(service_acc)
firebase_admin.initialize_app(cred)

firestoredb = firestore.client()

app = FastAPI()

origins = [
    "https://login.teamathena.ml",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"status": "working!"}


class Authorize(BaseModel):
    role: str
    userID: str
    studentID: str
    password: str


@app.post("/login")
def login(authorize: Authorize, response: Response):
    if authorize.role == "Teacher":
        main_db_ref = firestoredb.collection(
            "teachers").document(authorize.studentID)
    else:
        main_db_ref = firestoredb.collection(
            "users").document(authorize.studentID)
    doc = main_db_ref.get()
    if not doc.exists:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"status": "unauthorized"}
    if doc.get("password") != authorize.password:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"status": "unauthorized"}

    doc_ref = firestoredb.collection(
        "userIDmapping").document(authorize.userID)
    doc_ref.set(
        {
            "role": authorize.role,
            "ref": main_db_ref,
            "ID": authorize.studentID,
        }
    )
    return {"status": "authorized"}


class UserID(BaseModel):
    userID: str


@app.post("/loginintent")
def loginintent(userid: UserID, response: Response):
    userid_ref = firestoredb.collection(
        "userIDmapping").document(userid.userID)
    userid_doc = userid_ref.get()
    if userid_doc.exists:
        response.headers["Response-Type"] = "intent"
        if userid_doc.to_dict()["role"] == "Teacher":
            return {"intent": "IN_login_teacher_success"}
        return {"intent": "IN_login_student_success"}
    response.headers["Response-Type"] = "object"
    return {
        "line_payload": [
            {
                "type": "text",
                "text": "Please login at https://liff.line.me/1656986385-kPOKbx8a",
            },
        ]
    }


@app.post("/classtimetable")
def class_timetable(userid: UserID, response: Response):
    doc_ref = firestoredb.collection("userIDmapping").document(userid.userID)
    doc = doc_ref.get()
    response.headers["Response-Type"] = "object"
    if not doc.exists:
        return {
            "line_payload": [
                {
                    "type": "text",
                    "text": "Please login at https://liff.line.me/1656986385-kPOKbx8a",
                },
            ]
        }
    doc = doc.to_dict()
    user_doc = doc["ref"].get().to_dict()
    if doc["role"] == "Student":
        grade = user_doc["room"]
        time_table_doc_name = grade.replace("/", "")
        doc_ref = firestoredb.collection(
            "room_detail").document(time_table_doc_name)
        doc = doc_ref.get().to_dict()
        return {
            "line_payload": [
                {
                    "type": "image",
                    "originalContentUrl": doc["timetable"],
                    "previewImageUrl": doc["timetable"],
                }
            ]
        }
    return {
        "line_payload": [
            {
                "type": "image",
                "originalContentUrl": user_doc["teaching_timetable"],
                "previewImageUrl": user_doc["teaching_timetable"],
            }
        ]
    }


@app.post("/student/aboutme")
def student_aboutme(userid: UserID, response: Response):
    doc_ref = firestoredb.collection("userIDmapping").document(userid.userID)
    doc = doc_ref.get().to_dict()
    student_doc = doc["ref"].get().to_dict()
    flex_content = aboutme_flex(student_doc)
    response.headers["Response-Type"] = "object"
    return {
        "line_payload": [
            {
                "type": "flex",
                "altText": "ประวัติส่วนตัว",
                "contents": flex_content,
            }
        ],
    }


@app.post("/library")
def library(userid: UserID, response: Response):
    doc_ref = firestoredb.collection("userIDmapping").document(userid.userID)
    doc = doc_ref.get().to_dict()
    if doc["role"] == "Teacher":
        db_keys = f"T{doc['ID']}"
    else:
        db_keys = f"S{doc['ID']}"
    library_doc_ref = firestoredb.collection("library").document(db_keys)
    library_doc = library_doc_ref.get()
    response.headers["Response-Type"] = "object"
    if not library_doc.exists:
        return {
            "line_payload": [
                {
                    "type": "text",
                    "text": "คุณไม่ได้ยืมหนังสือไว้ค่ะ",
                },
            ]
        }
    library_doc = library_doc.to_dict()
    ans_text = "คุณต้องคืนหนังสือเรื่อง\n"
    remaining_book = library_doc["book_to_return"]
    for i, book in enumerate(remaining_book):
        ans_text += f"""{i+1}. {book["name"]}\n"""
    ans_text += "ภายในวันที่ " + \
        remaining_book[0]["return_date"].strftime("%d/%m/%Y")
    return {
        "line_payload": [
            {
                "type": "text",
                "text": ans_text,
            },
        ]
    }


@app.post("/teacher/getstudentname")
def getstudentname(userid: UserID, response: Response):
    doc_ref = firestoredb.collection("userIDmapping").document(userid.userID)
    doc = doc_ref.get()
    doc_data = doc.to_dict()
    response.headers["Response-Type"] = "object"
    if not doc.exists or doc_data["role"] == "Student":
        return {
            "line_payload": [
                {
                    "type": "text",
                    "text": "Unauthorized",
                },
            ]
        }
    teacher_doc = doc_data["ref"].get().to_dict()
    mainclass = teacher_doc["main_class"]["room"]
    mainclass_id = mainclass.replace("/", "")
    namelist_doc_ref = firestoredb.collection(
        "room_detail").document(mainclass_id)
    namelist_doc = namelist_doc_ref.get().to_dict()
    main_namelsit_doc_ref = firestoredb.collection(
        "room_detail").document(teacher_doc["main_grade"])
    main_namelsit_doc = main_namelsit_doc_ref.get().to_dict()
    flex_content = studentnamelist_flex(
        mainclass, teacher_doc["main_grade"], namelist_doc["namelist_xlsx"], namelist_doc["namelist_pdf"], main_namelsit_doc["namelist_all"])
    return {
        "line_payload": [
            {
                "type": "flex",
                "altText": "ใบรายชื่อ",
                "contents": flex_content,
            }
        ],
    }


@app.post("/getname")
def getname(userid: UserID):
    doc_ref = firestoredb.collection("userIDmapping").document(userid.userID)
    doc = doc_ref.get()
    doc_data = doc.to_dict()
    userdata = doc_data["ref"].get().to_dict()
    return {"name": userdata["name"]}


@app.post("/student/getdocs")
def getdocs(userid: UserID, response: Response):
    doc_ref = firestoredb.collection("userIDmapping").document(userid.userID)
    doc = doc_ref.get()
    doc_data = doc.to_dict()
    response.headers["Response-Type"] = "object"
    if not doc.exists or doc_data["role"] == "Teacher":
        return {
            "line_payload": [
                {
                    "type": "text",
                    "text": "การขอใบปพ.สามารถขอได้เฉพาะนักเรียน",
                },
            ]
        }
    student_doc = doc_data["ref"].get().to_dict()
    flex_content = studentdoc_flex(student_doc["ปพ.1"], student_doc["ปพ.7"])
    return {
        "line_payload": [
            {
                "type": "flex",
                "altText": "ใบปพ.",
                "contents": flex_content,
            }
        ],
    }


@app.post("/viewgrade")
def viewgrade(userid: UserID, response: Response):
    doc_ref = firestoredb.collection("userIDmapping").document(userid.userID)
    doc = doc_ref.get()
    doc_data = doc.to_dict()
    response.headers["Response-Type"] = "object"
    if not doc.exists or doc_data["role"] == "Teacher":
        return {
            "line_payload": [
                {
                    "type": "text",
                    "text": "การขอดูคะแนนสามารถขอได้เฉพาะนักเรียน",
                },
            ]
        }
    student_doc = doc_data["ref"].get().to_dict()
    flex_content = grade_flex(student_doc["grade"])
    return {
        "line_payload": [
            {
                "type": "flex",
                "altText": "รายงานผลการเรียน",
                "contents": flex_content,
            }
        ],
    }
