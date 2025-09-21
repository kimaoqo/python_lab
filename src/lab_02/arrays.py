def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    try:
        min(nums), max(nums)
    except ValueError:
        return "ValueError"
    else:
        return min(nums), max(nums)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))


def flatten(mat: list[list | tuple]) -> list:
    flatt = []
    for x in mat:
        if type(x) is str:
            return TypeError
        else:
            flatt += list(x)
    return flatt