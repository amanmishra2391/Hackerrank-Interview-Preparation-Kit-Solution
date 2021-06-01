n = int(input())
ar = list(map(int, input().rstrip().split()))
arr=set(ar)
Sum=0
for x in arr:
    Sum+=(ar.count(x)//2)
print(Sum)
