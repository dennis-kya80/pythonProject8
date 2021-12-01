def greetings_func(name, age):
    print("welcome " ,name, " you are " , str(age) ," years old.")
greetings_func("dennis",21)

def salary(name, basic_salary, sales):  
    if sales>=1000000:
        commission=sales*0.02
    salary = basic_salary+commission
    print(f"{name}s` salary:{salary}")
salary("dennis",100000,1500000)
salary("tumaini",1500000,50000000)