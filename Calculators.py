# The formula is BMI = kg/m2 where kg is a person's weight in kilograms and m2 is their height in metres squared.
def calculate_bmi1(kg, m):
    kg = float(kg)
    m = float(m)
    bmi = kg / (m * m)
    return format(bmi, '.2f')


# When using English measurements, pounds should be divided by inches squared.
# This should then be multiplied by 703 to convert from lbs/inches2 to kg/m2.

def calculate_bmi2(lb, inch):
    lb = float(lb)
    inch = float(inch)
    bmi = 703 * (lb / (inch * inch))
    return round(bmi, 2)


def convert_lb2kg(lb):
    lb = float(lb)
    kg = lb * 0.45359237
    return round(kg, 2)


def convert_kg2lb(kg):
    kg = float(kg)
    lb = kg * 2.20462
    return round(lb, 2)


def interpret_bmi(bmi):
    interpret = str
    if bmi.get() < 18.5:
        interpret = "Underweight"
    elif 18.5 <= bmi.get() <= 29.9:
        interpret = "Normal or Healthy Weight"
    elif 25.0 <= bmi.get() <= 29.9:
        interpret = "Overweight"
    elif bmi.get() >= 30.0:
        interpret = "Obese"
    return interpret


print(calculate_bmi1(95, 1.72))
print(calculate_bmi2(204, 68))
print(convert_lb2kg(204))
print(convert_kg2lb(85))
