
# not finished youtube solution

with open("data/data_day16.txt") as file:
    hexValues = {'0': "0000", '1': "0001",
                 '2': "0010", '3': "0011",
                 '4': "0100", '5': "0101",
                 '6': "0110", '7': "0111",
                 '8': "1000", '9': "1001",
                 'A': "1010", 'B': "1011",
                 'C': "1100", 'D': "1101",
                 'E': "1110", 'F': "1111"}
    data = ''
    for character in file.readline().strip('\n'):
        data += hexValues[character]
# print(data)


def DoIt(index):
    packetVersion = int(data[index:index+3], 2)
    packetTypeID = int(data[index+3:index+6], 2)
    index += 6
    if packetTypeID == 4:
        literaValue = ""
        group = '1'
        while group[0] == '1':
            group = data[index:index+5]
            literaValue += data[index+1:index+5]
            index += 5
        if data[index] == '0':
            lengthOfSubpacket = int(data[index+1:index+12], 2)
            index += 16
            totalPacketVersions = packetVersion
            total = 0
            while total < lengthOfSubpacket:
                value, newIndex = DoIt(index)
                total += (newIndex - index)
                index = newIndex
                totalPacketVersions += value
            return totalPacketVersions, index
        else:
            numberOfSubpackets = int(data[index+1:index+12], 2)
            index += 12
            totalPacketVersions = packetVersion
            total = 0
            for i in range(numberOfSubpackets):
                value, newIndex = DoIt(index)
                total += (newIndex - index)
                index = newIndex
                totalPacketVersions += value
            return totalPacketVersions, index


def Get():
    value, index = DoIt(0)
    return value


print(Get())
