# ==========================================
#           FULL TESTER FOR MMN 12
# ==========================================


from mmn12 import max_pos_seq, num_distance, is_balanced_idx, max_balanced_idx, magic_list

def run_full_tests():
    print("--- Starting Full Tests for MMN 12 ---")
    all_passed = True

    # ---------------------------------------------------------
    # Test Question 1: max_pos_seq
    # ---------------------------------------------------------
    print("\nTesting Q1: max_pos_seq...")
    try:
        # Example 1 (Reconstructed with negatives to make logic work)
        # Sequence: 3, 2, 10, 5 (Length 4)
        lst1 = [3, 2, 10, 5, -2, 4, 1, 2]
        res1 = max_pos_seq(lst1)
        assert res1 == 4, f"Ex1 Failed: Expected 4, got {res1}"

        # Example 2 (Reconstructed: Max length is 3)
        lst2 = [2, 4, 3, -2, 1, 2, -1, 2, 3]
        res2 = max_pos_seq(lst2)
        assert res2 == 3, f"Ex2 Failed: Expected 3, got {res2}"

        # Example 3 (All negative)
        lst3 = [-3, -4, -2]
        res3 = max_pos_seq(lst3)
        assert res3 == 0, f"Ex3 Failed: Expected 0, got {res3}"

        # Example 4 (Mixed)
        lst4 = [-2, 3, 2, 1, -1, 2]
        res4 = max_pos_seq(lst4)
        assert res4 == 3, f"Ex4 Failed: Expected 3, got {res4}"

        print(">> Q1 Passed!")
    except Exception as e:
        print(f">> Q1 Failed: {e}")
        all_passed = False

    # ---------------------------------------------------------
    # Test Question 2: num_distance
    # ---------------------------------------------------------
    print("\nTesting Q2: num_distance...")
    try:
        # List from PDF: [4, 1, 3, 7, 1, 1, 7, 7, 21, 11]
        lst_q2 = [4, 1, 3, 7, 1, 1, 7, 7, 21, 11]

        # 1. Check for 7
        # First idx: 3. Last idx: 7. Dist from end: (10-1)-7 = 2. Total: 3+2=5.
        assert num_distance(lst_q2, 7) == 5, f"Failed for 7: Expected 5, got {num_distance(lst_q2, 7)}"

        # 2. Check for 3 (The example you requested)
        # "המרחק של המספר 3 הוא 9, עבור 7 מהקצה הימני ו- 2 מהקצה השמאלי"
        # Index is 2. Left dist: 2. Right dist: (9-2)=7. Sum: 9.
        val_3_dist = num_distance(lst_q2, 3)
        assert val_3_dist == 9, f"Failed for 3: Expected 9, got {val_3_dist}"

        # 3. Check for 4
        # Index 0. Left: 0. Right: 9. Sum: 9.
        assert num_distance(lst_q2, 4) == 9, f"Failed for 4: Expected 9, got {num_distance(lst_q2, 4)}"

        # 4. Check for missing number (13) -> -1
        assert num_distance(lst_q2, 13) == -1, f"Failed for 13: Expected -1, got {num_distance(lst_q2, 13)}"

        print(">> Q2 Passed!")
    except Exception as e:
        print(f">> Q2 Failed: {e}")
        all_passed = False

    # ---------------------------------------------------------
    # Test Question 3: is_balanced_idx & max_balanced_idx
    # ---------------------------------------------------------
    print("\nTesting Q3: Balanced Indices...")
    try:
        # List 2 from PDF
        lst_q3 = [7, -7, 12, 6, 5, 2, 1, 9, 26]

        # Check is_balanced_idx
        assert is_balanced_idx(lst_q3, 7) is True, "is_balanced_idx Failed: Index 7 should be True"
        assert is_balanced_idx(lst_q3, 0) is False, "is_balanced_idx Failed: Index 0 should be False"
        assert is_balanced_idx(lst_q3, len(lst_q3) - 1) is False, "is_balanced_idx Failed: Last index should be False"

        # Check Exception
        try:
            is_balanced_idx(lst_q3, 100)
            print("Error: IndexError not raised for out of bounds!")
            all_passed = False
        except IndexError:
            pass  # Expected

        # Check max_balanced_idx
        res_max = max_balanced_idx(lst_q3)
        assert res_max == 7, f"max_balanced_idx Failed: Expected 7, got {res_max}"

        # Check list with no balanced index
        lst_none = [1, 2, 3, 4]
        assert max_balanced_idx(lst_none) is None, "max_balanced_idx Failed: Expected None"

        print(">> Q3 Passed!")
    except Exception as e:
        print(f">> Q3 Failed: {e}")
        all_passed = False

    # ---------------------------------------------------------
    # Test Question 4: magic_list
    # ---------------------------------------------------------
    print("\nTesting Q4: magic_list...")
    try:
        # Mat1 (Magic)
        mat1 = [
            [1, 1, 1, 1],
            [1, 3, 3, 1],
            [1, 3, 3, 1],
            [1, 1, 1, 1]
        ]
        assert magic_list(mat1) is True, "Failed: mat1 should be Magic"

        # Mat2 (Magic)
        mat2 = [
            [1, 2, 1, 1, 2],
            [1, 4, 4, 4, 1],
            [3, 3, 4, 3, 1],
            [2, 3, 1, 1, 2]
        ]
        assert magic_list(mat2) is True, "Failed: mat2 should be Magic"

        # Mat3 (Not magic)
        mat3 = [
            [1, 1, 1],
            [1, 5, 1],
            [1, 1, 1]
        ]
        assert magic_list(mat3) is False, "Failed: mat3 should NOT be Magic"

        print(">> Q4 Passed!")
    except Exception as e:
        print(f">> Q4 Failed: {e}")
        all_passed = False

    print("\n---------------------------------------")
    if all_passed:
        print("✅ ALL TESTS PASSED SUCCESSFULLY! ✅")
    else:
        print("❌ SOME TESTS FAILED. CHECK OUTPUT. ❌")
    print("---------------------------------------")


if __name__ == "__main__":
    run_full_tests()