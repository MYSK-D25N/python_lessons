dates = {}
pointsA = {}
pointsB = {}
max = -999
bestDate = {}
mostGas = {}

with open("travels.txt","r") as f:
    for i in f:
          l = i.split(" ")
          date = l[0] + l[1]
          pointA = l[2]
          pointB = l[3]
          distance = int(l[4])
          gas = int(l[5])
          weight = int(l[6])

          if date not in dates:
            dates[date] = [0,0,0]
            dates[date][0] += 1
            dates[date][1] += weight
            dates[date][2] += distance
          else:
            dates[date][0] += 1
            dates[date][1] += weight
            dates[date][2] += distance

          if pointA not in pointsA:
            pointsA[pointA] = weight
          else:
            pointsA[pointA] += weight

          if pointB not in pointsB:
            pointsB[pointB] = [weight, distance, gas]
          else:
            pointsB[pointB][0] += weight
            pointsB[pointB][1] += distance
            pointsB[pointB][2] += gas



for i in dates:
    if dates[i][0] > max:
        max = dates[i][0]
        bestDate = {}
        bestDate[i] = dates[i]

max = -999

for i in pointsB:
    print(i)
    avrgGas = pointsB[i][1] / pointsB[i][2]
    if avrgGas > max2:
        max2 = avrgGas
        mostGas = {}
        mostGas[i] = avrgGas

print(bestDate)
print(pointsA["Липки"])
print(dates["1октября"][2])
print(pointsA)
print(pointsB)
print(mostGas)
