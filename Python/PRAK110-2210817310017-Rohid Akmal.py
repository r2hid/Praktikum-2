import math
sisiA = 12
sisiC = 5
sisiB = sisiA**2 + sisiC**2
sisiB = round(math.sqrt(sisiB))
kelilingSegtiga = sisiA + sisiB + sisiC
luasSegitiga = 0.5 * sisiA * sisiC

print("Diketahui :")
print("Alas =", sisiC, "cm")
print("Tinggi =", sisiA, "cm\n")
print("Jawab :")
print("Sisi A =", sisiA,"cm")
print("Sisi B =", sisiB,"cm")
print("Sisi C =", sisiC,"cm")
print("Keliling =", kelilingSegtiga, "cm")
print("Luas =", round(luasSegitiga), "cm")