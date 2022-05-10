# importing essential libraries
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# declaring variables
url = "https://www.flipkart.com/"
text = "Iphone 11"
value = "30000"

# initializing Chrome driver
driver = webdriver.Chrome()
driver.get(url)

# maximizing window
driver.maximize_window()

# implicit wait for 30 seconds
driver.implicitly_wait(30)
driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@class='_3704LK']").send_keys(text)
time.sleep(2)

driver.find_element(By.CLASS_NAME, "_34RNph").click()
time.sleep(3)

Select(driver.find_element(By.XPATH, "//select[@class='_2YxCDZ']")).select_by_value(value)
time.sleep(3)

driver.find_element(By.XPATH, "//div[@class='_24_Dny']")
time.sleep(2)

driver.find_element(By.XPATH, "(//div[@class='_24_Dny'])[1]").click()
time.sleep(2)

# scrolling page
driver.execute_script("window.scrollTo(0,7560)")
time.sleep(5)

e = driver.find_elements(By.XPATH,"//*[@class='_4rR01T']")
list = []
list1 = []
list2 = []
list3 = []

for x in e:
    list.append(x.text)

e1 = driver.find_elements(By.XPATH,"//*[@class='_30jeq3 _1_WHN1']")

for x in e1:
    list1.append(x.text)

e2 = driver.find_elements(By.XPATH,"//*[@class='_1fQZEK']")

for x in e2:
    list2.append(x.get_attribute('href'))

for x in range(len(list)):
    list3.append([list[x],list1[x],list2[x]])
print(list3)

# closing the driver window
driver.quit()