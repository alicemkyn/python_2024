# https://www.youtube.com/watch?v=YbpKMIUjvK8
'''
To run test, we should cd to the file's directory and in terminal write
pytest. In convention pytest looks the files that begins with test_ or
ends with _test.py than run this files if exist. And the functions in test
file should also begin with test_ otherwise no test will run by pytest.

'''
from typing import List

class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        self.items: List[str] = list()
        self.max_size = max_size

    def add(self, item: str):
        if self.size() == self.max_size:
            raise OverflowError('Cannot add more items')
        self.items.append(item)
    
    def size(self) ->int:
        return len(self.items)
    
    def get_items(self) -> List[str]:
        return self.items
    
    def get_total_price(self, price_map):
        total_price = 0
        for item in self.items:
            total_price += price_map.get(item)
        return total_price