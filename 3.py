import sys
data = [line[:-1].split() for line in sys.stdin]

count = 0

for item in data:
    a = int(item[0])
    b = int(item[1])
    c = int(item[2])

    if a+b>c and b+c>a and a+c>b:
        count += 1

print(count)
