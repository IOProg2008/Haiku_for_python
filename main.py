def pars(in_string):
        m=in_string.split("\n")
        f={}
        for i in m:
           n=i.split("=")
           a=n[0]
           b=n[1]
           f[a]=b
        return f

# def reed(in_string):
#     out_dict=pars(in_string)
#     out_dict_keys=out_dict.keys()

