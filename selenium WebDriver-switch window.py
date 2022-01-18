from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# 切换浏览器窗口 switch_to.window(handle)
driver.get("http://localhost:8080/projectHtml/chapter3/period5-1-1.html")
time.sleep(1)

# print(driver.title)

# 获得当前页面句柄
handle_page = driver.current_window_handle

# 单击a标签进入第二个页面
driver.find_element(By.TAG_NAME, "a").click()
time.sleep(1)

# 获取所有语句的句柄
handles = driver.window_handles

for handle in handles:
    if handle == handle_page:
        driver.switch_to.window(handle)

print(driver.title)
time.sleep(1)

driver.switch_to.window(handles[1])
print(driver.title)
