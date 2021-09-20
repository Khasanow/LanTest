с= int(input())
b= int(input())
if b != 0:
    print(с/b)
else:
    print('delenie nevozmozno')
    b = int(input('vvedite ne null'))
    if b==0:
        print('you are failed')
    else:
        print(с/b)
