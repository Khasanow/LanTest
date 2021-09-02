a = int(input())
b = int(input())
if b != 0:
    print(a / b)
else:
        print('деление невозможно')
        b = input('введите не нулевое значение')
        if b==0:
            print('вы не справились')
        else:
           print(a / b)
