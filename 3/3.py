import timeit
import os

def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1
    
    skip = {pattern[i]: max(1, m - i - 1) for i in range(m - 1)}
    
    i = 0
    while i <= n - m:
        for j in range(m - 1, -1, -1):
            if text[i + j] != pattern[j]:
                i += skip.get(text[i + m - 1], m)
                break
        else:
            return i  
    return -1  


def kmp_search(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1
    
    lps = [0] * m
    j = 0  
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    
    i = j = 0  
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                return i - j 
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def rabin_karp(text, pattern, prime=101):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1
    
    base = 256  
    pattern_hash = 0
    text_hash = 0
    h = 1  
    
    for i in range(m - 1):
        h = (h * base) % prime
    
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime
    
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                return i  
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime
    return -1



def read_text(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        return f.read()

text1 = read_text("стаття_1.txt")
text2 = read_text("стаття_2.txt")


existing_substring = text1[:30]  
non_existing_substring = "це унікальна фраза, якої немає в тексті"

for name, func in zip(["Boyer-Moore", "KMP", "Rabin-Karp"], [boyer_moore, kmp_search, rabin_karp]):
    time1 = timeit.timeit(lambda: func(text1, existing_substring), number=10)
    time2 = timeit.timeit(lambda: func(text1, non_existing_substring), number=10)
    time3 = timeit.timeit(lambda: func(text2, existing_substring), number=10)
    time4 = timeit.timeit(lambda: func(text2, non_existing_substring), number=10)
    
    print(f"{name}:\n"
          f"  Article 1 (existing): {time1:.6f}s\n"
          f"  Article 1 (non-existing): {time2:.6f}s\n"
          f"  Article 2 (existing): {time3:.6f}s\n"
          f"  Article 2 (non-existing): {time4:.6f}s\n")
