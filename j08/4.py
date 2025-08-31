c = 50

for i in range(1, 6):
    guess = int(input(f"enter choice{i}: "))
    if guess == c:
        print("mashallah")
        break
    elif guess < c:
        print("kemeh")
    else:
        print("ziadeh")
else:
    print("bakhti")