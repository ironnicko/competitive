from sys import stdin,stdout
GETIN = stdin.readline

PUT = stdout.write

MOD = 10e4 

n, queries = map(int, GETIN().rstrip().split())
hash_map = {x+1 : i for x, i in enumerate(map(int, GETIN().rstrip().split()))}
sumed_up = sum(hash_map.values())
visited = set()
flag= None
for i in range(queries):
    s = GETIN().rstrip().split()
    if s[0] == '1':
        if not flag:
            sumed_up += int(s[2]) - hash_map[int(s[1])]
            hash_map[int(s[1])] = int(s[2])
        else:
            if int(s[1]) in visited:
                sumed_up += int(s[2]) - hash_map[int(s[1])]
            else:
                sumed_up = sumed_up - flag + int(s[2])
                hash_map[int(s[1])] = int(s[2])
                visited.add(int(s[1]))   
    else:
        flag = int(s[1])

        visited=set()

        sumed_up = n * flag


    PUT(str(sumed_up)+"\n")