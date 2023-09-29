#FIND_ELECTRICITY_BILL
print("   if unit 0 - 200 = Rs  0.50 per unit \n   if unit 201 - 400 = Rs 100 + Rs 0.80 per unit excess of 200 \n   if unit 401 - 600 = Rs 230 + Rs 0.90 per unit excess of 400 \n   if unit greater than 600 = Rs 390 + Rs 1 per unit excess of 600 ")

c_no=123

c_na="anbu"

anbu=1500 

no=int(input("enter custmer i'd:"))

if c_no==no:

	print( "Name:",c_na, '\n' "last  reading:",anbu,"Units")

	tr=int(input("enter recent reading:"))

	charge=tr-anbu

	print("consumption:", charge,"Units")

	if charge<=200:

		print( "Total_amount= Rs.",charge*0.50)

	elif charge<=400:

		print("Total_amount=Rs.",charge*0.80+100)

	elif charge<=600:

		print("Total_amount=Rs.",charge*0.90+230)

	else:

		print("Total_amount=Rs.",charge*1+390)

else:

	print("incorrect custmer i'd")



