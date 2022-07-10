#2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) 
# = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = False
y = False
z = False

if x == False and y == False:
    xvy = False
else:
    xvy = True

if xvy == False and z == False:
    xvyvz = False
else:
    xvyvz = True

if xvyvz == False:
    rez1 = True
else:
    rez1 = False




if x == False:
    x1 = True
else:
    x1 = False

if y == False:
    y1 = True
else:
    y1 = False

if z == False:
    z1 = True
else:
    z1 = False

if x1 == True and y1 == True:
    x1iy1 = True
else:
    x1iy1 = False

if x1iy1 == True and z1 == True:
    rez2 = True
else:
    rez2 = False



if rez1 == rez2:
    print('¬(X ⋁ Y ⋁ Z)  = ¬X ⋀ ¬Y ⋀ ¬Z')
else:
    print('¬(X ⋁ Y ⋁ Z)  не = ¬X ⋀ ¬Y ⋀ ¬Z')   