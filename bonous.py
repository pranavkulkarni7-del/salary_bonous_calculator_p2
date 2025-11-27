import sys

if len(sys.argv)==2:
  script_name=sys.argv[0]
  salary=float(sys.argv[1])
else:
  script_name=sys.argv[0]
  salary=10000

bonus= salary*0.10
finalSalary=bonus+salary

print(f"bonus: {bonus}\nFinal salary:{finalSalary}")
