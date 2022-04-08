from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('w3c', False)
driver = webdriver.Chrome(options=options)
driver.get('http://localhost:8080/projectHtml/chapter3/period5-3.html')
driver.implicitly_wait(30)


# 内容显示
"""show_text = driver.find_element(By.CLASS_NAME, 'show-text').is_displayed()
print(show_text)

hidden_text = driver.find_element(By.CLASS_NAME, "hidden-text").is_displayed()
print(hidden_text)

driver.quit()"""

# 输入框可编辑
enabled_text = driver.find_element(By.CLASS_NAME, 'enabled-text').is_enabled()
print(enabled_text)
# 输入框不可编辑
disabled_text = driver.find_element(By.CLASS_NAME, 'disabled-text').is_enabled()
print(disabled_text)

driver.quit()



