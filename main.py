from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from checkIfOnStock import checkIfOnStock
from CheckIfBan import checkIfban



browser = webdriver.Firefox()

browser.get('https://www.mediamarkt.de/de/product/_sony-playstation%C2%AE5-digital-edition-2661939.html')
# https://www.mediamarkt.de/de/product/_sony-playstation%C2%AE5-digital-edition-2661939.html

sleep(2)

cookietbn = browser.find_element_by_id('privacy-layer-accept-all-button')

cookietbn.click()
print("Cookies akzeptiert!")

sleep(3)

isOnStocked = 0
counter = 0


def func():
    while checkIfOnStock(browser) != 1 and checkIfban(browser) is False:
        counter = counter + 1
        browser.get('https://www.mediamarkt.de/de/product/_sony-playstation%C2%AE5-digital-edition-2661939.html')
        print("Try : " + counter.__str__())
        checkIfOnStock(browser)
        sleep(8)
        func()


while True:
    if checkIfban(browser) is False:
        while checkIfOnStock(browser) != 1:
            counter = counter + 1
            browser.get('https://www.mediamarkt.de/de/product/_sony-playstation%C2%AE5-digital-edition-2661939.html')
            print("Try : " + counter.__str__())
            checkIfOnStock(browser)
            sleep(8)
    else:
        sleep(10)
