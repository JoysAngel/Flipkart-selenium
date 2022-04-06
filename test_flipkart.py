from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

product = input("enter the product to be searched")
driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test started")
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(2)
driver.find_element_by_name("q").send_keys("flipkart")
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a/h3").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
time.sleep(1)
driver.find_element_by_name("q").send_keys(product)
time.sleep(1)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(2)
driver.execute_script("window.scrollTo(0,window.scrollY+700)")
time.sleep(5)
driver.find_element_by_xpath("/html/body/div/div/div[3]/div[1]/div[2]/div[9]/div/div/div/a/div[2]/div[1]/div[1]").click()
time.sleep(3)
driver.close()
print("Testcase completed")
