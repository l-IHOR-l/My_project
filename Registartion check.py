from string import digits
class Registraion:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @property
    def password(self):
        print('getter called')
        return self.password

    @staticmethod
    def is_in_digit(password:str):
        for digit in digits:
            if digit in password:
                return True
            return False

    @staticmethod
    def is_easy_pasword(password: str):
        with open(r'F:\Download\[Артем Егоров] Объектно-ориентированное программирование на Python (2022)\2. Методы и свойства\11. Практика по методам и свойствам (property)/easy_passwords.txt', 'r') as f:
            q = f.read()
        if password in q:
            return True
        return False

    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError('Пароль должен бить строкой')
        if len(value)<4:
            raise ValueError('Пароль слишком короткий, мин 4 символа')
        if len(value)>16:
            raise ValueError('Пароль слишком длиний, макс 16 символов')
        if Registraion.is_in_digit(value):
            raise ValueError('Пароль должен иметь хотяби 1 цифру')
        if Registraion.is_easy_pasword(value):
            raise ValueError('Пароль очень легко взломать. Пробуйте другой')
        self.__password = value

