class Email: 
    def __init__(self, firstname, lastname, cust_type, email ):
        self.firstname = firstname
        self.lastname = lastname
        self.cust_type = cust_type
        self.email =email
    def __repr__(self):
        return f'{self.firstname}, {self.lastname}, {self.cust_type}, {self.email}'