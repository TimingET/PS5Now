from time import sleep
from SendMail import sendMail
from ConfigDataMailInput import getConfigData


def checkIfOnStock(browser):
    try:
        onStock = browser.find_element_by_id("pdp-add-to-cart-button")
        print("Is on Stock")
        onStock.click()
        sleep(1)
        browser.get("https://www.mediamarkt.de/checkout")
        print("In Checkout")
        try:
            # Param
            # sendMail(mail.html, SENDER-EMAIL,RECEIVER-EMAIL, MAILHOST, MAILPORT, SENDER-EMAIL PASSWORD)
            sendMail(getConfigData()[5], getConfigData()[0], getConfigData()[1], getConfigData()[2], getConfigData()[3],
                     getConfigData()[4])
            return 1
        except:
            print("Mail can not send!")


    except:

        print("Not on stock")
        return 0
