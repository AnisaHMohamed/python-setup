# string manipulation for parsing csv
problems = "broke, pale, short, nerdy"
print(problems)
# split on comma which is the delimiter
l = problems.split(", ")
print(l)
# join
joined = ' and '.join(l)
print(joined)

# join
csv = ','.join(l)
print(csv)
# split on word which is the delimiter
l = problems.split("short")
print(l)
