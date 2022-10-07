cathet1, cathet2, hypotenuse = float(input('Введите длину первого катета: ')), float(input('Введите длину второго катета: ')), float(input('Введите длину гипотенузы: '))
if cathet1**2 + cathet2**2 == hypotenuse**2:
    print('Площадь =', cathet1*cathet2/2, 'Периметр =', cathet1+cathet2+hypotenuse)
else:
    print('Ошибка, данный треугольник не прямоугольный')