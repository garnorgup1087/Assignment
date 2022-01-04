#taking input of gross income and number of dependents
gross_income=int(input("Enter your gross income:",))
dependents=int(input("Enter number of dependents:",))
#calculating tax of user
standard_deduction=10000
#tax_rate=20%=0.2
tax_rate=0.2
taxable_amount=gross_income-standard_deduction-(dependents*3000)
tax=taxable_amount*tax_rate
#people having taxable amount eual or less than 0 should not pay any tax
if (taxable_amount<=0):
    print("NO tax to be paid.")
else:
    print("total income tax to be paid by user:",tax)