import os, json, requests, datetime, time, sys
from dotenv import load_dotenv

# 事前処理
session = requests.Session()

# 最初のログイン遷移
url_signin = "https://www.task-asp.net/cu/ykd402303/Top"
headers = {
    "Connection": "keep-alive",
    "Content-Length": "22984",
    "Cache-Control": "max-age=0",
    "Origin": "https://www.task-asp.net",
    "Upgrade-Insecure-Requests": "1",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://www.task-asp.net/cu/ykd402303/Top",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ja",
    "Cookie": "taskasp_cu_ykd_starturl=%2fcu%2feg%2fykd402303.task; taskasp_cu_ykd_sppage=1; taskasp_cu_ykd_sessionid=adufsolgpg2o1rz3d4ug5tsn",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "Android",
    "Sec-GPC": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
}

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
login_info = {
    # "username": username,
    # "password": password
    "ctl00$LoginContentPlaceHolder$UserLoginCtr$UserNoTextBox": username,
    "ctl00$LoginContentPlaceHolder$UserLoginCtr$PasswordTextBox": password
}
data = json.dumps(login_info)
res = session.post(url_signin, headers=headers, data=data)

print(res.status_code)

# ログイン後の遷移
