sekonds = int(input("number of sekonds:  "))
hours = sekonds // 3600
minutes = (sekonds - hours * 3600) // 60
sekonds = sekonds - (hours * 3600 + minutes * 60)

print(f"H:{hours} M:{minutes} S:{sekonds}")