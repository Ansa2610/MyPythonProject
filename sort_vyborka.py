def selection_sort(nums):
    # значение i соответствует кол-ву отсортированных значений
    for element in range(len(nums)):
        #  исходно считаем наименьший первый элемент
        lowest_value_index = element
        # этот цикл перебирает несортированные элементы
        for j in range(element + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # самый маленький элемент меняем с первым в списке
        nums[element], nums[lowest_value_index] = nums[lowest_value_index], nums[element]

random_list_of_nums = [12, 8, 3, 20, 11]
selection_sort(random_list_of_nums)
print(random_list_of_nums)