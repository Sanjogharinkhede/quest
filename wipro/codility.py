def solution(N, A):
    a = [0] * N
    current_max = 0  # The maximum value of any counter
    last_max_update = 0  # The value to apply during lazy propagation

    for i in A:
        if 1 <= i <= N:
            # Increase i
            if a[i - 1] < last_max_update:
                # Apply lazy propagation to the specific counter
                a[i - 1] = last_max_update
            a[i - 1] += 1
            # Update the current maximum
            current_max = max(current_max, a[i - 1])
        elif i == N + 1:
            # Max counter i
            last_max_update = current_max

    # Apply lazy propagation to all a
    for i in range(N):
        if a[i] < last_max_update:
            a[i] = last_max_update

    return a

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))