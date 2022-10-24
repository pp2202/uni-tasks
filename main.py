import lib_classes as lc
import housing_classes as hc

#Biblioteka

L1 = lc.Library('miasto a', 'ulica b', '00-000', '8:00-17:00', '+00 000 000 000')
L2 = lc.Library('miasto c', 'ulica d', '11-110', '6:00-17:00', '+04 200 000 000')
book1 = lc.Book(L1,'1998', 'a', 'b', '727')
book2 = lc.Book(L2,'1992', 'a', 'b', '727')
book3 = lc.Book(L1,'1994', 'a', 'c', '757')
book4 = lc.Book(L2,'1994', 'a', 'b', '727')
book5 = lc.Book(L1,'1991', 'a', 'b', '727')
empl1 = lc.Employee('a', 'b', 'x', 'x', 'x', 'x', 'x', 'x')
empl2 = lc.Employee('aa', 'bb', 'x', 'x', 'x', 'x', 'x', 'x')
empl3 = lc.Employee('aaa', 'bbb', 'x', 'x', 'x', 'x', 'x', 'x')

or1 = lc.Order(empl1,'Jerzy Brodzik',[book1,book3,book4],'0000-00-00')
or2 = lc.Order(empl3,'Andrzej E.',[book2,book5],'0000-00-00')


#Mieszkania

pos1 = hc.Flat('NYC',2,'4299000 USD','EEE',4)
pos2 = hc.House('AR',9,'8999999 AUD', 'TTT',14000)

print(pos1)
print(pos2)
