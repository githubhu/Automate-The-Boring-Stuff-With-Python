
tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]
coldwidth=[0]*len(tableData)

for i in range(len(tableData)):
    for j in range(len(tableData[i])):
        if (coldwidth[i] <= len(tableData[i][j])):
            coldwidth[i] =len(tableData[i][j])

for i in range(len(tableData[0])):
    print(' '.join(record[i].rjust(coldwidth[j]) for j, record in enumerate(tableData)))

