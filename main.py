from faker import Faker
import random

fake = Faker()

while True:
    q = int(input('Press 1 to continue generating data\nPress 2 to exit: '))
    
    if q == 2:
        break
    elif q == 1:
        file_name = input('Nome file: ')  
        table = input('Inserisci nome tabella:')
        columns = input('Inserisci nomi delle colonne separate da virgole: ').split(', ')
        times = int(input('Quante volte:'))
        typeOfData = input('Inserisci i tipi di dato rispettivamente per ogni colonna separati da virgole (char, int, point, date): ').split(', ') 
        
        with open(file_name, 'w') as f:
            for _ in range(times):
                a = []
                col_idx = 0
                
                for col_type in typeOfData:
                    if col_type == 'char':
                        a.append(f"'{fake.first_name_male()}'")
                    elif col_type == 'int':
                        a.append(str(random.randrange(10)))
                    elif col_type == 'point':
                        a.append(f"'{fake.coordinate()}'")
                    elif col_type == 'date':
                        a.append(f"'{fake.date()}'")
                    
                    col_idx += 1
                
                f.write(f"INSERT INTO {table} ({', '.join(columns)})\nVALUES ({', '.join(a)});\n")
    else:
        continue
