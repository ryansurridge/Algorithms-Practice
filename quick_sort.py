unsorted_list = []

length = int(input("How many numbers are in your list? : "))
for i in range(0, length):
    unsorted_list.append(float(input("Number "+str(i+1)+": ")))

print(unsorted_list)

counter = 0
def quickSort(seq):

    if len(seq) <= 1:
        return seq

    else:
        pivot = seq[0]

        items_low = []
        items_high = []
        
        for i in range(1,len(seq)):
            if seq[i] <= pivot:
                items_low.append(seq[i])
            else:
                items_high.append(seq[i])
            global counter+=1
        return quickSort(items_low) +[pivot]+ quickSort(items_high)

 
print(quickSort(unsorted_list), counter)

