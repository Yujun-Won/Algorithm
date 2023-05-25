T = int(input())

for i in range(1, T+1):
    number_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
                   "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    string_dict = {0: "ZRO", 1: "ONE", 2: "TWO", 3: "THR", 4: "FOR",
                   5: "FIV", 6: "SIX", 7: "SVN", 8: "EGT", 9: "NIN"}

    case_num = input().split()[1]

    str_list = input().split()
    num_list = []
    for str in str_list:
        num_list.append(number_dict[str])
    num_list.sort()

    result = []
    for num in num_list:
        result.append(string_dict[num])

    print(f"#{i}")
    for res in result:
        print(res, end=' ')
    print()