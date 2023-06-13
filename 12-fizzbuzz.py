def fizzbuzz():
    for i in range(1, 101):
        if (i % 10 == 0 or i % 10 == 5) and i % 3 == 0:
            print("FizzBuzz ", end= '')
        elif i % 3 == 0: 
            print("Fizz ", end= '')
        elif i % 10 == 0 or i % 10 == 5:
            print("Buzz ", end= '')
        else:
            print(f"{i} ", end= '')