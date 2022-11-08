from array import array

def createArray(troubleCodes):
    print(troubleCodes)
    splitAction = troubleCodes.split(" ")
    array = []
    for x in range(len(splitAction)):
        array.append(splitAction[x])
    print(array)

troubleCodes = input("Please paste the list that you want to convert here: ")
createArray(troubleCodes)
