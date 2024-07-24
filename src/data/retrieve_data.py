import yfinance as yf


def get_financial_data(ticker, start_date, end_date):
    # Download historical market data from Yahoo Finance
    data = yf.download(ticker, start=start_date, end=end_date)
    return data


def get_financial_statements(ticker):
    # Retrieve financial statements (income statement, balance sheet, cash flow)
    stock = yf.Ticker(ticker)
    income_statement = stock.financials
    balance_sheet = stock.balance_sheet
    cash_flow = stock.cashflow

    return income_statement, balance_sheet, cash_flow


if __name__ == "__main__":
    # Example usage
    ticker = "BVI.PA"  # Ticker symbol for Bureau Veritas on the Paris Stock Exchange
    start_date = "2010-01-01"
    end_date = "2023-01-01"
    financial_data = get_financial_data(ticker, start_date, end_date)
    financial_data.to_csv('data/raw/Bureau_Veritas_Financials.csv')

    income_statement, balance_sheet, cash_flow = get_financial_statements(ticker)

    # Save financial statements to CSV files
    income_statement.to_csv('data/raw/Bureau_Veritas_Income_Statement.csv')
    balance_sheet.to_csv('data/raw/Bureau_Veritas_Balance_Sheet.csv')
    cash_flow.to_csv('data/raw/Bureau_Veritas_Cash_Flow.csv')

    # Print columns
    print("Historical Market Data Columns:", financial_data.columns)
    print("Income Statement Columns:", income_statement.columns)
    print("Balance Sheet Columns:", balance_sheet.columns)
    print("Cash Flow Columns:", cash_flow.columns)
