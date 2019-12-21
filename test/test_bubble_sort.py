def bubble_sort(arry):
    n = len(arry)  # 获得数组的长度
    for i in range(n):
        for j in range(1, n - i):
            if arry[j - 1] > arry[j]:  # 如果前者比后者大
                arry[j - 1], arry[j] = arry[j], arry[j - 1]  # 则交换两者
    return arry


array_1 = [5, 4, 3, 1]
print(array_1)
bubble_sort(array_1)
print(array_1)
