
call_rate = 0.15
vat_rate = 20

minutes= float(input("Enter number of minutes: "))

minutes_used = minutes
basic_call_charge = minutes_used * call_rate
vat_due = basic_call_charge/100*vat_rate
total_bill = basic_call_charge + vat_due

print("Number of minutes used: {:.2f} ".format(minutes_used))
print("Basic call charge: £ {:.2f} " .format(basic_call_charge))
print("Vat due: £ {:.2f} " .format(vat_due))
print("Total bill: £ {:.2f}" .format(total_bill))


