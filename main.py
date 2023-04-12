from faker import Faker

f = Faker()


while True:
    
    i=int(input('press 1 to continue gen datas\n press 2 for exit:\n')) 
    file_name=input('\nNome_file: ')    
    
    if i == 2:
        break
    
    elif i == 1:
        
        table = input('inserisci nome tabella:')
        columns = input('Inserisci nomi delle colonne separate da virgole: ').split(',')
        times = int(input('quante volte:'))
      
        file = open(file_name, 'w')
        
        for _ in range(times):
            data = str(f.name())
            file.write(f'\nINSERT INTO {table}({", ".join(columns)}) \n VALUES({data});')
    
        file.close()
    else:
        continue