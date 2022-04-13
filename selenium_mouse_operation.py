import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random



drive = webdriver.Chrome()
drive.get("https://sso.ginolegaltech.cn/user/login/")
# # drive.find_element(By.ID, "s-top-loginbtn").click()
drive.find_element(By.CLASS_NAME, "username").send_keys("huangmiaolan@ginolegaltech.cn")
drive.find_element(By.ID, "password").send_keys("Hml12345678.")
drive.find_element(By.CLASS_NAME, "login-common-button").click()
time.sleep(2)

#drive.get("https://yunpan.360.cn")

# 鼠标右键
# 定位到要右击的元素
# right_click = drive.find_element(By.ID, "topPanel")

# 对定位到的元素执行鼠标右键操作
# ActionChains(drive).context_click(right_click).perform()


# 鼠标悬停
# 定位到要悬停的元素
# stop_ele = drive.find_element(By.ID, "packageli")
# ActionChains(drive).move_to_element(stop_ele).perform()
# time.sleep(2)

# 鼠标双击
# double_click = drive.find_element(By.ID, "packageli")
# ActionChains(drive).double_click(double_click).perform()


drive.find_element(By.XPATH, "/html/body/div/div[1]/header/div/div[2]/div[1]/button[2]/span[1]").click()
time.sleep(1)

# 点击下拉框
drive.find_element(By.CLASS_NAME, "mu-dropDown-menu-text-overflow").click()
# drive.find_element(By.CLASS_NAME, "state-filter").click()
time.sleep(2)

# 根据索引选择
# Select(sel).select_by_index("1")
# time.sleep(2)

# 根据text选择
# Select(sel).select_by_visible_text("removed")
# time.sleep(2)

key = random.randrange(1, 3)

if key == 1:
    drive.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div[2]/div[1]").click()

elif key == 2:
    drive.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div[1]").click()

elif key == 3:
    drive.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[2]/div[1]").click()

else:
    print("error")

time.sleep(3)


# 点击弹窗按钮
drive.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div[2]/div[2]/button[1]/div").click()
time.sleep(2)

# 关闭弹窗
drive.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/button/div").click()

