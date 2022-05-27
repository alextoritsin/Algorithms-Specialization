# uses python3
import random

# def naive_window(nums, n, m):
#     ans = [0] * (n - m + 1)
#     for i in range(len(ans)):
#         ans[i] = max(nums[i:i + m])

#     return " ".join([str(i) for i in ans])


def max_window(nums, n, m):
    if n == m:
        return str(max(nums))

    if m == 1:
        return " ".join([str(i) for i in nums])
      
    else:
        i, j = 0, 0
        ans = [0] * (n - m + 1)

        ints = n // m

        left_stack = [0] * m
        right_stack = [0] * m

        block = 1
        while block < ints:
            shift = 1
            last_r, last_l = float('-inf'), float('-inf') 
            index = block * m
            for i in range(m):
                right_stack[i] = max(nums[index], last_r)
                last_r = right_stack[i]

                left_stack[i] = max(nums[index - shift], last_l)
                last_l = left_stack[i]

                shift, index = shift + 2, index + 1
            
            ans[block * m - m] = last_l
            k = 0
            for j in range(block * m - m + 1, block * m):
                ans[j] = max(right_stack[k], left_stack[-2 - k])
                k += 1        
            block += 1

        rem = n % m

        if rem == 0:
            ans[j + 1] = right_stack[-1]
        else:
            last_l = last_r = float('-inf') 
            index = block * m - 1   
            for i in range(m):
                left_stack[i] = max(nums[index], last_l)
                last_l = left_stack[i]
                index -= 1

            index = block * m
            for i in range(rem):
                right_stack[i] = max(nums[index], last_r)
                last_r = right_stack[i]
                index += 1
            
            k = 0
            if j != 0:
                ans[j + 1] = right_stack[-1]
                for i in range(j + 2, len(ans)):
                    ans[i] = max(right_stack[k], left_stack[m - 2 - k])
                    k += 1
            else:
                ans[j] = left_stack[-1]
                for i in range(j + 1, len(ans)):
                    ans[i] = max(right_stack[k], left_stack[m - 2 - k])
                    k += 1  

        return " ".join([str(i) for i in ans])


if __name__ == '__main__':
    n = int(input())
    nums = [int(i) for i in input().split()]
    m = int(input())

    print(max_window(nums, n, m))
    
    # n = random.randint(1, 20)
    # nums = [0] * n
    # for i in range(n):
    #     nums[i] = random.randint(1, 10)

    # m = random.randint(1, n)
    # print("Array:", nums)
    # print("Window:", m)
    # print("Naive:", naive_window(nums, n, m))
    # print("Test:", max_window(nums, n, m))
    # print("Result:", naive_window(nums, n, m) == max_window(nums, n, m))