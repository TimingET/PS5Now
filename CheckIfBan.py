from time import sleep
from SendMail import sendMail
from ConfigDataMailInput import getConfigData


def checkIfban(browser):
    try:
        banned = browser.find_element_by_id("config-error")
        print(banned)
        print("IP Banned")
        return True


    except:

        return False
