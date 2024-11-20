def reverse_num(num: int):
    # Write your code here.
    s = str(num)
    list_s = list(s)
    rev_list_s = list_s[::-1]

    result = int("".join(rev_list_s))

    return result

# Run this file for test
assert reverse_num(1234) == 4321
assert reverse_num(20903) == 30902
assert reverse_num(1_000_234) == 4320001
assert reverse_num(4444) == 4444
assert reverse_num(1) == 1
assert reverse_num(0) == 0