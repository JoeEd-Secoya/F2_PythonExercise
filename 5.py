def decToBinary(dec):
    if dec == 0:
        return '0'

    binarystr = ''
    while dec > 0:
        remainder = dec % 2
        binarystr = str(remainder) + binarystr
        dec //= 2
    return binarystr

def binaryToN(binary, base):
    if base not in [8, 10, 16]:
        return "Unsupported Base"

    if base == 10:
        decres = 0
        binarystr = str(binary)
        length = len(binarystr)
        for i in range(length):
            decres += int(binarystr[length - 1 - i]) * (2 ** i)
        return decres
    else:
        decres = 0
        binarystr = str(binary)
        length = len(binarystr)
        for i in range(length):
            decres += int(binarystr[length - 1 - i]) * (2 ** i)
        if base == 8:
            return oct(decres)
        elif base == 16:
            return hex(decres)


def decToOctal(decnum):
    if decnum == 0:
        return '0'

    octal = ''
    while decnum > 0:
        remainder = decnum % 8
        octal = str(remainder) + octal
        decnum //= 8

    return octal


def decToHex(decnum):
    if decnum == 0:
        return '0'

    hex_chars = "0123456789ABCDEF"
    hexrep = ''

    while decnum > 0:
        remainder = decnum % 16
        hexrep = hex_chars[remainder] + hexrep
        decnum //= 16

    return hexrep


def main():
    x = int(input("Please enter any decimal num to test: "))
    print(f"Binary: {decToBinary(x)}")
    print(f"Decimal: {binaryToN(decToBinary(x), 10)}")
    print(f"Octal: {decToOctal(x)}")
    print(f"Hexadecimal: {decToHex(x)}")

main()