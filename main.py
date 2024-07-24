import os
from src.data.load_data import load_financial_data
from src.data.preprocess_data import preprocess_data
from src.models.train_model import train_model
from src.models.evaluate_model import evaluate_model
from src.visualization.plots import plot_revenue
from src.data.retrieve_data import get_financial_data, get_financial_statements

def main():
    # Create directories if they don't exist
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)

    # Retrieve historical financial data
    ticker = "BVI.PA"
    start_date = "2010-01-01"
    end_date = "2023-01-01"
    financial_data = get_financial_data(ticker, start_date, end_date)
    financial_data.to_csv('data/raw/Bureau_Veritas_Financials.csv')

    # Retrieve financial statements
    income_statement, balance_sheet, cash_flow = get_financial_statements(ticker)

    # Save financial statements to CSV files
    income_statement.to_csv('data/raw/Bureau_Veritas_Income_Statement.csv')
    balance_sheet.to_csv('data/raw/Bureau_Veritas_Balance_Sheet.csv')
    cash_flow.to_csv('data/raw/Bureau_Veritas_Cash_Flow.csv')

    # Print columns to understand the structure
    print("Historical Market Data Columns:", financial_data.columns)
    print("Income Statement Columns:", income_statement.columns)
    print("Balance Sheet Columns:", balance_sheet.columns)
    print("Cash Flow Columns:", cash_flow.columns)

    # Load data
    raw_data_path = 'data/raw/Bureau_Veritas_Financials.csv'
    data = load_financial_data(raw_data_path)

    # Preprocess data
    data = preprocess_data(data)

    # Train model
    model, X_test, y_test, y_pred = train_model(data)

    # Evaluate model
    evaluate_model(y_test, y_pred)

    # Plot results
    plot_revenue(y_test, y_pred)

if __name__ == "__main__":
    main()
