import datetime

def generate_receipt(username, mobile_number, items, payment_amount, payment_method):
    receipt = f"""
    ------------------------------
           Payment Receipt
    ------------------------------
    Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    Customer Name: {username}
    Mobile Number: {mobile_number}
    ------------------------------
    Items Purchased:
    {', '.join(items)}
    ------------------------------
    Total Amount: ${payment_amount:.2f}
    Payment Method: {payment_method}
    ------------------------------
    Thank you for your payment!
    ------------------------------
    """
    return receipt

def main():
    print("Welcome to the Payment Receipt Generator")
    
    # Get user input
    username = input("Enter customer's username: ")
    mobile_number = input("Enter customer's mobile number: ")
    
    # Allow the user to enter multiple items, separated by commas
    items = input("Enter items purchased (comma-separated): ").split(',')
    
    payment_amount = float(input("Enter total payment amount: $"))
    payment_method = input("Enter payment method: ")
    
    # Generate receipt
    receipt = generate_receipt(username, mobile_number, items, payment_amount, payment_method)
    
    # Display receipt
    print("\nGenerating Receipt...\n")
    print(receipt)

if __name__ == "__main__":
    main()
