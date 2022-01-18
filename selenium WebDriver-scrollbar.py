from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8080/projectHtml/chapter3/period5-2.html")
time.sleep(1)

# 移动到页面底部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)

# 移动到页面顶部
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
time.sleep(1)

# 移动到使"滚动条操作第二部分"顶部与窗口的顶部对齐位
element2 = driver.find_element(By.CLASS_NAME, "part2")
driver.execute_script("arguments[0].scrollIntoView();", element2)
time.sleep(1)

# 移动到使"滚动条操作第三部分"顶部与窗口的顶部对齐位
element3 = driver.find_element(By.CLASS_NAME, "part3")
driver.execute_script("arguments[0].scrollIntoView(false);", element3)


