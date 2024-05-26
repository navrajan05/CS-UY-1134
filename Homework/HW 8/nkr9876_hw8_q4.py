from nkr9876_BinarySearchTreeMap import BinarySearchTreeMap


def find_min_abs_difference(n):
    values = []
    for key in n:
        values.append(key)

    if len(values) < 2:
        raise Exception("less than two elements")
    else:
        minimum = None
        for i in range(1, len(values)):

            # These are be in order, so taking the absolute value isn't necessary.
            # The question does specify absolute difference though, so I oblige.

            diff = abs(values[i] - values[i-1])

            if minimum is None:
                minimum = diff
            else:
                minimum = min(minimum, diff)

        return minimum