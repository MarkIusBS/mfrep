password=input()

def ask_password(password):
    count = 0
    correct_password="230911"
    flag = Truei
    while (flag):
        if (password == correct_password):
            print("доступ разрешен")
            flag=False
        else:

            print("Пароли не совпадают")
            count += 1
            password=input()
            if count==3:
                print("Ваши попытки кончились")
                flag=False

print(ask_password(password))
