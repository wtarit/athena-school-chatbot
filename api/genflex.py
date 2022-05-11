def aboutme_flex(detail: dict):
    flex = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": detail["image"],
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {"type": "uri", "uri": detail["image"]},
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": detail["name"],
                    "weight": "bold",
                    "size": "xl",
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "ระดับชั้น",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1,
                                },
                                {
                                    "type": "text",
                                    "text": detail["room"],
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 3,
                                },
                            ],
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "อายุ",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1,
                                },
                                {
                                    "type": "text",
                                    "text": str(detail["age"]),
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 3,
                                },
                            ],
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "วันเกิด",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1,
                                },
                                {
                                    "type": "text",
                                    "text": detail["birthday"].strftime("%d/%m/%Y"),
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 3,
                                },
                            ],
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "กรุ๊ปเลือด",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1,
                                },
                                {
                                    "type": "text",
                                    "text": detail["bloodgroup"],
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 3,
                                },
                            ],
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "ศาสนา",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1,
                                },
                                {
                                    "type": "text",
                                    "text": detail["religion"],
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 3,
                                },
                            ],
                        },
                    ],
                },
            ],
        },
    }
    return flex


def studentnamelist_flex(
    mainclass: str, maingrade: str, main_xlsx: str, main_pdf: str, maingrade_link: str
):
    flex = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "ใบรายชื่อที่ต้องการ",
                    "size": "xl",
                    "weight": "bold",
                },
                {"type": "separator", "color": "#111111"},
                {
                    "type": "text",
                    "text": f"ห้อง{mainclass}",
                    "weight": "bold",
                    "size": "lg",
                    "offsetTop": "md",
                    "offsetBottom": "xxl",
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "uri",
                                "label": "Excel",
                                "uri": main_xlsx,
                            },
                            "style": "secondary",
                        },
                        {
                            "type": "button",
                            "action": {"type": "uri", "label": "PDF", "uri": main_pdf},
                            "style": "secondary",
                        },
                    ],
                    "spacing": "sm",
                    "offsetTop": "lg",
                    "action": {"type": "postback", "label": "action", "data": "hello"},
                },
            ],
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "uri",
                        "label": f"ระดับชั้น{maingrade}",
                        "uri": maingrade_link,
                    },
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "uri",
                        "label": "ระดับชั้นอื่น ๆ",
                        "uri": "https://drive.google.com/drive/folders/1a7XVX8lAwUEvmhr-8kGcyDKAswss8isl?usp=sharing",
                    },
                },
            ],
            "flex": 0,
            "borderWidth": "none",
        },
    }
    return flex


def studentdoc_flex(url1: str, url7: str):
    flex = {
        "type": "bubble",
        "body": {
            "contents": [
                {"size": "xl", "text": "Download", "type": "text", "weight": "bold"},
                {"color": "#111111", "type": "separator"},
                {
                    "action": {"data": "hello", "label": "action", "type": "postback"},
                    "contents": [
                        {
                            "action": {"label": "ปพ.1", "type": "uri", "uri": url1},
                            "style": "secondary",
                            "type": "button",
                        },
                        {
                            "action": {"label": "ปพ.7", "type": "uri", "uri": url7},
                            "style": "secondary",
                            "type": "button",
                        },
                    ],
                    "layout": "horizontal",
                    "offsetTop": "lg",
                    "spacing": "sm",
                    "type": "box",
                },
            ],
            "layout": "vertical",
            "type": "box",
        },
    }
    return flex


def grade_flex(grade_data: dict):
    flex = {
        "type": "bubble",
        "body": {
            "contents": [
                {
                    "size": "xl",
                    "text": "ผลการเรียนที่ต้องการ",
                    "type": "text",
                    "weight": "bold",
                },
                {"color": "#111111", "type": "separator"},
                {
                    "offsetBottom": "xxl",
                    "offsetTop": "md",
                    "size": "lg",
                    "text": "ม.4",
                    "type": "text",
                    "weight": "bold",
                },
                {
                    "action": {"data": "hello", "label": "action", "type": "postback"},
                    "contents": [
                        {
                            "action": {
                                "label": "เทอม 1",
                                "type": "uri",
                                "uri": grade_data["m4t1"],
                            },
                            "style": "secondary",
                            "type": "button",
                        },
                        {
                            "action": {
                                "label": "เทอม 2",
                                "type": "uri",
                                "uri": grade_data["m4t2"],
                            },
                            "style": "secondary",
                            "type": "button",
                        },
                    ],
                    "layout": "horizontal",
                    "offsetTop": "lg",
                    "spacing": "sm",
                    "type": "box",
                },
                {
                    "offsetBottom": "xxl",
                    "offsetTop": "xxl",
                    "size": "lg",
                    "text": "ม.5",
                    "type": "text",
                    "weight": "bold",
                },
                {
                    "action": {"data": "hello", "label": "action", "type": "postback"},
                    "contents": [
                        {
                            "action": {
                                "label": "เทอม 1",
                                "type": "uri",
                                "uri": grade_data["m5t1"],
                            },
                            "style": "secondary",
                            "type": "button",
                        },
                        {
                            "action": {
                                "label": "เทอม 2",
                                "type": "uri",
                                "uri": grade_data["m5t2"],
                            },
                            "style": "secondary",
                            "type": "button",
                        },
                    ],
                    "layout": "horizontal",
                    "offsetTop": "xxl",
                    "spacing": "sm",
                    "type": "box",
                },
                {
                    "contents": [],
                    "flex": 1,
                    "height": "20px",
                    "layout": "vertical",
                    "type": "box",
                },
            ],
            "layout": "vertical",
            "type": "box",
        },
    }
    return flex
