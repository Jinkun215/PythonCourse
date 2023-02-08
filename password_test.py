

password = input("Enter your password: ")

pass_length = False
pass_numeral = False
pass_lowercase = False
pass_uppercase = False
pass_total = {} #dictionary

if (len(password) > 9):
    pass_length = True

pass_total["Length"] = pass_length

for pn in password:
    if (pn.isdigit()):
        pass_numeral = True
        break

pass_total["Numeral"] = pass_numeral

for pl in password:
    if pl.islower():
        pass_lowercase = True
        break

pass_total["Lowercase"] = pass_lowercase

for pu in password:
    if pu.isupper():
        pass_uppercase = True
        break

pass_total["Uppercase"] = pass_uppercase

print(pass_total)
if all(pass_total.values()):        #use .values() to check the value of key
    print("Your password is strong.")
else:
    print("Your password is weak.")