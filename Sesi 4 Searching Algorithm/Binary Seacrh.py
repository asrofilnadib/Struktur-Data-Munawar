# syarat binary itu harus udah di sorting dulu, baru bisa dicari nilainya
# l (nilai terendah), r (nilai tertinggi)
def binary(arr, l, r, x):
    if r >= 1:
        mid = l + (r - l) // 2  # indikasinya disini itu indeksnya, bukan nilainya

        if arr[mid] == x:  # representasi jika x ada di tengah
            return mid
        elif arr[mid] > x:
            return binary(arr, l, mid - 1, x)  # subarray yang kiri
        else:
            return binary(arr, mid + 1, r, x)  # subarray yang kanan
    else:
        return -1


# binary serch itu udah di sorting
arr = [3, 7, 9, 13, 20, 27, 37, 57]
arr1 = []
x = 20

result = binary(arr, 0, len(arr)-1, x)

if result != -1:
    print("nilai %d berada pada indeks ke-%d" % (x, result))
else:
    print("nilai tidak ada dalam indeks")