ages = [20, 22, 19, 25]
print(ages)

for age in ages:
    print(age + 2)

ages.append(30)
ages[0] = 21
ages.remove(19)
print(ages)