# 冒泡排序：将列表从小到大排序
def bubble_sort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 最后 i 个元素已经就位，不需要再比较
        for j in range(0, n-i-1):
            # 如果当前元素 > 下一个元素，交换它们
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 测试一下
if __name__ == "__main__":
    test_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(test_list)
    print("排序后的列表:", sorted_list)
