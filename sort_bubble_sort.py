def bubble_sort(nums):
    #устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True

# Проверям, что оно работает

random_list_of_nums = [5, 4, 2, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)