def conSum(list, targetValue):
    sums = set()
    total = 0
    for i in list:
        total += i
        s = total - targetValue
        if s in sums:
            return True
        sums.add(total)
    return False

print(conSum([1,3,4,5,6,7,2,9], 11))