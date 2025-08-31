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
        self.resizable(False,False)
        self.geometry('950x900')
        ttk.Style("superhero")
        self.cities = ["Tehran", "Mashhad", "Esfahan", "Tabriz" , 'Alborz']
        self.widgets()
        self.location()
        self.runApp()
    #message 
    def errorHandler(self ,erorr_key , name) :
        errors = {
            'strError' : f"somting wrong : please using string input for this input [ {name} ] ! ",
            'phoneError' : f"somting wrong : your information for [ {name} ] not correct   !"
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
    
    def validation_input(self , input , name , slug):
              
        if(not self.checkString(input , name) and slug == 'str') :
            self.errorHandler('strError' , name)
            
        if(not self.checkPhone(input , name) and slug == 'phone'):
            self.errorHandler('phoneError' , name)
            
   
    def getCounty(self , event):
        county = {
            'Tehran' : ["option 1", "option 2", "option 3", "option 4"],
            'Mashhad' : ["option 5", "option 6", "option 7", "option 8"],
            'Esfahan' : ["option 9", "option 10", "option 11", "option 12"],
            'Tabris' : ["option 13", "option 14", "option 15", "option 16"],
            'Alborz' : ["option 17", "option 18", "option 19", "option 20"],
        }
        countyKey =self.cityVariable.get()
        self.county_comboBox.configure(values=county[countyKey])
        
       





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
        
        self.lable_HNumber = ttk.Label(self.userInfoFrame,text="House Number :"  , padding=(3,3) )
        self.HNumber_input = ttk.Entry(self.userInfoFrame , width=30)
        
        self.lable_unitNumber = ttk.Label(self.userInfoFrame,text="Unit Number :"  , padding=(3,3) )
        self.unitNumber_input = ttk.Entry(self.userInfoFrame , width=30)
        
        self.lable_floor = ttk.Label(self.userInfoFrame,text="Floor :"  , padding=(3,3) )
        self.floor_input = ttk.Entry(self.userInfoFrame , width=30)
        
        #food Info Frame
        self.foodFrame = ttk.LabelFrame(self,bootstyle="danger", text="Food Information", padding=(10,10,10,20))
        
        self.lable_foodType = ttk.Label(self.foodFrame,text="Food Type :"  , padding=(3,3) )
        self.foodType_comboBox = ttk.Combobox(self.foodFrame, width=28 
                                          , values=["option 1", "option 2", "option 3", "option 4"] , state="readonly")
        
        self.lable_foodSize = ttk.Label(self.foodFrame,text="Food Size :"  , padding=(3,3) )
        self.small_radio = ttk.Radiobutton(self.foodFrame, text="Small", value=1 ,bootstyle="primary-outline-toolbutton" , variable=self.foodSize )
        self.medium_radio = ttk.Radiobutton(self.foodFrame, text="Medium", value=2 ,bootstyle="primary-outline-toolbutton" , variable=self.foodSize )
        self.large_radio = ttk.Radiobutton(self.foodFrame, text="Large", value=3 ,bootstyle="primary-outline-toolbutton" , variable=self.foodSize )
        
        self.foodNumber = ttk.Label(self.foodFrame, text="Food Number :", padding=(3,3))
        self.foodNumber_input = ttk.Spinbox(self.foodFrame,from_=1, to=5, width=5, increment=1)
        #extra information Frame
        self.extraInformation = ttk.Labelframe(self,bootstyle="warning", text="Extra Information", padding=(10,10,10,20))
        
        self.lable_extraToppings = ttk.Label(self.extraInformation, text="Extra Toppings :" , padding=(3,3))
        self.cheeseTopping_input = ttk.Checkbutton(self.extraInformation, text="Cheese" ,bootstyle="success-outline-toolbutton", padding=(3,3))
        self.mushroomTopping_input = ttk.Checkbutton(self.extraInformation, text="Mushroom" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        self.pepperTopping_input = ttk.Checkbutton(self.extraInformation, text="Pepper" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        self.oliveTopping_input = ttk.Checkbutton(self.extraInformation, text="Olive" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        self.onionTopping_input = ttk.Checkbutton(self.extraInformation, text="Onion" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        
        self.lable_drink = ttk.Label(self.extraInformation, text="Drink :" , padding=(3,3))
        self.soda_input = ttk.Checkbutton(self.extraInformation, text="Soda" ,bootstyle="success-outline-toolbutton", padding=(3,3))
        self.water_input = ttk.Checkbutton(self.extraInformation, text="Water" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        self.maltbeverage_input = ttk.Checkbutton(self.extraInformation, text="Malt Beverage" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        self.dough_input = ttk.Checkbutton(self.extraInformation, text="Dough" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        self.icetae_input = ttk.Checkbutton(self.extraInformation, text="IceTae" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        
        self.lable_spicinessLevel = ttk.Label(self.extraInformation,text="Food Size :"  , padding=(3,3) )
        self.normalLevel_radio = ttk.Radiobutton(self.extraInformation, text="Normal", value=1 ,bootstyle="primary-outline-toolbutton",variable=self.spiceLevel)
        self.mediumLevel_radio = ttk.Radiobutton(self.extraInformation, text="Medium", value=2 ,bootstyle="primary-outline-toolbutton",variable=self.spiceLevel)
        self.hotLevel_radio = ttk.Radiobutton(self.extraInformation, text="Hot", value=3 ,bootstyle="primary-outline-toolbutton",variable=self.spiceLevel)
        
        self.lable_appetizer = ttk.Label(self.extraInformation, text="Appetizer :" , padding=(3,3))
        self.frenchfrize_input = ttk.Checkbutton(self.extraInformation, text="French Frise" ,bootstyle="success-outline-toolbutton", padding=(3,3))
        self.garlicBread_input = ttk.Checkbutton(self.extraInformation, text="Garlic Bread" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        self.salad_input = ttk.Checkbutton(self.extraInformation, text="Salad" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        
        self.lable_dessert = ttk.Label(self.extraInformation, text="Dessert :" , padding=(3,3))
        self.cheescake_input = ttk.Checkbutton(self.extraInformation, text="Chees Cake" ,bootstyle="success-outline-toolbutton", padding=(3,3))
        self.tiramisu_input = ttk.Checkbutton(self.extraInformation, text="Tiramisu" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        self.vanilIC_input = ttk.Checkbutton(self.extraInformation, text="Vanil Ice Cream" ,bootstyle="success-outline-toolbutton", padding=(3,3)) 
        
        self.lable_specialIns = ttk.Label(self.extraInformation,text="Special Instructions :"  , padding=(3,3) )
        self.specialIns_input = ttk.Entry(self.extraInformation , width=30)
        
        self.lable_delivery = ttk.Label(self.extraInformation,text="Delivery Time :"  , padding=(3,3) )
        self.delivery_comboBox = ttk.Combobox(self.extraInformation, width=28 
                                          , values=["option 1", "option 2", "option 3", "option 4"], state="readonly")
        
        #cashier section
        self.cashierFrame = ttk.LabelFrame(self,bootstyle="primary", text="Cashier information", padding=(10,10,10,20))
        self.pymentMethod_lable = ttk.Label(self.cashierFrame, text="Payment Method :" , padding=(3,3))
        self.chash_radio = ttk.Radiobutton(self.cashierFrame,width=38 ,text="Chash", value=1 ,bootstyle="warning-outline-toolbutton" , variable=self.peymentMethod )
        self.credit_radio = ttk.Radiobutton(self.cashierFrame,width=38 , text="Credit", value=2 ,bootstyle="warning-outline-toolbutton" , variable=self.peymentMethod )
        self.Pos_radio = ttk.Radiobutton(self.cashierFrame,width=38 , text="POS", value=3 ,bootstyle="warning-outline-toolbutton" , variable=self.peymentMethod )

        self.label_price = ttk.Label(self.cashierFrame, text="Price :" , padding=(3,3))
        self.price_input = ttk.Entry(self.cashierFrame , width=30 , state="readonly")
        
        self.label_discountCode = ttk.Label(self.cashierFrame, text="Discount Code :" , padding=(3,3))
        self.discountCode_input = ttk.Entry(self.cashierFrame , width=30)
        
        self.label_total = ttk.Label(self.cashierFrame, text="Total Price :" , padding=(3,3))
        self.total_input = ttk.Entry(self.cashierFrame , width=30 , state="readonly")
        
        #opration buttons
        self.operationFrame = ttk.Labelframe(self,bootstyle="success", text="Operations", padding=(100,10,10,20))
        self.clear_btn = ttk.Button(self.operationFrame, text="Clear", bootstyle="warning-outline",width=20) 
        self.Calculate_btn = ttk.Button(self.operationFrame, text="Calculate", bootstyle="success-outline",width=20)
        self.edit_btn = ttk.Button(self.operationFrame, text="Edit", bootstyle="primary-outline",width=20)
        self.close_btn = ttk.Button(self.operationFrame, text="Close", bootstyle="danger-outline",width=20)
        self.order_btn = ttk.Button(self.operationFrame, text="Order", bootstyle="success-outline",width=20)
       
        #menubar
        self.menubar = Menu(self)
        firstMenu = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="First Menu", menu=firstMenu)
        firstMenu.add_command(label="option 1")
        firstMenu.add_command(label="Option 2")
        firstMenu.add_separator()
        firstMenu.add_command(label="Option 3")
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
        
app = App()
