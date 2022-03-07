import csv

action = ''
result = True
'''items = [{'name':['Milk','Sugar','Flour','Coffe','Tea']}, {'quantity':[1,2,3,4,5]},{'unit':['ml','mg','mg','mg','lll']},{'unit_price':[1,2,3,4,5]}]'''

items_modified= [{'name':'Milk','quantity':1,'unit':'ml','unit_price':1}, {'name':'Coffe','quantity':2,'unit':'ml','unit_price':2}, {'name':'Tea','quantity':3,'unit':'ml','unit_price':3}, {'name':'Wine','quantity':4,'unit':'ml','unit_price':4}]
sold_items = []

#func that exports shop resouces status to the .csv file
def export_file_to_csv():
    with open('magazyn.csv', 'w', newline='') as csvfile:
        fieldnames = ['name','quantity','unit','unit_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for product in items_modified:
            writer.writerow({'name':product['name'],'quantity':product['quantity'],'unit':product['unit'],'unit_price':product['unit_price']})
        print('Successfully exported data to magazyn.csv.')

#func that imports shop resouces status from the .csv file
def import_items_from_csv():
    with open('magazyn.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            items_modified.append({'name':row['name'], 'quantity':row['quantity'], 'unit':row['unit'], 'unit_price':row['unit_price']})
        print('Successfully loaded data from magazyn.csv.')
        return items_modified

#adding new items to shop func
def add_item(name='', quantity ='', unit='', unit_price=''):
    print('Adding to warehouse...')
    items_modified.append({'name':input('Item name: ').capitalize(),'quantity':input('Item quantity: ').capitalize(), 'unit':input('Item unit of measure. Eg. l, kg, pcs: ').capitalize(), 'unit_price':input('Item price in PLN: ').capitalize()})

    print('Successfully added to warehouse. The current status is: ')
    get_items()

#func that sums up the items that were sold
def sold_items_summary(name, quantity,unit,unit_price):
    sold_items.append({'name':name, 'quantity':quantity, 'unit':unit, 'unit_price':unit_price})
 
#costs calculation func
def get_costs(sum_of_costs=0,list_of_costs=[]):
    list_of_costs = [product['quantity'] * product['unit_price'] for product in items_modified]
    sum_of_costs = sum(list_of_costs)
    return sum_of_costs

#income calculation func
def get_income(sum_of_income=0,list_of_income=[]):
    list_of_income = [product['quantity'] * product['unit_price'] for product in sold_items]
    sum_of_income = sum(list_of_income)
    return sum_of_income

#revenue calculation func
def show_revenue():
    print('Revenue breakdown (PLN)')
    print(f'Income:', get_income())
    print(f'Costs:', get_costs())
    print('------------')
    print(f'Revenue:', get_income() - get_costs(),' PLN')

#selling items func
def sell_item(name='', quantity=int()):
    name = input('Item name: ')
    name = name.capitalize()  
    i = len(items_modified)
    for product in items_modified:
        if name not in product.values():
            i -= 1
            if i == 0:
                print('There is no such product in the shop.')
        else:
            quantity = int(input('Quantity to sell: '))
            
            if product['quantity'] >= quantity:
                product['quantity'] = product['quantity']- quantity
                print('Successfully sold', product['quantity'], 'of ', name)
                sold_items_summary(name, quantity,unit = product['unit'],unit_price = product['unit_price'])
                get_items()
            else:
                buy_all = input('There is no enough quantity to fulfil your request. Do you want to buy what is available? (yes/no')
                if buy_all == 'yes':
                    product['quantity'] = product['quantity']- quantity
                    if product['quantity'] < 0:
                        quantity = quantity + product['quantity']
                        product['quantity'] = 0
                        print('Successfully sold', product['quantity'], 'of ', name)
                        sold_items_summary(name, quantity,unit = product['unit'],unit_price = product['unit_price'])

                        get_items()
                else:
                    print('You can choose another item or different quantity. ')

#func that shows current shop resurces status 
def get_items():
    print('Name\tQuantity\tUnit\tUnit Price (PLN)')
    print('----\t--------\t----\t----------------')
    
    for item in items_modified:
        print(item['name'],'\t',item['quantity'], '\t       ',item['unit'],'\t',item['unit_price'])

#function that triggers actions
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
        items_modified.clear()
        import_items_from_csv()
    elif action == 'exit':
        return True
    else:
        return False

#main program logic
import_items_from_csv()
while to_do(action) != True:
    action = str(input('What would you like to do? '))