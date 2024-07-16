import os, json, requests, datetime, time, sys, dateutil
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
sendingInfo = {
    "ctl00$LoginContentPlaceHolder$UserLoginCtr$UserNoTextBox": username,
    "ctl00$LoginContentPlaceHolder$UserLoginCtr$PasswordTextBox": password
}
data = json.dumps(sendingInfo)
res = session.post(url_signin, headers=headers, data=data)

print(f"ログインの確認: {res.status_code}")

# ログイン後の遷移(日時・施設名・競技選択)

# ************日付の設定***************
now = datetime.date.today()


# ログイン後の遷移（時間と内容記述）
url_details = "https://www.task-asp.net/cu/ykd402303/Order/Input"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ja;q=0.5",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "19424",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "taskasp_cu_ykd_starturl=%2fcu%2feg%2fykd402303.task; taskasp_cu_ykd_auth=256501A96458B193A293BE98B538AC81B0FA3892CBB2466A6355DDC41F8839E38E964F59D498EB362344496D7C6C1225042EE473CE7096007280E1241C043952296E2127C6969F04D1E019DDD97281E61AACE5C2CB7A4E21027AAA7003CF40F20B1F3F61EE65E5B4817A729E2DC0D4BFD72E1767F368B7E1BBB29707239DD1A25476957D5FBAE24C785697FA6902634A; taskasp_cu_ykd_sppage=1; taskasp_cu_ykd_sessionid=qdn335ec5lrsdevtdphaie5w; taskasp_cu_ykr_sessionid=gmtlwzd4jtmssnqjxfi1e3bf",
    "Host": "www.task-asp.net",
    "Origin": "https://www.task-asp.net",
    "Referer": "https://www.task-asp.net/cu/ykd402303/Order/Input",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Brave\";v=\"126\"",
    "Sec-Ch-Ua-Mobile": "?1",
    "Sec-Ch-Ua-Platform": "\"Android\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
}

sendingInfo = {
    "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_16: 1700:1730:1",
    "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_17: 1730:1800:1",
    "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_18: 1800:1830:1",
    "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_19: 1830:1900:1",
    "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_20: 1900:1930:1",
    "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_21: 1930:2000:1",
    "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_22: 2000:2030:1",
    "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_23: 2030:2100:1",
    "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_24: 2100:2130:1",
    "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_25: 2130:2200:1",
    "ctl00$MainContentPlaceHolder$InputUC$SekininsyaSeiTextBox: 厚地",
    "ctl00$MainContentPlaceHolder$InputUC$SekininsyaMeiTextBox: 俊哉",
    "ctl00$MainContentPlaceHolder$InputUC$UseClassDropDownList: 216",
    "ctl00$MainContentPlaceHolder$InputUC$GyouziNameTextBox: サークル利用",
    "ctl00$MainContentPlaceHolder$InputUC$NinzuuTotalTextBox: 14"
}
data = json.dump(sendingInfo)
res = session.post(url_details, headers=headers, data=data)