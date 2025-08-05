#!/usr/bin/env python3
"""
Simple Python script to add two numbers
Author: AI Assistant
Date: August 5, 2025
"""

def add_numbers(num1, num2):
    """
    Add two numbers and return the result.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
    
    Returns:
        float: Sum of the two numbers
    """
    return num1 + num2

def get_user_input():
    """Get input from user for two numbers."""
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None

def main():
    """Main function to execute the addition program."""
    print("=" * 40)
    print("    Simple Number Addition Program")
    print("=" * 40)
    
    # Get user input
    num1, num2 = get_user_input()
    
    if num1 is not None and num2 is not None:
        # Calculate sum
        result = add_numbers(num1, num2)
        
        # Display result
        print(f"\nResult: {num1} + {num2} = {result}")
        print("=" * 40)
    else:
        print("Program terminated due to invalid input.")

if __name__ == "__main__":
    main()
