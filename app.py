import tkinter as tk
import ttkbootstrap as ttk
from CTkMessagebox import CTkMessagebox
from ttkbootstrap.constants import *
from ttkbootstrap import  Menu
import re

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("..:: Food App ::..")
        self.spiceLevel= ttk.IntVar()
        self.foodSize = ttk.IntVar()
        self.peymentMethod = ttk.IntVar()
        self.cityVariable = ttk.StringVar()        
        self.foodVariable = ttk.StringVar()        
        self.resizable(False,False)
        self.geometry('950x900')
        ttk.Style("superhero")
        self.cities = ["Tehran", "Alborze", "Azarbaijan Shargh", "Khorasan Razavi" , 'Fars']
        self.foodNames = [
            "Peperoni" , "GoshtOGharch" , "SirOStaik" , "Sabzijat" , "RostBif" , "Baiken","Margarita" , "ChikenPesto" , "Makhlot" , "Makhsos",
            "HaberGer" , "CheesBerger" ,"MashromBerger" , "SojokBerger" , "BeikenBerger"
        ]
        self.deliveryItems = [
            "Now" , "Soon" ,"Check Me"
        ]
        self.priceFood = {
            "Peperoni" :[4300000,5300000,5300000],
            "GoshtOGharch" :[4800000,5800000,6800000],
            "SirOStaik" :[5200000,6200000,7200000],
            "Sabzijat" :[4000000,5000000,6000000],
            "RostBif" :[3500000,4500000,5500000],
            "Baiken":[4800000,5800000,6800000],
            "Margarita" :[3000000,4000000,5000000],
            "ChikenPesto" :[4500000,5500000,6500000],
            "Makhlot" :[4800000,5800000,6800000], 
            "Makhsos":[4300000,5300000,6300000],
            "HaberGer" :[3900000,4900000,5900000],
            "CheesBerger" :[3200000,4200000,5200000],
            "MashromBerger" :[3500000,4500000,5500000],
            "SojokBerger" :[3900000,4900000,5900000],
            "BeikenBerger":[3400000,4400000,5400000]
        }
        self.inputnames = [
            "firstName_input", "lastName_input","phoneNumber_input","fixedNumber_input",           
            "address_input","HNumber_input" ,"unitNumber_input" ,"specialIns_input",
            "floor_input" ,"foodNumber_input" ,"discountCode_input"
        ]
        self.radionameVar = [
            'soda', 'water', 'maltbeverage', 'dough', 'icetae',
            'fernchFrise', 'garlicBread', 'salad',
            'cheesCake', 'tiramisu', 'vanilIceCream',          
            'cheese', 'mushroom', 'pepper','olive', 'onion'
        ]

        self.countTopping = 0
        self.toppingName = []

        # self.countDrink = 0
        # self.drinkName = []

        self.sLevelSelect = 0
        self.sLevelName = False

        self.countOptionalItem = 0
        self.OptionalName = []
        self.widgets()
        self.location()
        self.runApp()

    def selectPaymentMetyhod(self):
        print(self.peymentMethod.get())
    

    def selectOptionalItem(self, optional_name , variable):
        if variable.get() :            
            self.countOptionalItem +=1
            self.OptionalName.append(optional_name)
        else : 
            variable.set(False) 
            self.OptionalName.remove(optional_name)
            self.countOptionalItem -=1
        
        print(self.countOptionalItem ,  self.OptionalName)

    def selectSlevel(self):
        match(self.spiceLevel.get()):
            case 1 :
                self.sLevelSelect = 1
                self.sLevelName = "Normal"
                
            case 2 :
                self.sLevelSelect = 2
                self.sLevelName = "Medium"
                
            case 3 :
                self.sLevelSelect = 3
                self.sLevelName = "Hot"
        print(self.sLevelName , self.sLevelSelect)

        

    # def selectDrink(self , drink_name , variable):
    #     if variable.get() :            
    #         self.countDrink +=1
    #         self.drinkName.append(drink_name)
    #     else : 
    #         variable.set(False) 
    #         self.drinkName.remove(drink_name)
    #         self.countDrink -=1
        
    #     print(self.countDrink ,  self.drinkName)




    def selectTopping(self , topping_name , variable):
        if(self.countTopping == 3 and variable.get()):
            variable.set(False)
            self.errorHandler("limitSelectd")
            return
        
        if variable.get() :
            if(self.countTopping < 3 ):
                self.countTopping +=1
                self.toppingName.append(topping_name)
            else:
                variable.set(False)                
                return
        else : 
            self.toppingName.remove(topping_name)
            self.countTopping -=1
        
        print(self.countTopping , self.toppingName)


    def changeStat(self , situation) :
        
        for name in self.inputnames :
            prop = self.getProp(name)
            prop.configure(state = situation)


    def calculation(self):
        self.order_btn.configure(state="normal")
        self.edit_btn.configure(state="normal")
        self.Calculate_btn.configure(state="disable")
        for name in self.inputnames :
            prop = self.getProp(name)
            prop.configure(state="readonly")
            
    def edit(self):
        self.order_btn.configure(state="disable")
        self.edit_btn.configure(state="disable")
        self.Calculate_btn.configure(state="normal")
        for name in self.inputnames :
            prop = self.getProp(name)
            prop.configure(state="normal")
    def cleanData(self):        
        for name in self.inputnames :
            prop = self.getProp(name)
            prop.configure(state="normal")
            prop.delete(0,tk.END)
            
        for radio in self.radionameVar:
            prop = self.getProp(radio+"_var")
            prop.set(False)
        
        self.countTopping = 0
        self.toppingName = []
        self.sLevelSelect = 0
        self.sLevelName = False
        self.countOptionalItem = 0
        self.OptionalName = []
        
        self.update()
        self.firstName_input.focus_set()
        


    #message 
    def errorHandler(self ,erorr_key , name = False) :
        errors = {
            'strError' : f"somting wrong : please using string input for this input [ {name} ] ! ",
            'phoneError' : f"somting wrong : your information for [ {name} ] not correct   !" , 
            'emptyError' : f"somting wrong :  [ {name} ] is Empty !",
            'numberError' : f"somting wrong :  Please using Number for [ {name} ] fild !",
            'FNameError' : f"somting wrong :  Please Select a FOOD !",
            'limitSelectd' : f"somting wrong :  You can select 3 items !",
        }
        CTkMessagebox(title="Warning Message!", message=errors[erorr_key],
                  icon="warning", option_1="Ok",width=600 , justify='cenert' , font=("Arial" , 16 , 'bold') , text_color="#FF0000" , title_color="#ffe600" , corner_radius=0 , sound=True)
        
    def wSpace(self ,frame):
        space = ttk.Label(frame, text=" " , padding=(10,10))
        return space
    #Widgets Configs :
    #validatopn :
    def getProp(self,name):
        return getattr(self, name  , NONE)
    
    def checkString(self , input, name) :
        prop_name = getattr(self, name  , NONE)
        
        if(prop_name.get() == ""):
          prop_name.configure(bootstyle="danger")
          return False  
        
        if(input.isalpha()):            
            prop_name.configure(bootstyle="defualt")
            return True
        prop_name.configure(bootstyle="danger")
        return False
    
    def checkPhone(self , input , name):
        prop_name = self.getProp(name)
        pattern = r'^0\d{10}$' #serach in stackOverFlow and Use it
        if(re.match(pattern, input)):
            prop_name.configure(bootstyle="defualt")
            return True
        prop_name.configure(bootstyle="danger")
        return False
    def checkEmpty(self , input , name):
        prop_name = self.getProp(name)
        if(input == ""):
            prop_name.configure(bootstyle="danger")
            return False
        return True
    
    def checkNumber(self , input , name):
        prop_name = self.getProp(name)
        pattern = r'^\d+' #serach in stackOverFlow and Use it
        if(re.match(pattern, input)):
            prop_name.configure(bootstyle="defualt")
            return True
        prop_name.configure(bootstyle="danger")
        return False
    
    def validation_input(self , input , name , slug = False):
        
        # if(not self.checkEmpty(input , name)):
        #      self.errorHandler('emptyError' , name)
        #      return False
              
        if(not self.checkString(input , name) and slug == 'str') :
            if(not self.checkEmpty(input , name)):
             self.errorHandler('emptyError' , name)
             return False
            self.errorHandler('strError' , name)
            
        if(not self.checkPhone(input , name)  and slug == 'phone'):
            if(not self.checkEmpty(input , name)):
             self.errorHandler('emptyError' , name)
             return False
            self.errorHandler('phoneError' , name)
            
        if(not self.checkEmpty(input , name) and slug == "empty"):
            self.errorHandler('emptyError' , name)
             
        if(not self.checkNumber(input , name ) and slug == "number"):
            self.errorHandler('numberError' , name)
            
   
    def getCounty(self , event):
        county = {
            'Tehran' : ["Tehran", "Shemiranat", "Ray", "Varamin" , "Eslam Abad" , "Shahriar"],
            'Alborze' : ["Karaj", "Fardis", "Talaghan", "Eshtehard" , "Nazar Abad"],
            'Azarbaijan Shargh' : ["Tabriz", "Maraghe", "Maran", "Mianeh" , "Jolfa" ],
            'Khorasan Razavi' : ["Mashhad", "Neyshabor", "Sabzevar", "Torghabeh" , "Gonabad"],
            'Fars' : ["Shiraz", "Jahrom", "Darab", "Pasarghad"],
        }
        countyKey =self.cityVariable.get()
        self.county_comboBox.configure(values=county[countyKey])
        

    def getFoodSize(self):
        if(self.foodVariable.get() == "") :
            self.foodType_comboBox.configure(bootstyle="danger")
            self.errorHandler("FNameError")
            return False
        self.foodType_comboBox.configure(bootstyle="defualt")
        price = self.priceFood[self.foodVariable.get()]
        print(price[self.foodSize.get() - 1])




    def widgets(self):        
        #user Info Frame
        self.userInfoFrame = ttk.LabelFrame(self,bootstyle="info", text="User Information", padding=(10,10,10,20))
        self.lable_firstName = ttk.Label(self.userInfoFrame,text="FirstName :"  , padding=(3,3))
        self.firstName_input = ttk.Entry(self.userInfoFrame, width=30)
        self.firstName_input.bind('<FocusOut>', lambda input : self.validation_input(self.firstName_input.get() , "firstName_input",'str'))
        
        self.lable_lastName = ttk.Label(self.userInfoFrame,text="Last Name :"  , padding=(3,3))
        self.lastName_input = ttk.Entry(self.userInfoFrame, width=30)
        self.lastName_input.bind('<FocusOut>', lambda input : self.validation_input(self.lastName_input.get() , "lastName_input",'str'))
        
        self.lable_phoneNumber = ttk.Label(self.userInfoFrame,text="Phone Number :"  , padding=(3,3))
        self.phoneNumber_input = ttk.Entry(self.userInfoFrame, width=30)
        self.phoneNumber_input.bind('<FocusOut>', lambda input : self.validation_input(self.phoneNumber_input.get() , "phoneNumber_input" , 'phone'))
         
        self.lable_fixedNumber = ttk.Label(self.userInfoFrame,text="Fixed :"  , padding=(3,3) )
        self.fixedNumber_input = ttk.Entry(self.userInfoFrame, width=30)
        self.fixedNumber_input.bind('<FocusOut>', lambda input : self.validation_input(self.fixedNumber_input.get() , "fixedNumber_input" , 'phone'))
        
        self.lable_city = ttk.Label(self.userInfoFrame,text="City :"  , padding=(3,3) )
        self.city_comboBox = ttk.Combobox(self.userInfoFrame, width=28 ,textvariable=self.cityVariable
                                          , values=self.cities  , state='readonly')
        self.city_comboBox.bind('<<ComboboxSelected>>', self.getCounty)
        
        self.lable_county = ttk.Label(self.userInfoFrame,text="County :"  , padding=(3,3) )
        self.county_comboBox = ttk.Combobox(self.userInfoFrame, width=28 
                                          , values=[], state="readonly" )
        #---------------------------------
        self.lable_address = ttk.Label(self.userInfoFrame,text="Address :"  , padding=(3,3) )
        self.address_input = ttk.Entry(self.userInfoFrame)
        self.address_input.bind('<FocusOut>', lambda input : self.validation_input(self.address_input.get() , "address_input",'empty'))
        
        self.lable_HNumber = ttk.Label(self.userInfoFrame,text="House Number :"  , padding=(3,3) )
        self.HNumber_input = ttk.Entry(self.userInfoFrame , width=30)
        self.HNumber_input.bind('<FocusOut>', lambda input : self.validation_input(self.HNumber_input.get() , "HNumber_input",'number'))
        
        self.lable_unitNumber = ttk.Label(self.userInfoFrame,text="Unit Number :"  , padding=(3,3) )
        self.unitNumber_input = ttk.Entry(self.userInfoFrame , width=30)
        self.unitNumber_input.bind('<FocusOut>', lambda input : self.validation_input(self.unitNumber_input.get() , "unitNumber_input",'number'))
        
        self.lable_floor = ttk.Label(self.userInfoFrame,text="Floor :"  , padding=(3,3) )
        self.floor_input = ttk.Entry(self.userInfoFrame , width=30)
        self.floor_input.bind('<FocusOut>', lambda input : self.validation_input(self.floor_input.get() , "floor_input",'str'))
        
      
      
      
      
      
        #food Info Frame
        self.foodFrame = ttk.LabelFrame(self,bootstyle="danger", text="Food Information", padding=(10,10,10,20))
        
        self.lable_foodType = ttk.Label(self.foodFrame,text="Food Type :"  , padding=(3,3) )
        self.foodType_comboBox = ttk.Combobox(self.foodFrame, width=28 
                                          , values=self.foodNames, textvariable=self.foodVariable , state="readonly")
        
        
        self.lable_foodSize = ttk.Label(self.foodFrame,text="Food Size :"  , padding=(3,3) )
        self.small_radio = ttk.Radiobutton(self.foodFrame, text="Small", value=1 ,bootstyle="primary-outline-toolbutton" , variable=self.foodSize ,
                                           command= lambda  : self.getFoodSize())
        self.medium_radio = ttk.Radiobutton(self.foodFrame, text="Medium", value=2 ,bootstyle="primary-outline-toolbutton" , variable=self.foodSize ,
                                             command= lambda  : self.getFoodSize())
        self.large_radio = ttk.Radiobutton(self.foodFrame, text="Large", value=3 ,bootstyle="primary-outline-toolbutton" , variable=self.foodSize ,
                                            command= lambda  : self.getFoodSize())
        
        self.foodNumber = ttk.Label(self.foodFrame, text="Food Number :", padding=(3,3))
        self.foodNumber_input = ttk.Spinbox(self.foodFrame,from_=1, to=5, width=5, increment=1)
        #'cheese', 'mushroom', 'pepper','olive', 'onion'
        #extra information Frame
        self.extraInformation = ttk.Labelframe(self,bootstyle="warning", text="Extra Information", padding=(10,10,10,20))
        
        self.lable_extraToppings = ttk.Label(self.extraInformation, text="Extra Toppings :" , padding=(3,3))
        
        self.cheese_var = tk.BooleanVar()

        
        self.cheeseTopping_input = ttk.Checkbutton(self.extraInformation,variable=self.cheese_var,
                                                    command= lambda : self.selectTopping("Cheese" , self.cheese_var),
                                                    text="Cheese" ,bootstyle="success-outline-toolbutton", padding=(3,3))
        self.mushroom_var = tk.BooleanVar()
        self.mushroomTopping_input = ttk.Checkbutton(self.extraInformation,variable=self.mushroom_var,
                                                    command= lambda : self.selectTopping("Mushroom" , self.mushroom_var), text="Mushroom" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
       
        self.pepper_var = tk.BooleanVar()
        self.pepperTopping_input = ttk.Checkbutton(self.extraInformation,variable=self.pepper_var,
                                                    command= lambda : self.selectTopping("Pepper" , self.pepper_var), text="Pepper" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        
        self.olive_var = tk.BooleanVar()
        self.oliveTopping_input = ttk.Checkbutton(self.extraInformation,variable=self.olive_var,
                                                    command= lambda : self.selectTopping("Olive" , self.olive_var), text="Olive" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        
        self.onion_var = tk.BooleanVar()
        self.onionTopping_input = ttk.Checkbutton(self.extraInformation,variable=self.onion_var,
                                                    command= lambda : self.selectTopping("Onion" , self.onion_var), text="Onion",bootstyle="success-outline-toolbutton", padding=(3,3)) 
        

        self.soda_var = ttk.BooleanVar()
        self.water_var = ttk.BooleanVar()
        self.maltbeverage_var = ttk.BooleanVar()
        self.dough_var = ttk.BooleanVar()
        self.icetae_var = ttk.BooleanVar()
        self.lable_drink = ttk.Label(self.extraInformation, text="Drink :" , padding=(3,3))
        

        self.soda_input = ttk.Checkbutton(self.extraInformation,
                                          variable=self.soda_var , command=lambda:self.selectOptionalItem("soda" , self.soda_var),
                                           text="Soda" ,bootstyle="success-outline-toolbutton", padding=(3,3))
        self.water_input = ttk.Checkbutton(self.extraInformation,
                                            variable=self.water_var , command=lambda:self.selectOptionalItem("water" , self.water_var),
                                            text="Water" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        self.maltbeverage_input = ttk.Checkbutton(self.extraInformation,
                                                   variable=self.maltbeverage_var , command=lambda:self.selectOptionalItem("maltbeverage" , self.maltbeverage_var),
                                                   text="Malt Beverage" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        self.dough_input = ttk.Checkbutton(self.extraInformation,
                                           variable=self.dough_var , command=lambda:self.selectOptionalItem("dough" , self.dough_var),
                                           text="Dough" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        self.icetae_input = ttk.Checkbutton(self.extraInformation,
                                             variable=self.icetae_var , command=lambda:self.selectOptionalItem("icetae" , self.icetae_var),
                                             text="IceTae" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        
        
        
        
        
        self.lable_spicinessLevel = ttk.Label(self.extraInformation,text="Spiciness Level :"  , padding=(3,3) )
      
        self.normalLevel_radio = ttk.Radiobutton(self.extraInformation,
                                                 variable=self.spiceLevel  , command=lambda : self.selectSlevel(),
                                                  text="Normal", value=1 ,bootstyle="primary-outline-toolbutton")
        self.mediumLevel_radio = ttk.Radiobutton(self.extraInformation, text="Medium",
                                                 variable=self.spiceLevel, command=lambda : self.selectSlevel(),
                                                  value=2 ,bootstyle="primary-outline-toolbutton")
        self.hotLevel_radio = ttk.Radiobutton(self.extraInformation,
                                               variable=self.spiceLevel, command=lambda : self.selectSlevel(),
                                               text="Hot", value=3 ,bootstyle="primary-outline-toolbutton")
        

        self.fernchFrise_var = ttk.BooleanVar()
        self.garlicBread_var = ttk.BooleanVar()
        self.salad_var = ttk.BooleanVar()

        
        self.lable_appetizer = ttk.Label(self.extraInformation, text="Appetizer :" , padding=(3,3))
        self.frenchfrize_input = ttk.Checkbutton(self.extraInformation,
                                                  variable=self.fernchFrise_var , command=lambda : self.selectOptionalItem('fernchFrise' , self.fernchFrise_var),
                                                  text="French Frise" ,bootstyle="success-outline-toolbutton", padding=(3,3))
        self.garlicBread_input = ttk.Checkbutton(self.extraInformation,
                                                  variable=self.garlicBread_var , command=lambda : self.selectOptionalItem('garlicBread' , self.garlicBread_var),
                                                  text="Garlic Bread" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        self.salad_input = ttk.Checkbutton(self.extraInformation,
                                            variable=self.salad_var , command=lambda : self.selectOptionalItem('salad' , self.salad_var),
                                            text="Salad" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        
        self.cheesCake_var=ttk.BooleanVar()
        self.tiramisu_var=ttk.BooleanVar()
        self.vanilIceCream_var=ttk.BooleanVar()
        self.lable_dessert = ttk.Label(self.extraInformation, text="Dessert :" , padding=(3,3))
        self.cheescake_input = ttk.Checkbutton(self.extraInformation,
                                                variable=self.cheesCake_var , command=lambda : self.selectOptionalItem('cheesCake' , self.cheesCake_var),
                                                text="Chees Cake" ,bootstyle="success-outline-toolbutton", padding=(3,3))
        self.tiramisu_input = ttk.Checkbutton(self.extraInformation, 
                                              variable=self.tiramisu_var , command=lambda : self.selectOptionalItem('tiramisu' , self.tiramisu_var),
                                              text="Tiramisu" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        self.vanilIC_input = ttk.Checkbutton(self.extraInformation, 
                                             variable=self.vanilIceCream_var , command=lambda : self.selectOptionalItem('vanilIceCream' , self.vanilIceCream_var),
                                             text="Vanil Ice Cream" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        
        
        
        self.lable_specialIns = ttk.Label(self.extraInformation,text="Special Instructions :"  , padding=(3,3) )
        self.specialIns_input = ttk.Entry(self.extraInformation , width=30)
        
        self.lable_delivery = ttk.Label(self.extraInformation,text="Delivery Time :"  , padding=(3,3) )
        self.delivery_comboBox = ttk.Combobox(self.extraInformation, width=28 
                                          , values=self.deliveryItems, state="readonly")
        


        #cashier section
        self.cashierFrame = ttk.LabelFrame(self,bootstyle="primary", text="Cashier information", padding=(10,10,10,20))
        self.pymentMethod_lable = ttk.Label(self.cashierFrame, text="Payment Method :" , padding=(3,3))
        self.chash_radio = ttk.Radiobutton(self.cashierFrame,width=38 ,
                                           command=lambda : self.selectPaymentMetyhod() , 
                                           text="Chash", value=1 ,bootstyle="warning-outline-toolbutton" , variable=self.peymentMethod )
        self.credit_radio = ttk.Radiobutton(self.cashierFrame,width=38 , 
                                            command=lambda : self.selectPaymentMetyhod() , 
                                            text="Credit", value=2 ,bootstyle="warning-outline-toolbutton" , variable=self.peymentMethod )
        self.Pos_radio = ttk.Radiobutton(self.cashierFrame,width=38 , 
                                         command=lambda : self.selectPaymentMetyhod() , 
                                         text="POS", value=3 ,bootstyle="warning-outline-toolbutton" , variable=self.peymentMethod )

        self.label_price = ttk.Label(self.cashierFrame, text="Price :" , padding=(3,3))
        self.price_input = ttk.Entry(self.cashierFrame , width=30 , state="readonly")
        
        self.label_discountCode = ttk.Label(self.cashierFrame, text="Discount Code :" , padding=(3,3))
        self.discountCode_input = ttk.Entry(self.cashierFrame , width=30)
        
        self.label_total = ttk.Label(self.cashierFrame, text="Total Price :" , padding=(3,3))
        self.total_input = ttk.Entry(self.cashierFrame , width=30 , state="readonly")
        
        #opration buttons
        self.operationFrame = ttk.Labelframe(self,bootstyle="success", text="Operations", padding=(100,10,10,20))
        self.clear_btn = ttk.Button(self.operationFrame,command=self.cleanData , text="Clear", bootstyle="warning-outline",width=20) 
        self.Calculate_btn = ttk.Button(self.operationFrame, text="Calculate", bootstyle="success-outline",width=20 ,command=self.calculation)
        self.edit_btn = ttk.Button(self.operationFrame, text="Edit", bootstyle="primary-outline",width=20 , state="disable",command=self.edit)
        self.close_btn = ttk.Button(self.operationFrame, text="Close", bootstyle="danger-outline",width=20 , command=self.closeApp)
        self.order_btn = ttk.Button(self.operationFrame, text="Order", bootstyle="success-outline",width=20 , state="disable")
       
        #menubar
        self.menubar = Menu(self)
        firstMenu = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="First Menu", menu=firstMenu)
        firstMenu.add_command(label="option 1")
        firstMenu.add_command(label="Option 2")
        firstMenu.add_separator()
        firstMenu.add_command(label="Exit" , command=self.closeApp)
        ##-----------------
        secondMenu = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Second Menu", menu=secondMenu)
        secondMenu.add_command(label="option 1")
        secondMenu.add_command(label="Option 2")
        secondMenu.add_separator()
        secondMenu.add_command(label="Option 3")
        self.config(menu=self.menubar)
   
    #Widget Location:
    def location(self):
        #usert Info Frame
        self.userInfoFrame.grid(row=0,  padx=20,pady=10, sticky="nsew" )
        self.lable_firstName.grid(row=0,column=0, sticky="w")
        self.firstName_input.grid(row=0, column=1)
        
        self.lable_lastName.grid(row=0,column=2, sticky="w",padx=(10,0))
        self.lastName_input.grid(row=0, column=3)
        
        self.lable_phoneNumber.grid(row=0,column=4, sticky="w",padx=(10,0))
        self.phoneNumber_input.grid(row=0, column=5)
        
        self.lable_fixedNumber.grid(row=1,column=0,sticky="w" , pady=(10,0))
        self.fixedNumber_input.grid(row=1, column=1)
        
        self.lable_city.grid(row=1,column=2,sticky="w" , pady=(10,0),padx=(10,0))
        self.city_comboBox.grid(row=1, column=3)
        
        self.lable_county.grid(row=1,column=4,sticky="w" , pady=(10,0),padx=(10,0))
        self.county_comboBox.grid(row=1, column=5)
        
        self.lable_address.grid(row=2,column=0,sticky="w" , pady=(10,0))
        self.address_input.grid(row=2, column=1 , columnspan=5, sticky="ew")
        
        self.lable_HNumber.grid(row=3,column=0, sticky="w",pady=(10,0))
        self.HNumber_input.grid(row=3, column=1)
        
        self.lable_unitNumber.grid(row=3,column=2, sticky="w",padx=(10,0))
        self.unitNumber_input.grid(row=3, column=3)
        
        self.lable_floor.grid(row=3,column=4, sticky="w",padx=(10,0))
        self.floor_input.grid(row=3, column=5)
        
        #food Info Frame
        self.foodFrame.grid(row=2, padx=20, pady=10, sticky="nsew" , columnspan=8)
        self.lable_foodType.grid(row=0,column=0, sticky="w")
        self.foodType_comboBox.grid(row=0, column=1)
        
        self.lable_foodSize.grid(row=0,column=2, sticky="w", padx=(10,0))
        self.small_radio.grid(row=0, column=3, padx=3, sticky="w")
        self.medium_radio.grid(row=0, column=4, padx=3, sticky="w")
        self.large_radio.grid(row=0, column=5, padx=3, sticky="w")
        
        self.foodNumber.grid(row=0, column=6, sticky="w", padx=(55,0))
        self.foodNumber_input.grid(row=0, column=7, sticky="ew" , padx=5 , columnspan=2)
        #extra information Frame
        self.extraInformation.grid(row=3,  padx=20,pady=10, sticky="nsew" )
        
        
        self.lable_extraToppings.grid(row=0, column=0, sticky="w",pady=10)
        
        self.cheeseTopping_input.grid(row=0, column=1, sticky="we"  , padx=3,pady=10)
        self.mushroomTopping_input.grid(row=0, column=2, sticky="we"  , padx=3,pady=10)
        self.pepperTopping_input.grid(row=0, column=3, sticky="we" , padx=3 ,pady=10)
        self.oliveTopping_input.grid(row=0, column=4, sticky="we" , padx=3,pady=10 )
        self.onionTopping_input.grid(row=0, column=5, sticky="we" , padx=3 ,pady=10)
        
        
        self.lable_drink.grid(row=1, column=0, sticky="w" , padx=(10 , 0))
        
        self.soda_input.grid(row=1, column=1, sticky="we"  , padx=3)
        self.water_input.grid(row=1, column=2, sticky="we"  , padx=3)
        self.maltbeverage_input.grid(row=1, column=3, sticky="we" , padx=3 )
        self.dough_input.grid(row=1, column=4, sticky="we" , padx=3 )
        self.icetae_input.grid(row=1, column=5, sticky="we" , padx=3 )
        
        self.lable_spicinessLevel.grid(row=2,column=0, sticky="w", padx=(10,0) , pady=10)
        
        self.normalLevel_radio.grid(row=2, column=1, padx=3, sticky="we" , pady=10)
        self.mediumLevel_radio.grid(row=2, column=2, padx=3, sticky="we" , pady=10)
        self.hotLevel_radio.grid(row=2, column=3, padx=3, sticky="we" , pady=10 )
        
        
        
        self.lable_appetizer.grid(row=4, column=0, sticky="w" , padx=(10 , 0))     
        self.frenchfrize_input.grid(row=4, column=1, sticky="we"  , padx=3)
        self.garlicBread_input.grid(row=4, column=2, sticky="we"  , padx=3)
        self.salad_input.grid(row=4, column=3, sticky="we" , padx=3)
        
        self.lable_dessert.grid(row=5, column=0, sticky="w" , padx=(10 , 0) , pady=10)     
        self.cheescake_input.grid(row=5, column=1, sticky="we"  , padx=3 , pady=10)
        self.tiramisu_input.grid(row=5, column=2, sticky="we"  , padx=3 , pady=10)
        self.vanilIC_input.grid(row=5, column=3, sticky="we" , padx=3 , pady=10)
        
        self.lable_specialIns.grid(row=0, column=6, sticky="w" , padx=(110 , 0) )     
        self.specialIns_input.grid(row=0, column=7, sticky="w"  , padx=3 )
        
        self.lable_delivery.grid(row=1, column=6, sticky="w" , padx=(110 , 0) )     
        self.delivery_comboBox.grid(row=1, column=7, sticky="w"  , padx=3 )
        
        #cashier information
        self.cashierFrame.grid(row=4,  padx=20,pady=10, sticky="nsew" )
        self.pymentMethod_lable.grid(row=0, column=0, sticky="w", pady=(10,0))
        self.chash_radio.grid(row=0, column=1, padx=3, sticky="we" , pady=(10,0) )
        self.credit_radio.grid(row=0, column=2, padx=3, sticky="we" , pady=(10,0))
        self.Pos_radio.grid(row=0, column=3, padx=3, sticky=" we" , pady=(10,0) )
        
        self.label_price.grid(row=1, column=0, sticky="w", pady=(10,0))
        self.price_input.grid(row=1, column=1, padx=3, sticky="we" , pady=(10,0) , columnspan=3)
        
        self.label_discountCode.grid(row=2, column=0, sticky="w", pady=(10,0))
        self.discountCode_input.grid(row=2, column=1, padx=3, sticky="we" , pady=(10,0) , columnspan=3)
        
        self.label_total.grid(row=3, column=0, sticky="w", pady=(10,0))
        self.total_input.grid(row=3, column=1, padx=3, sticky="we" , pady=(10,0) , columnspan=3)
        
        #opration buttons
        self.operationFrame.grid(row=5, padx=20, pady=10, sticky="nsew")
        self.clear_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.Calculate_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.edit_btn.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        self.order_btn.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        self.close_btn.grid(row=0, column=4, padx=5, pady=5, sticky="ew")        
    def runApp(self):
        self.mainloop()
    def closeApp(self):
        self.destroy()
        
app = App()
