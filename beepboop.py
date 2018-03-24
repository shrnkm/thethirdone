for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print('beep'+'boop')
    elif i % 5 == 0:
        print('boop')
    elif i % 3 == 0:
        print('beep')
    else:
        print(i)
