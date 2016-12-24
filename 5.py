import hashlib

door_id = input()
password = []
index = 0

while 1:
    m = hashlib.md5()
    m.update((door_id+str(index)).encode('utf-8'))
    m_hex = m.hexdigest()
    if m_hex[:5] == '00000':
        password += [m_hex[5]]
        if len(password) == 8:
            break
    index += 1

print(''.join(password))
