cost_item = float(20)
print("Cost to produce each item £" + str(cost_item))

sale_price_item = float(40)
print("The sale price per item £" + str(sale_price_item))

fixed_costs = float(50000)
print("Fixed costs £"+str(fixed_costs))

profit_per_item = float(sale_price_item-cost_item)
print("Profit per item £" + str(profit_per_item))

break_even = (fixed_costs/(sale_price_item-cost_item))
print("Breakeven £ " + str(break_even) + " items")



