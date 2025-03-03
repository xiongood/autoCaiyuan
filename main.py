import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


driver.get("https://www.roosf.com/")

time.sleep(20)

email_input = driver.find_element(By.ID, "email")

password_input = driver.find_element(By.ID, "password")


email_input.send_keys("java0417@163.com")
password_input.send_keys("xiong1991")
time.sleep(6)



login_submit = driver.find_element(By.ID, "login_submit")
login_submit.click()


time.sleep(20)


login_submit = driver.find_element(By.ID, "checkin")
login_submit.click()
time.sleep(20)


driver.quit()
