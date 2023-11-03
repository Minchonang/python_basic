score = [10.0, 9.0, 8.3, 7.1, 3.0, 9.0]
temp = 0
i = 0
while i < len(score) - 1:
   if score[i] < score[i + 1]:
      temp = score[i]
      score[i] = score[i + 1]
      score[i + 1] = temp
   i += 1


i = 1
sum = 0
while i < 5:
   sum += score[i]
result = sum / 4
print(result)

