# score = [
#     10.0,
#     9.0,
#     8.3,
#     7.1,
#     3.0,
#     9.0
# ]
#
# for i in range(5):
#     for j in range(5):
#         if score[j] < score[j + 1]:
#             temp = score[j]
#             score[j] = score[j + 1]
#             score[j + 1] = temp
#
# print(f'정렬된 점수: { score }')
#
# total = sum(score)
# average = total / len(score)
#
# print(
#     f'최고 점수: { max(score) }, 최저 점수: { min(score) }\n평균: { average }점'
# )


scores = list()
count = 0
while count < 7:
    count += 1
    score = input(f'{ count }번째 점수 입력. ')
    if score.isnumeric():
        scores.append(float(score))

min = min(scores)
max = max(scores)
scores.remove(min)
scores.remove(max)
avg = sum(scores) / len(scores)
print(f'평균: { avg }')
