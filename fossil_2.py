score = [9,10,9,8]
rank_list = []
#score=sorted(score,reverse=True)
print(score)
for i,value in enumerate(score):
    rank = score.index(value)+1
    print(value,rank)
    rank_list.append(rank)
    print(rank_list)
# rank = [score.index(i)+1 for i in sorted(score)[::-1]]
