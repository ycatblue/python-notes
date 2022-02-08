from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8080/projectHtml/chapter1/period2/index.html")

# 单击事件
# driver.find_element(By.ID, "btn-login").click()

# 在输入账号的输入框中输入内容“tynam@test.com”，然后清空输入的内容，以id='email'进行定位。
driver.find_element(By.ID, "email").send_keys("tynam@test.com")
time.sleep(1)
driver.find_element(By.ID, "email").clear()

# 获取文本内容
login_text = driver.find_element(By.ID, "btn-login").text
print(login_text)

# 获取账号输入框的name值，使用id='email'进行定位。
name_text = driver.find_element(By.ID, "email").get_attribute("name")
print(name_text)

