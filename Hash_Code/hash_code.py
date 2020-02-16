# first line - Max number pizza slices , Number of different types of pizzas
# Second Line - N integers # slices in each type of pizza 
from itertools import combinations
a,b = map(int,input().rstrip().split(" "))
type_pizza = list(map(int,input().rstrip().split(" ")))
tests = []
for i in range(1,b+1):
    tests.append([pair for pair in combinations(type_pizza,i) if sum(pair)>int(a/2) and sum(pair)<=a])
new_index = []

for each in tests:
    if each:
        new_index.append(([[type_pizza.index(each[i][j]) for j in range(len(each[i]))] for i in range(len(each))]))
        sum_ = [sum(each[i])for i in range(len(each))]
        sum_list = []
        sum_list.append(max(sum_))
        
print("maximum possible number of slices without wasting: %i"%(max(sum_list)))
for each in new_index:
    for x in each:
        new_sum = [type_pizza[i] for i in x]
        if sum(new_sum)==max(sum_list):
            result = x
            break

for r in result:
    print(r,end=" ")
print()