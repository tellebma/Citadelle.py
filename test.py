from Python.pygame import setup as f

f.screenSize(750, 750)

fuelColour = "yellow"
fuelLabel = f.makeLabel("Fuel: 50", 28, 10, 10, fuelColour)
f.showLabel(fuelLabel)


fuel = 0

while True:
    fuel += 1
    f.changeLabel(fuelLabel, "Fuel: " + str(int(fuel)), fuelColour)  # Update the label

