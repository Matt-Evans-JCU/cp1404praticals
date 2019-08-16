"""
Inputs should be:
which tariff
daily use in kWh, and
number of days in the billing period.
print price
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
print('Electricity bill estimator 2.0')
tariff_choice = int(input(' Which tariff? 11 or 31: '))
if tariff_choice == 11:
    daily_kWh = float(input('Enter daily use in kWh: '))
    billing_days = int(input('Enter number of billing days: '))
    billing_cost = (TARIFF_11*(daily_kWh*billing_days))
else:
    daily_kWh = float(input('Enter daily use in kWh: '))
    billing_days = int(input('Enter number of billing days: '))
    billing_cost = (TARIFF_31*(daily_kWh*billing_days))
print('Estimated bill: ${}'.format(billing_cost))