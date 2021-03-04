items = []

num_items = int(input("How many items have you got? : "))

for i in range(0, num_items):
    item = [input("\nLabel: "), int(input("Size: "))]
    items.append(item)
print("Your items are: "+str(items))


bin_size = int(input("What is the size of your bins/containers? : "))

bins = [["bin1", bin_size, []]]    #bin array [bin_name, remaining capacity, [items]]


#bubble sort

def bubbleSort(arr): 
    for i in range(len(arr)-1):  
        for j in range(0, len(arr)-i-1):  
            if arr[j][1] < arr[j+1][1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubbleSort(items)

            
for i in range(0, len(items)): # for every item in the items array

    added = False #initially they aren't added to any bin

    for b in range(0, len(bins)): #for every bin in the bin array

        if items[i][1] <= bins[b][1]: #check if the size of the current item is lower than the capacity of the bin
            bins[b][2].append(items[i]) #if it is, add the item to that bin
            bins[b][1] = bins[b][1] - items[i][1] #take the capacity of the bin added to, and subtract the size of the item
            added = True #the item has been added
            break #can stop checking the bins

    if (added != True):
        bins.append(["bin"+str(int(bins[len(bins)-1][0][3])+1), (bin_size-items[i][1]), [items[i]]])

for i in range(0, len(bins)):
    print("\n"+bins[i][0]+"("+str(bin_size)+") : "+ str(bins[i][2]))
