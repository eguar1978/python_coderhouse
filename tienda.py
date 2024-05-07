from cliente import Cliente

clientes = [] 

def register_customer(name, mail, address, phone):
    new_customer = Cliente(name, mail, address, phone)
    clientes.append(new_customer)
    return new_customer

def process_purchase(customer, buy):
    customer.register_purchase(buy)

def show_information():
    for customer in clientes:
        print(customer)

def show_count_clientes():
    return len(clientes) 

def get_customer(index):
    if 0 <= index < len(clientes):
        return clientes[index]
    else:
        return None

def get_total_customers():
    return len(clientes) - 1  
