'''Создайте класс UsepMait , у которого есть:
1. конструктор _init__ , принимающий 2 аргумента: логин и почтовый адрес. Их необходимо сохранить в экземпляр как
атрибуты login и _emaiI (обратите внимание, защищенный атрибут)
2. метод геттер get_emait , которое возвращает защищенный атрибут _emaiI ;
З. метод сеттер set_emait , которое принимает в виде строки новую почту. Метод должен проверять, что в новой почте есть
только один символ @ и после нее есть точка. Если данные условия выполняются, новая почта сохраняется в атрибут _emaiI, в
противном случае выведите сообщение
4. создайте свойство emai1 , у которого геттером будет метод get_email, а сеттером - метод set_email'''
class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if isinstance(new_email, str):
            if new_email.count('a') == 1 and '.' in new_email[new_email.find('@'):]:
                self.__email = new_email
        else:
            print('Email error')
    email = property(fget=get_email, fset=set_email)

k = UserMail('ihor', 'igor@gmail.com')
print(k.email)