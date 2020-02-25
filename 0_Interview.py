string = ["2019", "view" , "code" , "2017", "2018", "coding", "code", "coding", "2019", "2017", "2019", "2019"]
word_1= "2019"
word_2= "2018"

# def shortest_distance(string,word_1,word_2):
#     distance = 0
#     i_match = 0
#     j_match = 0
#     for i in range(len(string)):
#         j = len(string) - i - 1
#         print(i,j,i_match,j_match,distance,sep="  ")
#         if (word_1 == string[i]):
#             i_match = i
#         if (word_2 == string[j]):
#             j_match = j
#         distance = j_match - i_match
#         i = i+1
#         j = j-1
#     if (i_match == 0 or j_match == 0 ):
#         return False
#     else:
#         return distance

# print(shortest_distance(string,word_1,word_2))

def shortest_distance(string,word_1,word_2):
    distance = 9999
    start_index = -1
    for i in range(len(string)):
        if (string[i] == word_1 or string[i] == word_2):
            print(i,start_index,string[i],string[start_index],sep="   ")
            if (start_index != -1 and string[i] != string[start_index]):
                print(distance,start_index,i,sep=">>")
                distance = min(distance, i-start_index)
            start_index = i
    return distance
    
print(shortest_distance(string,word_1,word_2))