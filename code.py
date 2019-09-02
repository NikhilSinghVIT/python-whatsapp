import schedule
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
try:
    import autoit
except:
    pass
import time
import datetime
import os

browser = None
Contact = None
message = None
Link = "https://web.whatsapp.com/"
wait = None
unsaved_Contacts = None


def input_message():
    global message
    print()
    print("Enter the message and use the symbol '~' to end the message:\nFor example: Hi, this is a test message~\n\nYour message: ")
    message = []
    temp = ""
    done = False

    while not done:
      temp = input()
      if len(temp)!=0 and temp[-1] == "~":
        done = True
        message.append(temp[:-1])
      else:
        message.append(temp)
    message = "\n".join(message)
    print()
    print(message)

def whatsapp_login():
    global wait,browser,Link
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 600)
    browser.get(Link)
    browser.maximize_window()
    print("QR scanned")

def send_unsaved_contact_message():
    global message
    try:
        time.sleep(7)
        input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        for ch in message:
            if ch == "\n":
                ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
            else:
                input_box.send_keys(ch)
        input_box.send_keys(Keys.ENTER)
        print("Message sent successfuly")
    except NoSuchElementException:
        print("Failed to send message")
        return

def sender():
    if len(unsaved_Contacts)>0:
        for i in unsaved_Contacts:
            link = "https://wa.me/"+i
            #driver  = webdriver.Chrome()
            browser.get(link)
            time.sleep(1)
            browser.find_element_by_xpath('//*[@id="action-button"]').click()
            time.sleep(4)
            print("Sending message to", i)
            send_unsaved_contact_message()
            time.sleep(7)


if __name__ == "__main__":

    print("Web Page Open")
    #enter the contact numbers as shown below in the list
    unsaved_Contacts  = ['913453453453','912342342342']
    input_message()


    print("SCAN YOUR QR CODE FOR WHATSAPP WEB")
    whatsapp_login()
    sender()

    # First time message sending Task Complete
    print("Task Completed")

    # Messages are scheduled to send
    # Default schedule to send attachment and greet the personal
    # For GoodMorning, GoodNight and howareyou wishes
    # Comment in case you don't want to send wishes or schedule

    # browser.quit()
