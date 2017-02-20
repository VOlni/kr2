var_string = "sabrrtuwacaddabra"
#longest = "abrrtuw"


longest=""
output = ""
prev=""
for cur in var_string:
    if cur >= prev:
        output += cur
        if len(longest) < len(output):
            longest = output
    else:
        output = cur
    prev = cur


print(longest)