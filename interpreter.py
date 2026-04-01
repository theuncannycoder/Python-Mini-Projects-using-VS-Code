x, y, z=input("Enter your expression: ").strip().split()
x=int(x)
z=int(z)
match y:
    case "+":
        a=x+z
        print(f"{a:.1f}")
    case "-":
        a=x-z
        print(f"{a:.1f}")
    case "*":
        a=x*z
        print(f"{a:.1f}")
    case "/":
        a=x/z
        print(f"{a:.1f}")
    case _:
        print("error 404 not found")




