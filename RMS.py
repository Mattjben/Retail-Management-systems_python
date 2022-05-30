# COSC2531 Assignment 1 
# Matthew Bentham S3923076

# reflection: 
# The most challenging section of the code was displaying the order history of each customer because 
# it involved keeping tack of allot of varibales aT mutiple stages of the ordering process (i.e. needed to keep 
# track of the purchases number , quantity of each product in each purchase , customer name and product name across
# the entire sytem)


# with extra time I would:

#1) experiment with calculating the most valuable customer just using the product dictionary and order history 
# to see if that simplifers the code at all instead of using an extra dictionary for that calculation
#2) I would try and make the code more readible by finding more succinct alternatives to nested if statements and nested while loops


# CODE---------------------------------------------------------------------------------------------------------------------------------------------


# Predefined functions:

def waitfunc():
    ''' This functions just runs a while loop 10000000 which casues 
    the program to wait so that the user has time to read the previous  
    output before the code continues to run.
    '''
    print('\n')
    sys.stdout.write('Press ENTER to progress further ')
    sys.stdout.flush()
    wait = sys.stdin.readline().strip()
    return 

def checkvalidnum(x):
    ''' This functions checks if the value entered is a numeric value 
    '''
    if type(x) == float or type(x) == int:
        result = True
    else: 
        result = False
    return result




# Variables 
# Customers: Customers and total amount spent are stored into a dictionary 
# -> Using a dictionary allows each customer and total spent at store to 
# be stored cocurrently so that the 'most valuable customer' can be calculated
#  with ease


Customersdict = {'Matthew Bentham': 8.0,
                'Frank Johnson' : 33.0 ,
                'Zach Bentley' : 40.0}



# Members: Members are stored in a list as name is the only vairbale that needs to be 
# obtained

Members = ['Matthew Bentham']

# Products: products are stored in a 1D dictionary as both product name and price both 
# need to be stored 

Productdict = {
    "1kg whole wheat flour" : 3.90 ,
    "Uncle Tobys rolled oats" : 5.0,
    "2L full cream milk" : 8.0,
    "White sliced bread":3.40


}

# Order History: I stored customers order history as a dictionary with the values being 
# 2 dimensional lists so that the product name , quantity and purchases number could be stored 
# for each customer and their indivudal purchases.

# each list is formated as:   [Product name   , product quantity , purchases number ]
# for example if i bought 2 X milk and 1 x oats in my first purchase it would be stored as: 
# "Matthew Bentham" : [["2L full cream milk", 2,1],["Uncle Tobys rolled oats", 1,1]]

orderhistory = {
    "Matthew Bentham" : [["2L full cream milk", 1,1],]
    ,'Frank Johnson':[["2L full cream milk", 5,1],]
    ,"Zach Bentley":[["2L full cream milk",1,1],["Uncle Tobys rolled oats", 5,2]],
}


#--------- MENU: 
# I placed the entire code in an inifite while loop so that the code restarts after the respective 
#menu option has run (i perfer while loops for this function as its more succinct )
k=0
while k == 0:
    print("Welcome to Matthew Bentham's retail management system!\n")

    print("#########################################################")
    print("MENU OPTIONS:")
    print("1: Place an order")
    print("2: Add/update products and prices")
    print("3: Display existing customers")
    print("4: Display existing customers with membership")
    print("5: Display exisiting products")
    print("6: Reveal the most valuable customer")
    print("7: Display a customer order history")
    print("0: exit program")
    print("#########################################################")
    import sys
    
    sys.stdout.write("Choose one option:")
    sys.stdout.flush()
    Opt = int(sys.stdin.readline().strip())
    
    #--------- OPTION 1: Place an order
    if Opt == 1:
        # I used sys.stdout.write for all my input prompts and sys.stdout.flush() to push out all data that has been buffered
        sys.stdout.write("Enter a Customer name (First and last):")
        sys.stdout.flush()
        Customer = sys.stdin.readline().strip()

        # Initialise varibales: 
        # Used variables to keep track of the number of products the current user is buying in each purchase 
        #and the number of purchases a customer has made (refers ti order history dict if returning customer) 
        product_num = 0
        if Customer in Customersdict:
            purchase_num = orderhistory[Customer][-1][2]
        else: 
            purchase_num = 0 


        # Use list to store infomation on the names of all the products a customer is buying and the quanities of each product 
        product_names = []
        product_quants = []

        # Another inifite while loop was used so that a customer can keep purchasing products until they specificy no
        # when prompted
        w=0
        while w == 0:

            sys.stdout.write("Enter product name: (e.g. 1kg whole wheat flour, Uncle Tobys rolled oats, 2L full cream milk,White sliced bread) : " )
            sys.stdout.flush()
            product_name =sys.stdin.readline().strip()
            product_names.append(product_name)
            i = 0
            if product_names[product_num] not in Productdict:
                while i == 0:
                    # While loop was used so that the error keeps occuring till user enters the correct value
                    print(" \n//--------------------------------------------------//")
                    print("//ERROR: Product not available (not in product list)//")
                    print("//--------------------------------------------------// \n")
                    sys.stdout.write("Enter product name(e.g. 1kg whole wheat flour, Uncle Tobys rolled oats, 2L full cream milk,White sliced bread) : " )
                    sys.stdout.flush()
                    product_names[product_num] = sys.stdin.readline().strip()
                    if product_names[product_num] in Productdict:
                        i = 1
                        continue
                    else: continue
            if Productdict[product_names[product_num]] == 0:
                    print(" \n//--------------------------------------------------//")
                    print("//ERROR: This product has no price and cannot be sold//")
                    print("//--------------------------------------------------// \n")
            else:
                sys.stdout.write("Enter quantity of product: ")
                sys.stdout.flush()
                # try / except loop was used to account for users entering strings that cannot be converted to an integer 
                try:
                    product_quant = int(sys.stdin.readline().strip())
                    notneg = product_quant > 0 
                except ValueError:
                    product_quant = sys.stdin.readline().strip()
                    notneg = False
                product_quants.append(product_quant)
                i=0
                if notneg == False:
                    while i == 0:
                        # While loop was used so that the error keeps occuring till user enters the correct value
                        print(" \n//-------------------------------//")
                        print("//ERROR: INVALID PRODUCT QUANTITY//")
                        print("//-------------------------------// \n")
                        sys.stdout.write("Enter quantity of product: ")
                        sys.stdout.flush()
                        try:
                            product_quant = int(sys.stdin.readline().strip())
                            notneg = product_quant > 0 
                        except ValueError:
                            product_quant = sys.stdin.readline().strip()
                            notneg = False
                        product_quants.append(product_quant)
                        if notneg == True:
                            i = 1
                            continue
                        
                sys.stdout.write("Is another item being purchased [y/n] ? :")
                sys.stdout.flush()
                new_itemq = sys.stdin.readline().strip()
                i =0 
                while i == 0:
                    #Another inifite while loop is nested so that users can keep purchasing prodcucts still they speficy otherwise

                    if new_itemq == 'y':
                        product_num +=1
                        i=1
                        continue
                    if new_itemq == 'n':

                       
                        if Customer not in Members:
                            sys.stdout.write("Customer does not have a membership. Does the customer want to have a membership [ enter y or n]?")
                            sys.stdout.flush()
                            ans = sys.stdin.readline().strip()
                            z =0
                            while z == 0:

                                if ans == 'y':
                                    Members.append(Customer)
                                    z=1
                                    continue
                                if ans == 'n':
                                    z=1
                                    continue
                                else:
                                    print(" \n//-----------------------//")
                                    print("//ERROR: INVALID RESPONSE//")
                                    print("//-----------------------// \n")
                                    sys.stdout.write("Customer does not have a membership. Does the customer want to have a membership [ enter y or n]?")
                                    sys.stdout.flush()
                                    ans = sys.stdin.readline().strip()
                                    continue


                        #Use discount varibale to calcuate the discount a customer recives ( defaut = 0% , membership = 5%)
                        discount = 1
                        purchase_num += 1


                    
                        Unit_prices =[]
                        print("------------------------------ ")
                        # for loop is used to iterate through all the products a customer has bought , whilst 
                        # the varible i is used as an index for the current product name and quantity 
                        # I generally use for loops when i need to have an index varible that iterates through a specific range as it 
                        # requres less code than a while loop. 
                        for i in range(0,len(product_names)):
                            Unit_price = Productdict.get(product_names[i])*product_quants[i]
                            Unit_prices.append(Unit_price)
                            print("%s purchased %d x %s. " %(Customer,product_quants[i],product_names[i]))
                            print('Unit price:       $ %d (AUD)' %(Unit_price) )
                            if Customer in orderhistory:
                                orderhistory[Customer] += [[product_names[i],product_quants[i],purchase_num,]]
                            else:
                                new_order = {Customer :[[product_names[i],product_quants[i],purchase_num,]]}
                                orderhistory.update(new_order)
                            
                            
                        
                        # Calulate member discount:
                        if Customer in Members:
                            discount = 0.95
                            print(Customer,'gets a discount of 5.0%.')
                        total_price = sum(Unit_prices)*discount
                        print('Total price:      $ %d (AUD)' %(total_price))
                    
                        # Add any new customer to dictionary:
                        if Customer not in Customersdict:
                            Customersdict[Customer] = 0.0
                        Customersdict[Customer] += total_price
                        print("------------------------------ \n", end=" ")

                         # Use i and w to exit out of the currently nested while loops and the menu is shown after final price is calculated
                        i=1
                        w=1
                    else:
                        print(" \n//-----------------------//")
                        print("//ERROR: INVALID RESPONSE//")
                        print("//-----------------------// \n")
                        sys.stdout.write("Is another item being purchased [y/n] ? :")
                        sys.stdout.flush()
                        new_itemq = sys.stdin.readline().strip()
                        continue
                
                waitfunc()
    
    #--------- OPTION 2: Add/update products and prices
    if Opt == 2:
    
        sys.stdout.write("Enter products to add/update:")
        sys.stdout.flush()
        Prod_new = sys.stdin.readline().strip()
        Prod_new = Prod_new.split(",")
        # Split function enables the input to be split on every , and inserted into a list
        sys.stdout.write('Please enter Price(s) of product(s): ')
        sys.stdout.flush()
        Prod_new_price = (sys.stdin.readline().strip()).split(",")
        print('----------------------------')
        print('Product(s) updated:')
        print('------------------------')
        # for loop is used to iterate through the prices given and enumerate function is used to keep an index so that the correspoding product name given 
        # can be instered into the product dictionary 
        for indx , price in enumerate(Prod_new_price):
            #Try/Except is used to account for when user enters a non-numeric value 
            try:
                price = float(price)
                notneg = price > 0
            except ValueError:
                notneg = False

            if Prod_new[indx] in Productdict:
                del Productdict[Prod_new[indx]]
            if notneg == True:
                Productdict[Prod_new[indx]] = price
                print(str(Prod_new[indx]),':','$'.rjust(15-len(Prod_new[indx])) ,str(price),'(AUD)')
            else: 
                Productdict[Prod_new[indx]] = 0
                print(str(Prod_new[indx]),':','$'.rjust(15-len(Prod_new[indx])),'0.0 (AUD)')

        waitfunc()
    
#--------- OPTION 3:  Display existing customers
# FOR loops are used in options 3 , 4 and 5 as all require a loop that can easly iterate through
# a list / dictionary 
    if Opt == 3:
        print('--------------------------------------')
        print('Existing customers:')
        print('--------------------------------------')
        for keys , values in Customersdict.items():
            print(keys )
        print('--------------------------------------')
        waitfunc()
#--------- OPTION 4:  Display existing customers with membership
    if Opt == 4:
        print('--------------------------------------')
        print('Existing memebers:')
        print('--------------------------------------')
        for x in range(len(Members)):
            print(Members[x])
        print('--------------------------------------')
        waitfunc()

#--------- OPTION 5:  Display exisiting products
    if Opt == 5:
        print('--------------------------------------')
        print('Existing Products:'+'Price ($)'.rjust(20))
        print('--------------------------------------')
        for product , price in Productdict.items():
            print(product+'{:.2f}'.format(price).rjust(35-len(product)))
        print('--------------------------------------')
        waitfunc()
#--------- OPTION 6:  Reveal the most valuable customer
    if Opt == 6:
        # USED CODE FROM SORUCE HELP CODE THIS SECTION:
        # Citation: Thispointer.com. 2022. Python : How to get all keys with maximum value
        #  in a Dictionary – thisPointer. [online] Available at:
        #  <https://thispointer.com/python-how-to-get-all-keys-with-maximum-value-in-a-dictionary/>
        #  [Accessed 26 March 2022].

        itemMaxValue = max(Customersdict.items(), key=lambda x: x[1])
        listOfKeys = list()
        for key, value in Customersdict.items():
            if value == itemMaxValue[1]:
                listOfKeys.append(key)
        print('--------------------------------------')
        print('Most valuable customer/s:')
        print('--------------------------------------')
        for n in listOfKeys:
            print(n.center(25))
        print('--------------------------------------')
        waitfunc()
#--------- OPTION 7:  Display a customer order history
    if Opt ==7:
        sys.stdout.write("Enter customer name:")
        sys.stdout.flush()
        Customer = sys.stdin.readline().strip()

        w= 0 
        while w == 0:
            if Customer in Customersdict:


                print('This is the order history of',Customer,':')
                print('-----------------------------------------------------------------------------------------------------------------------------------')
                print(str('1kg whole wheat flour ').rjust(50) + 'Uncle Tobys rolled oats'.rjust(25) + '2L full cream milk'.rjust(25)+'Sliced white bread'.rjust(25))
                print('___________________________________________________________________________________________________________________________________')
                no_purchases = orderhistory[Customer][-1][2] # number of purchases is calulated from the purchase number of the final entry in a customers 
            
                # order history 

                # Double nested for loop iterates through each purchase and each product in said purchases to calculate the quantity of each 
                for n in range(no_purchases) :
                    
                 
                    for x in orderhistory[Customer]:
                        
                  
                      # If statements are used to identify which products and what quanities of each product is present in the orderhistory
                        if x[2] == n+1:
                            wwf =0 
                            utro = 0
                            fcm = 0
                            wsb = 0
                            if x[0] == '1kg whole wheat flour':
                                wwf = x[1]
                            if x[0] == 'White sliced bread':
                                wsb = x[1]
                               
                            if x[0] == 'Uncle Tobys rolled oats':
                                utro = x[1]
                                
                            if x[0] == '2L full cream milk':
                                fcm = x[1]
                               
                            print('Purchase ' + str(n+1)+str(wwf).rjust(30)+str(utro).rjust(25)+str(fcm).rjust(25)+str(wsb).rjust(25))
                        
                print('-----------------------------------------------------------------------------------------------------------------------------------')
                w=1
            else: 
                print(" \n//----------------------------//")
                print("//ERROR: CUSTOMER DOES NOT EXIST//")
                print("//-----------------------------// \n")
                sys.stdout.write("Enter customer name:")
                sys.stdout.flush()
                Customer = sys.stdin.readline().strip()
        waitfunc()
#--------- OPTION 0:  exit program
    if Opt == 0:
        break

