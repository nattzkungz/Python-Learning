phone_btn = {
    '2': 'a', '22': 'b', '222': 'c', '3': 'd', '33': 'e', '333': 'f', '4': 'g', '44': 'h', '444': 'i', '5': 'j',
    '55': 'k', '555': 'l', '6': 'm', '66': 'n', '666': 'o', '7': 'p', '77': 'q', '777': 'r', '7777': 's', '8': 't',
    '88': 'u', '888': 'v', '9': 'w', '99': 'x', '999': 'y', '9999': 'z', '0': ' '
}

def text2keys(text):
    prnt = []
    for _ in text.lower():
       for k in phone_btn:
           if _ == phone_btn[k]:
               prnt.append(k)
    return " ".join(prnt)

def keys2text(keys):
    prnt = []
    for _ in keys.split():
        for k in phone_btn:
            if _ == k:
                prnt.append(phone_btn[k])
    return "".join(prnt)

exec(input().strip())
