# __v 1.1
""" برنامه ای بنویسید که دارای دو ویژگی باشد:
1.کاربر بتواند ثبت نام کند
2.کاربر بتواند در برنامه لاگین کند

برنامه داری یک منو میباشد که شامل ۳ گزینه زیر است
۱. ثبت نام
۲. ورود
۳. خروج از برنامه

کاربر با وارد کردن هر یک از گزینه های مِنو وارد بخش مربوطه میشود
برای اینکه کاربر بتواند ثبت نام کند باید نام کاربری، پسورد و شماره تماس وارد کند
برای ورود به برنامه فقط باید نام کربری و پسورد را وارد کند
پسورد باید حداقل شامل ۸ کاراکتر بوده و فقط شامل حروف باشد """
#_______________________________________________________

#******Librarys******#
import os
#clear the cli screen
clear = lambda: os.system('cls')

#******Functions******#
def signup_def():
    print("** Sign Up **")
    username = input("\tUsername: ").strip()
    if username.isidentifier() and username not in [user.username for user in accounts]:
        phone_num = input("\tEnter your phone number (09*****): ").strip()
        if len(phone_num) == 11 and phone_num.startswith("09") and phone_num.isdecimal:
            password = input("\tPassword: ").strip()
            if len(password)<9 and password.isalpha():
                accounts.append(Users(username, password, phone_num))
                print("\n\t The account was created successfully !\n")
            else:
                print("\n\t Error: The password format is incorrect")
        else:
            print("\n\t Error: The phone number format is incorrect!")
    else:
        print("\n\t Error: The username format is incorrect or the username was already created!")
    
def signin_def():
    print("** Sign In **")
    username = input("\tUsername: ").strip()
    password = input("\tPassword: ").strip()
    if username.isidentifier():
        if len(password)<9 and password.isalpha():
            if {username : password} in [Users.checkpass(user) for user in accounts]:
                print("\n\t Yehh, Your in !")
            else:
                print("\n\t Error: Wrong Username or Password")
        else:
            print("\n\t Error: Wrong Username or Password")
    else:
        print("\n\t Error: Wrong Username or Password")

# def forgetpassword_def():
#     print("This section is Not ready")

#******Objects******#
class Users():
    def __init__(self, username:str, password:str, phone_number:str):
        self.username = username
        self.password = password
        self.phone_number = phone_number
    def checkpass(self):
        return {self.username : self.password}


class MenuItems():
    #define menu item
    def __init__(self, category:str, name:str, description:str, order:int):
        self.name = name
        self.description = description
        self.order = order
        self.category = category
        globals()[category].append(self)

    #sort Menus
    def sort_menu(items:list):
        sorted(items, key=lambda item : item.order)
    #show Menus
    def show_menu(menu : list,error) -> str: 
        print("** Menu **")
        count = 0
        for count,item in enumerate(menu):
            count += 1
            print(f"{count}. {item.name}")
        print(f"{count+1}. Exit\n")
        print(f"Choose service number(",end="")
        for i in range(1,count+2):
            if i<count+1:
                print (f"{i} - ", end = "")
            else:
                print(f"{i}): ",end ="")
        return ""
    
#******Default Messages******#
quit_message = "Are you sure you want to exit this section?(yes-no)"
wrong_choose = "Oops Wrong Input, Please choose the correct item below."

#******define Options and Menus******#
#put all items in a empty list
#if an item has submenu define it in options
main_bar, signin_menu, signup_menu = [], [], []
options = [       
            MenuItems("main_bar", "Sign Up", "Create account", 1),
            MenuItems("main_bar", "Sign In", "Login", 2)
            ]

#******define accounts******#
accounts = [
            Users("admin","admin","")
            ]

#******sort defined Menus******#
MenuItems.sort_menu(main_bar)

#******default values******#
clear()
current_menu = main_bar
error = False
#******User Select******#
while True:
#Check if The slkt(select) was Wrong!
    if error:
            input(wrong_choose)
            error = False

#Show Current Menu items
    #Put the Current Menu items in a dict
    current_items = {str(count):i for count,i in enumerate([item.name for item in current_menu],1)}
    #Finds the latest item number for EXIT item
    exit_key = str(int(list(current_items.keys())[-1])+1) if len(current_items) else "1"
    #show menu and get the choose
    slkt = input(MenuItems.show_menu(current_menu,error)).strip()

# Check input
    if slkt in current_items:
        clear()
        #opens selected item secion (returns string)
        slkted_item = "".join(current_items[slkt].lower().split())+"_menu"
        #remember the supermenu
        supper_menu = current_items[slkt]
        #change current menu to selected item's submenu
            #globals()[slkted_item] ==> it converts ("slkted_item" as string) to (slkted_item as global variable)
        current_menu = globals()[slkted_item]
    #Call selected item's Function
        for key in current_items:
            if key == slkt:
                globals()["".join(current_items[key].lower().split())+"_def"]()

#Exit Selcet
    elif slkt in [exit_key, "e", "exit", "q"]:
        x = input(quit_message + "\n").casefold()
        clear()
        if x in ["y", "yes", ""]:
        #check if there is a supermenu
            #if there is no supermenu exit the program
            if current_menu is main_bar:
                clear()
                print("See you Soon.")
                break
            #if there is a supermenu go back
            else:
                clear()
                for option in options:
                    if option.name is supper_menu:
                        current_menu = globals()[option.category]
#Wrong input
    else:
        clear()
        error = True