from sys import stdin

raw_ips = [line for line in stdin.readlines()]
ips = []

for line in raw_ips:
    ip = {'normal': [], 'hyper': []}
    entry = []
    for ch in line:
        if ch == '[' or ch == '\n':
            ip['normal'].append(''.join(entry))
            entry = []
            continue
        if ch == ']':
            ip['hyper'].append(''.join(entry))
            entry = []
            continue
        entry.append(ch)
    ips.append(ip)
count = 0
for ip in ips:
    foundNormal = False
    foundHyper = False
    for item in ip['hyper']:
        if foundHyper:
            break
        for i in range(len(item)-3):
            if item[i:i+2] == item[i+3:i+1:-1] and item[i] != item[i+1]:
                foundHyper = True
                break
    if not foundHyper:
        for item in ip['normal']:
            if foundNormal:
                break
            for i in range(len(item)-3):
                if item[i:i+2] == item[i+3:i+1:-1] and item[i] != item[i+1]:
                    foundNormal = True
                    break
    if foundNormal and not foundHyper:
        count += 1
print(count)
