from item import Item
import csv

class Phone(Item):
    
    def __init__(
        self, 
        name: str, 
        price: float, 
        quantity: int=0,
        broken_phones: int=0
        ):
        
        super().__init__(name,price,quantity)
        assert broken_phones >=0, f'{broken_phones} less than 0! '
        self.broken_phones = broken_phones
    
    def csv_file(csv_file_name: str='phones.csv'):
        def decorator(cls_method):
            def wrapper(cls, *args, **kwargs):
                with open(csv_file_name,'r') as f:
                    reader = csv.DictReader(f)
                    items = list(reader)
                
                for item in items:
                    if csv_file_name == 'phones.csv':
                        
                        cls(
                            name=item.get('name'),
                            price=float(item.get('price')),
                            quantity=int(item.get('quantity')),
                            broken_phones=int(item.get('broken_phones'))
                        )
                    else:
                        cls(
                            name=item.get('name'),
                            price=float(item.get('price')),
                            quantity=int(item.get('quantity'))
                        )
            return wrapper
        return decorator

    @classmethod
    @csv_file()
    def instantiate_from_csv(cls):
        with open('phones.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            cls(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
                broken_phones=int(item.get('broken_phones'))
            )