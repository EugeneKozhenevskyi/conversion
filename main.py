def conversion_to_number():
    try:
        user_input1 = input("Enter text for conversion: ")
        user_input2 = input("Enter text for conversion: ")

        number1 = int(user_input1)
        number2 = int(user_input2)

        return number1, number2
    except ValueError:
        print("Error: we can't conversion it")
    finally:
        print("Conversion end")


conversion_to_number()
