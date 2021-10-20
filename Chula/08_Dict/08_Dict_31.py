def total(pocket):
    total = 0
    for _ in pocket:
        total += pocket[_]*_
    return total

def take(pocket, money_in):
    for _ in money_in:
        if _ in pocket:
            pocket[_] += money_in[_]
        else:
            pocket[_] = money_in[_]
    return pocket

def pay(pocket, amt):
    pocket_list = [[i, pocket[i]] for i in pocket]
    if total(pocket) >= amt:
        notes_used = []
        if amt != 0:
            for _ in pocket:
                amt %= _
            
        return pocket
    else:
        return {}

exec(input().strip())