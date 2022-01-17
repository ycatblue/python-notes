from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# 访问网站
driver.get("http://localhost:8080/projectHtml/chapter3/period4.html")
time.sleep(3)


# 得到所有多选框
checkboxs = driver.find_elements(By.TAG_NAME, "input")

for checkbox in checkboxs:
    if checkbox.get_attribute('checked') is None:
        checkbox.click()
        time.sleep(1)


# driver.close()


# 取消第一个勾选，勾选第二个多选框。
checkboxs[0].click()
checkboxs[1].click()
time.sleep(1)
