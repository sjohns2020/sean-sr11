# WRITE YOUR FUNCTIONS HERE

from hashlib import new


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] = get_total_cash(pet_shop)+cash
    return get_total_cash(pet_shop)

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pets):
    pet_shop["admin"]["pets_sold"] = get_pets_sold(pet_shop)+pets
    return get_pets_sold(pet_shop)

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    breed_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breed_list.append(pet)
    return (breed_list)

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return (pet)

def remove_pet_by_name(pet_shop, name):
    pet_to_remove = find_pet_by_name(pet_shop, name)
    list_of_pets = pet_shop["pets"]
    for pet in list_of_pets:
        if pet["name"] == pet_to_remove["name"]:
            list_of_pets.remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    list_of_pets = pet_shop["pets"]
    list_of_pets.append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer_cash = get_customer_cash(customer) 
    customer["cash"] = customer_cash - cash
    return customer["cash"]

def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet):
    customer_pets = customer["pets"]
    customer_pets.append(new_pet)


# OPTIONAL ----

def customer_can_afford_pet(customer, new_pet):
    customer_funds = get_customer_cash(customer)
    new_pet_cost = new_pet["price"]
    if customer_funds >= new_pet_cost:
        return True
    else:
        return False 

def sell_pet_to_customer(pet_shop, pet, customer):
    customer_pets = customer["pets"]
    pet_shop_pets = pet_shop["pets"]
    for pet_shop_pet in pet_shop_pets:
        if pet_shop_pet == pet:
            if customer_can_afford_pet(customer, pet):
                customer_pets.append(pet)
                pet_shop["admin"]["pets_sold"] = get_pets_sold(pet_shop) +1
                remove_customer_cash(customer, pet["price"])
                pet_shop["admin"]["total_cash"] = get_total_cash(pet_shop) + pet["price"]

