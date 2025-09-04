requiredItems = [
   "firstName_input", "lastName_input","phoneNumber_input","fixedNumber_input", 
   "address_input","HNumber_input" ,"unitNumber_input" ,
]

inputnames = [
           "firstName_input", "lastName_input","phoneNumber_input","fixedNumber_input",           
           "address_input","HNumber_input" ,"unitNumber_input" ,"specialIns_input",
           "floor_input" ,"foodNumber_input" ,"discountCode_input"
        ]
comboBoxNames = ["city_comboBox","county_comboBox","foodType_comboBox" ,"delivery_comboBox"]
radioNamse = [
     "small_radio","medium_radio" , "large_radio" ,
     "normalLevel_radio","mediumLevel_radio","hotLevel_radio",
     "chash_radio" , "credit_radio" , "Pos_radio",
]
checkBoxNames = [
   "frenchfrize_input","garlicBread_input","salad_input","cheescake_input","tiramisu_input","vanilIC_input",
   "cheeseTopping_input","mushroomTopping_input","pepperTopping_input","oliveTopping_input","onionTopping_input",
   "soda_input","water_input","maltbeverage_input","dough_input","icetae_input",  
]

radionameVar = [
    'soda', 'water', 'maltbeverage', 'dough', 'icetae',
    'fernchFrise', 'garlicBread', 'salad',
    'cheesCake', 'tiramisu', 'vanilIceCream',          
    'Cheese', 'Mushroom', 'Pepper','Olive', 'Onion'
    ]

all= [
           "firstName_input", "lastName_input","phoneNumber_input","fixedNumber_input","city_comboBox","county_comboBox","address_input",
           "HNumber_input" , "unitNumber_input" , "floor_input" ,"foodType_comboBox" ,"small_radio","medium_radio" , "large_radio" ,
           "foodNumber_input" , "cheeseTopping_input","mushroomTopping_input","pepperTopping_input","oliveTopping_input","onionTopping_input",
           "soda_input","water_input","maltbeverage_input","dough_input","icetae_input","normalLevel_radio","mediumLevel_radio","hotLevel_radio",
           "frenchfrize_input","garlicBread_input","salad_input","cheescake_input","tiramisu_input","vanilIC_input","specialIns_input","delivery_comboBox",
           "chash_radio" , "credit_radio" , "Pos_radio","discountCode_input"
        ]
import customtkinter as TK
import math # power
from CTkMessagebox import CTkMessagebox #for massage Box
import datetime #get Year
import time #make ID

class App(TK.CTk):
    def __init__(self):
        super().__init__() 
        self.wscreen = self.winfo_screenwidth()
        self.hscreen = self.winfo_screenheight()
        self.geometry(f"420x800+{((self.wscreen//2) - 210)}+{((self.hscreen//2) - 400)}")
        self.resizable(0,0)
        self.title("App")
        self.fileName = 'database'
        self.fileMode = 'a'
        self.font ={
            "btn" : ('Arial',20 , 'bold') ,
            "lable" : ('Arial',16 ,),
            } 
        self.configForm = {
            'btn_height' : 40,
            'entry_height' : 40,
            'entry_pady' : 4
        }

    #helper 
    #clean Data
    def cleanData(self):
        self.firstNameInput.delete(0 , TK.END)
        self.lastNameInput.delete(0 , TK.END)
        self.yearOfBirthInput.delete(0 , TK.END)
        self.grossSalaryInput.delete(0 , TK.END)
        self.insuranceInput.delete(0 , TK.END)
        self.weightInput.delete(0 , TK.END)
        self.heightInput.delete(0 , TK.END)
        self.taxInput.delete(0 , TK.END)
        self.phonenumberInput.delete(0 , TK.END)
        self.resetReadOnlyInput()
        self.btn_Calculator.configure( state="normal")
        self.btn_save.configure( state="disabled")
        self.update()
        self.firstNameInput.focus_set()
    #reset RedOnly Input
    def resetReadOnlyInput(self):
        self.ageInput.configure(state= "normal")
        self.BMIInput.configure(state= "normal")
        self.netSalaryInput.configure(state= "normal")
        self.ageInput.delete(0 , TK.END)
        self.BMIInput.delete(0 , TK.END)
        self.netSalaryInput.delete(0 , TK.END)
        self.ageInput.configure(state= "readonly")
        self.BMIInput.configure(state= "readonly")
    #close App
    def closeApp(self):
        self.destroy()
    #validation Helpers
    def checkStringInput(self , data) :
        if(data.isalpha()):            
            return True
        return False
    def checkIntValue(self,data):
        print(data)
        if(data.isdigit() and len(data) == 4):
            return True
        return False
    def checkwieght(self):
        if(self.weightInput.get().isalpha() or self.weightInput.get() == ''):
            return False
        return True
    
    def checkHeight(self):
        if(self.heightInput.get().isalpha() or self.heightInput.get() == '' or self.heightInput.get().isdigit()):
            print(1)
            return False
        if(2.72 < float(self.heightInput.get()) or float(self.heightInput.get()) < 0.4) :
            print(2)
            return False
        print(self.heightInput.get())
        return True
    def checkGSalary(self):
        if(self.grossSalaryInput.get().isdigit()):
            return True
        return False
    def checkDigitAndRange(self , data , min_range = 0 , max_range = 100):
        if(data.isdigit()):
            if(int(data) > min_range or int(data) < max_range) :
                return True
            return False
        return False
    def checkPhoneNumber(self) :
        if(self.phonenumberInput.get().isdecimal() and len(self.phonenumberInput.get()) == 11):
            return True
        return False
    def notEqual(self , notMoreThan = 100) :
        if(self.taxInput.get() == '' or  self.insuranceInput.get()== '') :
            return 'empty'
        sum = int(self.taxInput.get()) + int(self.insuranceInput.get())
        if(sum >= notMoreThan) :
            return False
        return True
            
    #validation
    def validation(self):
        has_error = False
        self.errors = {}
        if(not self.checkStringInput(self.firstNameInput.get())) :
            has_error = True ;
            self.errors['firstName'] = "Please check your first name ! "
        if(not self.checkStringInput(self.lastNameInput.get())) :
            has_error = True ;
            self.errors['lastName'] = "Please check your last name ! "
        if(not self.checkIntValue(self.yearOfBirthInput.get())) :
            has_error = True ;
            self.errors['age'] = "Please check your age  ! "
        if(not self.checkwieght()) :
            has_error = True ;
            self.errors['weight'] = "Please check your weight  ! "
        if(not self.checkHeight()) :
            has_error = True ;
            self.errors['height'] = "Please check your height  ! "
        if(not self.checkDigitAndRange(self.grossSalaryInput.get())) :
            has_error = True ;
            self.errors['gSalary'] = "Please check your Gross Salary ! "
        if(not self.checkDigitAndRange(self.insuranceInput.get())) :
            has_error = True ;
            self.errors['insurance'] = "Please check your insurance ! "
        if(not self.checkPhoneNumber()) :
            has_error = True ;
            self.errors['phoneNumber'] = "Please check your Phone Number ! "
        if(not self.notEqual()) :
            has_error = True
            self.errors['NotEqual'] = "sum of Tax and insurance not to be Equal 100 or more than 100 ! "
        if(self.notEqual() == 'empty') :
            has_error = True
            self.errors['NotEqual'] = "Tax and insurance is empty ! "
        
            
        if(has_error) :
            return False
        return True
    #BMI
    def BMI(self):
        bmi = float(self.weightInput.get()) / math.pow(float(self.heightInput.get()) , 2)
        return  round(bmi , 2)
    def setBMI(self) :
        self.BMIInput.configure( state="normal")
        self.BMIInput.insert(0 , self.BMI())
        self.BMIInput.configure( state="readonly")
    #age cal
    def setAge(self):
        currentYear = datetime.datetime.today().year
        age = currentYear - int(self.yearOfBirthInput.get())
        self.ageInput.configure( state="normal")
        self.ageInput.insert(0 , age)
        self.ageInput.configure( state="readonly")
    #net salary
    def calNetSalary(self):
        tax = (int(self.grossSalaryInput.get()) * int(self.taxInput.get())) / 100 
        insurance = (int(self.grossSalaryInput.get()) * int(self.insuranceInput.get())) / 100 
        salary = int(self.grossSalaryInput.get()) - (tax + insurance)
        self.netSalaryInput.configure( state="normal")
        self.netSalaryInput.insert(0 , salary)
        self.netSalaryInput.configure( state="readonly")
    #disable Entry
    def readOnlyEntry(self) :
        self.firstNameInput.configure(state = "readonly")
        self.lastNameInput.configure(state = "readonly")
        self.yearOfBirthInput.configure(state = "readonly")
        self.grossSalaryInput.configure(state = "readonly")
        self.insuranceInput.configure(state = "readonly")
        self.weightInput.configure(state = "readonly")
        self.heightInput.configure(state = "readonly")
        self.taxInput.configure(state = "readonly")
        self.phonenumberInput.configure(state ="readonly")
        self.btn_edit.configure(state ="normal")
        self.btn_clear.configure(state ="disabled")
    #edit on
    def editOn(self):
        self.firstNameInput.configure(state = "normal")
        self.lastNameInput.configure(state = "normal")
        self.yearOfBirthInput.configure(state = "normal")
        self.grossSalaryInput.configure(state = "normal")
        self.insuranceInput.configure(state = "normal")
        self.weightInput.configure(state = "normal")
        self.heightInput.configure(state = "normal")
        self.taxInput.configure(state = "normal")
        self.phonenumberInput.configure(state ="normal")
        self.btn_edit.configure(state ="disabled")
        self.btn_clear.configure(state ="normal")
        self.btn_Calculator.configure(state ="normal")
        self.btn_save.configure(state ="disabled")
        
    #calculator
    def calculator(self) :
       
        if(not self.validation()):
            msg = "\n".join(list(self.errors.values()))
            msg = CTkMessagebox(title="Warning !", message=msg,
                        icon="warning", option_1="OK" , justify="right")
            response = msg.get()            
            if response=="OK":
                self.clear_current_data() 
            return False
        self.btn_Calculator.configure( state="disabled")
        self.resetReadOnlyInput()
        self.setBMI()
        self.setAge()
        self.calNetSalary()
        self.readOnlyEntry()
        self.btn_save.configure( state="normal")
        
    #save To file

    
    def saveToFile(self , extention = 'txt'   ) :
        with open(self.fileName +'.'+ extention , mode = self.fileMode ) as file :
            file.write(str(self.getDataForm()) + '\n')
        self.editOn()
        self.cleanData()
        CTkMessagebox(message="Your Information saved !",
                  icon="check", option_1="Ok")
        
        
    def getDataForm(self):
        data = {
            "id" :int(time.time()) ,
            "firstname" : self.firstNameInput.get(),
            "lastname" : self.lastNameInput.get(),
            "yea of brith" : self.yearOfBirthInput.get(),
            "age" : self.ageInput.get(),
            "weight" : self.weightInput.get(),
            "height" : self.heightInput.get(),
            "BMI" : self.BMIInput.get(),
            "Gross Salary" : self.grossSalaryInput.get(),
            "tax" : self.taxInput.get(),
            "insurance" : self.insuranceInput.get(),
            "net salaray" : self.netSalaryInput.get(),
            "phone Nimber" : self.phonenumberInput.get(),
        }
        return data
        
        
    def ui_items(self) :
        
        self.labelFirstName = TK.CTkLabel(self, text="First Name :" ,padx=10 ,pady = 10, height=20 , font=self.font['lable'])
        self.firstNameInput = TK.CTkEntry(self , placeholder_text="Ex : Mohammad"  , height=self.configForm['entry_height']  , width=250)

        self.labelLastName = TK.CTkLabel(self, text="Last Name :" ,padx=10 ,pady = 10, height=20 , font=self.font['lable'])
        self.lastNameInput = TK.CTkEntry(self , placeholder_text="Ex : Naghlani"  , height=self.configForm['entry_height']  , width=250)
        
        self.labelYearOfBirth = TK.CTkLabel(self, text="Year Of Birth :" ,padx=10 ,pady = 10, height=20 , font=self.font['lable'])
        self.yearOfBirthInput = TK.CTkEntry(self , placeholder_text="Ex : 1989"  , height=self.configForm['entry_height']  , width=250)
        
        self.labelAge = TK.CTkLabel(self, text="Age :" ,padx=10 ,pady = 10, height=20 , font=self.font['lable']) 
        self.ageInput = TK.CTkEntry(self , height=self.configForm['entry_height']  , width=250 , state='readonly')
        
        self.labelWeight = TK.CTkLabel(self, text="Weight (kg) :" ,padx=10 ,pady = 10, height=20 , font=self.font['lable']) 
        self.weightInput = TK.CTkEntry(self , placeholder_text="Ex : 93"  , height=self.configForm['entry_height']  , width=250) 
        
        self.labelHeight = TK.CTkLabel(self, text="Height (m) :" ,padx=10 ,pady = 10, height=20 , font=self.font['lable'])
        self.heightInput = TK.CTkEntry(self , placeholder_text="Ex : 1.83"  , height=self.configForm['entry_height']  , width=250) 
        
        self.labelBMI = TK.CTkLabel(self, text="BMI :" ,padx=10 ,pady = 10, height=20 , font=self.font['lable'] )
        self.BMIInput = TK.CTkEntry(self ,  height=self.configForm['entry_height']  , width=250 , state='readonly')
                
        self.labelGrossSalary = TK.CTkLabel(self, text="Gross Salary :" ,padx=10 ,pady = 10, height=20 , font=self.font['lable'])
        self.grossSalaryInput = TK.CTkEntry(self , placeholder_text="Ex : 2500000"  , height=self.configForm['entry_height']  , width=250) 
                
        self.labelTax = TK.CTkLabel(self, text="Tax :" ,padx=10 ,pady = 10, height=20 , font=self.font['lable'])
        self.taxInput = TK.CTkEntry(self , placeholder_text="Ex : 10"  , height=self.configForm['entry_height']  , width=250) 
                
        self.labelInsurance = TK.CTkLabel(self, text="Insurance  :" ,padx=10 ,pady = 10, height=20 , font=self.font['lable'])
        self.insuranceInput = TK.CTkEntry(self , placeholder_text="Ex : 20"  , height=self.configForm['entry_height']  , width=250) 
        
        self.labelNetSalary = TK.CTkLabel(self, text="Net Salary :" ,padx=10 ,pady = 10, height=20 , font=self.font['lable']) 
        self.netSalaryInput = TK.CTkEntry(self ,  height=self.configForm['entry_height']  , width=250 , state='readonly')
                
        self.labelPhoneNumber = TK.CTkLabel(self, text="Phone Number  :" ,padx=10 ,pady = 10, height=20 , font=self.font['lable'])
        self.phonenumberInput = TK.CTkEntry(self , placeholder_text="Ex : 09124610284"  , height=self.configForm['entry_height']  , width=250) 
        #btn
        
        self.btn_save = TK.CTkButton(self , text="Save" ,font= self.font['btn'] ,state='disabled', height=40 ,command=self.saveToFile)
        self.btn_close = TK.CTkButton(self , text="Close" ,fg_color="#ff0000" ,font= self.font['btn'], hover_color="#FF4343" , height=40 , command=self.closeApp)
        self.btn_clear = TK.CTkButton(self , text="Clear"  ,font= self.font['btn'] , height=40 , command=self.cleanData)
        self.btn_Calculator = TK.CTkButton(self , text="Calculation"  ,fg_color="#666666" ,font= self.font['btn'], hover_color="#333333" , height=40 , command=self.calculator)

        self.btn_edit = TK.CTkButton(self, text="Edit" ,font= self.font['btn'], hover_color="#333333" , height=40 ,state='disabled'  , command=self.editOn)
        
        
    def location_items(self) :
        self.labelFirstName.grid(row=0,column=0  , sticky="w")
        self.firstNameInput.grid(row= 0 , column = 1 , sticky="e"  ,pady=self.configForm['entry_pady'] )
        
        
        
        self.labelLastName.grid(row=1,column=0  , sticky="w")
        self.lastNameInput.grid(row= 1 , column = 1 , sticky="e",pady=self.configForm['entry_pady'] )
        
        self.labelYearOfBirth.grid(row=2,column=0  , sticky="w")
        self.yearOfBirthInput.grid(row= 2 , column = 1 , sticky="e",pady=self.configForm['entry_pady'] )
        
        self.labelAge.grid(row=3,column=0  , sticky="w")
        self.ageInput.grid(row= 3 , column = 1 , sticky="e" ,pady=self.configForm['entry_pady'])
        
        self.labelWeight.grid(row=4,column=0  , sticky="w")
        self.weightInput.grid(row= 4 , column = 1 , sticky="e",pady=self.configForm['entry_pady'] )
        
        self.labelHeight.grid(row=5,column=0  , sticky="w")
        self.heightInput.grid(row= 5 , column = 1 , sticky="e" ,pady=self.configForm['entry_pady'])
        
        self.labelBMI.grid(row=6,column=0  , sticky="w")
        self.BMIInput.grid(row= 6 , column = 1 , sticky="e" ,pady=self.configForm['entry_pady'])
        
        self.labelGrossSalary.grid(row=7,column=0  , sticky="w")
        self.grossSalaryInput.grid(row= 7 , column = 1 , sticky="e" ,pady=self.configForm['entry_pady'])
        
        self.labelTax.grid(row=8,column=0  , sticky="w")
        self.taxInput.grid(row= 8 , column = 1 , sticky="e" ,pady=self.configForm['entry_pady'])
        
        self.labelInsurance.grid(row=9,column=0  , sticky="w")
        self.insuranceInput.grid(row= 9 , column = 1 , sticky="e",pady=self.configForm['entry_pady'] )
        
        self.labelNetSalary.grid(row=10,column=0  , sticky="w")
        self.netSalaryInput.grid(row= 10 , column = 1 , sticky="e" ,pady=self.configForm['entry_pady'])
        
        self.labelPhoneNumber.grid(row=11,column=0  , sticky="w")
        self.phonenumberInput.grid(row= 11 , column = 1 , sticky="e",pady=self.configForm['entry_pady'] )
        
        #btn
        self.btn_save.grid(row= 12 , column = 0 , columnspan=1 , sticky="we" , padx=10  , pady = 10)
        self.btn_close.grid(row= 12 , column = 1 , columnspan=1 , sticky="we",padx=10,pady = 10)
        self.btn_clear.grid(row= 13 , column = 0 , columnspan=1 , sticky="we" , padx=10,pady = 10)
        self.btn_Calculator.grid(row= 13 , column = 1 , columnspan=1 , sticky="we" , padx=10,pady = 10)
        self.btn_edit.grid(row= 14 , column = 0 , columnspan=2 , sticky="we" , padx=10,pady = 10)
        
app =App()
app.ui_items()
app.location_items()
app.mainloop()