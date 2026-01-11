def permutations(s):
    if len(s) == 1:
        return [s]

    result = []
    for i in range(len(s)):
        for p in permutations(s[:i] + s[i+1:]):
            perm = s[i] + p
            if perm not in result:
                result.append(perm)
    return result


print(permutations("ab"))
