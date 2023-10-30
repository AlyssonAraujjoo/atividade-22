import time

print("numeros pares entre 0 e 50")

n = 0

for n in range (1, 51):
    if n % 2 == 0:
        print(n, end=' ')
        time.sleep(1)
    else:
        print("")