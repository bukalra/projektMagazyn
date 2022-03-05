import csv

action = ''
result = True
items = [{'name':['Milk','Sugar','Flour','Coffe','Tea']}, {'quantity':[1,2,3,4,5]},{'unit':['ml','mg','mg','mg','lll']},{'unit_price':[1,2,3,4,5]}]
sold_items = [
                     {'name':[]},
                     {'quantity': []},
                     {'unit': []},
                     {'unit_price':[]}]
def to_do(action):  
    if action == 'show':
        get_items()
    elif action == 'add':
        add_item()
    elif action == 'sell':
        sell_item()
    elif action == 'show rev':
        show_revenue()
    elif action == 'save':
        export_file_to_csv()
    elif action == 'load':
        items.clear()
        import_items_from_csv()
    elif action == 'exit':
        return True
    else:
        return False

def export_file_to_csv():
    with open('test.csv', 'w', newline='') as csvfile:
        fieldnames = ['name','quantity','unit','unit_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        b = []
        for param in items:
            for item in param.values():
                b.append(item)
                print(b)
        i = 0
        restructured = {}
        for entry in b[0]:
            restructured = {'name':b[0][i],'quantity':b[1][i],'unit':b[2][i],'unit_price':b[3][i]}
            i+=1
            writer.writerow(restructured)

def import_items_from_csv():
    with open('test.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        place_holder = []
        place_holder_1 = []
        place_holder_2 = []
        place_holder_3 = []

        for row in reader:
            place_holder.append(row['name'])
            place_holder_1.append(row['quantity'])
            place_holder_2.append(row['unit'])
            place_holder_3.append(row['unit_price'])

        items = [{'name':[]}, {'quantity':[]}, {'unit':[]}, {'unit_price':[]}]
        for i,each in enumerate(place_holder):
            items[0]['name'].append(place_holder[i])
            items[1]['quantity'].append(int(place_holder_1[i]))
            items[2]['unit'].append(place_holder_2[i])
            items[3]['unit_price'].append(int(place_holder_3[i]))

        print(f'====items==>>{items}')
        return items

def add_item(name='', quantity ='', unit='', unit_price=''):
    print('Adding to warehouse...')
    items[0]['name'].append(input('Item name: '))
    items[1]['quantity'].append(input('Item quantity: '))
    items[2]['unit'].append(input('Item unit of measure. Eg. l, kg, pcs: '))
    items[3]['unit_price'].append(int(input('Item price in PLN: ')))
    print('Successfully added to warehouse. The current status is: ')
    get_items()

def sold_items_summary(name, quantity,unit,unit_price):
    sold_items[0]['name'].append(name)
    sold_items[1]['quantity'].append(quantity)
    sold_items[2]['unit'].append(unit)
    sold_items[3]['unit_price'].append(unit_price)

    print(sold_items)

def get_costs(sum_of_costs=0,list_of_costs=[]):
    list_of_costs = [items[1]['quantity'][i] * items[3]['unit_price'][i] for i,_ in enumerate(items[0]['name'])]
    sum_of_costs = sum(list_of_costs)
    #print(sum_of_costs)
    return sum_of_costs

def get_income(sum_of_income=0,list_of_income=[]):
    list_of_income = [sold_items[1]['quantity'][i] * sold_items[3]['unit_price'][i] for i,_ in enumerate(sold_items[0]['name'])]
    sum_of_income = sum(list_of_income)
    #print(sum_of_income)
    return sum_of_income

def show_revenue():
    print('Revenue breakdown (PLN)')
    print(f'Income:', get_costs())
    print(f'Costs:', get_income())
    print('------------')
    print(f'Revenue:', get_income() - get_costs(),' PLN')

def sell_item(name='', quantity=int()):
    name = input('Item name: ')
    name = name.capitalize()

    quantity_index = items[0]['name'].index(name)
    unit = items[2]['unit'][quantity_index]
    unit_price = items[3]['unit_price'][quantity_index]
    print(unit)
    print(unit_price)
    if name not in items[0]['name']:
        print('There is no requested product.')

    else:
        quantity = int(input('Quantity to sell: '))
        
        if items[1]['quantity'][quantity_index] >= quantity:
            items[1]['quantity'][quantity_index] = items[1]['quantity'][quantity_index] - quantity
            print(f'Successfully sold {quantity} of {name}')
            sold_items_summary(name, quantity,unit,unit_price)
            get_items()
        else:
            buy_all = input('There is no enough quantity to fulfil your request. Do you want to buy what is available? (yes/no')
            if buy_all == 'yes':
                items[1]['quantity'][quantity_index] = items[1]['quantity'][quantity_index] - quantity
                if items[1]['quantity'][quantity_index] < 0:
                    quantity = quantity+(items[1]['quantity'][quantity_index])
                    items[1]['quantity'][quantity_index] = 0
                    print(f'Successfully sold {quantity} of {name}')
                    get_items()
            else:
                print('You can choose another item or different quantity. ')
                
def get_items():
    print('Name\tQuantity\tUnit\tUnit Price (PLN)')
    print('----\t--------\t----\t----------------')
    
    a = []
    print(items)

    for param in items:
        for item in param.values():
            a.append(item)
            
    i = 0
    for entry in a[0]:
        print(a[0][i],'\t',a[1][i],'\t       ',a[2][i],'\t',a[3][i])
        i+=1

while to_do(action) != True:
    action = str(input('What would you like to do?'))
