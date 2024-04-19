#4.1
def laba41(x):
    x = int(input("введие число"))
        if x % 3 == 0:
             print(f"{x} делится на 3.")
        else:
             print(f"{x} не делится на 3.")

laba41(x)

#4.2
def laba42():
    try:
        a = int(input("введите число: "))
        b = 100 / a
        print(b)
    except ValueError:
        print("Error! " + str("введите число"))
    except ZeroDivisionError:
        print("Error! " + str("введите число не равное 0"))

#4.3
def laba43():
    a=input("введите дату через точку(ДД.ММ.ГГГГ): ")
    d=int(a[0]+a[1])
    m=int(a[3]+a[4])
    y=int(a[8]+a[9])
    if d*m==y:
        print("True")
    else:
        print("False")

#4.4
def laba44():
    a = input("Введите номер билета: ")
    if a.isdigit():
        if len(a) % 2 == 0:
            b = len(a) // 2
            f = a[:b]
            s = a[b:]

            if sum(map(int, f)) == sum(map(int, s)):
                print("это счастливый билет")
            else:
                print("это несчастливый билет")
        else:
            print("введите чётное кол-во цифр")
    else:
        print("введите цифры")
laba41
