# task1: calculate how many unique names are there
person_a = input("Enter name: ")
person_b = input("Enter name: ")
person_c = input("Enter name: ")

if person_a == person_b:
    if person_b == person_c:
        num_unique = 1
    else:
        num_unique = 2
elif person_a == person_c or person_b == person_c:
    num_unique = 2
else:
    num_unique = 3

print(f"{num_unique} unique names")


# task2: calculate total tax one should pay
# this function is to calculate the federal tax part
def federaltax(income):
    if income < 0:
        print('please input a positive income')
    elif income <= 9950:
        federal_tax = income * 0.1
    elif income <= 40525:
        federal_tax = 995 + (income - 9950) * 0.12
    elif income <= 86375:
        federal_tax = 4664 + (income - 40525) * 0.22
    elif income <= 164925:
        federal_tax = 14751 + (income - 86375) * 0.24
    elif income <= 209425:
        federal_tax = 33603 + (income - 164925) * 0.32
    elif income <= 523600:
        federal_tax = 47843 + (income - 209425) * 0.35
    else:
        federal_tax = 157804.25 + (income - 523600) * 0.37
    return federal_tax

# this function is to calculate the california tax part
def caltax(income):
    if income < 0:
        print('please input a positive income')
    elif income <= 9325:
        federal_tax = income * 0.01
    elif income <= 22107:
        federal_tax = 93.25 + (income - 9325) * 0.02
    elif income <= 34892:
        federal_tax = 348.89 + (income - 22107) * 0.04
    elif income <= 48435:
        federal_tax = 860.29 + (income - 34892) * 0.06
    elif income <= 61214:
        federal_tax = 1672.87 + (income - 48435) * 0.08
    elif income <= 312686:
        federal_tax = 2695.19 + (income - 61214) * 0.093
    elif income <= 375221:
        federal_tax = 26082.09 + (income - 312686) * 0.103
    elif income <= 625369:
        federal_tax = 32523.20 + (income - 375221) * 0.113
    else:
        federal_tax = 60789.92 + (income - 625369) * 0.123
    return federal_tax

income = int(input('please input your annual income: '))

federal_tax = federaltax(income)
CA_tax = caltax(income)
income_tax = federal_tax + CA_tax
income_after_tax = income - income_tax

print(
    f'Your income is {income:.2f} before tax and {income_after_tax:.2f} after tax. You pay {income_tax:.2f} income tax.')
