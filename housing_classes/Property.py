class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
    
    def __str__(self):
        return f"{self.area}\n{self.rooms}\n{self.price}\n{self.address}"