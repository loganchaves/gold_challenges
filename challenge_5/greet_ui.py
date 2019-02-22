import greet_repo
import greet

def create():
    firstname = input('firstname: ')
    lastname = input('lastname: ')
    cust_type = input('type of customer: ')
    if cust_type == 'potential':
        email = 'We currently have the lowest rates on Helicopter Insurance!'
    elif cust_type == 'current':
        email = 'Thank you for your work with us. We appreciate your loyalty. Heres a coupon.'
    elif cust_type == 'past':
        email = 'Its been a long time since weve heard from you, we want you back'
    else: 
        email = 'sup'
    greet_repo.create_customer(firstname, lastname, cust_type, email)








while True:
    x = input('1.create a customer\n'+'2.view email\n'+'3.update\n'+'4.delete\n' ':')
    if x == "1":
        create()
    if x == '2':
        print(greet_repo.customers)
    if x == '4':
        customer_to_del = input('customers lastname: ')
        for i, customer in enumerate(greet_repo.customers):
            if customer.lastname == customer_to_del:
                greet_repo.customers.remove(customer)
      
            
               