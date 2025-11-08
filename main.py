from math import sin, cos

eps: float = 1e-2

def main():
    x = float(input("Ввод >> "))
    if abs(denominator := sin(2 * x)) < eps:
        raise ZeroDivisionError("Знаменатель близок к нулю!")

    enumerator = ( sin(x) + cos(x * 2) )**2

    f_x = enumerator / denominator

    print(f"x={x}")
    print(f"f={f_x:.6}")

if __name__ == "__main__":
    main()
