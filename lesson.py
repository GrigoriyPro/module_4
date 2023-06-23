def f(stroka):
    if stroka.strip() == stroka[::-1].strip():
        return True
    else:
        return False
print(f(input("Ввод: ")))