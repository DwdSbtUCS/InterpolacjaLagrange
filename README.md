# Interpolacja Lagrange’a

**Trzy punkty → wielomian → wartość funkcji.**

Prosta aplikacja konsolowa w Pythonie, przygotowana w ramach zajęć z metod numerycznych w Akademii WSB. Program wyznacza wielomian interpolacyjny dla trzech punktów oraz oblicza jego wartość dla wybranego argumentu.

## Co robi program?

- Pobiera trzy punkty: $(x_1,y_1)$, $(x_2,y_2)$, $(x_3,y_3)$.
- Sprawdza, czy współrzędne $x$ są parami różne.
- Wyznacza współczynniki $a$, $b$, $c$ wielomianu $W(x)=ax^2+bx+c$.
- Wyświetla współczynniki i postać wielomianu.
- Oblicza $W(x)$ bezpośrednio ze wzoru Lagrange’a dla argumentu podanego przez użytkownika.

## Szybki start

Potrzebny jest **Python 3.6 lub nowszy**. Program nie wymaga dodatkowych bibliotek.

Pobierz repozytorium i w jego katalogu uruchom:

```bash
# Linux / macOS
python3 interpolacja.py
```

```powershell
# Windows z launcherem Pythona
py interpolacja.py
```

Liczby dziesiętne wpisuj **z kropką**, np. `2.5`. Każdą wartość zatwierdź Enterem.

## Przykład działania

Dane pochodzą z funkcji $f(x)=x^2-3x+4$:

| Punkt | x | y |
|:---:|---:|---:|
| 1 | 0 | 4 |
| 2 | 1 | 2 |
| 3 | 2.5 | 2.75 |

```text
x1 = 0
y1 = 4
x2 = 1
y2 = 2
x3 = 2.5
y3 = 2.75

Wynik poniżej:
a = 1
b = -3
c = 4
W(x) = (1)*x^2 + (-3)*x + (4)
Podaj x, dla którego obliczyć W(x): 2
W(2) = 2
```

Otrzymujemy:

$$W(x)=x^2-3x+4$$

Wielomian przechodzi przez wszystkie trzy punkty: $W(0)=4$, $W(1)=2$ i $W(2.5)=2.75$.

## Jak to działa?

Dla trzech różnych węzłów istnieje dokładnie jeden wielomian **stopnia co najwyżej 2**, który odtwarza podane wartości. Może być również liniowy lub stały.

Wzór Lagrange’a:

$$
W(x)=y_1\frac{(x-x_2)(x-x_3)}{(x_1-x_2)(x_1-x_3)}
+y_2\frac{(x-x_1)(x-x_3)}{(x_2-x_1)(x_2-x_3)}
+y_3\frac{(x-x_1)(x-x_2)}{(x_3-x_1)(x_3-x_2)}.
$$

Program zapisuje mianowniki jako `d1`, `d2`, `d3`. Rozwinięcie nawiasów pozwala wyznaczyć współczynniki:

$$a=\frac{y_1}{d_1}+\frac{y_2}{d_2}+\frac{y_3}{d_3}$$

$$b=-\frac{y_1(x_2+x_3)}{d_1}-\frac{y_2(x_1+x_3)}{d_2}-\frac{y_3(x_1+x_2)}{d_3}$$

$$c=\frac{y_1x_2x_3}{d_1}+\frac{y_2x_1x_3}{d_2}+\frac{y_3x_1x_2}{d_3}$$

W ostatnim składniku wzoru na $c$ występuje iloczyn $x_1x_2$. Kod uwzględnia poprawkę literówki z materiałów laboratoryjnych.

### A gdzie są macierze?

Interpolację można opisać układem równań:

$$
\begin{bmatrix}
x_1^2 & x_1 & 1 \\
x_2^2 & x_2 & 1 \\
x_3^2 & x_3 & 1
\end{bmatrix}
\begin{bmatrix}a\\b\\c\end{bmatrix}
=
\begin{bmatrix}y_1\\y_2\\y_3\end{bmatrix}.
$$

Ten program korzysta jednak z bezpośrednich wzorów Lagrange’a. **Nie wykonuje operacji macierzowych** i nie wymaga NumPy.

## Struktura repozytorium

```text
InterpolacjaLagrange/
├── interpolacja.py   # Kod aplikacji
├── README.md         # Opis i instrukcja uruchomienia
└── .gitignore        # Pomijane pliki tymczasowe Pythona
```

## Sprawdzenie poprawności

| Dane | Argument | Oczekiwany wynik |
|---|---:|---|
| (0,4), (1,2), (2.5,2.75) | 2 | a=1, b=-3, c=4; W(2)=2 |
| (1,6), (2,11), (4,27) | 3 | a=1, b=2, c=3; W(3)=18 |
| (0,1), (1,3), (2,5) | 1.5 | a=0, b=2, c=1; W(1.5)=4 |
| Dwa punkty z takim samym x | — | Komunikat o błędzie |

## Zakres i ograniczenia

Projekt realizuje podstawowe zadanie dla **dokładnie trzech punktów**. Ma prostą, proceduralną budowę: zmienne, odczyt danych, warunek i działania matematyczne.

Program zakłada poprawny zapis skończonych liczb. Wpisanie tekstu zamiast liczby może spowodować wyjątek. Obliczenia typu `float` podlegają zaokrągleniom; bardzo bliskie węzły lub skrajne wartości mogą pogorszyć dokładność. Obliczanie poza przedziałem węzłów jest ekstrapolacją.

---

**Autor:** Dawid Sobota · Akademia WSB  
**Przedmiot:** Metody numeryczne
