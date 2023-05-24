T = int(input())

for i in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    
    company_a = P * W
    company_b = Q

    if W > R:
        company_b += S * (W - R)

    print(f"#{i} {min(company_a, company_b)}")