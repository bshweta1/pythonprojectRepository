bill=float(input("what is the amount of the bill:\n"))
tip=int(input("how many percent tip you are giving 10,12 ,15,20:\n"))

total_person=int(input("Enter the total no of person to split the bill:\n"))
tip_percent =tip/100
total_tip_amount =bill *tip_percent
total_bill=total_tip_amount+bill
bill_per_pesron=total_bill/total_person
final_amount=round(bill_per_pesron,2)

print(f"each person should pay: ${final_amount}")