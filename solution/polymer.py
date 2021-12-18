with open("data/data_day14.txt") as file:
    polymer = file.readline().strip('\n')
    line = file.readline()
    line = file.readline()
    data = dict()
    while line:
        insertion = line.strip('\n').split('->')
        data[insertion[0].strip(' ')] = insertion[1].strip(' ')
        line = file.readline()
    phrase = dict.fromkeys(data, 0)
    for index in range(len(polymer)-1):
        phrase[polymer[index:index+2]] += 1

# for generations in range(10):
#     next = polymer[0]
#     for index in range(len(polymer)-1):
#         start = polymer[index:index+2]
#         next += data[start]
#         next += start[1]
#     polymer = next

# elements = dict.fromkeys(set([x for x in polymer]), 0)
# for character in polymer:
#     elements[character] += 1

# maximum = elements[max(elements, key=elements.get)]
# minimum = elements[min(elements, key=elements.get)]
# print(maximum-minimum)

for generations in range(40):
    next = dict.fromkeys(phrase, 0)
    for key in phrase:
        next[key[0] + data[key]] += phrase[key]
        next[data[key] + key[1]] += phrase[key]
    phrase = next

elements = dict.fromkeys(data.values(), 0)
for key in phrase:
    elements[key[0]] += phrase[key]
    elements[key[1]] += phrase[key]

for key in elements:
    if elements[key] % 2 == 1:
        elements[key] = (elements[key] // 2) + 1
    else:
        elements[key] = (elements[key] // 2)

maximum = elements[max(elements, key=elements.get)]
minimum = elements[min(elements, key=elements.get)]
print(maximum-minimum)
