# mortgage.py
#
# Exercise 1.7
debt = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment = payment + 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108


while debt > 0:
    month = month + 1
    if month >= 61 and month <= 108:
       debt = debt * (1+rate/12) - extra_payment
       total_paid = total_paid + extra_payment

    else:
        debt = debt * (1+rate/12) - payment
        total_paid = total_paid + payment
    print(total_paid, debt)


print('Total paid: ', total_paid)
print(month)
