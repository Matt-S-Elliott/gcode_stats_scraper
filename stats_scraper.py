import glob
import os
import datetime

result = open("print_stats.csv", "w")
result.write("PR_Number,Print_Time,Print_Weight,Print_Date\n")
print("Starting...")
files = glob.glob("*.gcode")
totalFiles = str(len(files))
progress = 1
for fileName in files:
    with open(fileName) as file:
        prNumber = "not_found"
        seconds = 0
        weight = 0
        date = datetime.datetime.fromtimestamp(os.path.getmtime(fileName)).strftime("%m/%d/%Y")
        if fileName.startswith("PR-"):
            prNumber = fileName.split("_")[0][3:]
        for line in file:
            if line.startswith("; estimated printing time (normal mode) ="):
                timeEls = line.split("=")[1].strip().split(" ")
                for el in timeEls:
                    if el[-1] == "s":
                        seconds += int(el[:-1])
                    elif el[-1] == "m":
                        seconds += int(el[:-1]) * 60
                    elif el[-1] == "h":
                        seconds += int(el[:-1]) * 3600
            elif line.startswith("; total filament used [g] ="):
                weight = float(line.split("=")[1].strip())
        if seconds > 0 and weight > 0:
            result.write(str(prNumber) + "," + str(seconds) + "," + str(weight) + "," + date + "\n")
        print(str(progress) + " / " + totalFiles)
        progress += 1
        # print(prNumber)
        # print(seconds)
        # print(weight)
        # print(date)
print("Finished!")
