characters = list(set(input()))

mobis = ["M", "O", "B", "I", "S"]
result = []

for char in characters:
    if char in mobis:
        result.append(char)

if sorted(mobis) == sorted(result):
    print("YES")
else:
    print("NO")