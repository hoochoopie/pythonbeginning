f = open('/home/pi/Downloads/a', 'r+')
lines = f.readlines()
sal = []
potential = []
for line in lines:
    curStr = str(line).split('[')[1]
    salStr = curStr.split()[1][1:-4]
    potenStr = curStr.split()[3][1:-3]

    sal.append(int(salStr.replace(',', '')))
    potential.append(float(potenStr))

print(sum(sal) / len(sal))
print(sum(potential) / len(potential))
