import mmn13
import copy


def run_test(test_name, actual, expected):
    """
    Helper function to print test results clearly.
    """
    if actual == expected:
        print(f"[PASS] {test_name}")
        return True
    else:
        print(f"[FAIL] {test_name}")
        print(f"\tExpected: {expected}")
        print(f"\tGot:      {actual}")
        return False


def test_question_1():
    print("--- Testing Question 1 (arrange) ---")

    # Original list elements from visual example: 7, -2, -5, 61, 4, -1, 1, 33
    lst_orig = [7, -2, -5, 61, 4, -1, 1, 33]
    lst_test = copy.deepcopy(lst_orig)
    expected = [-2, -5, -1, 7, 61, 4, 1, 33]

    try:
        mmn13.arrange(lst_test)
        run_test("Example 1", lst_test, expected)
    except Exception as e:
        print(f"[ERROR] Q1 crashed: {e}")

    # Additional Test: Already sorted
    lst_sorted = [-1, -2, 1, 2]
    expected_sorted = [-1, -2, 1, 2]
    mmn13.arrange(lst_sorted)
    run_test("Already arranged", lst_sorted, expected_sorted)

    # Additional Test: All positive
    lst_pos = [10, 20, 30]
    mmn13.arrange(lst_pos)
    run_test("All positive", lst_pos, [10, 20, 30])
    print("")


def test_question_2():
    print("--- Testing Question 2 (most_frequent) ---")

    # Example 1
    lst1 = [1, 3, 3, 2, 1, 3, 2, 2, 2]
    run_test("Example 1 (val=2)", mmn13.most_frequent(lst1), 2)

    # Example 2 (Tie breaker - smallest value)
    lst2 = [5, 4, 5, 4, 6]
    run_test("Example 2 (Tie breaker)", mmn13.most_frequent(lst2), 4)

    # Example 3 (Single element)
    lst3 = [10]
    run_test("Example 3 (Single)", mmn13.most_frequent(lst3), 10)

    # Example 4 (Empty)
    lst4 = []
    run_test("Example 4 (Empty)", mmn13.most_frequent(lst4), None)
    print("")


def test_question_3():
    print("--- Testing Question 3 (balanced_exp) ---")

    run_test("Example 1 '(())'", mmn13.balanced_exp("(())"), True)
    run_test("Example 2 ')(()'", mmn13.balanced_exp(")(()"), False)
    run_test("Example 3 '' (Empty)", mmn13.balanced_exp(""), True)

    # Part A examples from text
    run_test("Part A.1 '(((()))'", mmn13.balanced_exp("(((()))"), False)
    run_test("Part A.3 ')'", mmn13.balanced_exp(")"), False)
    run_test("Part A.5 '(((())'", mmn13.balanced_exp("(((())"), False)
    print("")


def test_question_4():
    print("--- Testing Question 4 (is_hill) ---")

    run_test("Example 1 (1926 -> True)", mmn13.is_hill(1926), True)  # 9 is hill
    run_test("Example 2 (1234 -> False)", mmn13.is_hill(1234), False)
    run_test("Example 3 (73 -> False)", mmn13.is_hill(73), False)

    # Edge case
    run_test("Small number (5)", mmn13.is_hill(5), False)
    print("")


def test_question_5():
    print("--- Testing Question 5 (search) ---")

    run_test("Example 1 ('ewxabcs', 'abc')", mmn13.search("ewxabcs", "abc"), True)

    # Logic dictates if s2 is in s1 it is True.
    run_test("Identity ('a', 'a')", mmn13.search("a", "a"), True)

    run_test("Example 3 ('weqasdzxc', 'c')", mmn13.search("weqasdzxc", "c"), True)

    # Implicit/Negative examples
    run_test("Not found ('abc', 'z')", mmn13.search("abc", "z"), False)
    run_test("Empty s2 ('abc', '')", mmn13.search("abc", ""), True)
    print("")


def test_question_6():
    print("--- Testing Question 6 (switch_duality) ---")

    run_test("Example 1 (5490 -> True)", mmn13.switch_duality(5490), True)
    run_test("Example 2 (212 -> True)", mmn13.switch_duality(212), True)
    run_test("Example 3 (3 -> True)", mmn13.switch_duality(3), True)
    run_test("Example 4 (1823 -> False)", mmn13.switch_duality(1823), False)

    # Edge case: Same parity neighbors
    run_test("Two evens (22)", mmn13.switch_duality(22), False)
    print("")


def main():
    print("========================================")
    print("   Tester for Maman 13 - 2026a")
    print("========================================")

    try:
        test_question_1()
        test_question_2()
        test_question_3()
        test_question_4()
        test_question_5()
        test_question_6()
    except NameError as ne:
        print(f"\n[CRITICAL ERROR] Missing function or typo in naming: {ne}")
        print("Please ensure all function names match the PDF exactly.")
    except Exception as e:
        print(f"\n[CRITICAL ERROR] An unexpected error occurred: {e}")

    print("========================================")
    print("   Tests Completed")
    print("========================================")


if __name__ == "__main__":
    main()