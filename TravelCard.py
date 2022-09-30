n = int(input())

trip_1, trip_2 = 0, 0

time = []
f = [0] * (n+1)
for i in range(n):
    time.append(int(input()))

    while time[i] - time[trip_1] >= 90:
        trip_1 +=1
    while time[i] - time[trip_2] >= 1440:
        trip_2 += 1
    f[i+1] = min(min(f[trip_1] + 50, f[trip_2] + 120), f[i] + 20)
    print(f[i+1] - f[i])