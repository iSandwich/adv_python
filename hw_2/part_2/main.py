from hashlib import md5

def md5_gen(path):
    with open(path, encoding='utf-8') as file:
        for line in file:
            hashed = md5(b'line.strip()')
            yield hashed.hexdigest()

for item in md5_gen('text.txt'):
    print(item)