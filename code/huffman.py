import math
import re

# t[a] will be P(X=a) 

def initialize_table():
    t = [0] * 26
    return t

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
        for i in range(len(line)):
            x = line[i]
            if x != '$':
                num += 1
                t[ord(x) - ord('A')] += 1
    for i in range(26):
        t[i] = t[i] / num

def calculate_huffman(t):
    freq, length = {}, {}
    for i in range(26):
        freq[chr(ord('A') + i)] = t[i]
        length[chr(ord('A') + i)] = 0
    while len(freq) > 1:
        k = sorted(freq.keys(), key=lambda w: freq[w])
        a0 = k[0]
        a1 = k[1]
        s = freq[a0] + freq[a1]
        freq.pop(a0)
        freq.pop(a1)
        freq[a0 + a1] = s
        for c in a0 + a1:
            length[c] += 1
    return length

def mean_length(t, l):
    s = 0
    for i in range(26):
        s += t[i] * l[chr(ord('A') + i)]
    return s

if __name__ == "__main__":
    t = initialize_table()
    lines = clean_text("shakespeare.txt")
    build_table(lines, t)
    l = calculate_huffman(t)
    res = mean_length(t, l)
    print(res)
