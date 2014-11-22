Feature:  A customer checks out a CD.
		  The system makes sure the details are correct and it’s recorded as rented.

		  Scenario: Given customer has id
		  And CD has id 
		  And CD is not currently rented
		  When the clerk checks out the cd
		  Then the CD is recorded as rented and a rental contract is printed