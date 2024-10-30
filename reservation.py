import requests, os
from dotenv import load_dotenv

session = requests.Session()
load_dotenv()

login_url = "https://www.task-asp.net/cu/ykd402303/Top"
# login_url = "https://www.task-asp.net/cu/ykd402303/Information"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ja;q=0.6",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "taskasp_cu_ykd_starturl=%2fcu%2feg%2fykd402303.task; taskasp_cu_ykd_sppage=1; taskasp_cu_ykd_sessionid=qdn335ec5lrsdevtdphaie5w; taskasp_cu_ykr_sessionid=gmtlwzd4jtmssnqjxfi1e3bf",
    "Origin": "https://www.task-asp.net",
    "Referer": "https://www.task-asp.net/cu/ykd402303/Top",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Sec-GPC": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
}
payload = {
    "__EVENTTARGET": os.getenv("EVENTTARGET"),
    "__EVENTARGUMENT": os.getenv("EVENTARGUMENT"),
    "__VIEWSTATE": os.getenv("VIEWSTATE"),
    "__VIEWSTATEGENERATOR": os.getenv("VIEWSTATEGENERATOR"),
    "__EVENTVALIDATION": os.getenv("EVENTVALIDATION"),
    "ctl00$LoginContentPlaceHolder$UserLoginCtr$UserNoTextBox": os.getenv("USERNAME"),
    "ctl00$LoginContentPlaceHolder$UserLoginCtr$PasswordTextBox": os.getenv("PASSWORD"),
}

login_res = session.post(login_url, headers=headers, data=payload)
print(f"ログインの確認: {login_res.status_code}")
print(f"res_signinの結果:\n {login_res.text}")