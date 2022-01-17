from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
time.sleep(1)

# id 定位
driver.find_element(By.ID, 'kw')
id_maxlength = driver.find_element(By.ID, 'kw').get_attribute('maxlength')
assert id_maxlength == '255'

# class 定位
driver.find_element(By.CLASS_NAME, "s_btn")
class_btn = driver.find_element(By.CLASS_NAME, "s_btn").get_attribute("value")
assert class_btn == "百度一下"

# name 定位
driver.find_element(By.NAME, "wd")
class_name = driver.find_element(By.NAME, "wd").get_attribute("autocomplete")
assert class_name == "off"

# tag 定位
# driver.find_element(By.TAG_NAME, "h4")
# tag_text = driver.find_element(By.TAG_NAME, "h4").text
# tag_text = "tag 定位"

# xPath 定位
driver.find_element(By.XPATH, "/html/body/div")