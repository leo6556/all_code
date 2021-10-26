list_n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,2109]



def get_index(list, item):
    low = 0
    high = len(list) - 1
    ko=0

    while high >= low:
        mid = int((low + high)/2)
        guess = list[mid]
        if guess > item:
            high = mid -1
            ko +=1
        if guess < item:
            low = mid + 1
            ko += 1
        if guess == item:
            ko += 1
            print(ko)
            return mid

    return None

print(get_index(list_n, 2109))