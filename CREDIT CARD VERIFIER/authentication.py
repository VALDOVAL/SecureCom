import random #import library for ramdom number generation

class Authentication: # class create
    def __init__(self): # inititialsation method
        self.sum = 0 # assign zero to sum

    def verify_card(self, card_num): # method to verify card
        total_even_i = 0 #declare and initialize even numbers placements
        total_odd_i = 0 # declare and initialize oadd numbers placements
        str_list = str(card_num) # assign card numbers

        #loop to look through the length of card
        for i in range((len(str_list) - 1), -1, -1):
            if i % 2 == 0: # checkfor even number placements
                num_even_i = int(str_list[i]) # assign card numbes
                num_even_i = num_even_i * 2
                # check for even number placements
                if num_even_i > 9:
                    num_even_i = (num_even_i - 9) # assign even numbers
                total_even_i += num_even_i #add to variable
            else:
                total_odd_i += int(str_list[i]) #add up all odd number placements after converting to integer

        self.sum = total_even_i + total_odd_i # add together even and off number placements
        if self.sum % 10 == 0:
            return "Valid" # return valid card
        else:
            return "Invalid" # esle return invalid card

        # checksum method here
    def get_checksum(self, first_portion):
        first_portion = str(first_portion) # assign first didgit of card
        valid_card_lenght = 16 # assign card length to 16
       #loop through card length minus the first digits
        for x in range((valid_card_lenght-1) - len(first_portion)):
            other_portion = str(random.randint(0, 9))#generate random number for the rest of the digits
            first_portion += other_portion #add the two parts of the digits together

        self.verify_card(int(first_portion)) #verification of card type and validity
        if self.sum % 10 == 0: #if modulus 10 results in 0
            checksum = 0 #checksum is 0
        else:
            checksum = 10 - (self.sum % 10) #subtract modulus result of sum of card digits from 10
            full_card = first_portion + str(checksum) #append digits together
        print("Generated Card: ", full_card) #card is generated
        print(self.verify_card(full_card)) #card is verified
        return checksum #checksum is returned
