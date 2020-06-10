# -----------------------------------------------
# String
import json

first_name = "w"
last_name = "y"
full_name = "{} {}".format(first_name, last_name)
full_name.rstrip()
full_name.lstrip()

# -----------------------------------------------
# List
list_T = [1, 2, 3, 4, 5]
for i in list_T:
    i
# copy list
list_2 = list_T[:]
list_T.append(6)
# print(list_2)

# ---------------------------------------------------------
# IF
a = 0
if a > 0:
    a = a + 1
else:
    a = a - 1

# ---------------------
# distortion
dis = {'1': 'w', '2': 'y'}
dis['3'] = 'z'
for k, v in dis.items():
    kv = k + " " + v


def getValue(pIn):
    return pIn


def getValue1(*pIn):
    return pIn


def getValue2(**pIn):
    return pIn


# ---------------------
# Class
class DefineF:
    id

    def __init__(self, pId):
        self.id = pId


class Define1(DefineF):
    id = ''

    def __init__(self, pId):
        self.id = pId

    def getId(self):
        return self.id


df = Define1()
df.getId()

# -------------------------
# file
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    for line in file_object:
        line

file_object1 = open('pi_digits.txt', 'a')
file_object.write("I also love finding meaning in large datasets.\n")

with open('', encoding='utf-8') as f:
    contents = f.read()
    jsv = ''
    json.dump(jsv, f)
    jsv = json.load(f)

try:
    5/0
except ZeroDivisionError:
    p = "You can't divide by zero!"
else:
    p = "You can't divide by zero!"
