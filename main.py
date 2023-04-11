from faker import Faker
import subprocess

f = Faker()

i=input('press 1 to continue gen datas\n press 2 for exit')



while True:
    
    
    if i == '2':
        break
    
    
    elif i == '1':
        
        file = open('query.txt', 'x')
        
        table = input('inserisci nome tabella:')
        column = input('inserisci attributo:')
        times = input(int('quante volte:'))
        
        file = open('query.txt', 'a')
        
        for _ in range(times):
            data = f.
            file.write(f'\nINSERT INTO {table}({column}) \n VALUES')
    
    else:
        continue