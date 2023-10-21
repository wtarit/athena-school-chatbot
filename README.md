[ไทย](https://github.com/wtarit/athena-school-chatbot/blob/main/README_th.md)
# N'Hilight chatbot   
N'Hilight is a Line chatbot that assists students and faculty members in school. It can be used by students, teachers, and outside parties.  

Introductory video (Thai)  
[![IMAGE ALT TEXT](https://img.youtube.com/vi/hb0PVw82esA/0.jpg)](https://www.youtube.com/watch?v=hb0PVw82esA "BOTNOI Chatbot Mara-Hackathon : Athena 🤖💫")

**Note**

1. To test the chatbot, add Line ID: @518fquks  
2. For testing functions that require logging in, you can use the following credentials 
    Student  
    User: 10001  
    Password: pass  

    Teacher  
    User: 10000  
    Password: password  

To change an account, type Logout into the chatbot to Log out of an account.   

## Technical Detail 
The API is written in Python using FastAPI and Firebase Firestore for storing user data. Currently, the API is hosted on Vercel (Previously, it was on Google App Engine, so `app.yaml` is still included for reference in the repository).  

To run the project
1. Create Firebase Project, enable Firestore and download the service account file.
2. Copy content of the service account JSON file into `FIREBASE_SERVICE_ACCOUNT_KEY` in `.env` file
3. run `pip install -r requirement.txt` to install all the dependencies  
4. Run the server using  
```bash
uvicorn main:app
```
 
Note: To use the API through BOTNOI chatbot platform when running API on a local machine, you may need to use a tunneling service (e.g. ngrok, Cloudflare Tunnel) to make API accessible outside local network.

For the login page, we created a Liff App hosted on Github Pages. To make the backend accept requests from the login page, you must set CORS origin by putting your URL into `LOGIN_URL` in `.env` file. [(reference)](https://fastapi.tiangolo.com/tutorial/cors/)

## How the login system work
We used the Liff app to log users in, which can collect Line UserID and send Messages into Line chat.  

1. We created a login form that collects Line UserID when users submit the form. If the user login successfully, we save the UserID into the database and send "Login" message into the chat. 
2. In BOTNOI Platform, create an intent to check for "Login" keyword and call an API to check if the UserID is in the database.
3. If the UserID matches, the API will return another Intent that will change the Rich Menu. (Since API can't directly return Rich Menu object, we have to do it through an intent.)
