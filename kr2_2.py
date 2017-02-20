var_string = '1486371'
# change_string = '1137864'

neven = []
even = []
# change_string = []

for num in var_string:
    if (int(num) % 2) != 0:
        neven.append(num)
    else:
        even.append(num)

neven.sort()
even.sort(reverse=True)

unite = neven + even
change_string = ''.join(unite)

print(change_string)