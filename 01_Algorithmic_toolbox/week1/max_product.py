# python3
# import random

def max_pairwise_product_perf(array):
    copy_array = sorted(array)
    return copy_array[-1] * copy_array[-2]

def max_pairwise_product_fast(array):

    max_index1 = 0

    for i in range(1, len(array)):
        if array[i] > array[max_index1]:
            max_index1 = i

    max_index2 = 1 if max_index1 == 0 else 0

    for j in range(max_index2, len(array)):
        if array[j] > array[max_index2] and j != max_index1:
            max_index2 = j
            
    return array[max_index1] * array[max_index2]

        
    
if __name__ == '__main__':
    # for i in range(10):
    #     length = random.randint(2, 10)
    #     array = [0] * length
    #     for j in range(length):
    #         array[j] = random.randint(1, 10)

    #     res_test = max_pairwise_product_fast(array)
    #     res_perf = max_pairwise_product_perf(array)
    #     if res_test != res_perf:
    #         print(f"Test failed with test res {res_test}, perf res {res_perf}")
    #         break
    #     else:
    #         print("OK!")
        
    n = int(input())
    array = [int(elem) for elem in input().split()]
    print(max_pairwise_product_fast(array))

    
