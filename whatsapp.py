from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def rep():
    askUser = input("Do You want to send more msg(Y/N):")
    if askUser == 'Y' or askUser == 'y':
        msg()
        rep()
    elif askUser == 'N' or askUser == 'n':
        print("Testing Complete")
    else:
        print("Invalid Input")
        rep()

def msg():

    count = int(input('\n Enter number of test cases'))


    for i in range(1,count+1):
        message = "Testing Selenium Case: "
        message = message + str(i)
        message_box = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
        message_box.send_keys(message,Keys.ENTER)


os.environ['PATH'] += r"D:\SeleniumDrivers"
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
sleep(2)

print("Scan QR code")
input()
name = input('\n Enter Group/User Name:')

sleep(2)
search_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]')
search_box.send_keys(name,Keys.ENTER)

sleep(2)

msg()

rep()





