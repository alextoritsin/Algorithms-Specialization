# uses python3
import math

def prim_calc(n):
    steps_array = [(0, 0)] * n
    for num in range(2, n + 1):
        step = num - 1
    
        step_plus_1 = steps_array[step - 1][0] + 1
        step_over_2 = steps_array[int(num / 2) - 1][0] + 1 if num % 2 == 0 else math.inf
        step_over_3 = steps_array[int(num / 3) - 1][0] + 1 if num % 3 == 0 else math.inf

        if step_over_3 <= step_over_2:
            if step_over_3 <= step_plus_1:
                steps_array[step] = (step_over_3, 3)
            else:
                steps_array[step] = (step_plus_1, 1)
        else:
            if step_over_2 <= step_plus_1:
                steps_array[step] = (step_over_2, 2)
            else:
                steps_array[step] = (step_plus_1, 1)

    ans = [n]
    while n != 1:
        if steps_array[n - 1][1] == 1:
            n -= 1
        elif steps_array[n - 1][1] == 2:
            n = int(n / 2)
        else:
            n = int(n / 3)
        ans.append(n)
    
    ans.reverse()
    ans = [str(num) for num in ans]

    return steps_array[-1][0], ans


if __name__ == '__main__':
    n = int(input())
    m, steps = prim_calc(n)
    print(m)
    print(" ".join(steps))