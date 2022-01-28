s = []
o = {
    "+": lambda x: x + s.pop(),
    "-": lambda x: x - s.pop(),
    "*": lambda x: x * s.pop(),
    "/": lambda x: x / s.pop(),
}
while True:
    op = input(f": ").strip()
    if op == "":
        break
    for arg in op.split():
        if op == "?":
            print(f":", *s)
            continue
        func = o[arg] if arg in o.keys() else None
        try:
            s.append(float(func(s.pop()) if func else arg))
        except:
            s.clear()
            pass

