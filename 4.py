import sys
from collections import Counter
rooms = []
secids = []
chksums = []
mostcom = []
for line in sys.stdin.readlines():
    rooms += [''.join(line[:-11].split('-'))]
    secids += [''.join(line[-12:-8].split('-'))]
    chksums += [line[-7:-2]]
for room in rooms:
    first = sorted(Counter(room).most_common())
    entry = {}
    for item in first:
        key = item[1]
        entry.setdefault(key, []).append(item[0])
    mostcom.append(sorted(entry.items(), reverse=True))
secid_sum = 0
for i in range(len(rooms)):
    expect_chksum = []
    count = 0
    for item in mostcom[i]:
        if count == 5:
            break
        for ch in item[1]:
            if count == 5:
                break
            expect_chksum += [ch]
            count += 1
    if ''.join(expect_chksum) == chksums[i]:
        secid_sum += int(secids[i])
# print(rooms)
# print(secids)
# print(chksums)
# print(mostcom)
print(secid_sum)
