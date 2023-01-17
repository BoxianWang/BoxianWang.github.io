import math
import re

# t[a][b] will be P(X=a, Y=b) 

def initialize_table():
    t = []
    for _ in range(26):
        t.append([0] * 26)
    return t

# calculate entropy from a vector, assuming normalized
def entropy(v):
    H = 0
    for p in v:
        if p != 0:
            H += p * math.log2(1/p)
    return H

# calculate H(X)
def entropy_X(t):
    marginals = [sum(r) for r in t]
    return entropy(marginals)

# calculate H(Y)
def entropy_Y(t):
    marginals = [0] * 26
    for i in range(26):
        for j in range(26):
            marginals[i] += t[j][i]
    return entropy(marginals)

# calculate H(Y|X)
def conditional_entropy(t):
    H = 0
    for x in range(26):
        px = sum(t[x])
        cond_y = [p / px for p in t[x]] # re-normalize
        H += px * entropy(cond_y)
    return H

# calculate I(Y:X)
def mutual_info(t):
    return entropy_Y(t) - conditional_entropy(t)

def clean_text(fn):
    with open(fn) as f:
        lines = [line.rstrip('\n') for line in f]
        lines = lines[244:-20]
        lines = [line.upper() for line in lines]
        lines = [re.sub('[^A-Z]+', '$', line).strip('$') for line in lines]
        return lines

def build_table(lines, t):
    num = 0
    for line in lines:
        for i in range(len(line) - 1):
            x = line[i]
            y = line[i + 1]
            if x != '$' and y != '$':
                num += 1
                t[ord(x) - ord('A')][ord(y) - ord('A')] += 1
    for i in range(26):
        for j in range(26):
            t[i][j] = t[i][j] / num

if __name__ == "__main__":
    t = initialize_table()
    lines = clean_text("shakespeare.txt")
    build_table(lines, t)
    print("H(X): ", entropy_X(t))
    print("H(Y): ", entropy_Y(t))
    print("H(Y|X): ", conditional_entropy(t))
    print("I(Y:X): ", mutual_info(t))