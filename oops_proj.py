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
            pass
        if user_input == "2":
            pass
        if user_input == "3":
            pass
        if user_input == "4":
            pass
        if user_input == "4":
            exit()

project = chatbook()