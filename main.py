import time,os,win32con,win32gui,subprocess

from selenium import webdriver

from selenium.webdriver.common.by import By

from capture import capture_and_handle

from waterRPA import RPA

def main():

    global filename

    filename = capture_and_handle()

    browser.get('http://student.zhixuehuijiao.cn/#/coursePreview?classType=0&classId=822&courseId=18243')

    browser.implicitly_wait(3)

    browser.find_elements(By.CLASS_NAME, "van-button--round")[3].click()

    browser.find_elements(By.CLASS_NAME, "label")[1].click()

    app = subprocess.Popen(r'fileupload.exe ' + path + filename)

    time.sleep(2)

    app.kill()

    browser.find_element(By.CLASS_NAME,"confirm.van-button.van-button--info.van-button--small").click()

    browser.find_element(By.CLASS_NAME,"van-button.van-button--default.van-button--large.van-dialog__confirm.van-hairline--left").click()

    os.remove(filename)

def main_next():

    global filename

    filename = capture_and_handle()

    browser.find_element(By.CLASS_NAME,"svg-icon.cancel").click()

    browser.find_elements(By.CLASS_NAME, "van-button--round")[3].click()

    browser.find_elements(By.CLASS_NAME, "label")[1].click()

    app = subprocess.Popen(r'fileupload.exe ' + path + filename)

    time.sleep(2)

    app.kill()

    browser.find_element(By.CLASS_NAME,"confirm.van-button.van-button--info.van-button--small").click()

    browser.find_element(By.CLASS_NAME,"van-button.van-button--default.van-button--large.van-dialog__confirm.van-hairline--left").click()

    os.remove(filename)

ok = 0

path = os.getcwd()

path = os.getcwd()

path = path+"\\"

chrome_options = webdriver.ChromeOptions()

browser = webdriver.Chrome(options=chrome_options)

browser.get('http://student.zhixuehuijiao.cn/#/login')

browser.implicitly_wait(3)

chrome_app = win32gui.FindWindow("Chrome_WidgetWin_1","登录 - Google Chrome")

win32gui.ShowWindow(chrome_app, win32con.SW_SHOWMINIMIZED)

browser.find_elements(By.CLASS_NAME, "van-field__control")[0].send_keys("hdxz2021004936")

browser.find_elements(By.CLASS_NAME, "van-field__control")[1].send_keys("wyf5950")

browser.find_element(By.CLASS_NAME, "van-button--block").click()

filename = ""

while ok == 0:

    try:

        main()

        ok = 1

    except:

        pass

while True:

    try:

        main_next()

    except:

        pass

        os.remove(filename)