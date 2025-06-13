# Problem: Decimal to binary number using recursion - https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/

def dec_to_bin_rec(d):
    if d > 1:
        dec_to_bin_rec(d // 2)
    return str(d % 2) + (dec_to_bin_rec(d // 2) if d > 1 else '')

def dec_to_bin(d):
    return dec_to_bin_rec(d)

if __name__ == '__main__':
    d = 1048576
    print(dec_to_bin(d))