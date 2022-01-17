from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# 设置浏览器宽为500像素，高为900像素。
driver.set_window_size(500, 900)

# 浏览器最大化
driver.maximize_window()

# 关闭浏览器
# driver.quit()

# 访问百度首页并且搜索“tynam”，然后操作浏览器退回百度首页
driver.get("https://baidu.com")
time.sleep(1)
driver.find_element(By.ID, "kw").send_keys("tynam")
driver.find_element(By.ID, "su").click()
time.sleep(1)

# 操作浏览器后退
driver.back()

# 操作浏览器前进
driver.forward()

# 刷新浏览器
driver.refresh()

# 关闭浏览器当前窗口
driver.close()