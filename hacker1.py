def funnyString(s):
    r = s[::-1]  # Reverse the string
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
            return "Not Funny"
    return "Funny"
