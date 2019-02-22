from greet import Email 
customers = []

def create_customer(firstname, lastname, cust_type, email):
    cutomer = Email(firstname, lastname, cust_type, email)
    customers.append(cutomer)
    return customers
def update(cust_to_delete, firstname, lastname,):
    pass


     