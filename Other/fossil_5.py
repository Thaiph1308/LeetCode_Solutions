num = 2
word = '9zb'
ascii_1 = [x for x in range(48,57+1)]
ascii_2 = [x for x in range(97,122+1)]
ascci_list = ascii_1 + ascii_2
#print(ascci_list)
output = []
def convert_words(num,word):
    ascii_1 = [x for x in range(48,57+1)]
    ascii_2 = [x for x in range(97,122+1)]
    ascci_list = ascii_1 + ascii_2
    #print(ascci_list)
    output = []
    for char in word:
        ascii_value = ord(char)
        if (ascii_value + num) in ascci_list:
            result = chr(ascii_value+num)
            #print(result)
            output.append(result)
        else:
            #print(char,ascii_value + num,"NOT IN LIST")
            index = ascci_list.index(ascii_value)
            if (ascii_value + num < ascci_list[-1]):
                index = index + num
                result = chr(ascci_list[index])
                #print(result)h
                output.append(result)
                

            if (index + num >= len(ascci_list)):
                #print(">",index,len(ascci_list))
                index = (index + num) % (len(ascci_list))
                #print("new index",index)
                result = chr(ascci_list[index])
                #print(result)
                output.append(result)
                
    return ''.join(str(x) for x in output)

a = convert_words(num,word)
print(a)
