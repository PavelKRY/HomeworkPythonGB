names = ["John", "Piter", "Jack"]
base_salary = [1000, 1200, 700]
bonus = ["10%", "12.5%", "7.5%"]
print({name: int(sal) / 100 * float(per[:-1]) for name, sal, per in zip(names, base_salary, bonus)})