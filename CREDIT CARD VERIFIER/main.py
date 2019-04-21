from bankcard import * # import bankcard class
from authentication import * # import authentication library
#main method
def main(): #sample bank card numbers to test
    card_num_list = [4319473018453644, 4319550212629259, 4319327412228129, 4319473018453644]
    cnum = input("Please enter the card number")
    print(cnum)
    card_num = card_num_list[3] #assign list to card_num
    card_num=int(cnum)
    auth = Authentication() #create a variable to call on Authentication class
    card = BankCard(card_num) #create a variable to call on Bankcard class


    # 1)Verify
    # assign verification to variable
    verify = auth.verify_card(card_num)
    print(verify)


    #2) Vendor: Displaying Vendor information
    #assign verification of vendor card details
    details = card.get_card_details()
    print(details) #print vendor card details


    #3) Calculate checksum
    portion = input("Please enter the first ") #assign call to checksum method

    checksum=str(fportion)
    checksum = auth.get_checksum(fportion)

    print("Checksum: ", checksum) #print checksum



    # 4) Generate random valid card
    vendor = "MasterCard" # declare and initialize vendor variable
    if vendor == 'Visa': # check if vendor variable is assigned VISA
        first_digit = '4' # check if first digit contains 4
    elif vendor == 'MasterCard': #check for Mastercard
        first_digit = '5' #check if first digit is 5
    checksum = auth.get_checksum(first_digit) #call checksum method and assign result to checksum
    print("Checksum: ", checksum) #print out result of checksum

#call main method
if __name__ == '__main__':
    main()
