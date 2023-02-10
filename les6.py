password=input()

def ask_password(password):
    correct_password="230911"
    while (True):
        if (password == correct_password):
            print("доступ разрешен")
        else:
            print("Пароли не совпадают")
ask_password(password)
print(ask_password(password))
