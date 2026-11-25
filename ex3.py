ru_alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
two_sim = [i+j for i  in ru_alf for j in ru_alf]

with open("Dostoevsky_Povesti_i_rasskazy.txt", encoding="utf-8") as f1:
    with open("Chekhov_Sochineniya.txt", encoding="utf-8") as f2:
        txt_1 = f1.read().lower()
        txt_2 = f2.read().lower()
        couple = [[i, txt_1.count(i), txt_2.count(i)] for i in two_sim]
        total_c1 = sum((i[1]) for i in couple)
        total_c2 = sum((i[2]) for i in couple)
        sims = [[i[0], i[1] / total_c1, i[2] / total_c2, max(i[1] / total_c1, i[2] / total_c2) / min(i[1] / total_c1, i[2] / total_c2) if min(i[1] / total_c1, i[2] / total_c2) > 0 else 0.0] for i in couple]
        sims.sort(key = lambda x: -x[3])


j = 1
for i in sims:
    if i[3] > 1.5: 
        print(j, i[0], i[3]) 
        j+=1