# Interpolacja Lagrange'a dla trzech punktów.
# Wyznaczamy W(x) = a*x**2 + b*x + c.

x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
x3 = float(input("x3 = "))
y3 = float(input("y3 = "))

if x1 == x2 or x1 == x3 or x2 == x3:
    print("Błąd: współrzędne x muszą być różne.")
else:
    d1 = (x1 - x2) * (x1 - x3)
    d2 = (x2 - x1) * (x2 - x3)
    d3 = (x3 - x1) * (x3 - x2)

    a = y1 / d1 + y2 / d2 + y3 / d3
    b = -(y1 * (x2 + x3) / d1
          + y2 * (x1 + x3) / d2
          + y3 * (x1 + x2) / d3)
    # Poprawiony ostatni licznik wzoru (6): y3*x1*x2.
    c = (y1 * x2 * x3 / d1
         + y2 * x1 * x3 / d2
         + y3 * x1 * x2 / d3)

    print("\nWynik poniżej:")
    print(f"a = {a:g}")
    print(f"b = {b:g}")
    print(f"c = {c:g}")
    print(f"W(x) = ({a:g})*x^2 + ({b:g})*x + ({c:g})")

    x = float(input("Podaj x, dla którego obliczyć W(x): "))
    wynik = (y1 * (x - x2) * (x - x3) / d1
             + y2 * (x - x1) * (x - x3) / d2
             + y3 * (x - x1) * (x - x2) / d3)
    print(f"W({x:g}) = {wynik:g}")
