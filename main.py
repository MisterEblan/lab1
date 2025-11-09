from math import sin, sqrt

# Значение аргумента, при котором знаменатель обнуляется
BAD_X: float = 3.0

def main():
    x = float(input("Ввод >> "))
    if x == BAD_X:
        raise ZeroDivisionError(f"Функция не определена в точке {BAD_X}")

    f_x = sin(x) * sqrt( (x+3) / (x-3) )

    print(f"x={x}")
    print(f"f={f_x:.6}")

if __name__ == "__main__":
    main()
