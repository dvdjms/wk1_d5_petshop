# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop_name):
    return shop_name['name']


def get_total_cash(shop_name):
    return shop_name['admin']['total_cash'] 


def add_or_remove_cash(shop_name, cash):
    shop_name['admin']['total_cash'] += cash

 
def get_pets_sold(shop_name):
    return shop_name['admin']['pets_sold'] 


def increase_pets_sold(shop_name, num):
    shop_name['admin']['pets_sold'] += num


def get_stock_count(shop_name):
    return len(shop_name['pets'])


# def get_pets_by_breed(shop_name, breed):
    # list_breed = []
    # i = 0
    # for j in shop_name['pets']:
    #     if breed == shop_name['pets'][i]['breed']:
    #         i += 1
    #         list_breed.append(breed)
    # return list_breed


def get_pets_by_breed(shop_name, breed):
    list_breed = []
    for pet_breed in shop_name["pets"]:
        if pet_breed["breed"] == breed:
            list_breed.append(breed)
    return list_breed


# def find_pet_by_name(shop_name, name):
#     dict_pet_name = { }
#     i = 0
#     for j in shop_name['pets']:
#         if name == shop_name['pets'][i]['name']:
#             dict_pet_name['name'] = name
#             return dict_pet_name
#         i += 1
#     return None


def find_pet_by_name(shop_name, name):
    for pet_name in shop_name["pets"]:
        if pet_name["name"] == name:
            return pet_name

 
def remove_pet_by_name(shop_name, name):
    i = 0
    for j in shop_name['pets']:
        if name == shop_name['pets'][i]['name']:
            del shop_name['pets'][i]
        i += 1

# def remove_pet_by_name(shop_name, name):
#     for pet_name in shop_name['pets']:
#         if pet_name['name'] == name:
#             print(pet_name)
#             del shop_name['pets'] ???????????



def add_pet_to_stock(shop_name, new_pet):
    shop_name['pets'].append(new_pet)


def get_customer_cash(customer):
    return customer['cash']
   

def remove_customer_cash(customer, cash):
    customer['cash'] -= cash


def get_customer_pet_count(customer):
    return len(customer['pets'])


def add_pet_to_customer(customer, new_pet):
    customer['pets'].append(new_pet)
    

  # --- OPTIONAL ---

def customer_can_afford_pet(customer, new_pet):
    if new_pet['price'] <= customer['cash']:
        return True
    return False


def sell_pet_to_customer(shop_name, pet_name, customer):
    # Check pet_name is not None
    if pet_name == None:
        return False
    # Get pet_name out of dictionary
    pet_nam = pet_name['name']
    # Get price of pet - call function
    price = get_price_of_pet(shop_name, pet_nam)
    # Can customer afford pet - if yes call further functions to action changes
    if get_customer_cash(customer) >= price:
        remove_customer_cash(customer, price)
        add_or_remove_cash(shop_name, price)
        add_pet_to_customer(customer, pet_name)
        increase_pets_sold(shop_name, 1)


# Function created to get price of pet from shop_name
# def get_price_of_pet(shop_name, name):
#     i = 0
#     for j in shop_name['pets']:
#         if name == shop_name['pets'][i]['name']:
#             price = shop_name['pets'][i]['price']
#             return price
#         i += 1
#     return None
    

def get_price_of_pet(shop_name, name):
    for pet_name in shop_name["pets"]:
        if pet_name["name"] == name:
            return pet_name['price']

