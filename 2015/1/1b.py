with open('big.txt') as f:
    data = f.read()[:-1]

cumsum = [data[:i].count('(') - data[:i].count(')') for i in range(len(data))]
signs = [-1+2*int(i>=0) for i in cumsum]
print(signs.index(-1))
