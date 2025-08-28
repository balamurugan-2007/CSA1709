import itertools

def solve_cryptarithm():
    letters = ('S','E','N','D','M','O','R','Y')
    digits = range(10)
    
    for perm in itertools.permutations(digits, len(letters)):
        assign = dict(zip(letters, perm))
        if assign['S'] == 0 or assign['M'] == 0:
            continue
        
        send = assign['S']*1000 + assign['E']*100 + assign['N']*10 + assign['D']
        more = assign['M']*1000 + assign['O']*100 + assign['R']*10 + assign['E']
        money = assign['M']*10000 + assign['O']*1000 + assign['N']*100 + assign['E']*10 + assign['Y']
        
        if send + more == money:
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
            print("Mapping:", assign)
            return

solve_cryptarithm()
