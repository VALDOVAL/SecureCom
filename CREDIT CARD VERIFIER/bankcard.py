from authentication import Authentication #athentication library import

#class
class BankCard:
    def __init__(self, card_num):# initialization
        self.card_num = card_num #assign card number
        self.vendor = self.get_vendor(self.card_num) #assign vendor fro calling get_vendor method
#method
    def get_vendor(self, card_num):
        validity = Authentication().verify_card(card_num) #call verify card method fron Authentication class and assign it to variable
       #check for validity
        if validity == 'Valid':
            first_digit = str(card_num)[0] #assign first digits of card number
            industry = '' #declare which type of industry card belongs to

            if first_digit == '1' or first_digit == '2': #if first digit of card is 1 or 2
                industry = 'Airline' #it is in airline industry
            elif first_digit == '3': #if digit is 3
                industry = 'Travel & Entertainment'
                issuer = 'American Express' #amex card
            elif first_digit == '4' or first_digit == '5' or first_digit == '6': #if digits are 4 or 5 or 6
                industry = 'Banking' # it is banking industry
                if first_digit == '4': #if digit is 4
                    issuer = 'Visa' #card is VISA
                elif first_digit == '5': #if digit is 5
                    issuer = 'MasterCard' #it is Mastercard
                else:
                    issuer = 'Discover' #any other digit is Discover
            return '\tIndustry: {0} \n\tIssuer: {1}'.format(industry, issuer)
        else:
            self.vendor = "Invalid card has no Vendor" #otherwise card has no vendor
            return self.vendor

    def get_card_details(self):
        return "\nCARD DETAILS\nCard No.: {0} \nVendor Info: \n{1}".format(self.card_num, self.vendor)

