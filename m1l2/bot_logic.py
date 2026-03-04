import random
def gen_pass(n):
    passcode = []

    yn = 'n'

    char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    def password():
        global choose
        choose = random.randint(1,72)
        

        
    for i in range(n):
        password()
        passcode.append(char[choose])

    print("".join(passcode))
