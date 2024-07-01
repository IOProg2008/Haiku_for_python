def pars(in_string):
    m = in_string.split("\n")
    f = {}
    for i in m:
        n = i.split("=")
        a = n[0]
        b = n[1]
        f[a] = b
    return f


def reed(in_string):
    out_dict = pars(in_string)
    f = {}
    out_dict_keys = out_dict.keys()
    for i in out_dict_keys:
        if out_dict[i][0] == '*':
            l = out_dict[i]
            ls = l.replace('*', '')
            f[i] = ls.split(",")
        else:
            f[i] = out_dict[i]
    return f
