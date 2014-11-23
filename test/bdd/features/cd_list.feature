Feature:  A customer checks out a CD.
		  The system makes sure the details are correct and it’s recorded as rented.

		  Scenario: Check out a CD
		  Given Customer "James" with ID "007"
		  And CD with ID "CD2", title "Beatles Greatest Hits", has a rental period of "2" days and isnot currently rented
		  When the clerk checks out the CD with ID "CD2" to customer with ID "007" on "1/21/2011"
		  Then CD with ID "CD2" is recorded as rented with customer ID "007"
		  And rental contract printed with customer ID "007", customer name "James", CD ID "CD2", CD title "Beatles Greatest Hits", and rental due on "1/23/2011"
		  