# Test for hw5.py
from best_library.hw5 import Patient, Deck, PlaneFigure, Rectangle, Triangle, Circle
import math

# Tests for exercise 1
def test_patient_add_test():

    patient = Patient("John Doe", ["fever", "cough"])
    assert patient.name == "John Doe"
    assert patient.symptoms == ["fever", "cough"]

    patient.add_test("covid", True)
    assert patient._tests["covid"] is True

    patient.add_test("flu", False)
    assert patient._tests["flu"] is False

def test_patient_has_covid():
    patient1 = Patient("Alice", ["fever", "cough"])
    assert patient1.has_covid() == 0.25  # 0.05 + 0.1 + 0.1

    patient2 = Patient("Bob", ["headache"])
    assert patient2.has_covid() == 0.05  # no symptoms

    patient3 = Patient("Charlie", ["anosmia", "cough", "fever"])
    assert patient3.has_covid() == 0.35  # 0.05 + 0.1 + 0.1 + 0.1

    patient4 = Patient("David", [])
    patient4.add_test("covid", True)
    assert patient4.has_covid() == 0.99  # positive test

    patient5 = Patient("Eve", ["fever"])
    patient5.add_test("covid", False)
    assert patient5.has_covid() == 0.01  # negative test

# Tests for exercise 2
def test_deck_shuffle():
    deck = Deck()
    original_order = deck.cards.copy()
    deck.shuffle()
    shuffled_order = deck.cards
    assert original_order != shuffled_order  # Check that the order has changed
    for card in original_order: 
        assert card in shuffled_order  # Check that all cards are still present

def test_deck_draw():
    deck = Deck()
    initial_count = len(deck.cards)
    drawn_card = deck.draw()
    assert len(deck.cards) == initial_count - 1  # Check that one card is removed
    assert drawn_card not in deck.cards  # Check that the drawn card is no longer in the deck


# Tests for exercise 3
def test_plane_figure_compute_perimeter():
    rectangle = Rectangle(4, 6)
    assert rectangle.compute_perimeter() == 20  # 2*(4+6)

    square = Circle(5)
    assert square.compute_perimeter() == 10*(math.pi) # 2 * pi * 5

    triangle = Triangle(3, 4, 5, 6)
    assert triangle.compute_perimeter() == 12  # 3+4+5

def test_plane_compute_surface():
    rectangle = Rectangle(4, 6)
    assert rectangle.compute_surface() == 24  # 4*6

    square = Circle(5)
    assert square.compute_surface() == (math.pi)*25  # pi * 5 ** 2

    triangle = Triangle(3, 4, 5, 6)
    assert triangle.compute_surface() == 9  # (3*6)/2
