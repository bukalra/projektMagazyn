action = ''
result = True
items = [{'name':['Milk','Sugar','Flour','Coffe','Tea']}, {'quantity':[120,1000,1000,2000,444]},{'unit':['ml','mg','mg','mg','lll']},{'unit_price':[2.3,3,1.2,30,555]}]

def to_do(action):  
    if action == 'show':
        get_items()
    elif action == 'add':
        add_item()
    elif action == 'sell':
        sell_item()
    elif action == 'exit':
        return True
    else:
        return False

def add_item(name='', quantity ='', unit='', unit_price=''):
    print('Adding to warehouse...')
    items[0]['name'].append(input('Item name: '))
    items[1]['quantity'].append(input('Item quantity: '))
    items[2]['unit'].append(input('Item unit of measure. Eg. l, kg, pcs: '))
    items[3]['unit_price'].append(int(input('Item price in PLN: ')))
    print('Successfully added to warehouse. The current status is: ')
    get_items()

def sell_item(name='', quantity=int()):
    name = input('Item name: ')
    name = name.capitalize()
    if name not in items[0]['name']:
        print('There is no requested product.')
    else:

        quantity = int(input('Quantity to sell: '))
        quantity_index = items[0]['name'].index(name)
        if items[1]['quantity'][quantity_index] >= quantity:
            items[1]['quantity'][quantity_index] = items[1]['quantity'][quantity_index] - quantity
            print(f'Successfully sold {quantity} of {name}')
            get_items()
        else:    
            print('There is not enough product to sell')
        


def get_items():
    print('Name\tQuantity\tUnit\tUnit Price (PLN)')
    print('----\t--------\t----\t----------------')
    
    a = []
    for param in items:
        for item in param.values():
            a.append(item)

    i = 0
    for entry in a[0]:
        print(a[0][i],'\t',a[1][i],'\t       ',a[2][i],'\t',a[3][i])
        i+=1

while to_do(action) != True:
    action = str(input('What do you want to do?'))
