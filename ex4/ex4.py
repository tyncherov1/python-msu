ru_alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя,.!- '
n_ru = len(ru_alf)
with open("data/key.txt", encoding='utf-8') as f:
    key = f.read().lower()
    new_key = [i for i in key if i in ru_alf]
    key = ''.join(new_key)
    n = len(key)

with open("data/message.txt", encoding='utf-8') as f:
    message = f.read().lower()
    res = ''
    for j, i in enumerate(message):
        if i not in ru_alf: res += i
        else: res += ru_alf[(ru_alf.find(i) + ru_alf.find(key[j % n])) % n_ru]

    # print(res)
    simvols = [[i, res.count(i) / len(res)] for i in set(res)]
    simvols.sort(key=lambda x: x[1], reverse=True)
    print('\n'.join(list(map(str, simvols))))
