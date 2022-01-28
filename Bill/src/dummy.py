def fnc_seven_args(a, b, c, d, e, f, g):
    return a + b + c + d + e + f + g

def fnc_nested_ifs():
    if 1 < 2:
        if 2 < 3:
            if 3 < 4:
                if 4 < 5:
                    if 5 < 6:
                        print("DevOps is fun")

def fnc_many_return_statements(x, y, z, w):
    return x + y, x + y + z, x + y + z + w, x - y, x - y - z, x - y - z - w, x*y, x*y*z, x*y*z*w

print(fnc_seven_args(1, 2, 3, 4, 5, 6, 7))
fnc_nested_ifs()
print(fnc_many_return_statements(6, 9, 13, 88))