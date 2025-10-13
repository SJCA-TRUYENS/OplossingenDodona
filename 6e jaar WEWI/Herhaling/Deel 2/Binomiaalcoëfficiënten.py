n = int(input())
k = int(input())

def fac(num):
    answer = 1
    while num > 1:
        answer *= num
        num -= 1
    return answer

print(int(fac(n) / (fac(k) * fac(n-k))))