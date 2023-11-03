score = [
    10.0,
    9.0,
    8.3,
    7.1,
    3.0,
    9.0
]

for i in range(5):
    for j in range(5):
        if score[j] < score[j + 1]:
            temp = score[j]
            score[j] = score[j + 1]
            score[j + 1] = temp

print(f'정렬된 점수: { score }')


sum = 0
for i in range(1, 5):
    sum += score[i]

result = sum / 4

print(
    f'최고 점수: { max(score) }, 최저 점수: { min(score) }\n평균: { result }점'
)
