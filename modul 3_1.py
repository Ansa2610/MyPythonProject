calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    my_tuple = (len(string), string.upper(), string.lower())  # len, upper and lower
    return my_tuple


def is_contains(string, list_to_search):  # arg are a string and a list
    count_calls()
    for i in list_to_search:
        list_to_check = []
        list_to_check.append(i.lower())
    if string.lower() in list_to_check:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Vox populi'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
