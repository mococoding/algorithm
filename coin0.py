n, k = map(int, input().split())
coin_list = [int(input()) for _ in range(n)]

cnt = 0
coin_list.sort(reverse=True)

for coin in coin_list:
    if k == 0:
        break
    cnt += k // coin
    k %= coin
    print(cnt, k, coin)
print(cnt)