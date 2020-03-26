pi = 0.0
for i in range(1, 10000, 4):
    pi += 4/i
    pi -= 4/(i+2)
print(pi)
