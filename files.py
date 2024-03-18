f = open('wasteland.txt', mode='wt', encoding='utf-8')
f.writelines(['Hi', 'How are you?'])
f.close()

with open('wasteland.txt', mode='rt', encoding='utf-8') as f:
    for line in f:
        print(line)
