from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

drive = webdriver.Chrome()
# drive.get("https://ovh.ginolegaltech.com/user/login/")
# # drive.find_element(By.ID, "s-top-loginbtn").click()
# drive.find_element(By.CLASS_NAME, "username").send_keys("huangmiaolan@ginolegaltech.cn")
# drive.find_element(By.ID, "password").send_keys("Hml12345678.")
# drive.find_element(By.CLASS_NAME, "login-common-button").click()

drive.get("https://yunpan.360.cn")

# 定位到要右击的元素
# right_click = drive.find_element(By.ID, "topPanel")

# 对定位到的元素执行鼠标右键操作
# ActionChains(drive).context_click(right_click).perform()

# 定位到要悬停的元素
stop_ele = drive.find_element(By.ID, "packageli")
ActionChains(drive).move_to_element(stop_ele).perform()