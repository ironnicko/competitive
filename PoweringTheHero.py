from heapq import heappop, heappush

t = int(input())
while t:
    int(input())
    list = {}
    final= 0
    list =[]
    for i in map(int, input().split()):
        if i != 0:
            heappush(list, -i)
        else:
            if len(list) > 0:
                final += -heappop(list)
    print(final)
    t -= 1