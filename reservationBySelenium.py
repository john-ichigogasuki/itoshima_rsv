import os

from selenium import webdriver
from time import sleep
from datetime import datetime
from dateutil.relativedelta import relativedelta
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv

driver = webdriver.Chrome()

def getSignInUrl():
    options = Options()
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
    driver.get("https://www.task-asp.net/cu/eg/ykd402303.task")

def executeLogIn():
    logInButton = driver.find_element(By.ID, "UserLoginLinkButton")
    logInButton.click()
    sleep(0.2)
    
    load_dotenv()
    ID_area = driver.find_element(By.ID, "UserNoTextBox")
    PW_area = driver.find_element(By.ID, "PasswordTextBox")
    signIn_button = driver.find_element(By.ID, "LoginButton")
    ID_area.send_keys(os.getenv('USERNAME'))
    PW_area.send_keys(os.getenv('PASSWORD'))
    signIn_button.click()
    sleep(0.2)
    topPage_button = driver.find_element(By.ID, "TopLinkButton")
    topPage_button.click()

def submitDetails():
    ########## 日程の予約 ##########
    ####  事前準備  ####
    # ターゲットになる予約日程を取得する
    today = datetime.today()
    three_month_later = today + relativedelta(months=2)
    formatted_date = three_month_later.strftime('%Y%m%d')# YYYYMMDDに変換
    #### 事前準備 ####
    wait = WebDriverWait(driver, 10)
    open_schedule = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.ui-collapsible-heading-toggle.ui-btn.ui-btn-icon-left.ui-btn-inherit.ui-icon-calendar")))
    open_schedule.click()
    sleep(0.2)
    for _ in range(2):
        next_month_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContentPlaceHolder_SearchItemInput_UseDateCalendarPicker_UseDateCalendarPicker"]/table/tbody/tr[1]/td/table/tbody/tr/td[3]')))
        next_month_button.click()
        sleep(0.2)
    date_element = wait.until(EC.element_to_be_clickable((By.XPATH, f'//a[@class="lg-cal-date" and @data-lg-date="{formatted_date}"]')))
    date_element.click()
    ########## 日程の予約 ##########
    
    ########## 予約内容の入力 ##########
    #### 施設の選択 ####
    facility_select = wait.until(EC.presence_of_element_located((By.ID, "MainContentPlaceHolder_SearchItemInput_SisetuNameDropDownList")))
    select = Select(facility_select)
    select.select_by_value("0002")
    #### 施設の選択 ####
    
    #### 利用目的 ####
    change_to_purpose_select = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContentPlaceHolder_SearchItemInput_SearchTypeRadioButtonList"]/div[2]/label')))
    change_to_purpose_select.click()
    purpose_wrapper = wait.until(EC.element_to_be_clickable((By.ID, "select-10-button")))
    purpose_wrapper.click()
    purpose_option_select = wait.until(EC.element_to_be_clickable((By.XPATH, '//select/option[@value="216"]')))
    purpose_option_select.click()
    #### 利用目的 ####
    
    search_button = wait.until(EC.element_to_be_clickable((By.ID, "LinkButtonSearch")))
    search_button.click()
    sleep(0.5)

def reservation():
    wait = WebDriverWait(driver, 10)
    
    full_area_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'ctl00$MainContentPlaceHolder$AkiListView$ctrl2$AddYoyakuKagoButton')]")))
    full_area_button.click()
    sleep(0.5)
    
    time_slot_1700to1730 = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="UseTimeCheckBoxList_16"]')))
    time_slot_1700to1730.click()
    time_slot_1730to1800 = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="UseTimeCheckBoxList_17"]')))
    time_slot_1730to1800.click()
    time_slot_1800to1830 = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="UseTimeCheckBoxList_18"]')))
    time_slot_1800to1830.click()
    time_slot_1830to1900 = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="UseTimeCheckBoxList_19"]')))
    time_slot_1830to1900.click()
    time_slot_1900to1930 = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="UseTimeCheckBoxList_20"]')))
    time_slot_1900to1930.click()
    time_slot_1930to2000 = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="UseTimeCheckBoxList_21"]')))
    time_slot_1930to2000.click()
    time_slot_2000to2030 = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="UseTimeCheckBoxList_22"]')))
    time_slot_2000to2030.click()
    time_slot_2030to2100 = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="UseTimeCheckBoxList_23"]')))
    time_slot_2030to2100.click()
    time_slot_2100to2130 = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="UseTimeCheckBoxList_24"]')))
    time_slot_2100to2130.click()
    time_slot_2130to2200 = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="UseTimeCheckBoxList_25"]')))
    time_slot_2130to2200.click()
    
    event_name_input = wait.until(EC.presence_of_element_located((By.ID, "GyouziNameTextBox")))
    event_name_input.clear()  # 既存のテキストがある場合はクリア
    event_name_input.send_keys("サークル活動")
    
    total_people_input = wait.until(EC.presence_of_element_located((By.ID, "NinzuuTotalTextBox")))
    total_people_input.clear()  # 既存のテキストがある場合はクリア
    driver.execute_script("arguments[0].value='14';", total_people_input)
    
    complete_button = wait.until(EC.element_to_be_clickable((By.ID, "RegistForYoyakuKagoButton")))
    complete_button.click()

def registration():
    wait = WebDriverWait(driver, 10)
    confirm_button = wait.until(EC.element_to_be_clickable((By.ID, "YoyakuConfirmButton")))
    confirm_button.click()
    
    finalConfirm_button = wait.until(EC.element_to_be_clickable((By.ID, "YoyakuButton")))
    finalConfirm_button.click()
    sleep(5)


getSignInUrl()
executeLogIn()
submitDetails()
reservation()
registration()