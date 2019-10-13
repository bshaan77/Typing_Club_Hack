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
    for char in '''Seawater cannot be drunk safely because it has high salinity, or concentration of salt. Seawater is also called salt water. Both people and animals often live near rivers, because they need water to survive. The water in a river is called fresh water. Fresh water comes from rain or snow and it can usually be drunk safely, unless it has been polluted.''':
        errorFactor = random.randint(0,100)
        if errorFactor <= AccuracyControl:
            keyboard.press(char)
            keyboard.release(char)
        else:
            errorChar = error(random.randint(0,60))
            keyboard.press(errorChar)
            keyboard.release(errorChar)
        delay = random.uniform(0.09,0.18)
        time.sleep(float(delay))
        print(char)
        print(delay)

sleep(3); controlKeyboard()

