def reciprocal_of_even_number(n):
    try:
        if n == 0:
            raise ZeroDivisionError("Zero is not reciprocal.")
        if n % 2 != 0:
            raise ValueError("Only even numbers are allowed.")
        
        return 1 / n

    except ZeroDivisionError as e:
        return f"Zero Exception: {e}"
    except ValueError as e:
        return f"Value Error: {e}"

number = int(input("Enter NUMBER: "))
print(f"Input: {number}  : {reciprocal_of_even_number(number)}")
