import random
import time
import base64


def get_random():
    tm = time.time()
    pt = list(time.gmtime(tm))
    string = ""
    for i in range(3):
        string += str(pt[i])
    string += "-"
    dc = ""
    for i in range(3, 6):
        dc += str(pt[i])
    dc = dc.encode()
    enc = str(base64.b64encode(dc))
    for i in enc:
        if i != "'" and i != "b":
            string += i
    for i in range(4):
        string += "-"
        for j in range(5):
            tp = random.randint(0, 2)
            if tp == 0:
                string += str(random.randint(1, 9))
            elif tp == 1:
                string += chr(random.randint(65, 90))
            else:
                string += chr(random.randint(97, 122))
    string += "-" + str(int(tm))
    return str(string)
