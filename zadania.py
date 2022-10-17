
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

        
    def is_passed(self):
        avgMarks =  sum(self.marks)/len(self.marks)
        if (avgMarks > 50):
            return True
        else:
            return False

b1 = Student('Antoni',[1,3,5,6,4,3])
b2 = Student('Jerzy',[6,66,727])

print(b1.is_passed())
print(b2.is_passed())

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street=street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
    def __str__(self):
        return f"{self.city}\n{self.street}\n{self.zip_code}\n{self.open_hours}m{self.phone}" 
        
class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
        
    def __str__(self):
        return f"{self.first_name}\n{self.last_name}\n{self.hire_date}\n{self.birth_date}\n{self.city}\n{self.street}\n{self.zip_code}\n{self.phone}"
        
class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date =publication_date
        self.author_name=author_name
        self.author_surname=author_surname
        self.number_of_pages = number_of_pages
    
    def __str__(self):
        return f"{self.library}\n{self.publication_date}\n{self.author_name}\n{self.author_surname}\n{self.number_of_pages}"
        
class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student=student
        self.books = books
        self.order_date = order_date
    def __str__(self):
        return f"{self.employee}\n{self.student}\n{self.books}\n{self.order_date}"

L1 = Library('miasto a','ulica b','00-000','8:00-17:00','+00 000 000 000')
L2 = Library('miasto c','ulica d','11-110','6:00-17:00','+04 200 000 000')
book1 = Book(L1,'1998','a','b','727')
book2 = Book(L2,'1992','a','b','727')
book3 = Book(L1,'1994','a','c','757')
book4 = Book(L2,'1994','a','b','727')
book5 = Book(L1,'1991','a','b','727')
empl1 = Employee('a','b','x','x','x','x','x','x')
empl2 = Employee('aa','bb','x','x','x','x','x','x')
empl3 = Employee('aaa','bbb','x','x','x','x','x','x')

or1 = Order(empl1,'Jerzy Brodzik',[book1,book3,book4],'0000-00-00')
or2 = Order(empl3,'Andrzej E.',[book2,book5],'0000-00-00')

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
    
    def __str__(self):
        return f"{self.area}\n{self.rooms}\n{self.price}\n{self.address}"
    
class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
        self.plot = plot
        
    def __str__(self):
        return f"{self.area}\n{self.rooms}\n{self.price}\n{self.address}\n{self.plot}"    
    
class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
        self.floor = floor
        
    def __str__(self):
        return f"{self.area}\n{self.rooms}\n{self.price}\n{self.address}\n{self.floor}"   
    
pos1 = Flat('NYC',2,'4299000 USD','EEE',4)
pos2 = House('AR',9,'8999999 AUD', 'TTT',14000)

print(pos1)
print(pos2)
        
        