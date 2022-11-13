
from subprocess import check_output

traces = ["traces/ls.trace", "traces/mmulijk.trace"]

BYTES = 32768
for trace in traces:
    print(f"/* {trace} */")
    print("----------------")
    for s in range(1,12+1):
        for b in range(3,14+1):
            E = BYTES / ((2**s)*(2**b))
            if E.is_integer():
                print(check_output(["./csim-ref","-s", f"{int(s)}","-b", f"{int(b)}", "-E", f"{int(E)}", "-t", trace]),end="")
                print(f" s,b,E: {s},{b},{E}")
