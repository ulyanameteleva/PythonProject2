N, K, M = map(int, input().split())

total_rides = N * 2

sessions = total_rides // K

if total_rides % K > 0:
    sessions = sessions + 1

total_time = sessions * M

print(total_time)