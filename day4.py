from operator import attrgetter
from typing import List
# Problem-1 Create a class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def is_adult(self):
        if self.age > 18:
            return 'The Person is a adult'
        return 'You not a adult'
person1 = Person('peter', 67)
person2 = Person('Alex', 12)
print(person1.is_adult())
print(person2.is_adult())


# Problem-2 Create a class Rectangle
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2* (self.width + self.height)
rect1 = Rectangle(12,23)
rect2 = Rectangle(10,6)
print(rect1.area())
print(rect2.perimeter(), rect2.height)

# Problem-3 BankAccount Class
class BankAccount:
    def __init__(self, owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return(f'The total balance in the account {self.balance}')
    def withdraw(self, amount):
        if amount > self.balance:
            return('Insufficient funds Transcation cannot be processed!!')
        else:
            self.balance -= amount
            return(f'The avalible balance is {self.balance}')
account1 = BankAccount('Prudhvi', 12000)
account2 = BankAccount('Alex', 22000)
print(account1.deposit(10000))
print(account1.withdraw(4000))

# Problem-4 Student Class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        return (sum(self.marks)/len(self.marks),2)
    def add_mark(self,m):
        self.marks.append(m)
        return(f'Updated marks list is {self.marks}')
s1 = Student('Prudhvi', [25,24,23,21,25,25])
s2 = Student('Alex', [12,22,3,3,22,22])
print(s1.average())
print(s1.add_mark(23))

# Problem-5 Class Book
class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return(f'The book title {self.title} written by {self.author}, has nearly {self.pages}')
    def is_bigbook(self):
        if self.pages > 300:
            return(f'The book is bigger it has {self.pages} pages')
b1 = Book('HarryPotter', 'Prudhvi', 240)
b2 = Book('All the time', 'Prudhvi', 400)
print(b1)
print(b2.is_bigbook())

# Problem-6 Car Class with Classmethod
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    @classmethod
    def from_string(cls,model):
        brand,model = model.split("-")
        return cls(brand, model)
    @staticmethod
    def is_valid_brand(brand):
        if len(brand) > 0:
            return('The is a valid brand')
        else:
            return('The brand must contain validity')
    def __str__(self):
        return(f'The brand is {self.brand} and model is {self.model}')
c1 = Car.from_string('Tesla-Model3')
c2 = Car.from_string('BMW-M6')
print(c1)
print(c1.is_valid_brand(''))
print(c1.is_valid_brand('tata'))

# Problem-7 Employee Class with Encapsulation
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
        if salary <= 0:
            return('Salary cannot be negative or zero')
        else:
            self.__salary = salary
            return(f'updated salary is {self.__salary}')
E1 = Employee('prudhvi', 52000)
E2 = Employee('Alex', 12000)

print(E1.get_salary())
print(E2.set_salary(-12))
print(E2.set_salary(120000))

#Problem-8 Inheritance Problem
class Animal:
    def speak(self):
        return "Some sound"
class Dog(Animal):
    def __init__(self,name,bredd):
        self.name = name
        self.bredd = bredd
    def speak(self):
        return 'The bog barks woww woww'
a = Animal()
print(a.speak())
d = Dog('max', 'Belgium Malinwas')
print(d.bredd)
print(d.name)
print(d.speak())

#Problem-9 Polymorphism Example
class Animal:
    def speak(self):
        return "Some Generic Sound"
class Dog(Animal):
    def speak(self):
        return "The dog barks: Woof Woof"
class Cat(Animal):
    def speak(self):
        return "The cat meows: Meow Meow"
class Bird(Animal):
    def speak(self):
        return "The bird chirps: Tweet Tweet"
def animal_sound(animal):
    print(animal.speak())
cat1 = Cat()
dog1 = Dog()
bird1 = Bird()
animal_sound(cat1)
animal_sound(dog1)
animal_sound(bird1)



# Problem-10 Sorting objects (lambda required)
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __rep__(self):
        return f"Studnet({self.name!r}, age={self.age})"

s1: list[student] = [Student("Prudhvi", 23), Student('Alex', 24), Student('Ranger', 55)]
print('Orginal_List')
print(s1)

sort_by_age = sorted(s1, key = lambda s: s.age)
print('\n sorted by Assending order according to age')
print(sorted_by_age)

sorted_by_age_larger = sorted(s, key =lambda s: s.age, reverse= True)
print('/n The age is sorted by larger to smaller')
print(sorted_by_age_larger)

sort_by_name = sorted(s1, key= lambda s: len(s.name))
print('\n Sorted by length of the name')
print(sorted_by_name)

sorted_by_age_name = sorted(s, key= lambda s: (s.age, s.name))
print('\n The names are sorted by age & names')
print(sorted_by_age_name)

sorted_by_age_atter = sorted(s, key=attrgetter(s.age))








# day4_oop_clean.py
from typing import List, Optional


# ---------------------------
# Problem 1 — Person
# ---------------------------
class Person:
    """Simple Person class."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        """Return True if person is adult (age >= 18)."""
        return self.age >= 18

    def __repr__(self) -> str:
        return f"Person(name={self.name!r}, age={self.age})"


# ---------------------------
# Problem 2 — Rectangle
# ---------------------------
class Rectangle:
    """Rectangle with width and height."""

    def __init__(self, width: float, height: float) -> None:
        self.width = float(width)
        self.height = float(height)

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


# ---------------------------
# Problem 3 — BankAccount
# ---------------------------
class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds balance."""


class BankAccount:
    """Simple bank account with deposit and withdraw."""

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float) -> float:
        """Deposit amount and return new balance. Raises ValueError on invalid amount."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """Withdraw amount and return new balance. Raises InsufficientFundsError if not enough balance."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self.balance})"


# ---------------------------
# Problem 4 — Student
# ---------------------------
class Student:
    """Student with marks; compute average and update marks."""

    def __init__(self, name: str, marks: Optional[List[float]] = None) -> None:
        self.name = name
        self.marks = list(marks) if marks else []

    def average(self) -> float:
        """Return rounded average (2 decimals). Return 0.0 if no marks."""
        if not self.marks:
            return 0.0
        avg = sum(self.marks) / len(self.marks)
        return round(avg, 2)

    def add_mark(self, mark: float) -> None:
        """Append a new mark."""
        self.marks.append(float(mark))

    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, marks={self.marks})"


# ---------------------------
# Problem 5 — Book
# ---------------------------
class Book:
    """Book representation."""

    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = int(pages)

    def is_big_book(self) -> bool:
        """Return True if book has more than 300 pages."""
        return self.pages > 300

    def __str__(self) -> str:
        return f"{self.title} by {self.author} — {self.pages} pages"

    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages})"


# ---------------------------
# Problem 6 — Car (classmethod & staticmethod)
# ---------------------------
class Car:
    """Car that can be created from a 'Brand-Model' string."""

    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    @classmethod
    def from_string(cls, text: str) -> "Car":
        """
        Create Car from 'Brand-Model' string.
        Example: 'Tesla-Model3' -> Car('Tesla', 'Model3')
        """
        parts = text.split("-", 1)
        if len(parts) != 2:
            raise ValueError("Input must be 'Brand-Model'.")
        brand, model = parts
        return cls(brand.strip(), model.strip())

    @staticmethod
    def is_valid_brand(brand: str) -> bool:
        """Return True if brand is non-empty and alphabetic-like (basic check)."""
        return bool(brand and brand.strip())

    def __str__(self) -> str:
        return f"{self.brand} — {self.model}"

    def __repr__(self) -> str:
        return f"Car(brand={self.brand!r}, model={self.model!r})"


# ---------------------------
# Problem 7 — Employee (encapsulation)
# ---------------------------
class Employee:
    """Employee with encapsulated salary."""

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.__salary = float(salary)

    def get_salary(self) -> float:
        return self.__salary

    def set_salary(self, salary: float) -> None:
        """Set salary; raise ValueError for invalid value."""
        if salary <= 0:
            raise ValueError("Salary must be positive.")
        self.__salary = float(salary)

    def __repr__(self) -> str:
        return f"Employee(name={self.name!r}, salary=PROTECTED)"


# ---------------------------
# Problem 8 — Inheritance
# ---------------------------
class Animal:
    """Base class for animals."""

    def speak(self) -> str:
        return "Some sound"


class Dog(Animal):
    """Dog extends Animal."""

    def __init__(self, name: str, breed: str) -> None:
        super().__init__()
        self.name = name
        self.breed = breed

    def speak(self) -> str:
        return "Woof Woof"

    def __repr__(self) -> str:
        return f"Dog(name={self.name!r}, breed={self.breed!r})"


# ---------------------------
# Problem 9 — Polymorphism
# ---------------------------
class Cat(Animal):
    def speak(self) -> str:
        return "Meow Meow"


class Bird(Animal):
    def speak(self) -> str:
        return "Tweet Tweet"


def animal_sound(animal: Animal) -> str:
    """Return the sound of the animal; demonstrates polymorphism."""
    return animal.speak()


# ---------------------------
# Small test-run when executed directly
# ---------------------------
if __name__ == "__main__":
    # Problem 1
    p1 = Person("Peter", 67)
    p2 = Person("Alex", 12)
    assert p1.is_adult() is True
    assert p2.is_adult() is False

    # Problem 2
    r1 = Rectangle(12, 23)
    r2 = Rectangle(10, 6)
    assert r1.area() == 12 * 23
    assert r2.perimeter() == 2 * (10 + 6)

    # Problem 3
    acc = BankAccount("Prudhvi", 12000.0)
    bal_after_deposit = acc.deposit(10000.0)
    assert bal_after_deposit == 22000.0
    bal_after_withdraw = acc.withdraw(4000.0)
    assert bal_after_withdraw == 18000.0
    try:
        acc.withdraw(10_000_000.0)
        raise AssertionError("Expected InsufficientFundsError")
    except InsufficientFundsError:
        pass

    # Problem 4
    s1 = Student("Prudhvi", [25, 24, 23, 21, 25, 25])
    assert isinstance(s1.average(), float)
    s1.add_mark(23)
    assert len(s1.marks) == 7

    # Problem 5
    b1 = Book("Harry Potter", "J. K. Rowling", 240)
    b2 = Book("All the Time", "Someone", 400)
    assert b1.is_big_book() is False
    assert b2.is_big_book() is True

    # Problem 6
    c1 = Car.from_string("Tesla-Model3")
    assert isinstance(c1, Car)
    assert Car.is_valid_brand("Tata") is True
    assert Car.is_valid_brand("") is False

    # Problem 7
    e1 = Employee("Prudhvi", 52000)
    assert e1.get_salary() == 52000.0
    try:
        e1.set_salary(-100)
        raise AssertionError("Expected ValueError on negative salary")
    except ValueError:
        pass
    e1.set_salary(60000)
    assert e1.get_salary() == 60000.0

    # Problem 8 & 9
    a = Animal()
    d = Dog("Max", "Belgian Malinois")
    cat = Cat()
    bird = Bird()
    assert animal_sound(a) == "Some sound"
    assert animal_sound(d) == "Woof Woof"
    assert animal_sound(cat) == "Meow Meow"
    assert animal_sound(bird) == "Tweet Tweet"

    print("All Day-4 OOP tests passed ✅")
