from frappe.model.document import Document

class AirplaneTicket1(Document):
	#Total Amount = Flight Price + Sum of amounts of all the add-ons
  def validate(self):
       
        self.remove_duplicate_add_ons()  # Remove duplicate add-ons before calculating the total amount
        self.calculate_total_amount() # Calculate the total amount after ensuring add-ons are unique

  def remove_duplicate_add_ons(self):
        unique_add_ons = {} # Dictionary to track unique add-ons based on their type or identifier
        
        # Iterate through the add-ons to keep only unique ones
        for add_on in list(self.add_ons):  # Create a copy to iterate over
            if add_on.amount not in unique_add_ons:
                unique_add_ons[add_on.amount] = add_on  # Use a relevant field as identifier
            else:
                self.remove(add_on)# Remove the duplicate entry from the child table

        
        self.add_ons = list(unique_add_ons.values())# Reassign the filtered unique add-ons back to the child table

  def calculate_total_amount(self):
        total_amount = self.flight_price or 0 # Initialize the total amount with the flight price
        add_ons_total = sum([add_on.amount for add_on in self.add_ons]) # add the amounts of all unique add-ons

        total_amount += add_ons_total # Final total amount including flight price and add-ons total

        # Set the total amount in the document
        self.total_amount = total_amount   
