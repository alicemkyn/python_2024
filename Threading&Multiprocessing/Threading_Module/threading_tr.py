'''
Thread — İş Parçaciği
Bir işin eş zamanli olarak işlenen her bir bölümüdür.¹

Yazdiğimiz kodlarin sirayla satir satir işleme alindiği bölüm diyebiliriz. Thread içindeki kodlar sirayla işleme girerler, bir önceki kod satiri çaliştirilmadan bir sonraki çaliştirilmaz. Satirlar birbirlerini beklerler.

Main Thread — Ana iş parçaciği ise programimizin başlangiç noktasidir. Yazdiğimiz kodlari varsayilan olarak çaliştirdiğimiz iş parçaciğidir.

Multi Thread — Çoklu İş Parçaciği
Birden fazla iş parçaciğinin bulunduğu senaryodur. Çalişacak olan bir kod bloğunun yaninda ayni anda ona paralel olarak çalişmasini istediğimiz kod bloklari olabilir.

Diyelim ki Main Thread’de programimiz bir iş yapiyor fakat diğer taraftan da ağ üzerinden bilgi almasi gerekiyor. Böyle bir durumda bize Multi Thread eşlik ediyor. Multi Thread ile Main Thread’i engellemeden paralel olarak iş yapabiliriz.
'''
from threading import Thread
import time
# İki tane 0'dan 5'e kadar ekrana sayi yazan fonksiyonumuz olsun.
def thread_function():
    for i in range(5):
        print('Thread ile cagrildi:' + str(i))
        time.sleep(1)
        
def function():
    for i in range(5):
        print(i)
        time.sleep(3)

# Bu iki fonksiyonun birini Thread ile diğerini de normal bir şekilde(Main Thread) çağiralim.
thread_fun = Thread(target=thread_function)
thread_fun.start()
function()
# Burada Thread içinde target = ile çalıştıracağımız fonksiyonu seçiyoruz ve start() diyerek fonksiyonumuzu çalıştırıyoruz.
'''
Output:
Thread ile cagrildi:0
0
Thread ile cagrildi:1
Thread ile cagrildi:2
1
Thread ile cagrildi:3
Thread ile cagrildi:4
2
3
4

Görüldüğü gibi normal fonksiyonumuz 3 saniye bekleyerek ekrana yazarken Thread ile çağirdiğimiz fonksiyonumuz da onunla paralel işlem yaparak, onu engellemeden 1 saniye bekleyerek ekrana yaziyor.
'''

#Peki ben Thread ile çalıştıracağım fonksiyonuma argüman göndermek istiyorum bunu nasıl yapıyoruz?
# Bu sefer fonksiyonumun bir tane parametresi olsun.

def thread_function(number):
    for i in range(number):
        print('Thread ile cagrildi: ' + str(i))
        time.sleep(1)

def function():
    for i in range(5):
        print(i)
        time.sleep(3)
# Bu durumda fonksiyonumuzu çağırırken args= ile argüman gönderebiliyoruz.

thread_fun = Thread(target=thread_function, args=(4,))
