x, y, w, h = map(int, input().split())

diff = [x, w-x, y, h-y]    # x와 y를 나눠서 생각
print(min(diff))