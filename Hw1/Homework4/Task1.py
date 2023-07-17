def change_var(var_dict: dict):
    vars_to_change = [k for k in var_dict if len(k) > 1 and k[-1] == 's']
    for k in vars_to_change:
        var_dict[k[:-1]] = var_dict[k]
        var_dict[k] = None

abcde = 123
abcds = 'Test'
abc = 'teeeest'
s = 567
abcd_s = 1

all_var = globals()
print(f"{abcde = }\n{abcds = }\n{abc = }\n{s = }\n{abcd_s = }\n{all_var = }\n")

change_var(all_var)
print(f"{abcde= }\n{abcds = }\n{abc = }\n{s = }\n{abcd_s = }\n{all_var = }\n")
print(f"{abc = }\n{abcd_ = }\n")