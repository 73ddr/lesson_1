a = int(input("enter number of months (1 to 12)" ))
months_list = ["spring", "summer", "autumm", "winter"]
while True:
     if 2 < a < 6:
         print(months_list[0])
     elif 5 < a < 9:
         print(months_list[1])
     elif 8 < a < 12:
         print(months_list[2])
     else:
         print(months_list[3])
     break

a = input("enter number of months (1 to 12) ")
M_dict = {"3": spring, "4": spring, "5": spring, "6": summer, "7": summer, "8": summer, "9": autumm, "10": autumm, "11": autumm, "12": winter, "1": winter, "2": winter}
print(M_dict[a])
