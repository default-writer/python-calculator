ops = ()
s = []
o = {
    "+": lambda x: (s.pop() if len(s) > 0 else 0) + x,
    "-": lambda x: (s.pop() if len(s) > 0 else 0) - x,
    "*": lambda x: (s.pop() if len(s) > 0 else 0) * x,
    "/": lambda x: (s.pop() if len(s) > 0 else 0) / x if x > 0 else 0,
}
f = ":"
while True:
    op = input(f"{f} ").strip()
    if op == "":
        break
    for ch in op.split():
        if op == "?":
            print(f, *s)
            continue
        func = o[ch] if ch in o.keys() else None
        s.append(func(s.pop() if len(s) > 0 else 0) if func else float(ch))
