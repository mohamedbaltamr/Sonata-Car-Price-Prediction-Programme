import numpy as np

# futers: [Class, Year, Mileage, Engine, Sunroof, Tires]
x_raw = np.array([
    [2, 2024, 2000, 2.5, 1, 1],     [0, 2020, 98000, 2.0, 0, 0],
    [1, 2022, 45000, 2.5, 1, 0],    [2, 2019, 120000, 2.4, 1, 1],
    [0, 2021, 60000, 2.0, 0, 0],    [1, 2023, 15000, 2.5, 1, 0],
    [2, 2020, 85000, 2.5, 1, 1],    [0, 2018, 160000, 2.4, 0, 0],
    [1, 2021, 55000, 2.5, 1, 0],    [2, 2024, 1000, 2.5, 1, 1],
    [0, 2019, 110000, 2.0, 0, 0],   [0, 2020, 90000, 2.5, 1, 0],
    [2, 2022, 35000, 2.5, 1, 1],    [0, 2023, 20000, 2.0, 0, 0],
    [1, 2018, 180000, 2.4, 0, 0],   [2, 2021, 50000, 2.5, 1, 1],
    [0, 2024, 3000, 2.0, 0, 0],     [1, 2019, 130000, 2.5, 1, 0],
    [2, 2023, 12000, 2.5, 1, 1],    [0, 2022, 42000, 2.0, 0, 0],
    [1, 2024, 500, 2.5, 1, 1],      [2, 2018, 190000, 2.4, 1, 1],
    [0, 2021, 75000, 2.0, 0, 0],    [1, 2020, 105000, 2.5, 1, 0],
    [2, 2022, 28000, 2.5, 1, 1]
])

y = np.array([
    32000, 18500, 26000, 16000, 21000, 29000, 19500, 14000, 23500, 33500,
    17000, 20000, 27500, 25500, 13000, 24000, 26500, 15500, 28500, 22500,
    31500, 13500, 20500, 19000, 27000
])

#########################################################################################

mean = np.mean(x_raw, axis=0)
std = np.std(x_raw, axis=0)
x = (x_raw - mean) / std

w = np.zeros(x_raw.shape[1])
b = 0.0
alpha = 0.00001
m = len(y)
previous_cost = float('inf')

for i in range(10000000):

    fx = np.dot(x, w) + b

    errors = fx - y

    dj_dw = np.dot(x.T, errors)/m 
    dj_db = sum(errors) / m
    
    w = w - (alpha * dj_dw)
    b = b - (alpha * dj_db)

    cost = sum(errors ** 2) / (2*m)
    
    if i % 10000 == 0:
            print(f"Iteration: {i} | Cost: {cost}")

    if abs(previous_cost - cost) < 0.0000001:
        print(f"\nFinal Weights: {w}")
        print(f"Final Bias: {b}\n\n")
        break
    previous_cost = cost

######################################################################################### 
# To get number only
def get_number_only():
    while True:
        user_input = input("Enter a number : \n")
        try: return float(user_input)
        except ValueError: print("Input Error, Press Enter To re-enter")

# To display options to the user
def cop(cop_1):
    print("Choose one of the options:\n")
    for i in range(len(cop_1)):
        print(i, "- ", cop_1[i]," press (",i,")\n")
    while True:
        option_cop = get_number_only()

        if 0 <= option_cop < len(cop_1):
            return int(option_cop)

        else:
            print("Input Error, Press Enter To re-enter.")


print("Welcome to the program for predicting the price of your Sonata car !!\n")

while True :
    option = cop(["Expected price of a Sonata car", "Exit"])

    if option == 0:
        input("Press Enter to find out the price of your Sonata car :\n")

        class0 = cop(["Standard", "Mid-option", "Full Option"])

        print("Enter the car's manufacturing year :\n")
        year0 = get_number_only()

        print("Enter the distance traveled in kilometers :\n")
        mileage0 = get_number_only()

        print("Enter engine capacity in liters :\n")
        engine0 = get_number_only()

        sunroof0 = cop(["Without a Sunroof", "With a Sunroof"])

        tires0 = cop(["Plain, smooth Tires", "Sports Tires"])   


        x_chose = np.array([class0, year0, mileage0, engine0, sunroof0, tires0])
        chose = (x_chose - mean) / std
        fwb = np.dot(chose, w) + b 

        print(f"The price of the car is: {round(fwb, 1)}\n")
    else:
        break
