# refactore it & keep it DRY
Appetizers = ["wings","cookies","spring rolls"]
Entrees = ["salmon","steak","meat tornado","a literal garden"]
Desserts = ["ice cream","cake","pie"]
Drinks = ["coffee","tea","unicorn tears"]
def intro():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Drinks
------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************
''')
def user_insertion():
    user_input=input(">")
    return user_input
def main():
    user_input = user_insertion()
    obj ={}
    while(user_input.lower() != "quit"):
        # if user_input.lower() == "quit":
        #     end_application()
            if user_input.lower() in Appetizers:
                if user_input in obj :
                 obj[user_input] +=1
                else :
                    obj[user_input]=1
                print (f"** {obj[user_input]} orders of {user_input.lower()} has been added to your meal")
            else:
             if user_input.lower() in Entrees:
                 if user_input in obj :
                  obj[user_input] =obj[user_input]+1
                 else :
                    obj[user_input]=1
                 print(f"** {obj[user_input]} orders of {user_input.lower()} has been added to your meal")
             else:
              if user_input.lower() in Desserts:
                 if user_input in obj :
                  obj[user_input] +=1
                 else :
                    obj[user_input]=1
                 print(f"** {obj[user_input]} orders of {user_input.lower()} has been added to your meal")
              else:
               if user_input.lower() in Drinks:
                 if user_input in obj :
                  obj[user_input] += 1
                 else :
                    obj[user_input]=1
                 print(f"** {obj[user_input]} orders wings of {user_input.lower()} has been added to your meal")
               else:
                 print("sorry we didint have this item")
            user_input = user_insertion()
    end_application()
def end_application():
    print("thanks for using snakes cafe application !")
#invoke the function
intro()
main()