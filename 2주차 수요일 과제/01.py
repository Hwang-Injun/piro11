question = ['dogaa', 'dogaaseddd', 'dogaasedds']

min_length = 100
for i in range(len(question)):          # 리스트의 가장 짧은 요소는 min_length
    if len(question[i]) < min_length:
        min_length = len(question[i])
#x = [0, 0, 0]
#for j in range(len(question)):
 #   x[j] = [question[j][0:i] for i in range(len(question[j]))]
a = [question[0][0:i] for i in range(len(question[0]) + 1)]
b = [question[1][0:i] for i in range(len(question[1]) + 1)]
c = [question[2][0:i] for i in range(len(question[2]) + 1)]
#print(x[0][1], b, c)
result = ""
#result1 = ""


#for i in range(min_length):
 #   for j in range(1, len(question)-1):
  #      if x[j+1][i] == x[j][i]:
   #         result1 = x[j][i]      #자동화 실패 ㅠㅠ

for i in range(min_length + 1):
    if a[i] == b[i] == c[i]:
        result = a[i]
    else:
        break
print(result)
