name = input("Enter your name: ")
print(f'Hi {name}, please enter your marks')
marks = int(input("Marks: "))


def did_pass():
    while marks >= 35:
        did_pass = True
        print("Congratulations You have passed!")
        break
    else:
        did_pass = False
        print("You have failed!")


did_pass()
if marks >= 85:
    print('Congratulations you have passed with FCD')