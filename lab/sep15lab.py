# calculate total tax one should pay (with the income between 10,000 and 20,000)

income = 12000    # must between 10,000 and 20,000

federal_tax = 995 + (income - 9950)*0.12
CA_tax = 93.25 + (income - 9325)*0.02
income_tax = federal_tax + CA_tax
income_after_tax = income - income_tax

print(f'Your income is {income} before tax and {income_after_tax} after tax. You pay {income_tax} income tax.')


