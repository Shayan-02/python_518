def bmi(w, h):
    b = w / (h*h)
    if b < 18.5:
        return "Underweight"
    elif b < 25:
        return "Normal"
    elif b < 30:
        return "Overweight"
    elif b >= 30:
        return "Obese"


print(bmi(70, 1.84))
