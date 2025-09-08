# Function to return patterns row by row
def get_U(ch):
    return [
        f"{ch}   {ch}",
        f"{ch}   {ch}",
        f"{ch}   {ch}",
        f"{ch}   {ch}",
        f" {ch*3} "
    ]

def get_R(ch):
    return [
        f"{ch*4}",
        f"{ch}  {ch}",
        f"{ch*4}",
        f"{ch}{ch}  ",
        f"{ch}  {ch}"
    ]

def get_V(ch):
    return [
        f"{ch}     {ch}",
        f" {ch}   {ch} ",
        f"  {ch} {ch}  ",
        f"   {ch}{ch}   ",
        f"    {ch}    "
    ]

def get_A(ch):
    return [
        f" {ch*3} ",
        f"{ch}   {ch}",
        f"{ch*5}",
        f"{ch}   {ch}",
        f"{ch}   {ch}"
    ]

def get_L(ch):
    return [
        f"{ch}",
        f"{ch}",
        f"{ch}",
        f"{ch}",
        f"{ch*4}"
    ]

# Collect patterns
U = get_U('@')
R = get_R('#')
V = get_V('$')
A = get_A('&')
L = get_L('*')

# Print row by row (landscape style)
for i in range(5):
    print(U[i], " ", R[i], " ", V[i], " ", A[i], " ", L[i])
