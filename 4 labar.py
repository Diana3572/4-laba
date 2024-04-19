#4.1
def laba41(x):
    if x % 3 == 0:
         print(f"{x} делится на 3.")
    else:
         print(f"{x} не делится на 3.")
x = int(input("введие число"))
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
def laba44(ticket_number):
    half_length = len(ticket_number) // 2 #выч половину номера, чтобы разделить на 2
    first_half = sum(map(int, ticket_number[:half_length])) # склад цифры первой и второй половины
    second_half = sum(map(int, ticket_number[half_length:]))
    return first_half == second_half

ticket_number = input("Введите номер билета: ")
if laba44(ticket_number):
    print("Этот билет - счастливый!")
else:
    print("Этот билет не является счастливым.")
