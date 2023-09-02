import time

num = 100

l = []
for i in range(1, 100000000001):
    l.append(i)
print(l)

left = 0
right = len(l)

start = time.time()
while left <= right:
    mid = (left+right)//2

    if l[mid] == num:
        print(mid+1)
        break
    if l[mid] > num:
        right = mid
    if l[mid] < num:
        left = mid
end = time.time()
print(end-start)
