Feature:  A customer checks out a CD.
		  The system makes sure the details are correct and it’s recorded as rented.

		  Scenario: Check out a CD
		  Given customer has id
		  And CD has id 
		  And CD is not currently rented
		  When I check out the cd
		  Then the CD is recorded as rented 
		  And a rental contract is printed