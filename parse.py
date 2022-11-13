


with open("out.txt") as f:
    for line in f:
        if line.startswith("b'"):
            l = line.split("ratio")[1].replace(r"\n","").replace("'","").replace("%","").split()
            print(l[1], end="")
            print(f",{l[3]}")