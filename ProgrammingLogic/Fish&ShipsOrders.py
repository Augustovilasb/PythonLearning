# Big Al’s chipper sells fish and chips to its customers. You are required do design and write a
# Python program to help with Fish and Chips orders.
# Fresh Cod Fillets sell at €7.80, and Chips sell at €3.50 per portion.
# VAT of 13.5% is included in the sale price. If you remove the VAT from the total sales price,
# then half of the remainder is profit for Big Al.

print("--Welcome to Big Al’s chipper--")
print("\t\t----MENU----\t")
print("1. Cod Fillets: €7.80")
print("2. Chips: €3.50 (Portion)")
print("All prices include VAT!")
print("")
print("Please, enter your order:")
print("")

chipsPrice = float(3.50)
CodFilletsPrice = float(7.80)
vat = float(0.135)

orderCodFillets = int(input("How many Cod Fillets would you like? "))
orderChips = int(input("How many Chips would you like? "))

CodFilletsFinalPrice = orderCodFillets * CodFilletsPrice
chipsFinalPrice = orderChips * chipsPrice

print("")
print("You have ordered", orderCodFillets, "Cod Fillets and", orderChips, "Chips.")
print("")

finalPrice = CodFilletsFinalPrice + chipsFinalPrice
print("The total order is €:", round(finalPrice,2))
print("")

priceRemovingVAT = finalPrice / (1 + vat)
calculationVAT = finalPrice - priceRemovingVAT

print("The total of VAT on this order is: €",round(calculationVAT,2))
print("")
print("The sales price without the VAT is: €", round(priceRemovingVAT,2))
print("")
totalBigProfit = priceRemovingVAT / 2
print("The total Big's profit is: €", round(totalBigProfit,2))