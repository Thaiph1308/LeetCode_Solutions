numbers = [2,7,8,11,16]
target = 111

def twoSum(numbers,target):
    i = 0
    j = len(numbers) - 1
    result = 0
    while i != j:
        result = target - numbers[i]
        if (result < numbers[j]):
            j = j - 1
        if (result > numbers[j]):
            i = i + 1
        if (result == numbers[j]):
            return (i+1,j+1)
        print(i,j,result,numbers[i],numbers[j])
    return False

a = twoSum(numbers,target) 
print(a)       

################################################################

