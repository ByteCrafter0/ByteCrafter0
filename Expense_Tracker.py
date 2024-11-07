class Expense():
    def __init__(self,description, amount,category):
        self.descripton=description
        self.amount=amount
        self.catagory=category

class ExpenseTracker():
    def __init__(self):
        self.Expenses=[]
        self.category=[]
        self.description=[]

    def add_expense(self,des, Exp, cat) :
        self.description.append(des)
        self.category.append(cat)
        self.Expenses.append(Exp)
        print(f"Expense added: {des} - Rs{Exp} in category {cat}")

    def display_expenses(self) :
        if not self.Expenses and self.category and self.description :
            return "Error Information"
        else:
            print("All expenses are :")
            for i, (expense, category,description) in enumerate(zip(self.Expenses, self.category,self.description)):
                print(f"{i+1}. {description} - Rs{expense} - {category}")
    def total_expenses(self) :
        total_sum = sum(self.Expenses)
        print(f"Total expenses is Rs{total_sum}")
    def expenses_by_category(self):
        print("Expenses in category Food:")
        for i,(category,Expenses) in enumerate(zip(self.category,self.Expenses)):
            print(f'{i+1}.{category} - {Expenses}')
        print("The sum of all category are",sum(self.Expenses))
            

tracker = ExpenseTracker()
tracker.add_expense("rice",100,"Groceries")
tracker.add_expense("Movie",120,"Entertainment")
tracker.add_expense("Rent",300,"Housing")
tracker.add_expense("pitty",300,"other")

tracker.display_expenses()
tracker.total_expenses()
tracker.expenses_by_category()