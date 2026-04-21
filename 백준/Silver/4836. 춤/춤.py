import sys

input = sys.stdin.readline

while True:
    dance = list(input().strip().split())

    if dance == []:
        break

    violations = set()
    for i in range(len(dance)):
        step = dance[i]

        if step == "dip":
            is_valid = False

            if ((i >= 1 and dance[i-1] == "jiggle") or (i >= 2 and dance[i-2] == "jiggle")):
                is_valid = True
            elif (i <= len(dance) - 2 and dance[i+1] == "twirl"):
                is_valid = True
            
            if not is_valid:
                violations.add(1)
                dance[i] = "DIP"
        
    if len(dance) < 3 or dance[-3::] != ["clap", "stomp", "clap"]:
        violations.add(2)

    if "twirl" in dance and "hop" not in dance:
        violations.add(3)

    if dance[0] == "jiggle":
        violations.add(4)

    if "dip" not in dance and "DIP" not in dance:
        violations.add(5)

    violations = sorted(list(violations))
    violations = list(map(str, violations))
    if not violations:
        print("form ok:", ' '.join(dance))
    elif len(violations) == 1:
        print(f"form error {violations[0]}:", ' '.join(dance))
    else:
        print(f"form errors {', '.join(violations[:-1])} and {violations[-1]}:", ' '.join(dance))