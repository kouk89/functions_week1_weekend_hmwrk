# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

    
    



def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(pets_sold, number_sold):
    pets_sold["admin"]["pets_sold"] += number_sold

def get_stock_count(stock_count):
    stock_count = len(["pets"])
    return stock_count

def get_pets_by_breed(pet_shop, breed):
    basket = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            basket.append(pet)
    return basket
            




def find_pet_by_name(pet_shop):
    return pet_shop["pets"][3]["name"]

def find_pet_name(pet_shop, name):
    for name in pet_shop:
        if pet_shop["name"] == ("Fred"):
           return name
    else:
           return None

def find_pet_name(pet_shop, name):
    for name in pet_shop:
        if pet_shop["name"] == ("Arthur"):
            return name
        else:
            return None
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def remove_customer_cash(self_customers):
        return self_customers[0]["cash"] - 100

def get_customer_pet_count(self_customers):
    return self_customers[0]["pets"]

def add_pet_to_customer(self_customers):
    return self_customers[0]["pets"] + 1
    
