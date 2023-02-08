# Program to input marks of five subjects. Calculate percentage and grade.

m1 = int(input("Enter Physics Mark : "))
m2 = int(input("Enter Chemistry Mark : "))
m3 = int(input("Enter Biology Mark : "))
m4 = int(input("Enter Maths Mark : "))
m5 = int(input("Enter Computer Mark : "))
per = ((m1+m2+m3+m4+m5)/500) * 100
print("Percentage : ",per,"%")
if per > 100:
    print("You have entered an Invalid Mark")
elif per >= 90 and per <= 100:
    print("Grade : A")
elif per >= 80:
    print("Grade : B")
elif per >= 70:
    print("Grade : C")
elif per >= 60:
    print("Grade : D")
elif per >= 40:
    print("Grade : E")
elif per < 40:
    print("Grade : F")
