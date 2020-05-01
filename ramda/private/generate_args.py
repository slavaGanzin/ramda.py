def generate_args(args, n):
    n_original = len(args)
    add_args = ["None"] * (len(args) - n)
    args.extend(["x" + str(i) for i in range(0, n - len(args))])
    args2 = args[0 : min(n, n_original)] + add_args
    return ", ".join(args[0:n]), ", ".join(args2)
