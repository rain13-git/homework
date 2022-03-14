x = int(input("Введите любое целое число x:"))
y = int(input("Введите второе любое целое число y:"))
if x<y:
    x+=1
    print(f'x={x} y={y}')
else:
    x-=1
    print(f'x={x} y={y}')