def solution(X, Y, D):
    # How far the frog has to travel
    distance = Y - X

    # How many full jumps fit into the distance.
    # Use math instead of a loop, because the distance could be up to a billion.
    jumps = distance // D

    # If there's leftover distance, the full jumps fall short,
    # so the frog needs one more jump
    if distance % D != 0:
        jumps = jumps + 1

    return jumps