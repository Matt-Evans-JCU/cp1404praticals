"""
Inputs should be:
price per kWh in cents,
daily use in kWh, and
number of days in the billing period.
print price
"""

print('Electricity bill estimator')
cents_kWh = float(input('Enter cents per kWh: '))
daily_kWh = float(input('Enter daily use in kWh: '))
billing_days = int(input('Enter number of billing days: '))
billing_cost = (cents_kWh*(daily_kWh*billing_days))/100
print('Estimated bill: ${}'.format(billing_cost))
