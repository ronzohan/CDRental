Feature:  A customer checks out a CD.
		  The system makes sure the details are correct and it’s recorded as rented.

		  Scenario: Check out a CD
		  Given I visit the homepage
		  Given customer has id "001"
		  And CD has id "CD2"
		  And CD "CD2" is not currently rented
		  When I check out the cd "CD2" with customer_id "001"
		  Then the CD "CD2" is recorded as rented 
		  And a rental contract is printed