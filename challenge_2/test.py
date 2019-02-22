import unittest
import claim_repo
from claim import Claim


class Testclaim_repo (unittest.TestCase):

    def test_claim_repo_create_claim_should_add_to_all_claims(self):
        #arrange
        claimID = 5
        claimtype = 'something'
        description = 'description'
        claimamount = 4
        dateofincident = 'dateofincident'
        dateofclaim = 'dateofclaim'
        isvalid = 'yes'
        #act
        claim1 = claim_repo.create_claim(claimID, claimtype, description, claimamount, dateofincident, dateofclaim, isvalid)
        claim2 = claim_repo.create_claim(2, 'hat', 'hi', 6, '1/0', '1/0', 'yes')
        actual = len(claim_repo.all_claims)
        expected = 2
        #assert
        self.assertEqual(actual, expected)
    def test_claim_repo_take_care_should_first_claim(self):
        actual = claim_repo.take_care()
        expected = 1