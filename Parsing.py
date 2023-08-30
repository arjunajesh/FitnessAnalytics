def colonSplit(string):
    return string.rsplit(": ")

def commaSplit(string):
    return string.rsplit(", ")

def xSplit(string):
    array = string.rsplit("x")
    for x in range(0, 2):
        array[x] = int(array[x])
    return array

def xSplitArray(array):
    for x in range(0, len(array)):
        array[x] = xSplit(array[x])
    return array

def maxWeight(array):
    maxWeight = -1
    for x in array:
        if x[0] > maxWeight:
            maxWeight = x[0]
    return maxWeight
            
def maxVolume(array):
    maxVolume = -1
    for x in array:
        volume = x[0]*x[1]
        if volume > maxVolume:
            maxVolume = volume
    return maxVolume
    
def totalVolume(array):
    volume = 0
    for x in array:
        current_volume = x[0]*x[1]
        volume += current_volume
    return volume


test_phrase = "Bench Press: 138x3, 140x3, 105x5, 120x4"

array = colonSplit(test_phrase)
#print(new)

exercise_name = array[0]
exercise_data = array[1]

sets_array = commaSplit(exercise_data)
#print(sets_array)

new_sets_array = xSplitArray(sets_array)
#print(new_sets_array)

print("Max Weight = " + str(maxWeight(new_sets_array)))
print("Max Volume = " + str(maxVolume(new_sets_array)))
print("Total Volume = " + str(totalVolume(new_sets_array)))

