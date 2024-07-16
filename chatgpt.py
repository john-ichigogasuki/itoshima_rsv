import os, requests
from dotenv import load_dotenv

# 事前処理
session = requests.Session()

# 環境変数のロード
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
login_info = {
    "username": username,
    "password": password
}

# 最初のログイン遷移
url_signin = "https://www.task-asp.net/cu/ykd402303/Top"
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
}
res = session.post(url_signin, headers=headers, data=login_info)

print(res.status_code)
print(res.text)