#Largest Sum subarray

def largest_sum_subarray(list, k):
    current_sum = 0
    max_sum = 0
    output_list = list[:k]
    start_index = 0
    current_sum = sum(list[:k])
    max_sum = current_sum

    for i in range(k,len(list)):
        current_sum += list[i] - list[i-k]

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = i - k + 1
    output_list = list[start_index: start_index+k]
    


    return output_list, max_sum

my_list = [-2, -5, 6, 4, 3, 8, -1, 0, 9]
k = 4
print(largest_sum_subarray(my_list, k))
