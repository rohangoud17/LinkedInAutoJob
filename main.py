from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

password = ""

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


EMAIL = input("Please enter your Email ID: ")
PASSWORD = input("Please enter your Password: ")
PHONE = (input("Please enter your Phone Number: "))

driver = webdriver.Chrome(options=chrome_options)

driver.get(url="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0")
time.sleep(2)
button = driver.find_element(By.LINK_TEXT,value="Sign in")
button.click()

time.sleep(2)
username = driver.find_element(By.CSS_SELECTOR,value="#username")
username.send_keys(EMAIL,Keys.ENTER)

time.sleep(2)
password = driver.find_element(By.CSS_SELECTOR,value="#password")
password.send_keys(PASSWORD,Keys.ENTER)

time.sleep(2)
easy_apply = driver.find_element(By.XPATH,value='/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[5]/div/div/div/button/span')
easy_apply.click()

time.sleep(2)
phno = driver.find_element(By.XPATH,value='/html/body/div[3]/div/div/div[2]/div/div/form/div/div[1]/div[4]/div/div/div[1]/div/input')
phno.send_keys(PHONE,Keys.ENTER)

submit = driver.find_element(By.XPATH,value='/html/body/div[3]/div/div/div[2]/div/div/form/footer/div[3]/button/span')
submit.click()
