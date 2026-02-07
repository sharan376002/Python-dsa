def To_deciamal(binary):
    rev_bin = binary[::-1]
    dec= 0
    for i in range(len(binary)):
        power = (2**i)*int(rev_bin[i])
        dec= dec + int(power)

    return dec



binary = '1001010010'

print("Deciml to Binary ")

result = To_deciamal(binary)
print( result)