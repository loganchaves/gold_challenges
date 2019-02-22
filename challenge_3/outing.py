class Outing:
    def __init__(self, outing_type, numberpeople, date, totalcostperson, totalcostevent):
        self.outing_type = outing_type
        self.numberpeople = numberpeople
        self.date = date
        self.totalcostperson = totalcostperson
        self.totalcostevent = totalcostevent
    def __repr__ (self):
        return f'{self.outing_type} {self.numberpeople} {self.date} {self.totalcostperson} {self.totalcostevent}'

