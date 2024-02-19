import heapq
'''
Heap Queue (Heapq) tree-like Kütüphanesi Nedir?
2 ana turu vardir:
- Minimum heap(Default)
- Maximum heap
Temel Kavramlar: Heap ve Kök Düğüm
Öncelik Kuyruğu (Priority Queue) İlkesi
heapq Modülü ve Temel Fonksiyonlari
heapify(iterable) Fonksiyonu
heappush(heap, item) Fonksiyonu
heappop(heap) Fonksiyonu
heapreplace(heap, item) Fonksiyonu
heappushpop(heap, item) Fonksiyonu
heapreplace(heap, item) Fonksiyonu
nlargest(n, iterable) Fonksiyonu
nsmallest(n, iterable) Fonksiyonu
Örnek: E-Ticaret Siparişleri ve Heap Queue
Veri Yapilari ve Heap Queue
Öncelikli İşlemler ve Heap Queue
Veri Siralama ve Heap Queue
Heap Queue Uygulamalari
https://www.youtube.com/watch?v=WPbIeiWQzek&t=3s
'''

# heapify()
numbers = [7, 3, 11, 5, 4]
heapq.heapify(numbers)
print(numbers) # [3, 4, 11, 5, 7]
'''
Begins with 7. Then left branch:3 but 3 < 7, places changed. [3,7]
Right branch : 11. 11 > 3 and 11 > 7. It stays on the bottom right.[3,7,11]
Next left branch from 7, 5. 5 < 7, places changed.[3,5,11,7]
Right branch : 4. 4<5 places changed. [3,4,11,7,5]
But 7 on the left 5 on the right. 7>5 so places changed.[3,4,11,5,7]
'''

# heappush() Pushes the digit and heapifies it.
heapq.heappush(numbers, 2)
print(numbers) # [2, 4, 3, 5, 7, 11]


# heappop() Pop the smallest item off the heap, and heapifies it.
smallest = heapq.heappop(numbers)
print(smallest) # 2
print(numbers) # [3, 4, 11, 5, 7]


# heapreplace()
'''
Returns the smallest value in the heap and replaces it with given num.
'''
smallest = heapq.heapreplace(numbers, 1)
print(smallest) # 3
print(numbers) # [1, 4, 11, 5, 7]


# heappushpop() 
'''
Pushes the given value, pops the smallest, and heapifies it.
'''
smallest = heapq.heappushpop(numbers, 1)
print(smallest) # 1
print(numbers) # [1, 4, 11, 5, 7]


# nlargest() Finds the largest numbers
largest = heapq.nlargest(3, numbers)
print(largest) # [11, 7, 5]


# nsmallest() Finds the smallest numbers
smallest = heapq.nsmallest(3, numbers)
print(smallest) # [1, 4, 5]



####################### E Commerce Example #############################
class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount
        
    def __lt__(self, other):
        return self.amount < other.amount
    
orders_heap = []

order1 = Order(101,250)
order2 = Order(102,150)
order3 = Order(103,350)
order4 = Order(104,200)

heapq.heappush(orders_heap, order1)
heapq.heappush(orders_heap, order2)
heapq.heappush(orders_heap, order3)
heapq.heappush(orders_heap, order4)

min_order = heapq.heappop(orders_heap)

print('The minimum amount order is: ')
print('Min order ID:', min_order.order_id, 'Order Amount:', min_order.amount)
# Min order ID: 102 Order Amount: 150