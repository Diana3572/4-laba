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
        tmp = 100 / a
        print(tmp)
    except ValueError:
        print("Error! " + str("введите число"))
    except ZeroDivisionError:
        print("Error! " + str("введите число не равное 0"))

#4.3
def laba43():
    user_input = input("Введите дату месяц и год (в формате ДД.ММ.ГГГГ): ")
    if is_magic_date(user_input):
        print("Это магическая дата!")
    else:
        print("Это не магическая дата.")

if name == "__laba43__":
    laba43()

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