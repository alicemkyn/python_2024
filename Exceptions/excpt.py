######################### EXCEPTION HANDLING ###########################
'''
try, except, as, else, raise, assert, finally
- except: 
    except ValueError: (singular)
    except (TypeError, ValueError): (plural)
    except: (Catches all types of errors.)

- as:
    Hatadan sonraki aciklama field ini alir.

- else:
    Hata gruplamasi gibi ama ayri ayri bloklarda. Bu olmazsa bunu dene gibi.
    try:
        ....
    except ZeroDivisionError:
        print('ZD Error')
        
    else:
        try: 
            ...
        except ...:

- raise:
    raise Exception('Write Anything...')
    raise TypeError('Wrote Wrong...')
    raise stops the flow no code works after raise line

- assert:
    iddia etmek anlamina gelir. False olursa yandaki kod calisir.
    eg > assert len(name) != 0, 'Isim bolumu bos'

- finally:
    En sonuncu blok. Kesinlikle calismasini istedigimiz kodlar buraya 
    yazilir cunku her ne olursa olsun bu bloga giris yapilir.
    Ornegin : dosya.close()
    
'''





while True:
    try:
        x = int(input('Enter a number: '))
        break
    except ValueError:
        print('Ooops! It is not a number')

'''
except(RuntimeError, TypeError, NameError):
    pass

except OSError as err:
    print(f'Some {err} occurred')

raise NameError('Hi There')

'''

x = 'hundred thousand'
try:
    y = int(x)
except ValueError as err:
    print(f'Some {err} occurred.')
# Some invalid literal for int() with base 10: 'hundred thousand' occurred.

# raise NameError('Hi there !')

try:
    y = int(x)
except ValueError as exc:
    raise RuntimeError('This is an exception chaining!') from exc
'''
Output:
ValueError: invalid literal for int() with base 10: 'hundred thousand'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
    File "/Users/alicemkoyun/Programming/Exceptions/excpt.py", line 32, in <module>
    raise RuntimeError('This is an exception chaining!') from exc
RuntimeError: This is an exception chaining!
'''