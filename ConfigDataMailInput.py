import codecs


def getConfigData():
    # Param: SENDER-EMAIL,RECEIVER-EMAIL, MAILHOST, MAILPORT, SENDER-EMAIL PASSWORD, MAIL.html
    configdata = ["JonDoeSendere@test.com", "JonDoeReceiver@gmail.de", "MAILHOST", "PORT", 'SenderMailPassword',
                  codecs.open("Mail/Ps5Mail.html")]

    return configdata
