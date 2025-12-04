# MMN12

def max_pos_seq(lst):
    """
    Return the length of the longest contiguous subsequence of positive numbers in a list.

    Args:
        lst: A list of numeric values.

    Returns:
        int: The maximum number of consecutive elements in lst that are strictly greater than 0.
    """
    max_pos = 0
    current_pos = 0
    for num in lst:
        if num > 0:
            current_pos += 1
            if current_pos > max_pos:
                max_pos = current_pos
        else:
            current_pos = 0
    return max_pos


def num_distance(lst, num):
    """
    Compute the distance between the first and last occurrence of a given value
    in terms of elements outside the range between them.

    The distance is defined as:
        number of elements before the first occurrence of num + number of elements after the last occurrence of num

    Args:
        lst: A list of values.
        num: The value to search for in lst.

    Returns:
        int: The calculated distance as defined above, or -1 if num does not appear in lst.
    """
    left_distance = -1
    right_distance = -1
    i = 0
    for n in lst:
        if n == num:
            if left_distance < 0:
                left_distance = i
            right_distance = (len(lst) - 1) - i

        i += 1
    if left_distance < 0:
        return -1
    return left_distance + right_distance


def is_balanced_idx(lst, idx):
    """
    Check whether a given index in a list is 'balanced'.

    An index is considered balanced if:
        sum of all elements to the left of idx ==
        product of all elements to the right of idx.

    Args:
        lst: A list of numeric values.
        idx: The index to check.

    Returns:
        bool: True if the index is balanced, False otherwise.

    Raises:
        IndexError: If idx is outside the valid range of indices for lst.
    """
    if idx < 0 or idx >= len(lst):
        raise IndexError("Index out of bounds")

    left_sum = sum_all(lst[:idx])
    right_prod = 1
    for n in (lst[idx + 1:]):
        right_prod *= n

    return left_sum == right_prod


def max_balanced_idx(lst):
    """
    Find the maximum index in a list that is 'balanced' according to is_balanced_idx.

    A balanced index is one where:
        sum(lst[:idx]) == product(lst[idx+1:]).

    Args:
        lst: A list of numeric values.

    Returns:
        int | None: The largest balanced index if any exist, otherwise None.
    """
    max_idx = 0
    try:
        for i in range(len(lst)):
            if is_balanced_idx(lst, i):
                max_idx = i

    except IndexError:
        return None
    if max_idx:
        return max_idx
    else:
        return None


def magic_list(mat):
    """
    Determine whether a matrix is 'magic' by comparing frame and inner sums.

    A matrix is considered magic here if:
        sum of all frame elements ==
        sum of all inner elements.

    The frame includes the first and last rows, and the first and last columns.
    Corner elements are counted only once.

    Args:
        mat: A rectangular 2D list (matrix) of numeric values.

    Returns:
        bool: True if the sum of frame elements equals the sum of inner elements,
              False otherwise.
    """
    fram_sum = (
        sum_all(mat[0]) +
        sum_all(mat[-1]) +
        sum_all(row[0] for row in mat) +
        sum_all(row[-1] for row in mat) -
        mat[0][0] - mat[0][-1] - mat[-1][0] - mat[-1][-1]
    )
    inner_sum = 0
    for i in range(1, len(mat) - 1):
        inner_sum += sum_all(mat[i][1:-1])
    return fram_sum == inner_sum


def sum_all(lst):
    """
    Calculate the sum of all elements in a list.

    Args:
        lst: A list of numeric values.

    Returns:
        int | float: The sum of all elements in lst.
    """
    total = 0
    for num in lst:
        total += num
    return total
