
def levenshtein_distance(first: str, second: str) -> int:
    if first == "":
        return len(second)
    elif second == "":
        return len(first)
    elif first[0] == second[0]:
        return levenshtein_distance(first[1:], second[1:])
    else:
        centre = levenshtein_distance(first[1:], second[1:])
        left = levenshtein_distance(first[1:], second)
        right = levenshtein_distance(first, second[1:])
        return min(centre, left, right) + 1
