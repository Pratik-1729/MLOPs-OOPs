class chatbook:
    def __init__(self):
        self.username =''
        self.password =''
        self.loggedin = False
        self.main_menu()


    def main_menu(self):
        user_input = input("""\n \t \t \t Welcome to the chatbook👋
                           
                           How would you like to proceed?
                           1. Press 1 to SignUp
                           2. Press 2 to signin
                           3. Press 3 to Write a post
                           4. Press 4 to send a msg to friend
                           5. Press any other key to exit
                           -> """)
        if user_input == "1":
            self.signup()
        if user_input == "2":
            self.login()
        if user_input == "3":
            self.my_post()
        if user_input == "4":
            self.snd_msg()
        if user_input not in ["1","2","3","4"]:
            print("You have been successfully exited")
            exit()

    def signup(self):
        email = input("Enter your email as username:-> ")
        if(email==" "):
            print("username cannot be empty!")
            email = input("Enter your email as username:-> ")
            self.username = email
        pwd = input("Enter the password:-> ")
        if(pwd==" " or len(pwd)<8 ):
            print("Password cannot be empty and should be min 8 char! ")
            pwd = input("Enter the password:-> ")
            self.password = pwd
        self.username = email
        self.password = pwd
        print("You are Signed up successfully!")
        self.main_menu()
    def login(self):
        if (self.username == '' and self.password == ''):
            print("SignUp first by pressing 1 key in main menu!")
            self.main_menu()
        else:
            uname = input("Enter the username:-> ")
            pwd = input("Enter the password:-> ")
            if self.username == uname and self.password == pwd:
                print("You have successfully logged in! ")
                self.loggedin = True
            else:
                print("Input Valid credentials! ")
        self.main_menu()
    
    def my_post(self):
        if self.loggedin:
            txt = input("Enter your text here:-> ")
            print("Your content has been posted.")
        else:
            print("You need to signin first to post something!")
        self.main_menu()
    
    def snd_msg(self):
        if self.loggedin:
            txt = input("Enter your message here:-> ")
            frnd = input("Enter whom to msg:-> ")
            print(f"The message has been sent to {frnd}")
        else:
            print("You need to signin first to send message to anyone!!")
        self.main_menu()




# project = chatbook()