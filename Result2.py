import statistics

data = []
rinda = []

with open("data.csv", "r") as dati:
    for line in dati:
        rinda = line.rstrip().split(",")
        data.append(rinda)

saraksts = []

for i in range(len(data)):
    vertiba = data[i][5]
    nozare = data[i][1]
    #if nozare == "Insurance":
        #saraksts.append(int(vertiba))
    #if nozare == "Agriculture":
        #saraksts.append(int(vertiba))
    #if nozare == "Publishing":
        #saraksts.append(int(vertiba))
    if nozare == "Finance":
        saraksts.append(int(vertiba))

#list.sort(saraksts)    
#max_vertiba = max(saraksts)
#x = statistics.mean(saraksts)

#print("6.", max_vertiba)
#print("7.", len(saraksts))
#print("8.", int(x))
#print("9. ", saraksts)
print("10.", sum(saraksts[::2]))


