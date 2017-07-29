import logging
import os
import multiprocessing
from flask import Flask
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('HelloIntent')
def hello():
    speech_text = "Hello set system state"
    return statement(speech_text)

@ask.intent('ArmAwayIntent')
def armaway():
    p = multiprocessing.Process(target=os.system("curl -X POST -b cookies.txt -d 'state=away&mobile=1&no_persist=1&XDEBUG_SESSION_START=session_name' https://simplisafe.com/mobile/646615/sid/518950/set-state"))
    speech_text = "System Armed Away"
    return statement(speech_text)

@ask.intent("DisarmIntent", convert={'pin': int})

def disarm(pin):

    correct_pin = 9999 #sample pin

    if pin == correct_pin:
        p = multiprocessing.Process(target=os.system("curl -X POST -b cookies.txt -d 'state=off&mobile=1&no_persist=1&XDEBUG_SESSION_START=session_name' https://simplisafe.com/mobile/646615/sid/518950/set-state"))
        msg = "System disarmed"
    else:

        msg = "Incorrect PIN, disarm failed. Please try to disarm again"

    return statement(msg)

if __name__ == '__main__':
    app.run()
