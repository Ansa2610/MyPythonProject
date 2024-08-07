grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # СПИСОК LIST оценок для каждого ученика в алфавитном порядке
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # МНОЖЕСТВО SET содержит неупорядоченную последовательность имён всех учеников в классе
grades_0 = sum(grades[0])/len(grades[0])
grades_1 = sum(grades[1])/len(grades[1])
grades_2 = sum(grades[2])/len(grades[2])
grades_3 = sum(grades[3])/len(grades[3])
grades_4 = sum(grades[4])/len(grades[4])
print(grades_0, grades_1, grades_2, grades_3, grades_4)
average_point = [[grades_0], [grades_1], [grades_2], [grades_3], [grades_4]]
print(average_point)
students1 = sorted(students)
print(students1)
my_dict = {students1[0]: grades_0, students1[1]: grades_1, students1[2]: grades_2, students1[3]: grades_3,students1[4]: grades_4}
print(my_dict)