import json
import os


class Expense_Tracker():
    def __init__(self):
        self.Expense={}
    
    def Add_Expense(self):
        month=int(input("Enter the month Number(1-12): "))
        if month in self.Expense:
            print("The Month's Expense is Already Tracked.")
        else:
            Amount=int(input("Enter the Total Income for the Month: "))
            self.Expense[month]={"Expense Amount": Amount,
                                 "Category":{}}
            print("The Tracking for the Month Started Successfully.")
            
    def Catergories(self):
        month=int(input("Enter the Month Nubmer(1-12): "))
        if not month in self.Expense:
            print("The Month's Expense Hasn't been Tracked Yet.")
        else:
            category=input("Enter the Category: ").capitalize()
            expense=int(input("Enter the Spend Amount: "))
            self.Expense[month]["Category"][category]=expense
            print("The expense for the Category Tracked succesfully.")

    def edit_remove_category(self):
        print("1.Edit Category")
        print("2.Remove Category")
        option=int(input("Select(1,2): "))
        month=int(input("Enter the Month Number(1-12): "))
        if option==1:
            category=input("Enter the Category: ")
            if category in self.Expense[month]["Category"]:
                amount=int(input("Enter the modified Amount: "))
                self.Expense[month]["Category"][category]=amount
                print("The category edited successfully.")
            else:
                print(f"THe Category {category} doesn't exist.")
        else:
            category=input("Enter the Category Name to Remove:  ")
            if category in self.Expense[month]["Category"]:
                del self.Expense[month]["Category"][category]
                print("THe Category removed successfully.")
            else:
                print(f"The Category {category} doesn't exists.")

    def monthly_summery(self):
        if self.Expense:
            option=input("Do you Want to view expenses in Specific of Month or All Months(S/A): ").upper()
            if option=="S":
                month=int(input("Enter the Month Number(1-12): "))
                if not month in self.Expense:
                    print("The Expense for this Month isn't Tracked.")
                else:
                    total_monthly_expense=0
                    print(f"Expense for the Month: {month}")
                    print(f"Total Income: {self.Expense[month]["Expense Amount"]}")
                    print(f"Spending in Each Category:")
                    for category , spending in self.Expense[month]["Category"].items():
                        print(f"{category}:{spending}")
                        total_monthly_expense+=spending
                    print(f"Total Spending:{total_monthly_expense}")
            else:
                print("********Total Expenses For ALL Months*********")
                for months , data in self.Expense.items():
                    print(f"Month:{months}")
                    print(f"Total Income: {data["Expense Amount"]}")
                    print(f"Total Spending in Each Category")
                    total=0
                    for categories, spend in self.Expense[months]["Category"].items():
                        print(f"{categories}:{spend}")
                        total+=spend
                    print(f"Total Spending in Month {months} ={total} ")
                    print()
        else:
            print("NO Months Are Traked")

    def save_to_file(self):
        with open("expenses.json", "w") as file:
            json.dump(self.Expense, file)
        print("Expenses saved successfully.")

    def load_from_file(self):
        if os.path.exists("expenses.json"):
            with open("expenses.json", "r") as file:
                self.Expense = json.load(file)
            # Convert month keys back to int
            self.Expense = {int(k): v for k, v in self.Expense.items()}
            print("Expenses loaded successfully.")
        else:
            print("No saved data found.")

         
             
    def menu(self):
        while True:
            print("***********MONTHLY EXPENSE TRACKER************")
            print("1.Add Expense")
            print("2.Categories")
            print("3.Edit_Remove_Category")
            print("4.Monthly Summery")
            print("5.Load Form file")
            print("6.Save and Exit")
            selection=int(input("Select from option(1-5): "))
        
            if selection==1:
                    self.Add_Expense()
            elif selection==2:
                    self.Catergories()
            elif selection==3:
                    self.edit_remove_category()
            elif selection==4:
                    self.monthly_summery()
            elif selection==5:
                 self.load_from_file()
            elif selection==6:
                    self.save_to_file()
                    print("Exiting Program....")
                    break
et=Expense_Tracker()
et.menu()


