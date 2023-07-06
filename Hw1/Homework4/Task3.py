def params_to_dict(**kwargs):
    res = {}
    for k, v in kwargs.items():
        if v.__hash__:
            res[v] = k
        else:
            res[v.__str__()] = k
    return res


print(params_to_dict(b=2, a=1, c=[111]))