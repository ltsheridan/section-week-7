with open('sherlock.txt', 'r', encoding='utf-8') as f_small:
    sherlock_content = f_small.read()

with open('sherlock.big.txt', 'a', encoding='utf-8') as f_big:
    for i in range(300):
        f_big.write(sherlock_content)
