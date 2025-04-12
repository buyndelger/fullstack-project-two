print("-Calculaator-")
ehnii_too = int(input("Ehnii too:"))
hoyrdoh_too= int(input("hoyrdoh_too:"))
nemeh = "nemeh"
print(nemeh)
xasah = "xasah"
print(xasah)
urjih= "urjih"
print(urjih)
xuvaah= "xuvaah"
print(xuvaah)
zeregt_devshuuleh = "zeregt_devshuuleh "
print(zeregt_devshuuleh )
kvadrat_yzguur= "kvadrat_yzguur"
print(kvadrat_yzguur)
uldegdel = "uldegdel"
print(uldegdel)
songoson_uildel= input("uildelee songoorei:")
print("{songoson_uildel}:")
import math
if songoson_uildel == "nemeh":
    hariu = ehnii_too + hoyrdoh_too
elif songoson_uildel == "hasah":
    hariu = ehnii_too - hoyrdoh_too
elif songoson_uildel == "urjih":
    hariu = ehnii_too * hoyrdoh_too
elif songoson_uildel == "xuvaah":
    if hoyrdoh_too !=0:
          hariu = ehnii_too // hoyrdoh_too
    else:
          hariu = "toog 0d xuvaaj bolohgui"
elif songoson_uildel == "zeregt_devshuuleh":
    hariu = ehnii_too ** hoyrdoh_too
elif songoson_uildel == "kvadrat_yzguur":
    hariu = math.sqrt(ehnii_too), math.sqrt(hoyrdoh_too)
elif songoson_uildel == "uldegdel ":
    hariu = ehnii_too / hoyrdoh_too
else:
    hariu = "iim uildel baihgui"
print(f"Hariu :{hariu}")    


