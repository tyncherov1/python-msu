def solver():
    ru_alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    two_sim = {i+j: [0, 0] for i  in ru_alf for j in ru_alf}

    with open(r"data\Dostoevsky_Povesti_i_rasskazy.txt", encoding="utf-8") as f:
        txt = f.read().lower()
        prev = ""
        for ch in txt:
            if prev in ru_alf and ch in ru_alf:
                two_sim[prev + ch][0] += 1
            prev = ch

        len_txt1 = len(txt)

    with open(r"data\Chekhov_Sochineniya.txt", encoding="utf-8") as f:
        txt = f.read().lower()
        prev = ""
        for ch in txt:
            if prev in ru_alf and ch in ru_alf:
                two_sim[prev + ch][1] += 1
            prev = ch
        len_txt2 = len(txt)

    for pair in two_sim: 
        two_sim[pair][0] /= len_txt1
        two_sim[pair][1] /= len_txt2

solver()