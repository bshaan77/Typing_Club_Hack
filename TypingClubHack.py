from time import sleep
from pynput.keyboard import Key, Controller
import random
import time

keyboard = Controller()
#delay = 0.11231 * pow(2, 0.092854 * random.randint(0, 101))
#delay = 0.009 * pow(2, 0.062854 * 55)


def error (errorNum):
    errorList = ("fksdlajf89quyr8934hqw9ufhe9u8ahe98h2fqp9hadujbdsvycayurwsgdfcvuyfgeuyg8923hp09h))(#D@&^hbeuiwfhb9uiebwqifrbfuejsdkfndas.dsa'asd'f[as]\fafiuhegfiqwugfu8vgsauf")
    for i in errorList:
        errorChar = i
    #errorChar = errorNum in errorList
    return errorChar

def controlKeyboard():
    AccuracyControl = random.randint(90,97)
    for char in '''At first, Washington D.C. was made up of a piece of Virginia located south of the Potomac River and a piece of Maryland located north of the Potomac River. In 1847, Virginia's land was returned to it. This area is now part of Arlington County. Since 1847, all of Washington D.C. is on the north side of the Potomac River.''':
        errorFactor = random.randint(0,100)
        if errorFactor <= AccuracyControl:
            keyboard.press(char)
            keyboard.release(char)
        else:
            errorChar = error(random.randint(0,60))
            keyboard.press(errorChar)
            keyboard.release(errorChar)
        delay = random.uniform(0.07,0.15)
        time.sleep(float(delay))
        print(char)
        print(delay)

sleep(3); controlKeyboard()

