s = "() [] { }"

sta = []

hass = {"[":"]", "{":"}","(":")"}

for i in s:
    if i in hass.keys():
        sta.append(i)

    else:
        if sta ==[]:
            print("False")

        else:
            if hass[sta[-1]] == i:
                sta.pop()

            else:
                print("false")


if sta ==[]:
    print("true")

else:
    print("false")

