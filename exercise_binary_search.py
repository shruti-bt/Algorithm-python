def binary_search(number_list, number_to_find):
    left_index = 0
    right_index = len(number_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = number_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number <= number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    
    return -1
def find_all_occurances(number, number_to_find):
    index = binary_search(number, number_to_find)
    indices = [index]

    i = index - 1
    while i >= 0:
        if number[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1
    while i < len(number):
        if number[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)

if __name__ == '__main__':
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15
    indices = find_all_occurances(numbers, number_to_find)
    print(f"Indices of occurances of {number_to_find} are {indices}")


    

