def sum_calc(*args):
    total=0
    for items in args:
        total += items
    return total

l1=[1,2,3]
l2=[2,4,8,10]
l3=[-3,4,0,13,-25]

l1_sum= sum_calc(*l1)
l2_sum= sum_calc(*l2)
l3_sum= sum_calc(*l3)

print(f"l1_Sum: {l1_sum} l2_sum: {l2_sum} l3_sum: {l3_sum}")