def bin_src(l,n):
    l.sort()
    low = 0
    high = len(l)-1
    p = -1
    while low <= high:
        mid = (low+high)//2
        if l[mid] == n:
            p = mid
            print("found at ",p)
            break
        else:
            if n > l[mid]:
                low = mid+1
            else:
                high = mid-1
    else:
        print("not found")
l = [1,2,3,4,5,6,7,8,9]
n = int(input("Enter a number: "))
print(bin_src(l,n))



