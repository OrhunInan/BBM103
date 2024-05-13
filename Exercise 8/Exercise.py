def min_max_avg(arr, minn, maxn, avgn):
    if len(arr) == 0:
        return maxn, minn, (avgn/10)

    elif len(arr) == 10:
        minn = arr[-1]
        maxn = arr[-1]
    else:
        if arr[-1] > maxn:
            maxn = arr[-1]
        elif arr[-1] < minn:
            minn = arr[-1]
    
    avgn += arr[-1]
    arr.pop()
    return min_max_avg(arr, minn, maxn, avgn)
arr = [int(input()) for i in range(10)]
minn = 0
maxn = 0
avgn = 0
print(min_max_avg(arr, minn, maxn, avgn))