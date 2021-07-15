from prettytable import PrettyTable

x = PrettyTable()
x.add_column("Name", ["A", "b", "c"])
x.add_column("Name", ["A", "b", "c"])

x.align = "l"

print(x)