score = 0

n = list(map(float, input().split()))

for i in range(8):
    score += n[i]

result = score / 8

print(f"{result:.1f}")