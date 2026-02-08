

def is_identity(mat: list[list], x: int, size: int) -> bool:
    for i in range(size**2):
        if i % (size + 1) == 0:
            if mat[x + i % size][x + i // size] != 1:
                return False
        else:
            if mat[x + i % size][x + i // size] != 0:
                return False
    return True

def max_matrix(mat: list[list]) -> int:
    scan_range = int((len(mat) - 3)/2) + 1
    for i in range(scan_range):
        size = len(mat) - i * 2
        if is_identity(mat=mat, x=i, size=size):
            return size
    return 0


def big_small(s: str) -> bool:
    # תנאי בסיס: אורך חייב להיות זוגי
    if len(s) % 2 != 0:
        return False
    return check(s)

def remove_first(target: str, text: str):
    """
    מחזיר (found, new_text)
    found = האם target נמצא ב-text
    new_text = text אחרי הסרה של ההופעה הראשונה של target
    (בלי להשתמש ב-in)
    """
    if text == "":
        return False, ""

    if text[0] == target:
        return True, text[1:]

    found, rest = remove_first(target, text[1:])
    if found:
        return True, text[0] + rest
    return False, text  # לא נמצא -> מחזירים את הטקסט המקורי

def check(text: str) -> bool:
    if text == "":
        return True

    c = text[0]
    target = c.swapcase()

    found, remaining = remove_first(target, text[1:])
    if not found:
        return False

    return check(remaining)

