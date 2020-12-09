from random import *
pos = range(1,51)
pos = list(pos)
people = range(1,51)
people = list(people)

for i in people:
    people[i-1] = randint(5,50)

for j in range(0,50):
    if 5 <= people[j] <= 15:
        pos[j] = "O"
    else:
        pos[j] = " "

for l in range(0,50):
    print(f"[{pos[l]}] {l+1}번째 손님 (소요시간 : {people[l]}분)")

pos_list = pos.count("O")
print(f"총 탑승 승객 : {pos_list}분")