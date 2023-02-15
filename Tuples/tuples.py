


def minimum(positions):
    a = 100
    b = 100
    for i in positions:
        if i[1] < a:
            a = i[1]
        else:
            a = a
        if i[2] < b:
            b = i[2]
        else:
            b = b
    return print(f"Les plus petites positions sont x={a} et y={b}")


position = [
    ('Bob',  0.0, 21.0),
    ('Cat',  2.5, 13.1),
    ('Dog', 33.0,  1.2)
]
f = minimum(position)
print(f)
