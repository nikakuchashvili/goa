a = 5
b = 3

sum = 5 + b
print(sum)



#  Python-ში ტიპის კონვერტაციის ორი ტიპი არსებობს: იმპლიციტური კონვერტაცია: Python კოდის გაშვებისას მონაცემთა
#  ტიპს თავისით ცვლის, შეცდომების ან მონაცემთა დაკარგვის თავიდან ასაცილებლად. ექსპლიციტური კონვერტაცია: მონაცემთა
#  ტიპს შეგნებულად ცვლით ისეთი ფუნქციების გამოყენებით, როგორიცაა



a = float(input("14: "))
b = float(input("71: "))

print("შენი შეტანილი რიცხვებია:", a, "და", b)


# მომხმარებელს შემოატანინეთ ორი მთელი რიცხვი
num1 = int(input("8: "))
num2 = int(input("14: "))

# ვამოწმებთ, ორივე რიცხვი ლუწია თუ არა
if num1 % 2 == 0 and num2 % 2 == 0:
    result = num1 + num2
    print("ორივე რიცხვი ლუწია, მათი ჯამი არის:", result)
else:
    print("The given numbers are not even so they will not be summed")


    name = input("ნიკა: ")
surname = input("კუჭაშვილი: ")
age = input("15: ")
city = input("ბოლნისი: ")
country = input("საქართველო: ")

# შედეგის გამოტანა
print("\nშენი მონაცემებია:")
print("სახელი:", name)
print("გვარი:", surname)
print("ასაკი:", age)
print("ქალაქი:", city)
print("ქვეყანა:", country)