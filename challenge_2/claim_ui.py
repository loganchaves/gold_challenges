import claim_repo




def create():  
    
    claimID = (input('ClaimID: '))
    claimtype = input('Enter type of claim: ')
    description = input('Description: ')
    claimamount = (input('amount:'))
    dateofincident = input('date of incident: ')
    dateofclaim = input('date of claim: ')
    isvalid = input('is this claim valid yes or no: ')

    claim_repo.create_claim(claimID, claimtype, description, claimamount, dateofincident, dateofclaim, isvalid) 

while True:

    x = input('1.add new claim\n'+'2.view claims\n'+'3.take care of next claim\n')
    
    if x == '1':
        create()
    elif x == '2':
        print (f'ClaimID,','claimtype,','description,','date of incident,','date of claim,', 'valid or nah') 
        print(claim_repo.all_claims)
            
    elif x == '3':
        print (claim_repo.all_claims[0])
        y = input('take care of this claim right meow? Y/N: ').lower()
        if y == 'y':
            claim_repo.take_care()
        elif y == 'n':
            pass
