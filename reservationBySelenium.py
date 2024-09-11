from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def getSignInUrl():
    options = Options()
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
    driver.get("https://www.task-asp.net/cu/eg/ykd402303.task")

def executeLogIn():
    logInButton = driver.find_element(By.ID, "UserLoginLinkButton")
    logInButton.click()
    sleep(0.2)
    
    ID_area = driver.find_element(By.ID, "UserNoTextBox")
    PW_area = driver.find_element(By.ID, "PasswordTextBox")
    ID_area.send_keys(os.getenv('USERNAME'))
    PW_area.send_keys(os.getenv('PASSWORD'))

getSignInUrl()
executeLogIn()
