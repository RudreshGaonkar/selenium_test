from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get('file:///path/to/your/html/file.html')

name_input = driver.find_element(By.CLASS_NAME, 'namejs')
email_input = driver.find_element(By.CLASS_NAME, 'emailjs')
password_input = driver.find_element(By.CLASS_NAME, 'passwordjs')
button = driver.find_element(By.ID, 'btn')

sleep(2)
name_input.send_keys("Rudresh R. Gaonkar")
email_input.send_keys("rudresh7gaonkar@gmail.om")
password_input.send_keys("Your Password")

sleep(2)
button.click()

sleep(20)

driver.quit()
