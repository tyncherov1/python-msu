file = open(r"data\input.txt", encoding="utf-8").read().lower()

# print(sum("111"))
simvols = [[i, file.count(i)/len(file)] for i in set(file)]

# simvols = [[file[i], sum((1 for j in file if file[i] == j))/len(file)] for i in range(len(file)) if file[i] not in file[i+1:]]
simvols.sort(key = lambda x: -x[1])
print(simvols)
