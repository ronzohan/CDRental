Feature:  A customer checks out a CD.
		  The system makes sure the details are correct and it’s recorded as rented.

		  Scenario: Check out a CD
		  Given Customer "Ron Magno" with ID "1"
		  And CD with ID "1", title "Beatles Greatest Hits", has a rental period of "2" days and is not currently rented
		  When the clerk checks out the CD with ID "1" to customer with ID "1" on "1/21/2011"
		  Then CD with ID "1" is recorded as rented with customer ID "1"
		  And rental contract printed with customer ID "1", customer name "Ron Magno", CD ID "1", CD title "Beatles Greatest Hits", and rental due on "1/23/2011"
		  