from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# 引入key模块
from selenium.webdriver.common.keys import Keys

drive = webdriver.Chrome()
drive.get("https://sso.ginolegaltech.cn/dex/#/desk/robot")

# 输入框输入内容
drive.find_element(By.ID, "username").send_keys("huangmiaolan@")
time.sleep(1)

# 删除多输入的n
drive.find_element(By.ID, "username").send_keys(Keys.BACK_SPACE)
time.sleep(1)

# 空格 + 输入内容
drive.find_element(By.ID, "username").send_keys(Keys.SPACE)
drive.find_element(By.ID, "username").send_keys("@ginolegaltech.cn")
time.sleep(1)

# ctrl + a全选内容
drive.find_element(By.ID, "username").send_keys(Keys.CONTROL, "a")
time.sleep(1)

# ctrl + x剪切输入框内容
drive.find_element(By.ID, "username").send_keys(Keys.CONTROL, "x")
time.sleep(1)

# ctrl + v 粘贴
drive.find_element(By.ID, "username").send_keys(Keys.CONTROL, "v")
time.sleep(1)

# ctrl + enter 回车
drive.find_element(By.ID, "password").send_keys("Hml123456789.")
time.sleep(1)

drive.find_element(By.CLASS_NAME, "loginbutton ").send_keys(Keys.ENTER)
