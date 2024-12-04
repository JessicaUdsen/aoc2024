# Input file test_input.txt is the sample, input.txt is the final input
# sum(resultList) is the answer to part 1
# simScore is the answer to part 2

import pandas as pd

file = 'input.txt'
df = pd.read_fwf(file, names=['Col1', 'Col2'])

Col1 = df['Col1'].tolist()
Col2 = df['Col2'].tolist()

Col1.sort()
Col2.sort()

resultList = [abs(a - b) for a, b in zip(Col1, Col2)]

# print(sum(resultList))

common = set(Col1).intersection(set(Col2))
# print(common)

simScore = 0

for x in common:
    simScore += x * Col1.count(x) * Col2.count(x)

print(simScore)
