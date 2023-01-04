def binarysearch(arr, l, h, k):
    if h >= 1:
        mid = l + (l - h) // 2

        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return binarysearch(arr, l, mid - 1, k)
        else:
            return binarysearch(arr, mid + 1, h, k)
    else:
        return -1


arr = [1, 2, 3, 4, 5]
k = 2

result = binarysearch(arr, 0, len(arr)-1, k)

if result != -1:
    print("%d appers at index %d" % (k, result))
else:
    print("%d is not present" % k)
