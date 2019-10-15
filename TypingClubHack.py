from time import sleep
from pynput.keyboard import Key, Controller
import random
import time

keyboard = Controller()
#delay = 0.11231 * pow(2, 0.092854 * random.randint(0, 101))
#delay = 0.009 * pow(2, 0.062854 * 55)

def error (errorNum):
    errorList = ("qwertyuiopasdfghjklzxcvbnm,;'qwertyuiopzxcvbnm;'fksdlajf89quyr8934hqw9ufhe9u8ahe98h2fqp9hadujbdsvycayurwsgdfcvuyfgeuyg8923hp09h))(#D@&^hbeuiwfhb9uiebwqifrbfuejsdkfndas.dsa'asd'f[as]\fafiuhegfiqwugfu8vgsauf")
    errorChar = errorList[errorNum]
    #for i in errorList:
        #errorChar = i
    #errorChar = errorNum in errorList
    return errorChar

def controlKeyboard():
    AccuracyControl = random.randint(83,95)
    for char in '''Education is about teaching, learning skills, and acquiring knowledge. Education also means helping people to learn how to do things and encouraging them to think about what they learn. It is important for educators to teach ways to find and use information. Through education, the knowledge of societies, countries, and of the world is passed on from generation to generation.

''':
        errorFactor = random.randint(0,100)
        if errorFactor <= AccuracyControl:
            keyboard.press(char)
            keyboard.release(char)
        elif errorFactor <= (AccuracyControl+5):
            errorChar = error(random.randint(0,100))
            print(errorChar)
            keyboard.press(errorChar)
            keyboard.release(errorChar)
            time.sleep(float(0.3))
            keyboard.press(Key.backspace)
            time.sleep(float(0.2))
            keyboard.press(char)
            keyboard.release(char)
        else:
            errorChar = error(random.randint(0,100))
            keyboard.press(errorChar)
            keyboard.release(errorChar)
        delay = random.uniform(0.06,0.13)
        time.sleep(float(delay))
        #print(char)
        #print(delay)

sleep(5); controlKeyboard()

