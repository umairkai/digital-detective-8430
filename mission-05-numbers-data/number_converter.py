# Number Converter - Decimal to Binary and Hexadecimal
# Mission 5: Numbers and data

def main():
    print("=== Decimal Number Converter ===")
    user_input = input("Enter a positive decimal integer: ")
    
    try:
        decimal_number = int(user_input)
        if decimal_number < 0:
            print("Please enter a positive integer.")
            return
            
        binary_result = bin(decimal_number)
        hex_result = hex(decimal_number)
        
        print("\n--- Conversion Results ---")
        print(f"Decimal:     {decimal_number}")
        print(f"Binary:      {binary_result} (or {binary_result[2:]})")
        print(f"Hexadecimal: {hex_result.upper()} (or {hex_result[2:].upper()})")
    except ValueError:
        print("Invalid input! Please enter a valid decimal integer.")

if __name__ == "__main__":
    main()
