
def reverse_string(s: str):
    # Write your code here.
    # Do not use list reverse method
    list_s = list(s)
    rev_list_s = list_s[::-1]

    result = "".join(rev_list_s)

    return result

assert reverse_string("abcd") == "dcba"
assert reverse_string("a3bE5dQPos") == "soPQd5Eb3a"
assert reverse_string("aka$aka") == "aka$aka"