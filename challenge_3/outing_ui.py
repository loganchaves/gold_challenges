import outing_repo
def create ():
    try:
        outing_type = input('what is the outing type: ')
        numberofpeople = int(input('How many people in attendince: '))
        date = input ('Date: ')

        costperperson = float(input('cost per person: '))

        costperevent = numberofpeople * costperperson

        outing_repo.create_outing(outing_type, numberofpeople, date, costperperson, costperevent )
    except Exception:
        print('invalid input')

while True:

    x = input('1.enter event info\n'+'2.view outings\n'+'3.total cost by type\n'+'4.total cost of all\n'+'5.EXIT\n')
    if x == '1':
        create()
    elif x == '2':
        print(outing_repo.all_outings)
    elif x == '3':
        user_input = input('event type: ')
        totalcost = outing_repo.total_cost_of_type(user_input)
        if totalcost == 0:
            print ('not found')
    elif x == '4':
        outing_repo.total_cost_this_year()
    elif x == '5':
        outing_repo.exit_yo()
    else: 
        print('dont be dumb enter a number')