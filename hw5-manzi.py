# 1. Patient class

class Patient:
    def __init__(self, name, symptoms):
        self.name = name
        self.symptoms = symptoms
        self.tests = {}

    def add_test(self, test_name, result):
        """Add a test result for the patient."""
        self.tests[test_name.lower()] = bool(result)

    def has_covid(self):
        """Estimate probability of having Covid-19."""
        if "covid" in self.tests:
            return 0.99 if self.tests["covid"] else 0.01

        prob = 0.05
        for s in ["fever", "cough", "anosmia"]:
            if s in self.symptoms:
                prob += 0.1
        return min(prob, 1.0)


# 2. Card and Deck classes

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(s, v) for s in suits for v in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            print("No more cards in the deck.")
            return None
        card = self.cards.pop()
        print(card)
        return card


# 3. PlaneFigure interface + subclasses


from abc import ABC, abstractmethod
import math

class PlaneFigure(ABC):
    @abstractmethod
    def compute_perimeter(self):
        pass

    @abstractmethod
    def compute_surface(self):
        pass


class Triangle(PlaneFigure):
    def __init__(self, base, c1, c2, h):
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.h = h

    def compute_perimeter(self):
        return self.base + self.c1 + self.c2

    def compute_surface(self):
        return 0.5 * self.base * self.h


class Rectangle(PlaneFigure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute_perimeter(self):
        return 2 * (self.a + self.b)

    def compute_surface(self):
        return self.a * self.b


class Circle(PlaneFigure):
    def __init__(self, radius):
        self.radius = radius

    def compute_perimeter(self):
        return 2 * math.pi * self.radius

    def compute_surface(self):
        return math.pi * self.radius ** 2


#Tests
if __name__ == "__main__":
    # Patient
    p = Patient("Alice", ["fever", "cough"])
    print("Covid probability before test:", p.has_covid())
    p.add_test("covid", True)
    print("Covid probability after positive test:", p.has_covid())

    # Deck
    deck = Deck()
    deck.shuffle()
    for _ in range(3):
        deck.draw()

    # Figures
    t = Triangle(3, 4, 5, 2.5)
    r = Rectangle(4, 6)
    c = Circle(3)

    print("Triangle area:", t.compute_surface())
    print("Rectangle perimeter:", r.compute_perimeter())
    print("Circle area:", c.compute_surface())
