def lcs(s1, s2):
    if s1 < s2:
        return lcs(s2, s1)
    n = len(s1)
    m = len(s2)
    dp = [0] * (m+1)
    for i in range(1, n+1):
        prev_diagonal = 0
        for j in range(1, m+1):
            backup = dp[j]
            if s1[i-1] == s2[j-1]:
                dp[j] = prev_diagonal + 1
            else:
                dp[j] = max(dp[j], dp[j-1])
            prev_diagonal = backup
    return dp[m]

s1 = "ababfc"
s2 =  "abaxfcj"
print(lcs(s1, s2))