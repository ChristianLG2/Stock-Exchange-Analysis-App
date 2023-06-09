from Stock_Analyzer import get_stock_data, plot_stock_prices, calculate_returns

def test_get_stock_data():
    # Define test inputs
    symbol = 'AAPL'
    start_date = '2022-01-01'
    end_date = '2022-12-31'

    # Call the function being tested
    data = get_stock_data(symbol, start_date, end_date)

    # Perform assertions to verify the expected behavior
    # You can add assertions based on your specific requirements

    # Assert that the returned data is not empty
    assert not data.empty

    # Print a message indicating the test passed
    print("test_get_stock_data passed successfully.")

def test_plot_stock_prices():
    # Define test inputs
    data = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                         'Close': [100, 110, 120]})
    symbol = 'AAPL'

    # Call the function being tested
    plot_stock_prices(data, symbol)

    # Manual check required for the plot
    print("Check the plot generated by test_plot_stock_prices.")

def test_calculate_returns():
    # Define test inputs
    data = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                         'Close': [100, 110, 120]})

    # Call the function being tested
    data_with_returns = calculate_returns(data)

    # Perform assertions to verify the expected behavior
    # You can add assertions based on your specific requirements

    # Assert that the 'Return' column is present in the data
    assert 'Return' in data_with_returns.columns

    # Print a message indicating the test passed
    print("test_calculate_returns passed successfully.")

def run_tests():
    # Run all the individual test functions
    test_get_stock_data()
    test_plot_stock_prices()
    test_calculate_returns()

# Run the testing program
run_tests()
