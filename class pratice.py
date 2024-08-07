# Создадим форму для регистрации пользователя(регистрация, логин, пароль)


class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Hello! Choose action: \n1 - Enter\n2 - Registration\n'))
        if choice == 1:
            login = input('Enter login: ')
            password = input('Enter password: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Enter is ok, {login}')
                    break
                else:
                    print('Неверный пароль')
            else:
                print('No such user.')
        if choice == 2:
            user = User(input('Enter login: '), password := input('Enter password: '),
                        password2 := input('Retype password: '))
            if password != password2:
                print("Пароли не совпадают, попробуйте еще раз.")
                continue
            database.add_user(user.username, user.password)