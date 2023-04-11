from faker import Faker

f = Faker()


while True:
    
    i=input('press 1 to continue gen datas\n press 2 for exit:\n') 
    file_name=input('\nNome_file: ')    
    
    if i == '2':
        break
    
    elif i == '1':
        
        table = input('inserisci nome tabella:')
        column = input('inserisci attributo:')
        times = input(input('quante volte:'))
        
        file = open(file_name, 'w')
        
        for _ in range(times):
            data = f.name
            file.write(f'\nINSERT INTO {table}({column}) \n VALUES')
    
        file.close()
    else:
        continue