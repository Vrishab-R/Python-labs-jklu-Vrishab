balls = input().split()
total = 0
wickets = 0
boundaries = 0
overs = []
current = 0
count = 0
for b in balls:
    if b == "W":
        wickets += 1
    else:
        runs = int(b)
        total += runs
        current += runs
        if runs == 4 or runs == 6:
            boundaries += 1
    count += 1
    if count == 6:
        overs.append(current)
        current = 0
        count = 0
if count > 0:
    overs.append(current)
print("Total Runs:", total)
print("Wickets:", wickets)
print("Boundaries:", boundaries)
print("Runs per over:", overs)
