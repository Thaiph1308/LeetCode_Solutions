x = -123
def reverse(x):
    sign = [1,-1][x<0]
    #print(sign)
    reverse_string = str(abs(x))[::-1]
    #print("RST",reverse_string)
    result = int(reverse_string)*sign
    if (-(2**31)-1 < result < (2**31)):
        return result 
    else:
        return 0

print(reverse(x))