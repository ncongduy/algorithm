def y(x):
    return x**2 + 4

def square_cal(a, b, n, f):
    square = 0
    x = a
    delta_X = (b - a)/n

    for i in range(n):
        square += f(x)*delta_X
        x += delta_X
    
    return square

print(f'square_50:  {square_cal(0, 4, 50, y)}')
print(f'square_100:  {square_cal(0, 4, 100, y)}')
print(f'square_1000:  {square_cal(0, 4, 1000, y)}')
print(f'square_10,000:  {square_cal(0, 4, 10000, y)}')
print(f'square_1,000,000:  {square_cal(0, 4, 1000000, y)}')
print(f'square_10,000,000:  {square_cal(0, 4, 10000000, y)}')


