a = [3,10,9,9]

def remove_duplicate(a):
    result = list(dict.fromkeys(a))
    return result 

print(remove_duplicate(a))