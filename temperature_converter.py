print("---Temperture---")
C_to_F ="1.Цельсээс Фаренгейтрүү "
print(C_to_F)
F_to_C ="2.Фаренгейтээс Цельсрүү"
print(F_to_C)
C_to_K ="3.Цельсээс Кельвинрүү "
print(C_to_K)
K_to_C ="4. Кельвиээс Цельсрүү "
print(K_to_C)
F_to_K ="5. Фаренгейтээс Кельвинрүү "
print(F_to_K)
K_to_F ="6. Кельвиээс Фаренгейтрүү "
print(K_to_F)

hurvuuleh_utag = input("Xo")
print("Hurvuuleh utga:" +hurvuuleh_utag)
temp_num = int(input("Температурын утга:"))


hario=0
if hurvuuleh_utag == "1":
    hario =(float(temp_num *9/5) +32)
elif hurvuuleh_utag =="2":
    hario =(float(temp_num) +32) *5/9
elif hurvuuleh_utag =="3":
    hario =(float(temp_num)) +273.15 
elif hurvuuleh_utag =="4":
    hario =(float(temp_num)) -273
elif hurvuuleh_utag =="5":
    hario =(float(temp_num) +459.67)*5/9
elif hurvuuleh_utag =="6":
    hario =(float(temp_num)) *9/5 -459.67              

    print(f"hariu ni:{hario}")