# Requested modules
# - Selenium
# - win10toast

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

Options = Options()
Options.headless = True

browser = webdriver.Chrome(options = Options,
                           executable_path = r"C:\Users\Eduardo\Documents\DataAnalysis\Python\chromedriver_win32\chromedriver.exe")

URL = "https://bss.bcit.ca/owa_prod/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu"

browser.get(URL)
time.sleep(1)

print(" \n **** Login ****")
BCIT_ID = "A0..."     # Add your A0 number
password = ""     # and your password

browser.find_element_by_id('userid').send_keys(BCIT_ID)
browser.find_element_by_id('pwd').send_keys(password)
time.sleep(0.5)
browser.find_element_by_id('button_sign-in').click()
time.sleep(2)

print(" **** Connected ****\n")

browser.get("https://bss.bcit.ca/owa_prod/swstrans.p_disptran?InLevel=00")

credential = browser.find_element_by_xpath("/html/body/table[5]/tbody/tr[1]/td[2]/font/b")

if credential.text != "None Awarded":
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
    toaster.show_toast("BCIT Notification",
                       "Your BCIT Credential was updated!!!",
                       threaded=True)
else:
    print(" **** Nothing Yet ****\n")
        
browser.quit()
