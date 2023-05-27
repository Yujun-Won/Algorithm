T = int(input())

week = {'MON': 6, 'TUE': 5, 'WED': 4, 'THU': 3, 'FRI': 2, 'SAT': 1, 'SUN': 7}

for i in range(1, T+1):
    today = input()

    print(f"#{i} {week[today]}")