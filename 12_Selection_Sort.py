def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallesIdx = currentIdx
        for i in range(currentIdx + 1,len(array)):
            if(array[smallesIdx] > array[i]):
                smallesIdx = i
        swap(currentIdx,smallesIdx,array)

def swap(i,j,array):
    array[i], array[j] = array[j], array[i]