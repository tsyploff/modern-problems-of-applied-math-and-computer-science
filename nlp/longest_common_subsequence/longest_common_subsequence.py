
def common_prefix(first: str, second: str) -> str:
    c = 0
    n = min(len(first), len(second))
    while c < n and first[c] == second[c]:
        c += 1
    return first[:c]


def longest_common_subsequence(first: str, second: str) -> str:
    result = ""
    for i in range(len(first)):
        for j in range(len(second)):
            result = max(result, common_prefix(first[i:], second[j:]), key=len)
    return result
