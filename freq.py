def freq(s, t):
    ans = [0 for _ in range(26)]
    for item in t:
        ans[ord(item) - ord('a')] += 1
    for item in s:
        ans[ord(item) - ord('a')] -= 1
    for i,item in enumerate(ans):
        if item == 1:
            return chr(ord('a') + i)
    return 0

print(freq('abdc', 'adcbe'))