# Digital Evidence Timeline Tool (Basic)

with open("../evidence/auth.log", "r") as file:
    for line in file:
        if "Failed password" in line or "Accepted password" in line:
            print(line.strip())
