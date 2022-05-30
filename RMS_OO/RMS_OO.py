# COSC2531 Assignment 2 
# Matthew Bentham 
# Student ID: S3923076

# External python modules: 
import datetime # used for storing date variable in order class
from datetime import  datetime
from logging import exception
import sys

# CREATE LIST OF FILES INPUTTED AS COMMAND LINE ARGUMENTS:
files = [None , None , None]
for i,file in enumerate(sys.argv):
    if i != 0:
        files[i-1]=file
      


#IMPROVEMENTS: 
# Ideally if time wasnt a factor i would like to find better ways to deal with errors derived from the user inputs as using 
# a bunch of if statements in a while loop uses up allot of space and effects the overall readability. Additionally , i would like 
# to find a more succient way to check the formats of the inputed files. 

#MOST CHALLANGING ASPECT: 
# The most challanging aspect of this code for me was mainly the inital class definitions and incorperating the classes 
# into my code mainly due to the fact that i had never done object oriented programming before so there was a big learning curve 



# CLASSES: 


class Customer:
    #Attributes:
     ID = 0
     Name = None
     Value = 0
     Discount_rate = 0
    # Constructor:

     def __init__(self,ID,name,value,discount_rate):
         self.ID = ID
         self.Name = name 
         self.Value = value
         self.Discount_rate = discount_rate


    # methods:

     def get_discount(self,price):
        discount_rate = 0 
        dis = (discount_rate,price)
        return dis
     @property
     def display_info(self):
         print("--------------")
         print("Customer id: ",self.ID)
         print("Customer name: ",self.Name)
         print("Customer value: ",self.Value)

# I made Memeber and VIPmemeber classes child attributes of the Customer class due to 
# the volume of atributes they both share with the customer class       

class Member(Customer):
    #Attributes 
    Discount_rate = 0.05
    # Constructor:
    def __init__(self,ID,name,value,dis=Discount_rate):
        super(Member,self).__init__(ID,name,value,dis)
        
    # methods:
    def get_discount(self,price):
        discount = self.Discount_rate 
        price = float(price)*(1-self.Discount_rate)
        return (round(discount,2),price)
    @property
    def display_info(self):
        super(Member,self).display_info()
        print("Discount rate: ",(1-self.Discount_rate)*100,"%")
    
    def set_rate(self,rate):
        self.Discount_rate = rate

class VIPMember(Customer):
    #Attributes 
    Discount_rate = 0.10
    discount_r2 = Discount_rate -0.05
    threshold_lim = 1000.0
    # Constructor:
    def __init__(self,ID,name,value,dis=Discount_rate):
        super(VIPMember,self).__init__(ID,name,value,dis)
    # methods:
    def get_discount(self,price):
        if float(price) <= self.threshold_lim:
            dis = self.Discount_rate
        if float(price) > self.threshold_lim:
            dis = self.Discount_rate -0.05
        
        price = float(price)*(1-dis)
        return (round(dis,2),price)
    @property
    def display_info(self):
        super().display_info(self)
        print("1st discount rate: ",(1-self.Discount_rate)*100,"%")
        print("2nd discount rate: ",(1-self.discount_r2)*100,"%") 
        print("Discount threshold: ",self.threshold_lim)
    @staticmethod  
    def set_rate(self,rate):
        self.Discount_rate = rate 
    @staticmethod 
    def set_threshold(threshold):
        VIPMember.threshold_lim = threshold


class Products:
    # Defualt attributes 
    ID= None
    Name = None 
    Price = 0 
    Stock = 0 
    # Constructor:
    def __init__(self,ID,Name,Price,Stock):
        self.ID=ID
        self.Name=Name
        self.Price = Price
        self.Stock = Stock
    # Methods 

    def set_stock(self,Stock):
        self.Stock = Stock 

    def set_price(self,Price):
        self.Price = Price
    @staticmethod
    def checkprice(price):
        try:
            positive = float(price) > 0
        except Exception:
            positive = False
        if positive == False:
            print("-"*63)
            print("\n//ERROR: Invalid product price//\n")
            print("-"*63)
            valid = False
        else:
            valid = True
        return valid



class Orders(): 
    # I used lists to store product objects and Quantitiy values so that an order can 
    #contain multiple products with a corresponding quantity 
    # Defualt Attributes 
    Quantity = []
    Customer = None
    Products = []
    Membership = 0
    Date = None
    #Constructor:
    def __init__(self,Quantity,customer,Products,date,membership=0):
        self.Quantity = Quantity
        self.Customer = customer
        self.Products = Products
        self.Membership = membership 
        self.Date=date
    #Methods:

    def Totalprice(self):
        price =0
        for i in range(len(self.Products)):
            price += round((self.Products[i].Price*self.Quantity[i]),2)
            
        dis_price = round(self.Customer.get_discount(price)[1]+self.Membership,2)

        return [dis_price, price]
    

class Bundle(Products):
    # bundle is a chile class of products with the only additional attribute being product 
    #Default attributes 
    ID = None
    Name = None
    Stock = 0 
    Products = []
    Price = 0
    #Constructor 
    def __init__(self,ID,name,price,stock,products):
        super().__init__(ID,name,price,stock)
        self.Products = products
    @staticmethod 
    def getprice(Products):
        """Method to get the overall price of the bundle giving the
        list of product objects as an input"""
        rec = Records()
        Price = 0
        for product in Products:
            Price += float(rec.find_product(product,"n")[1].Price)
        Price = round(Price * 0.8,2)
        return Price

    def set_stock(self, Stock):
        super().set_stock(Stock)
   

class Records(): 
    # I decided to save each current and past customer , product , bundle and order in a list of objects 
    # that belong to their respective classes so that attributes of all these objects called be easily referenced throughout 
    # the rest of the program 
    Customers = []
    products = []
    bundles = []
    orders = []
# Read-files:
    def read_customers(self,file):
        """ This method is used to read in the customer.txt
        file and save each corresponding line into the attribute 
        Customers 
        """
        with open(file,"r") as txtfile:
            for line in txtfile:
                currentline = line.split(",")
                strip_line = [item.strip() for item in currentline]

                if strip_line[0][0] == 'M':
                    self.Customers.append(Member(strip_line[0],strip_line[1],float(strip_line[3]),float(strip_line[2])))
                if strip_line[0][0] == 'C':
                    self.Customers.append(Customer(strip_line[0],strip_line[1],float(strip_line[3]),float(strip_line[2])))
                if strip_line[0][0] == 'V':
                    self.Customers.append(VIPMember(strip_line[0],strip_line[1],float(strip_line[3]),float(strip_line[2])))
            txtfile.close()


    def read_products(self,file):
        """ This method is used to read in the products.txt
        file and save each corresponding line into the attribute 
        products 
        """
        with open(file,"r") as txtfile:
            for line in txtfile:
                currentline = line.split(",")
                strip_line = [item.strip() for item in currentline]
                if strip_line[0][0] == "B":
                    row = strip_line[0:2]
                    bundle_products = []
                    for strip_line in strip_line[2:-1]:
                        bundle_products.append(strip_line)
                    row.append(Bundle.getprice(bundle_products))
                    row.append(strip_line[-1])
                    try:
                        self.bundles.append(Bundle(row[0],row[1],int(row[2]),float(row[3]),bundle_products))
                    except Exception:
                        self.bundles.append(Bundle(row[0],row[1],int(row[2]),0,bundle_products))
                    

                else:
                    try:
                        self.products.append(Products(strip_line[0],strip_line[1],float(strip_line[2]),int(strip_line[3])))
                    except Exception:
                        self.products.append(Products(strip_line[0],strip_line[1],0,int(strip_line[3])))
            txtfile.close()

    def read_orders(self,file):
        """ This method is used to read in the orders.txt
        file and save each corresponding line into the attribute 
        orders 
        """
        with open(file,"r") as txtfile:
            for line in txtfile:
                products = []
                products_class = []
                quants = []
                currentline = line.split(",")
                strip_line = [item.strip() for item in currentline]
                no_of_orders = (len(strip_line)-2)/2
                for i in range(int(no_of_orders)):
                    prod_indx = 2*i+1
                    products.append(strip_line[prod_indx])
                    quants.append(strip_line[prod_indx+1])
                for prod in products:
                    found = self.find_product(prod,dis='n')
                    products_class.append(found[1])
                found2 = self.find_customer(strip_line[0],dis='n')
                
                date = strip_line[-1]
                
                order = Orders(quants,found2[1],products_class,date)
                self.orders.append(order)
            txtfile.close()
# Find methods:
    def find_customer(self,name,dis = 'y'):
        """This method finds customers based off inputted ID or name"""
        found = False
        data = []
        indx = 0
        for i,item in enumerate(self.Customers):
            if name == item.Name or name == item.ID:
                if dis =='y':
                    print("Customer found!\n","-"*20)
                    print("Customer ID: ",item.ID.rjust(20-len("Customer ID: ")))
                    print("Name: ",item.Name.rjust(20-len("Name: ")))
                    print("Discount rate: ",str(item.Discount_rate).rjust(20-len("Discount rate: ")))
                    print("Value: ",str(item.Value).rjust(20-len("Value: ")))
                    print("-"*20)
                found = True
                data = item
                indx = i
        return found , data ,indx
    def find_product(self,name,dis = 'y'):
        """This method finds Products based off inputted ID or name"""
        found = False
        data = []
        indx = 0
        for i,item in enumerate(self.products):
            if name == item.Name or name == item.ID:
                if dis == 'y':
                    print("-"*20,"\nProduct found!\n","-"*20)
                    print("Product ID: ",item.ID.rjust(20-len("Product ID: ")))
                    print("Name: ",item.Name.rjust(20-len("Name: ")))
                    print("Price: ",'$'.rjust(15-len("Price: ")),item.Price,'(AUD)')
                    print("Stock: ",str(item.Stock).rjust(20-len("Stock: ")))
                    print("-"*20)
                found = True
                data = item
                indx = i
        for w,item2 in enumerate(self.bundles):
            if name == item2.Name or name == item2.ID:
                if dis == 'y':
                    print("-"*20,"\nBundle found!\n","-"*20)
                    print("Bundle ID: ",item2.ID.rjust(20-len("Product ID: ")))
                    print("Name: ",item2.Name.rjust(20-len("Name:2 ")))
                    print("Stock: ",str(item2.Stock).rjust(20-len("Stock: ")))
                    print("-"*20)
                found = True
                data = item2
                indx = w
        return found , data,indx

    def find_order(self,name):
        """This method finds Orders based off inputted ID or name"""
        found1 = self.find_customer(name,'n')
        data = []
        found = False
        if found1[0] == True:
            for item in self.orders:
                
                if name == item.Customer.Name or name == item.Customer.ID:
                    data.append(item)
                    found = True
        return found , data 
# List methods:
    def list_customers(self):
        """This method displays a table of all customers present in the customer attribute"""
        print("-"*70)
        print("Customer list:")
        print("-"*70)
        print("{:<8} {:<15} {:<17} {:<8} {:<8}".format('ID','Name','Discount rate','Value','Threshold limit'))
        print("-"*70)
        for row in self.Customers:
            if isinstance(row,VIPMember):
                print(str(row.ID).ljust(8),str(row.Name).ljust(18),str(row.Discount_rate).ljust(15),str(row.Value).ljust(8),str(row.threshold_lim))
            else:
                print(str(row.ID).ljust(8),str(row.Name).ljust(18),str(row.Discount_rate).ljust(15),str(row.Value).ljust(8),"N/A")
        print("-"*70)
       

    def list_Products(self):
        """This method displays a table of all products present in the customer attribute"""
        print("-"*60)
        print("PRODUCTS".center(60))
        print("-"*60)
        print("{:<8} {:<13} {:>15} {:>10}".format('ID','Name','Price($)','Stock'))
        print("-"*60)
        for row in self.products:
            print(str(row.ID).ljust(8),str(row.Name).ljust(20),str(row.Price).ljust(15),str(row.Stock))
            
            
        print("-"*60)
        print("BUNDLES".center(60))
        print("-"*60)
        print("{:<8} {:<12} {:<20} {:>10}".format('ID','Name','IDs of Comp.','Stock'))
        print("-"*60)
        for row in self.bundles:
            print(str(row.ID).ljust(8),str(row.Name).ljust(12),str(row.Products).ljust(25),str(row.Stock))
            
        print("-"*60)

    def list_orders(self):
        """This method displays a table of all orders present in the customer attribute"""
        print("-"*80)
        print("ORDERS".center(80))
        print("-"*80)
        print("{:<8} {:<8} {:>25} {:>25}".format('Customer','Product/s','Quantitiy/s','Date'))
        print("-"*80)
        for row in self.orders:
            prods = []
            for prod in row.Products:
                prods.append(prod.ID)
            print(str(row.Customer.ID).ljust(6),str(prods).ljust(25),str(row.Quantity).ljust(25),str(row.Date))
            
           
        print("-"*80)

# UPDATE methods
    def add_customer(self,Customer):
        '''add_customer adds customers that are not in the records and updates the value of
            customers that are allready in the records
        '''
        found = self.find_customer(Customer.ID,dis='n')
       
        if found[0] == True:
            self.Customers[found[2]] = Customer
        else: 
            self.Customers.append(Customer)

    def updatestock(self,product_id,quantity):
        '''This method updates the current stock 
            of specifc products bought
        '''
        found = self.find_product(product_id,dis='n')
        
        if found[0] == True:
            if isinstance(found[1],Bundle):
                stock = self.bundles[found[2]].Stock - quantity
                self.bundles[found[2]].set_stock(stock)
            else:
                stock = self.products[found[2]].Stock - quantity
                self.products[found[2]].set_stock(stock)
    def add_order(self,order):
        '''This method adds current order to the records 
        '''
        self.orders.append(order)

     
    def newid(self,mtype):
        '''this method generates a unique id given the membership
            type 
        '''
        ids = []
        for cust in self.Customers:
            ids.append(cust.ID)
        i=0
        num = 1
        while i==0:
            id = mtype + str(num)

            if any(id in subl for subl in ids):
                num += 1
            else:
                i=1
        return id

    # checking files: These methods check to see if the inputted files are in the correct formatt 
    # NOTES : I find these functions to be very messy and unreabable , in any future iterations i would like to 
    # use a much cleaner implementation of these functions 

    def checkcustomerfile(self,file):
        '''This method checks to see if all the
        rows in the customer.txt file is in the 
        correct format
        '''
        with open(file,"r") as txtfile:
            saveid=[]
            check=None
            for line in txtfile:
                currentline = line.split(",")
                strip_line = [item.strip() for item in currentline]
                # check id is unique: 
                saveid.append(strip_line[0])
                if (len(set(saveid)) == len(saveid)):
                    unique = True
                else:
                    unique = False
                # 2. check format:
                if len(strip_line) != 4:
                    valid = False
                else:
                    valid = True
                    # 3. check datatypes 
                    IDbool = type(strip_line[0]) is str
                    namebool = type(strip_line[1]) is str
                    ID1bool = strip_line[0][0] in ["C","V","M"]
                    try:
                        a=float(strip_line[2])
                        b=float(strip_line[3])
                        c=int(strip_line[0][1])   
                    except ValueError:
                        valid = False
                        a , b,c =-1,-1,-1
                    if a or b or c >= 0:
                        positive = True
                    else:
                        
                        positive = False
                if valid== False  or IDbool== False  or namebool == False or ID1bool== False  or unique == False or positive == False:
                    
                    check = False
                    break
                else:
                    check = True
            txtfile.close()
            return check

    def checkproductfile(self,file):
        check = None
        with open(file,"r") as txtfile:
            saveid=[]
            for line in txtfile:
                
                
                currentline = line.split(",")
                strip_line = [item.strip() for item in currentline]
                # check id is unique: 
                saveid=[]
                saveid.append(strip_line[0])
                
                if (len(set(saveid)) == len(saveid)):
                    unique = True
                else:
                    unique = False
                # checking bundle format : 
                if strip_line[0][0] == "B":
                    
                    namebool = type(strip_line[1]) is str
                    try: 
                        d= float(strip_line[-1])
                    except ValueError:
                        valid = False
                        d = -1
                    pos = d > 0 
                    if valid == False or pos == False:
                        check == False
                        break
                    else: 
                        check == True
                else:
                # 2. check product formateformat:
                    if len(strip_line) != 4:
                        valid = False
                    else:
                        valid = True
                        # 3. check datatypes 
                        IDbool = type(strip_line[0]) is str
                        namebool = type(strip_line[1]) is str
                        ID1bool = strip_line[0][0] == "P"
                        try:
                            b=int(strip_line[3])
                            c=int(strip_line[0][1])
                        except ValueError:
                            valid = False
                            b,c =-1,-1
                        if b or c >=0:
                            positive = True
                        else:
                            positive = False
                    if valid== False or IDbool== False or namebool == False or ID1bool == False or unique == False:
                        
                        check = False
                        break
                    else:
                        check = True
        txtfile.close()
        return check
    def checkordersfile(self,file):

        """ This method is used to check if the orders.txt file has 
        the correct file formatting 
        """
        with open(file,"r") as txtfile:
            saveid=[]
            saveprodids = []
            saveprods = []
            for line in txtfile:
                currentline = line.split(",")
                strip_line = [item.strip() for item in currentline]
                
                saveid.append(strip_line[0])
                for i,object in enumerate(strip_line[1:-1]):
                    if (i % 2) ==0:
                        saveprodids.append(object)
                    else:
                        saveprods.append(object)

                
                # Check datatypes 
                IDbools = type(strip_line[0]) is str and type(strip_line[1]) is str
                try:
                    datetime.strptime(strip_line[-1], '%d/%m/%Y %H:%M:%S')
                    valid = True
                except ValueError:
                    valid = False
                if valid== False or IDbools== False:
                    check = False
                    break
                else:
                    check = True
                
        # check is customer and products exists
        for item in saveid:
            custids = self.find_customer(item,dis='n')
            if custids[0] == False:
                check = False
        for i,item in enumerate(saveprodids):
            try:
                prodids = self.find_product(item,dis='n')
                int(saveprods[i])
                if prodids[0] == False:
                    check = False
            except exception:
                check = False

            txtfile.close()
            
            return check
    def updatefiles(self,file1,file2,file3):
        # update customers:
        with open(file1,"w") as txtfile:
            for cust in self.Customers:
                txtfile.write(str(cust.ID))
                txtfile.write(', ')
                txtfile.write(str(cust.Name))
                txtfile.write(', ')
                txtfile.write(str(cust.Discount_rate))
                txtfile.write(', ')
                txtfile.write(str(cust.Value))
                txtfile.write('\n') 
        txtfile.close()
        # update products:
        with open(file2,"w") as txtfile:
            for prod in self.products:
                    txtfile.write(str(prod.ID))
                    txtfile.write(', ')
                    txtfile.write(str(prod.Name))
                    txtfile.write(', ')
                    txtfile.write(str(prod.Price))
                    txtfile.write(', ')
                    txtfile.write(str(prod.Stock))
                    txtfile.write('\n')
            for prod in self.bundles:
                    txtfile.write(str(prod.ID))
                    txtfile.write(', ')
                    txtfile.write(str(prod.Name))
                    txtfile.write(', ')
                    for prods in prod.Products:
                        txtfile.write(str(prods))
                        txtfile.write(', ')
                    txtfile.write(str(prod.Stock))
                    txtfile.write('\n')
        txtfile.close()
        #update orders: 
        with open('orders.txt',"w+") as txtfile:
                for order in self.orders:
                    txtfile.write(str(order.Customer.ID))
                    txtfile.write(', ')
                    for i,prods in enumerate(order.Products):
                        txtfile.write(str(prods.ID))
                        txtfile.write(', ')
                        txtfile.write(str(order.Quantity[i]))
                        txtfile.write(', ')
                    txtfile.write(str(order.Date))
                    txtfile.write('\n')
                txtfile.close()
        

        
                        


# MAIN CLASS----------------------
# to increase readability i have seperated all the functionailities of the operations class
# into individual methods as described below

# In order to run the overall program the user needs to call the method Operations.run(customerfile,productfile,orderfile)
#  with the respective inputted files being the command line arguments 

class Operations():
    # Find customer.txt and products.txt
    file_1 ="customers.txt"
    file_2 = "products.txt"
    file_3 ="orders.txt"
    # I used attributes current_cust , curren_order and current_product to save the the information on the customer , order and product 
    # for the current interation of an order , so that information regarding these varibles could easily be referenced when printing the file 
    # order 

    # NOTES: in cases where mulitple products are being bought the current product only refers to the last product being bought , 
    # whilst the order object saves the list of all the products in the current order 
    current_cust = None
    current_order = None 
    current_product = None 

    # Member_type is just used to determie if someone has bought a VIP membership in the current order
    member_typ = None
    rec = Records()
    
    def set_files(self,customer_file,product_file,order_file):
        """This method checks to see if the user inputted the required files as command line arguments and sets the values 
        of the file attributes using these inputs 
        """
        cust_bool = customer_file == None
        prod_bool = product_file== None
        order_bool = order_file == None
        # I used IF statements with the bool statements above to determine what files the user has entered and 
        # react accorindingly  ---> i found this to be the simplest way to implement 

        if (cust_bool == True and prod_bool == False) or (cust_bool == False and prod_bool == True):
            print("-"*60)
            print("//ERROR: wrong number of arguments used//")
            print("-"*60)
            print("->  (customer file , product file) are both mandatory arguments")
            print("-"*60)
            exit()
        if cust_bool & prod_bool & order_bool:
    
            pass
        else:
         
           self.file_1 = customer_file
           self.file_2 = product_file
           self.file_3 = order_file 

    def check_files(self):
        """This method checks to see if the required files are present in the 
        current working directory
        """

        # I used try and except clauses for reading files as i found it to be the easiest way to test for filenot found errors 
        try:
                
            self.rec.read_customers(self.file_1)
            self.rec.read_products(self.file_2)
        

        except FileNotFoundError:
            print("-"*60)
            print("//ERROR: Missing correct files for system to run//")
            print("-"*60)
            print("->  Please make sure correct files are in local working \ndirectory and try again")
            print("-"*60)
            exit()
        try:
            self.rec.read_orders(self.file_3)
            check3 = self.rec.checkordersfile(self.file_3)
        except Exception:
          print("-"*60)
          print("//ERROR: Cannot load the order file//")
          print("-"*60)
          print("->Program will run assuming no orders have been placed")
          print("-"*60)
          check3 = True
        
        # check format of files: 
        check = self.rec.checkcustomerfile(self.file_1)
        check2 = self.rec.checkproductfile(self.file_2)
        if check== False or check2 == False or check3 == False:
            print("-"*63)
            print("//ERROR: One or more of the input files has incorrect format//")
            print("-"*60)
            print("Please make sure: ")
            print("-> Each line is formated correctly\n-> Each ID value is unique\n-> Correct datatypes are used")
            print("-"*63)
            exit()
    
    def menu(self):
        """Operates the menu displayed to user and returns user inputted 
        menu option"""
        print("="*50)
        print("Welcome to Matthew's retail management system! \n")
        print("="*50)
        print("you can choose from the followin options:")
        print("1: Place an order")
        print("2: Display existing customers")
        print("3: Display existing products")
        print("4: Adjust the discount rates of a VIP member")
        print("5: Adjust the threshold limit of all VIP members")
        print("6: Display all orders")
        print("7: Display all orders of a customer")
        print("8: Summarize all orders")
        print("9: Reveal the most valuable customer")
        print("10: Reveal the most popular product")
        print("0: Exit the program")
        print("="*50)
        opt = input("Choose One option: ").strip()
        return opt
    
    # PLACE ORDER OPTION:
    def placeorder(self):
        """Records all required customer attributes needed for an order to be placed""" 
        Name = input("Enter the name or ID of the customer [e.g. James]:")
        found = self.rec.find_customer(Name)
        if found[0] == False:
            print("Customer not found in records please enter following information.\n")
            # I used nested while loops with if statements to handle errors contained in the user inputted values 
            i=0
            while i ==0:
                member = input("Does the customer want to have a membership [enter y or n]:")
                if member == 'y':
                    w=0
                    while w==0:
                        self.member_typ = input("What type of membership does the customer want [ e.g. M (member) or V (VIP member)]")
                        id = self.rec.newid(self.member_typ)
                        if self.member_typ == 'M':
                                self.current_cust = Member(id,Name,0)
                                w=1
                                continue
                        if self.member_typ == 'V':
                                self.current_cust = VIPMember(id,Name,0)
                                w=1
                                continue
                        else:
                            print("-"*60)
                            print("//ERROR: Invalid response//")
                            print("-"*60)
                            print("->  Please make sure response is either 'M' or 'V'\nsystem IS case sensitive")
                            print("-"*60)
                    i=1 
                    continue
                if member == 'n':
                    self.member_typ = 'C'
                    id = self.rec.newid(self.member_typ)
                    self.current_cust = Customer(id,Name,0,0)
                    i=1 
                    continue
                else:
                    print("-"*60)
                    print("//ERROR: Invalid response//")
                    print("-"*60)
                    print("->  Please make sure response is either 'y' or 'n'\nsystem IS case sensitive")
                    print("-"*60)

                
            
        else: 
            self.current_cust = found[1]
    
    def purchase_products(self):
        """Records all required product attributes needed for an order to be placed""" 
        w = 0
        order_prods = []
        order_quants = []

        while w == 0 :
            i=0
            while i ==0:
                Product = input("Enter the product name or ID[valid products only, e.g. shirt, towel, oven]:")
                found = self.rec.find_product(Product)
                
                if found[0] == False:
                    print("-"*60)
                    print("//ERROR: Product does not exist in product list//")
                    print("-"*60)
                    print("->  Please make sure product is entered correctly \nand try again")
                    print("-"*60)
                else:
                    self.current_prod = found[1]
                    i=1
            valid = Products.checkprice(self.current_prod.Price)
            if valid == True:
                i=0 
                while i ==0:
                    
                    Quantity = input("Enter the product quantity [enter a positive integer only, e.g. 1,2,3]:")
                    if self.current_prod.Stock == 0:
                        print("-"*60)
                        print("//ERROR: Product NOT in stock//")
                        print("-"*60)
                        valid =False
                        i=1
                    else:
                        # Throughout my code i used TRY and EXCEPT clauses whenever the datatype of a user 
                        # input needs to be checked --> i this case i used it to check if the user had entered a valid 
                        # quantity (in stock , interger and above zero)
                        try: 
                            Q= int(Quantity)
                            isint = True
                            ispos = Q > 0
                            instock = Q <= self.current_prod.Stock
                            date = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
                            
                            order_prods.append(self.current_prod)
                            order_quants.append(Q)
                            self.current_order = Orders(order_quants,self.current_cust,order_prods,date,0)
                            if self.member_typ == "V":
                                self.current_order = Orders(order_quants,self.current_cust,order_prods,date,200)
                                 
                        except Exception:
                            isint = False
                            ispos = False
                            instock = False

                        if isint == False or ispos ==False or instock==False:

                            print("-"*60)
                            print("//ERROR: Invalid product quantity entered//")
                            print("-"*60)
                            print("->  The quantity entered is either not a positive integer or\nnot enough product is in stock currently.\n-> please enter valid stock quantity")
                            print("-"*60)
                        else:
                            i=1
            
                
                i = 0 
            while i ==0:
                Another_product = input("Is another item being purchased [y/n]: ")
                if Another_product == 'y':
                    i = 1
                    valid =False
                    continue
                if Another_product == 'n':
                    i =1 
                    w = 1
                    continue
                else:
                    print("-"*60)
                    print("//ERROR: Invalid response//")
                    print("-"*60)
                    print("->  Please make sure response is either 'y' or 'n'\nsystem IS case sensitive")
                    print("-"*60)
        # I used the valid variable to deal with errors that require the user to be directed back to the main menu 
        return valid


        
            
    def Printorder(self):
        """Prints the final order screen to users"""

            # ORDER COST:
        print('='*50)
        for i in range(len(self.current_order.Products)):
            print(self.current_cust.Name , " purchases",self.current_order.Quantity[i],' x ',self.current_order.Products[i].Name)
            print('Unit price:','$'.rjust(10),self.current_order.Products[i].Price,' (AUD)')
        if self.current_order.Membership >0:
            print('Membership price:','$ 200 (AUD)'.rjust(14))

        
        price_before_dis = (self.current_order.Totalprice())[1]
        total_price = (self.current_order.Totalprice())[0]
            
        print(self.current_cust.Name,"gets a discount of",str(self.current_cust.get_discount(price_before_dis)[0]*100).rjust(7-len(self.current_cust.Name)),"%")
        print('Total price:','$'.rjust(9),total_price,'(AUD)')
        self.current_cust.Value = round(self.current_cust.Value+total_price,4)
        print('='*50)

    def updaterecords(self):
        #Add customer to records / update customer records 
        if self.current_cust.ID[0] =="V":
            self.rec.add_customer(self.current_cust)
        else:
           self.rec.add_customer(self.current_cust)
        
        #UPDATE PRODUCT STOCK:
        for i in range(len(self.current_order.Products)):
            self.rec.updatestock(self.current_order.Products[i].ID,self.current_order.Quantity[i])

        # Add order to records 
        self.rec.add_order(self.current_order)


        input("\nPress ENTER to continue")
    
    def Display_customers(self):
        """displays list of all customers"""
        self.rec.list_customers()
        input("\nPress ENTER to continue")
    def Display_products(self):
        """displays list of all products"""
        self.rec.list_Products()
        input("\nPress ENTER to continue")
    def UpdateVIPdis(self):
        """Updates discount rate for a specific VIP member"""
        vip = input("Enter name or ID of VIP member: ")
        found = self.rec.find_customer(vip,'n')
        v = isinstance(found[1],VIPMember)
        if found[0] == True and v == True:
            i=0
            while i==0:
                discount_r1 = input("Enter 1st discount rate (%):")
                try:
                    discount_r1 = float(discount_r1)/100
                    valid = (discount_r1 >=0)
                except Exception:
                    valid = False
                    pass
                if valid == False:
                    print("-"*60)
                    print("//ERROR: Invalid Input//")
                    print("-"*60)
                else:
                    i=1
            cust = found[1]
            print(discount_r1)
        
            VIPMember.set_rate(cust,discount_r1)
            self.rec.add_customer(cust)
        else:
            print("-"*60)
            print("//ERROR: Invalid customer!//")
            print("-"*60)
           

    def UpdateVIPthres(self):
        """Updates the VIP threshold for ALL VIP members """
        i=0
        while i==0:
                threshold = input("Enter new VIP threshold: ")
                try:
                    threshold = float(threshold)
                    valid = (threshold >0)

                except Exception:
                    valid = False
                    pass
                if valid == False:
                    print("-"*60)
                    print("//ERROR: Invalid Input//")
                    print("-"*60)
                else:
                    i=1
        # set threshold for future customers 
        VIPMember.set_threshold(threshold)
        self.rec.Customers = []
        self.rec.read_customers(self.file_1)
        # reintialise records
    def Display_orders(self):
        """Displays a list of all orders"""
        self.rec.list_orders()
        input("\nPress ENTER to continue")
    def Display_an_order(self):
        """Displays all orders from a customer"""
        Customer = input("Enter name or ID of customer: ")
        found  = self.rec.find_order(Customer)
        
        if found[0] == True:
            print("-"*60)
            print(Customer,"'s ","ORDERS")
            print("-"*60)
            print("{:<8} {:<10} {:>15} {:>10}".format('Customer','Product','Quantitiy','Date'))
            print("-"*60)
            prodid = []
            for row in found[1]:
                for prod in row.Products:
                    prodid.append(prod.ID)
                print(str(row.Customer.ID).ljust(7),str(prodid).ljust(20),str(row.Quantity).ljust(12),str(row.Date))
  
            print("-"*60)
        else:
            print("-"*60)
            print("//ERROR: Invalid Customer//")
            print("-"*60)
        input("\nPress ENTER to continue")

    def Summarise_orders(self):
        """Summarises all orders and displays the the number of orders made for each product
        and the quanity of products bought for each product to date"""
        orders = self.rec.orders
        Products = self.rec.products
        bundles = self.rec.bundles
        Ids = []
        sum_data = []
        print("-"*60)
        print('ORDER SUMMARIES'.center(60))
        print("-"*60)
        # I used for loops to 
        for product in Products:
            Ids.append(product.ID)
        for bundles in bundles:
            Ids.append(bundles.ID)
        print(''.ljust(10),'    '.join(str(x) for x in Ids))
        for order in orders:
            order_quants = [0]*len(Ids)
            for i,product in enumerate(order.Products):
                id = product.ID
                indx = Ids.index(id)
                order_quants[indx] =order.Quantity[i]
            sum_data.append(order_quants)
            print(str(order.Customer.Name).ljust(10),'     '.join(str(x) for x in order_quants))
        print("-"*60)
        num = [0]*len(Ids)
        qty = [0]*len(Ids)
        for order in sum_data:
            for i,val in enumerate(order):
                num[i] += int(val)
                if int(val) > 0:
                    qty[i] =qty[i]+ 1
        print('OrderNum'.ljust(10),'     '.join(str(x) for x in qty))
        print('OrderQty'.ljust(10),'     '.join(str(x) for x in num))
        input("\nPress ENTER to continue")

    def Valuablecustomer(self):
        """Prints out the list of the most valuable customers"""
        Customers = self.rec.Customers
        val_list = []
        MVC = []
        for customer in Customers:
            val_list.append(customer.Value)
        for customer in Customers:
            if customer.Value == max(val_list):
                cus = [customer.ID,customer.Name,customer.Value]
                MVC.append(cus)
        print("-"*60)
        print('MOST VALUABLE CUSTOMER/S'.center(60))
        print("-"*60)
        print("{:<8} {:<8} {:>10}".format('ID','Name','Money spent ($)'))
        print("-"*60)

        for customer in MVC:
            print('        '.join(str(x) for x in customer))
        print("-"*60)

        input("\nPress ENTER to continue")

    def Popularproduct(self):
        """Displays the most popular product"""
        orders = self.rec.orders
        Products = self.rec.products
        bundles = self.rec.bundles
        Ids = []
        sum_data = []
        
        for product in Products:
            Ids.append(product.ID)
        for bundles in bundles:
            Ids.append(bundles.ID)
        bought = [0]*len(Ids)
        for order in orders:
            
            for i,product in enumerate(order.Products):
                id = product.ID
                indx = Ids.index(id)
                bought[indx] += 1
            sum_data.append(bought)
        m = max(bought)
      
            
        popitemindx = [i for i,j in enumerate(bought) if j == m]
        popitems = []
        for indx in popitemindx:
            popitemid = Ids[indx]
            item = self.rec.find_product(popitemid,dis='n')
            popitems.append(item[1])
        print("-"*60)
        print('MOST POPULAR PRODUCT/s'.center(60))
        print("-"*60)
     
        for product in popitems:
            print('ID: ',product.ID,' '*4,'Name: ',product.Name)
        print("-"*60)
        print('No. of orders: ',m)
        print("-"*60)
        
        input("\nPress ENTER to continue")
    def Updatefiles(self):
        """Updates the inputted product , customer and order files"""
        #if no order is inputted at the begining the updatefiles function will write all 
        #orders onto the new file called Orders.txt
        if self.file_3 == None:
            self.file_3='Orders.txt'
        self.rec.updatefiles(self.file_1,self.file_2,self.file_3)

    def run(self,arguments):
        """This method runs the UI/functionality of the operations class and all its methods """
        customer_file = arguments[0]
        product_file = arguments[1]
        order_file = arguments[2]
        self.set_files(customer_file,product_file,order_file)
        self.check_files()
        i=0
        while i == 0:
            option = self.menu()

            if option == '1':
                self.placeorder()
                valid = self.purchase_products()
                if valid == True:
                    self.Printorder()
                    self.updaterecords()
            if option == "2":
                self.Display_customers()
            if option == "3":
                self.Display_products()
            if option =='4':
                self.UpdateVIPdis()
            if option =='5':
                self.UpdateVIPthres()
            if option =='6':
                self.Display_orders()
            if option =='7':
                self.Display_an_order()
            if option =='8':
                self.Summarise_orders()
            if option =='9':
                self.Valuablecustomer()
            if option =='10':
                self.Popularproduct()
            if option =='0':
                i=1
            self.Updatefiles()

    
# RUN COMMANDS 
op = Operations()
op.run(files)




       

        



  




        







   
