r = [0, 0.25, 0.65, 0.8, 0.9, 1.0]
c = int("0101010110111011011100101", 2) / 2 ** 25
w = ['', 'A', 'B', 'C', 'D', 'E']
ans = ""
s = 1.0
for _ in range(12):
    for i in range(1, len(r)):
        if c <= s * r[i]:
            ans += w[i]
            c -= s * r[i - 1]
            s *= r[i] - r[i - 1]
            break
print(ans)