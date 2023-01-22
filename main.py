flight_list = [
    {'id': 12, 'name': 'Бишкек-Стамбул', 'price': 35000, 'time': '15:00'},
    {'id': 13, 'name': 'Бишкек-Нур-Сутлан', 'price': 20000, 'time': '11:00'},
    {'id': 14, 'name': 'Бишкек-Москава', 'price': 27500, 'time': '17:40'}
]

for f in flight_list:
    print()
    print(f'Номер рейса: {f["id"]}\n')
    print(f'От куда-куда: {f["name"]}\n')
    print(f'Цена: {f["price"]}\n')
    print(f'Время: {f["time"]}\n')
    print('--------------------------')


def flight_number_selection() -> int:
    confirmation = True
    while True:
        try:
            flight_number = int(input('Пожалуйста, введите номер рейса: '))
        except ValueError:
            print('Введите номер рейса правильно')
            continue


        for f in flight_list:
            if flight_number != f['id']:
                confirmation =  False
                
            else:
                confirmation = True
                break
        
        if confirmation == False:
            print('Извините, такого рейса нет')
            continue 
       
        break       

    return flight_number


fl_number = flight_number_selection()

print()

full_name = input('Введите ФИО: ')

print()

def ticket_paymnet(fl_number: int):
    ticket_price = 0
    for f in flight_list:
        if fl_number == f['id']:
            ticket_price = f['price']
            ticket_name = f['name']

    print(f'Цена рейса: {ticket_name} = {ticket_price}')  
    print()      

    succes_text = f'\nОплата прошла успешно!'
    while True:
        try:
            cash = int(input('Оплатите стоимость билета: '))
        except ValueError:
            print('Вы ввели неверное значение, пожалуйста внесите оплату за билет корректно')
            continue
        
        if cash < ticket_price:
            print('У вас недостаточно средств! Попробуйте снова.')
            continue
        elif cash > ticket_price:
            print(succes_text)
            print(f'Сдача: {cash - ticket_price}')
        else:
            print(succes_text)

        break

ticket_paymnet(fl_number)

print()

def message(fl_number: int, full_name: str):
    print(f'Номер рейса: {fl_number}')
    print(f'ФИО: {full_name}')

    for fl in flight_list:
        if fl_number == fl['id']:
            print(f'От куда-куда: {fl["name"]}')
            print(f'Время: {fl["time"]}')        


message(fl_number, full_name)            

        

            


