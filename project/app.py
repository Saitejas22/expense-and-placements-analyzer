import pandas as pd





def menu():
    while True:
        print("====MENU=====")
        print("\n1. add expense")
        print("\n2. view expense")
        print("\n3. delete expense")
        print("\n4. analyze expense")
        print("\n5. add placements")
        print("\n6. view placements")
        print("\n7. generate report")
        print("\n8. placement analysis")
        print("\n9. exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            analyze_expense()
        elif choice == "5":
            add_placements()
        elif choice == "6":
            view_placements()
        elif choice == "7":
            generate_report()
        elif choice == "8":
            placement_analysis()
        elif choice == "9":
            print("exitted successfully")
            break
        else:
            print("Invalid choice")


def add_expense():
    date = input("Enter your date: ")
    amount = float(input("Enter your amount: "))
    category = input("Enter your category: ")
    description = input("Enter your description: ")

    new_data=pd.DataFrame({"Date":[date],"Amount":[amount],"Category":[category],"Description":[description]})
    new_data.to_csv("expenses.csv",mode='a',index=False,header=False)
    print("done adding expense")

def view_expense():
    df=pd.read_csv("expenses.csv")
    print("\n===expenses===")
    print(df.head(20))

def delete_expense():
    date = input("Enter your date: ")
    amount = float(input("Enter your amount: "))
    category = input("Enter your category: ")
    description = input("Enter your description: ")
    df=pd.read_csv("expenses.csv")
    matching_rows=df[
        (df["Date"] == date)&
        (df["Amount"] == amount)&
        (df["Category"] == category)&
        (df["Description"] == description)
    ]
    if matching_rows.empty:
        print("No expenses found")
    else:
        df=df.drop(matching_rows.index)
        df.reset_index(drop=True, inplace=True)
        df.to_csv("expenses.csv",index=False)
        print("done deleting expense")
def analyze_expense():
    df=pd.read_csv("expenses.csv")
    print("\nTotal spending")
    print(df["Amount"].sum())
    print("\navg spending")
    print(df["Amount"].mean())
    print("\nCategory wise spending")
    print(df.groupby("Category")["Amount"].sum())
    print("\nHighest spending in each category")
    print(df.groupby("Category")["Amount"].max())

def add_placements():
    company = input("Enter your company name: ")
    role=input("Enter your role: ")
    status=input("Enter your status: ")
    deadline=input("Enter your deadline: ")
    df=pd.DataFrame({
        "Company":[company],
        "Role":[role],
        "Status":[status],
        "Deadline":[deadline]
    })
    df.to_csv("placements.csv",index=False,header=False,mode="a")
    print("added succesfully")

def view_placements():
    df=pd.read_csv("placements.csv")
    print("\n===placements===")
    print(df.head(20))

def generate_report():
    placements_df=pd.read_csv("placements.csv")
    expenses_df=pd.read_csv("expenses.csv")

    total_spending=expenses_df["Amount"].sum()
    avg_spending=expenses_df["Amount"].mean()
    total_applications=len(placements_df)

    report=f"""
    ===MONTHLY REPORT===
    Total spending: ${total_spending}
    avg spending: ${avg_spending}
    total applications: ${total_applications}
    category wise spending:{expenses_df.groupby("Category")["Amount"].sum()}
    """

    with open("reports/report.txt","w") as f:
        f.write(report)

    print("done generating report")

def placement_analysis():
    df=pd.read_csv("placements.csv")
    print(df["Status"].value_counts())

menu()