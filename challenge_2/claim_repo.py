import claim

all_claims = []

def create_claim(claimID, claimtype, description, claimamount, dateofincident, dateofclaim, isvalid):
    new_claim = claim.Claim(claimID, claimtype, description, claimamount, dateofincident, dateofclaim, isvalid)
    all_claims.append(new_claim)
def take_care():
   del all_claims[0] 