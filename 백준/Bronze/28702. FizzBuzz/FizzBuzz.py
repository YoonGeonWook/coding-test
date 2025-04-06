def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return str(i)

# 입력
seq = [input().strip() for _ in range(3)]

# 숫자가 있다면 추정 시작점 찾아서 시도해보기 (최대 3번)
for idx, val in enumerate(seq):
    if val.isdigit():
        possible_start = int(val) - idx
        for i in range(possible_start - 1, possible_start + 2):  # 여유 범위
            if [fizzbuzz(i), fizzbuzz(i+1), fizzbuzz(i+2)] == seq:
                print(fizzbuzz(i+3))
                exit()

# 숫자가 없다면 fallback: 1부터 탐색 (필요하면)
i = 1
while True:
    if [fizzbuzz(i), fizzbuzz(i+1), fizzbuzz(i+2)] == seq:
        print(fizzbuzz(i+3))
        break
    i += 1
