password=input()

def ask_password(password):
    count = 0
    correct_password="230911"

    if (password == correct_password):
        print("доступ разрешен")
    else:
        print("доступ запрещен")


print(ask_password(password))
