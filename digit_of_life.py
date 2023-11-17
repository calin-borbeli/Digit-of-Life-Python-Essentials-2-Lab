invalid_dob = True

while invalid_dob:
    dol = input(
        "Please enter date of birth in the format DDMMYYYY or YYYYMMDD, 8 digits: "
    )
    if len(dol) == 8 and dol.isdigit():
        invalid_dob = False
    else:
        print("Invalid date entry")


while len(dol) > 1:
    dol_sum = 0
    for d in dol:
        dol_sum += int(d)
    dol = str(dol_sum)

print("Your Digit of Life is: " + dol)
