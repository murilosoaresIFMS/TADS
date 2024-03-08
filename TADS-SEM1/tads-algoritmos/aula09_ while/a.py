c = 0
n = 12
d = 0

while(d != 1):
    d = n / 10
    n = d
    c += 1

print(f"O número digitado tem {c} digitos")