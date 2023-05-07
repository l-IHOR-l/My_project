'''
A-Z -> chr(65)-chr(90)
'''

digit = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def decrypt_cesar(step:int, a:str = 'Hello World'):
    q = ''
    for i in a:
        if i.isupper():
            q += chr(ord(i)%90 + 5).upper()
        elif i.isdigit() or i.is


