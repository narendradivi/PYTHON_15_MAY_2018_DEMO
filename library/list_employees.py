f = open(r"e:\classroom\python\employees.txt","rt")

employees = {}
for line in f.readlines():
    parts = line.split(",")
    if len(parts) < 2:
        continue

    deptid = parts[0].strip(' \n')
    empname = parts[1].strip(' \n')
    if len(deptid) == 0 or len(empname) == 0:
        continue

    if deptid in employees:
        employees[deptid].append(empname)
    else:
        employees[deptid] = [empname]


f.close()
for deptid, names in sorted(employees.items()):
    print(deptid, end = ' ')
    for n in sorted(names):
        print(n, end = ' ')

    print()




