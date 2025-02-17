from validation.validations import valid_email,valid_mobile,hash_password
class User :
    User_info = "users.txt"
    #init information 
    def __init__(self, first_name, last_name, email, password, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password =  hash_password(password)  
        self.phone = phone
 
 
    #load 
    @classmethod
    def load(cls):
        try:
            with open(cls.User_info, 'r') as f:
                lines = f.readlines()
                data = [line.strip().split("|") for line in lines]
                return data  
        except Exception :
            print("CAN NOT LOAD THIS FILE!")
            return []
     #save data   
    @classmethod
    def save_info (cls,data):
        try:
            with open(cls.User_info,"a") as f:
                for i in data:
                    f.write("|".join(i)+"\n")
        except Exception as e :
            print(f"Error in saving user info : {e}")
 
    
    #register 
    @classmethod
    def register(cls):
        email = input("Enter Your Email :")
        users=cls.load()

        if not valid_email(email):
            print("Invalid email.")
            return 0 
        for user in users:
            if len (user)>2 and user[2]==email:
                print("This Email already exist Try again!!")
                return 0 
        FirstName = input("Enter Your First Name : ")
        LastName = input("Enter Your Last Name : ")
        Password = input("Enter Your Password : ")
        ConfirmPassword = input("Enter Your Password Again : ")
        if Password != ConfirmPassword :
                print("Passwords do not match !")
                return 0
        Phone = input("Enter Phone : ")
        if not valid_mobile(Phone):
                print("Invalid Phone Number !")
                return 0 
        new_user = User(FirstName, LastName, email, hash_password(Password), Phone)
        users.append([FirstName, LastName ,email, hash_password(Password), Phone])
        cls.save_info(users)
        print("Registration Successful !")
        return new_user

    @classmethod 
    def login(cls):
        try:
            email = input("Enter Your Email :")
            Password = input("Enter Your Password : ")
            users=cls.load()
            hashed_password=hash_password(Password)
            for user in users:
                if len(user) > 2 and user[2]==email and user[3]==hashed_password:
                    print(f"Login succesfully !! Hello {user[0]} {user[1]} . ")
                    return email 
        except Exception:
             
            print( " Invalid email  or password please try again !!" )
                    
    