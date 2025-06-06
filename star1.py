import streamlit as st
import pandas as pd
import json


st.title("Star Example 1")
st.header("Budget Tracker")
st.subheader("Are you ready to save money?")

transaction = st.selectbox("Select a transaction type", options=[
    "", "Add Expense", "Add Income"
])

def write_json(transaction_type, new_data, filename="json_files/budget_tracker.json"):
    with open(filename, "r+") as file:
        file_data = json.load(file)
        file_data[transaction_type].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)

def countExpensesByCategory(table):
    x = table.groupby("category")["amount"].count()
    y = table.groupby("category")["amount"].sum()
    return x, y

if transaction == "Add Income":
    income = st.text_input("Enter your income: ")
    if income:
        write_json("income", float(income))
        st.success(f"${income} has been added as income to your account")

elif transaction == "Add Expense":
    with st.form("Expense", clear_on_submit=True):
        category = st.selectbox("Select a category", options=[
            "",
            "Entertainment",
            "Utilities",
            "School",
            "Rent",
            "Transportation",
            "Health",
            "Groceries"
        ])
        amount = st.text_input("Enter your expense amount: ")
        submit = st.form_submit_button("Submit")
        if submit:
            expense={
                "category": category,
                "amount": float(amount)
            }
            write_json("expenses", expense)

with open("json_files/budget_tracker.json", "r") as read_file:
    file_data = json.load(read_file)
    if len(file_data["expenses"]) > 0:
        idx = []
        for i in range(len(file_data["expenses"])):
            idx.append(str(i))
        df = pd.DataFrame(file_data["expenses"], index=idx)
        st.dataframe(df)
        x,y = countExpensesByCategory(df)
        st.bar_chart(y)
    if len(file_data["income"]) > 0:
        incomeTotal = sum(file_data["income"])
        moneySpent = 0
        for j in file_data["expenses"]:
            moneySpent += j["amount"]
        st.success(f"Total income: US${incomeTotal:.2f}.")
        st.error(f"Total money spent: US${moneySpent:.2f}.")
        st.warning(f"Amount left: US${incomeTotal - moneySpent:.2f}.")
