class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02d} eur"

    def __eq__(self, another: "Money"):
        return self._euros == another._euros and self._cents == another._cents

    def __lt__(self, another: "Money"):
        if self._euros < another._euros:
            return True
        elif self._euros == another._euros and self._cents < another._cents:
            return True
        else:
            return False

    def __gt__(self, another: "Money"):
        if self._euros > another._euros:
            return True
        elif self._euros == another._euros and self._cents > another._cents:
            return True
        else:
            return False

    def __ne__(self, another: "Money"):
        if self._euros != another._euros:
            return True
        elif self._euros == another._euros and self._cents != another._cents:
            return True
        else:
            return False

    def __add__(self, another: "Money"):
        total_cents = self._cents + another._cents
        total_euros = self._euros + another._euros + total_cents // 100
        remaining_cents = total_cents % 100

        return Money(total_euros, remaining_cents)

    def __sub__(self, another: "Money"):
        total_cents_self = self._euros * 100 + self._cents
        total_cents_another = another._euros * 100 + another._cents
        if total_cents_self < total_cents_another:
            raise ValueError("a negative result is not allowed")

        total_cents_result = total_cents_self - total_cents_another
        result_euros = total_cents_result // 100
        result_cents = total_cents_result % 100

        return Money(result_euros, result_cents)

if __name__ == '__main__':
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1
