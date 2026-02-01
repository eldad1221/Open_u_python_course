def arrange(lst: list):
    """
    Reorder a list in-place so that all negative values come before non-negative values.

    This performs a stable-like insertion: whenever a negative value is found, it is shifted left
    until it sits just after the previous negative value (preserving the relative order of the
    negative elements).

    Args:
        lst: List of numbers to reorder.

    Returns:
        The same list instance, after reordering.
    """
    for i in range(len(lst)):
        if lst[i] < 0:
            for j in range(i, 0, -1):
                if lst[j - 1] < 0:
                    break
                a = lst[j]
                lst[j] = lst[j - 1]
                lst[j - 1] = a
    return lst


def most_frequent(lst: list):
    """
    Return the most frequent value in a list of positive integers.

    The implementation uses a frequency array sized by ``max(lst)`` and counts occurrences by
    indexing ``num - 1``. Therefore, the function assumes all values in ``lst`` are positive
    integers (>= 1). If ``lst`` is empty, ``None`` is returned.

    Args:
        lst: List of positive integers (>= 1).

    Returns:
        The integer value that appears most frequently, or ``None`` if ``lst`` is empty.
    """
    if not lst:
        return None
    freq = [0] * max(lst)
    for num in lst:
        freq[num - 1] += 1
    max_freq = max(freq)
    return freq.index(max_freq)+1


def balanced_exp(s: str) -> bool:
    """
    Check whether parentheses in a string are balanced.

    Only the characters '(' and ')' affect the balance; all other characters are ignored.
    The expression is considered balanced if scanning left-to-right never yields more closing
    parentheses than opening ones, and the total counts match at the end.

    Args:
        s: Input string.

    Returns:
        True if parentheses are balanced, otherwise False.
    """
    open_count = 0
    close_count = 0
    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            close_count += 1
        if close_count > open_count:
            return False
    return close_count == open_count


def is_hill(num: int) -> bool:
    """
    Determine whether a number contains a 'hill' pattern in its digits.

    A 'hill' is any sequence of three consecutive digits (reading right-to-left) where the middle
    digit is strictly greater than both neighbors (e.g., 4-9-1 forms a hill at 9).
    The function checks the rightmost triplet, then recursively checks the number without its
    rightmost digit. Numbers with fewer than 3 digits return False.

    Args:
        num: Non-negative integer to examine.

    Returns:
        True if any 3-digit window forms a hill; otherwise False.
    """
    if num < 100:
        return False
    else:
        third_from_right = num % 1000 // 100
        second_from_right = num % 100 // 10
        rightmost = num % 10
        if third_from_right < second_from_right > rightmost:
            return True
        else:
            return is_hill(int(num / 10))


def search(s1: str, s2: str) -> bool:
    """
    Recursively check whether one string is a prefix of any suffix of another.

    This is effectively an implementation of substring search: it returns True if ``s2`` occurs
    anywhere within ``s1`` (including at the start).

    Args:
        s1: The string to search within.
        s2: The substring to search for.

    Returns:
        True if ``s2`` is contained in ``s1``, otherwise False.
    """
    len_s1 = len(s1)
    len_s2 = len(s2)
    if len_s1 < len_s2:
        return False
    elif s1[:len_s2] == s2:
        return True
    elif len_s1 == len_s2:
        return False
    else:
        return search(s1[1:], s2)

def switch_duality(num: int) -> bool:
    """
    Check whether adjacent digits in a number alternate parity.

    For the decimal representation of ``num``, each neighboring pair of digits must have opposite
    parity (even/odd). Single-digit numbers satisfy the condition by definition.

    Args:
        num: Non-negative integer to examine.

    Returns:
        True if parities alternate for all adjacent digits; otherwise False.
    """
    if num < 10:
        return True
    else:
        rightmost = num % 10
        second_from_right = num % 100 // 10
        if (rightmost % 2 == 0 and second_from_right % 2 == 1) or (rightmost % 2 == 1 and second_from_right % 2 == 0):
            return switch_duality(int(num / 10))
        else:
            return False
