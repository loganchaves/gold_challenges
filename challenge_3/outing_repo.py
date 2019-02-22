from outing import Outing 
all_outings = []
def create_outing(outing_type, numberofpeople, date, costperperson, costperevent):
    new_outing = Outing(outing_type, numberofpeople, date, costperperson, costperevent)
    all_outings.append(new_outing)
    return new_outing
def total_cost_this_year():
    for o in all_outings:
        cost = 0 
        for o in all_outings:
            cost += o.totalcostevent
            print(cost)
        return cost 
            
def total_cost_of_type(user_input):
    for o in all_outings:
        cost = 0
        outing_type = o.outing_type
        
        if outing_type == user_input:
            cost += o.totalcostevent
            print(cost)
            return cost 
        
def exit_yo ():
    exit(0)