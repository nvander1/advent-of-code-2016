compressed = input()
decompressed = []
i = 0
while i < len(compressed):
    if compressed[i] != '(':
        decompressed += [compressed[i]]
        i += 1
    else:
        i += 1
        num_ch = []
        while 1:
            if compressed[i] == 'x':
                i += 1
                break
            num_ch += [compressed[i]]
            i += 1 
        times = []
        while 1:
            if compressed[i] == ')':
                i += 1
                break
            times += [compressed[i]]
            i += 1
        times = int(''.join(times))
        num_ch = int(''.join(num_ch))
        seq = []
        while num_ch > 0:
            seq += compressed[i]
            i += 1
            num_ch -= 1
        decompressed += times*seq
print(len(decompressed))
