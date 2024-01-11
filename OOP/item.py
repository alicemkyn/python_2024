import csv

class Item:
    all = []
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity: int=0):
        assert isinstance(name, str), f'{name} is not str !'
        assert price >= 0, f'{price} is less than 0!'
        assert quantity >= 0, f'{quantity} is less than 0!'
        
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self): 
        self.price *= self.pay_rate # if it can find the pay_rate at 
        # instance level it will look up to class level. It will work
        # like a charm, no worries.
        
    def __repr__(self):# Fixed here Item to self.__class__.__name__
        return  f'{self.__class__.__name__}("{self.name}",{self.price},\
{self.quantity})'
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            cls(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    
    @staticmethod
    def is_it_integer(number): 
        if isinstance(number, float):
            return number.is_integer()
        elif isinstance(number, int):
            return True
        else:
            return False