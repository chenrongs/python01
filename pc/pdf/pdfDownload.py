from selenium import webdriver
import win32api
import pyperclip
import win32con
import time

CHROME_DRIVER = 'D:\\chormedriver\\chromedriver.exe'
download_img_path = 'E:\\pdf\\'


driver = webdriver.Chrome(executable_path=CHROME_DRIVER)

driver.get('http://www.jkjsf.com/printservices/preview?__report=flReports/ecna/SisGradeReport.rptdesign&__format=pdf&reportId=005201&urlA=10001013SIGN&urlB=15876527980SIGN')

pyperclip.copy(download_img_path)

win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
win32api.keybd_event(83, 0, 0, 0)  # s键位码是83
# 放开
win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

time.sleep(2)

win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
win32api.keybd_event(86, 0, 0, 0)  # v键位码是17
# 放开
win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

time.sleep(1)
win32api.keybd_event(13, 0, 0, 0) #回车
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)

time.sleep(1)





