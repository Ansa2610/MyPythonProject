#color = 'black'
#size = 42
#color == 'white' size == ('42')
color = 'black'
if not(color == 'black'):
    print('Начнем покупки')
else:
    print('покупкам бой')

#age = int(input('Enter your name to know your place in a car '))
#f age <= 8:
#    print('Take back sit in a child chair')
#elif age <= 12:
#    print('Front sit in a car')#elif age <= 18:
#    print('You are able to get driving licence')


#a = 0
#a_slovo = 'holiday in Bali'
#for i in a_slovo: # i - это счетчик цикла
#    print('______')
#    a = a + 1
#    print('i =', i, 'a =', a)
#    print('______')

a = 0
for i in range(3):
    print('___')
    a = a + 1
    print('___')
    for j in range(3):
        print('___')
        a = a + 1
        print('i =', i, 'j =', a)
        print('___')
