class Claim:
    def __init__(self, claimID, claimtype, description, claimamount, dateofincident, dateofclaim, isvalid):
        self.claimID = claimID
        self.claimtype = claimtype
        self.description = description
        self.claimamount = claimamount
        self.dateofincident = dateofincident
        self.dateofclaim = dateofclaim
        self.isvalid = isvalid
    def __repr__(self):
        return f'{self.claimID} {self.claimtype} {self.description} {self.claimamount} {self.dateofincident} {self.dateofclaim} {self.isvalid}'
  