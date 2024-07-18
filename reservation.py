import os, json, requests, datetime, time, sys
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv

# 事前処理
session = requests.Session()

# 最初のログイン遷移
url_signin = "https://www.task-asp.net/cu/ykd402303/Top"
response = session.get(url_signin)

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
    # "Cookie": "taskasp_cu_ykd_starturl=%2fcu%2feg%2fykd402303.task; taskasp_cu_ykd_sppage=1; taskasp_cu_ykd_sessionid=adufsolgpg2o1rz3d4ug5tsn",
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
res_signin = session.post(url_signin, headers=headers, data=data)

print(f"ログインの確認: {res_signin.status_code}")
print(f"res_signinの結果: {res_signin.text}")

# # ログイン後の遷移(日時・施設名・競技選択)
# url_choice = "https://www.task-asp.net/cu/ykd402303/Order/List"

# # ************日付の設定***************
# todayDate = datetime.date.today()
# targetDate = todayDate + relativedelta(months=3)
# targetDate_formatted = targetDate.strftime("%Y%m%d")
# targetDate_previous = todayDate + relativedelta(months=2)
# targetDate_previous_formatted = targetDate_previous.strftime("%Y%m%d")
# targetDate_next = todayDate + relativedelta(months=4)
# targetDate_next_formatted = targetDate_next.strftime("%Y%m%d")
# wareki = datetime.date.today().year - 2018
# wareki_formatted =str(50)+str(wareki)+str(targetDate.strftime("%m%d"))
# # ***********************************

# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "ja;q=0.5",
#     "Cache-Control": "max-age=0",
#     "Connection": "keep-alive",
#     "Content-Length": "47899",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Cookie": "taskasp_cu_ykd_starturl=%2fcu%2feg%2fykd402303.task; taskasp_cu_ykd_auth=256501A96458B193A293BE98B538AC81B0FA3892CBB2466A6355DDC41F8839E38E964F59D498EB362344496D7C6C1225042EE473CE7096007280E1241C043952296E2127C6969F04D1E019DDD97281E61AACE5C2CB7A4E21027AAA7003CF40F20B1F3F61EE65E5B4817A729E2DC0D4BFD72E1767F368B7E1BBB29707239DD1A25476957D5FBAE24C785697FA6902634A; taskasp_cu_ykd_sppage=1; taskasp_cu_ykd_sessionid=qdn335ec5lrsdevtdphaie5w; taskasp_cu_ykr_sessionid=gmtlwzd4jtmssnqjxfi1e3bf",
#     "Host": "www.task-asp.net",
#     "Origin": "https://www.task-asp.net",
#     "Referer": "https://www.task-asp.net/cu/ykd402303/Order/List",
#     "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Brave\";v=\"126\"",
#     "Sec-Ch-Ua-Mobile": "?1",
#     "Sec-Ch-Ua-Platform": "\"Android\"",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "same-origin",
#     "Sec-Fetch-User": "?1",
#     "Sec-Gpc": "1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
# }
# sendingInfo = {
#     "MainContentPlaceHolder_ResearchItemInputCtr2_UseDateCalendarPicker_UseDateCalendarPickerPrevDateTemp: "+str(targetDate_previous_formatted),
#     "MainContentPlaceHolder_ResearchItemInputCtr2_UseDateCalendarPicker_UseDateCalendarPickerNextDateTemp: "+str(targetDate_next_formatted),
#     "ctl00$MainContentPlaceHolder$ResearchItemInputCtr2$UseDateCalendarPicker$UseDateCalendarPickerVisibleDate: "+str(targetDate_formatted),
#     "ctl00$MainContentPlaceHolder$ResearchItemInputCtr2$UseDateCalendarPicker$UseDateCalendarPickerSelectedDate: "+str(targetDate_formatted),
#     "ctl00$MainContentPlaceHolder$ResearchItemInputCtr2$UseDateCalendarPicker$UseDateCalendarPickerSelectedWarekiDate: "+str(wareki_formatted),
#     # "ctl00$MainContentPlaceHolder$ResearchItemInputCtr2$UseDateCalendarPicker$UseDateCalendarPickerPrevMonthDispType: 1",
#     # "ctl00$MainContentPlaceHolder$ResearchItemInputCtr2$UseDateCalendarPicker$UseDateCalendarPickerNextMonthDispType: 1",
#     # "ctl00$MainContentPlaceHolder$ResearchItemInputCtr2$UseDateCalendarPicker$UseDateCalendarPickerDateFormatType: 1",
#     # "ctl00$MainContentPlaceHolder$ResearchItemInputCtr2$UseDateCalendarPicker$UseDateCalendarPickerIsSelectedClose: 0",
#     # "ctl00$MainContentPlaceHolder$ResearchItemInputCtr2$UseDateCalendarPicker$UseDateCalendarPickerIsEnablePastDays: 0",
#     "ctl00$MainContentPlaceHolder$ResearchItemInputCtr2$SearchTypeRadioButtonList: 0",
#     "ctl00$MainContentPlaceHolder$ResearchItemInputCtr2$SisetuNameDropDownList: 0002", #志摩体育館
#     # "ctl00$MainContentPlaceHolder$ResearchItemInputCtr2$UseClassRadioButtonList: 1",
#     "ctl00$MainContentPlaceHolder$ResearchItemInputCtr2$SelectedUseClassTextBox: 216"
#     # "ctl00$MainContentPlaceHolder$ResearchItemInputCtr2$CultureListHidden: "
# }
# # data = json.dumps(sendingInfo)
# res_choice = session.post(url_choice, headers=headers, data=data)

# print(f"予約日程確認:{targetDate_formatted, targetDate_previous_formatted, targetDate_next_formatted}")
# print(f"選択の確認: {res_choice.status_code}")
# print(sendingInfo)
# print(f"res_choiceのテキストは以下の通り\n{res_choice.text}")

# # ログイン後の遷移（時間と内容記述）
# url_details = "https://www.task-asp.net/cu/ykd402303/Order/Input"
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "ja;q=0.5",
#     "Cache-Control": "max-age=0",
#     "Connection": "keep-alive",
#     "Content-Length": "19424",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Cookie": "taskasp_cu_ykd_starturl=%2fcu%2feg%2fykd402303.task; taskasp_cu_ykd_auth=256501A96458B193A293BE98B538AC81B0FA3892CBB2466A6355DDC41F8839E38E964F59D498EB362344496D7C6C1225042EE473CE7096007280E1241C043952296E2127C6969F04D1E019DDD97281E61AACE5C2CB7A4E21027AAA7003CF40F20B1F3F61EE65E5B4817A729E2DC0D4BFD72E1767F368B7E1BBB29707239DD1A25476957D5FBAE24C785697FA6902634A; taskasp_cu_ykd_sppage=1; taskasp_cu_ykd_sessionid=qdn335ec5lrsdevtdphaie5w; taskasp_cu_ykr_sessionid=gmtlwzd4jtmssnqjxfi1e3bf",
#     "Host": "www.task-asp.net",
#     "Origin": "https://www.task-asp.net",
#     "Referer": "https://www.task-asp.net/cu/ykd402303/Order/Input",
#     "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Brave\";v=\"126\"",
#     "Sec-Ch-Ua-Mobile": "?1",
#     "Sec-Ch-Ua-Platform": "\"Android\"",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "same-origin",
#     "Sec-Fetch-User": "?1",
#     "Sec-Gpc": "1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
# }

# sendingInfo = {
#     "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_16: 1700:1730:1",
#     "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_17: 1730:1800:1",
#     "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_18: 1800:1830:1",
#     "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_19: 1830:1900:1",
#     "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_20: 1900:1930:1",
#     "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_21: 1930:2000:1",
#     "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_22: 2000:2030:1",
#     "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_23: 2030:2100:1",
#     "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_24: 2100:2130:1",
#     "ctl00$MainContentPlaceHolder$InputUC$UseTimeCheckBoxList$UseTimeCheckBoxList_25: 2130:2200:1",
#     "ctl00$MainContentPlaceHolder$InputUC$SekininsyaSeiTextBox: 厚地",
#     "ctl00$MainContentPlaceHolder$InputUC$SekininsyaMeiTextBox: 俊哉",
#     "ctl00$MainContentPlaceHolder$InputUC$UseClassDropDownList: 216",
#     "ctl00$MainContentPlaceHolder$InputUC$GyouziNameTextBox: サークル利用",
#     "ctl00$MainContentPlaceHolder$InputUC$NinzuuTotalTextBox: 14"
# }
# # data = json.dump(sendingInfo)
# res_details = session.post(url_details, headers=headers, data=data)
# print(f"詳細の確認: {res_details.status_code}")
# # print(f"res_detailsのテキストは以下の通り\n{res_details.text}")