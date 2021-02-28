import matplotlib.pyplot as plt

n = int(input("n = "))
xAnomaly = []
yAnomaly = []
nValues = [i for i in range (n, 0, -1)]
xValues = [x/1000000 for x in range(-100000, 1100000)]
yValues = []
for i in xValues:
	yValues.append(i)

for n in nValues:
	print(n)
	oneOverN = round(1/n, 6)
	oneOverNPlusOne = round((1/(n+1)), 6)
	i = 0
	for x in xValues:
		if x == oneOverN:
			yValues[i] = oneOverNPlusOne
			xAnomaly.append(xValues[i])
			yAnomaly.append(oneOverNPlusOne)
		i += 1
			
i = 0
for y in yValues:
	if y == 0.0:
		yValues[i] = 0.5
		break
	i += 1
		
plt.plot(xValues, yValues, "o", markersize=1)
plt.plot(xAnomaly, yAnomaly, "ro", markersize=1)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

