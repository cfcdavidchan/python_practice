def solve_runes(runes):
    import re
    import operator as op

    parse_op = re.compile(r"(-?[0-9?]+)([-+*])(-?[0-9?]+)(=)(-?[0-9?]+)")  # For parsing the LHS.
    ops = {"*": op.mul, "+": op.add, "-": op.sub}
    search = set("0123456789") - set(c for c in runes if c.isnumeric())
    num1, op, num2, x, answer = parse_op.search(runes).groups()
    all_num = [num1, num2, answer]

    if any(len(x) > 1 and x[0] == "?" for x in all_num):
        search -= {"0"}
    for i in sorted(search):
        v = [int(num.replace('?', str(i))) for num in all_num]
        if ops[op](v[0], v[1]) == int(v[2]):
            return int(i)
    return int(-1)