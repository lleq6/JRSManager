import re

def checkThaiLanguage(text : str):
    return bool(re.fullmatch("^[\u0E00-\u0E7F]*$", text))

def checkEng(text : str):
    return bool(re.fullmatch("^[A-Za-z]*$", text))
def checkENGoTH(text: str):
    if checkThaiLanguage(text) or checkEng(text):
        return True
    return False
def checkEmail(text : str):
    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
    match = bool(re.fullmatch(pattern, text))
    return match

def checkCitizenID(text : str):
    print(text,'citizen')
    text = str(text)
    pattern = r'[0-9]{13}$'
    match = bool(re.fullmatch(pattern, text))
    return match


def checkZip(text : str):
    text = str(text)
    pattern = r'[0-9]{5}$'
    match = bool(re.fullmatch(pattern, text))
    return match
def checkPhone(text : str):
    pattern = r'[0]+[0-9]{9}$'
    match = bool(re.fullmatch(pattern, text))
    return match

def checkInt(text):
    try:
        int(text)
        return True
    except:
        return False
def checkEmpty(text : str):
    text = str(text)
    if text.strip(' ') == '':
        return False
    return True

def checkJuristic(text : str):
    text = text.split(' ')
    th = 0
    en = 0
    for i in text:
        if checkThaiLanguage(i):
            th=1

        if checkEng(i):
            en=1

    if en != th:
        return True
    return False