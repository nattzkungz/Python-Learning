import modin.pandas as md
import ray
from matplotlib import pyplot as plt
import matplotlib as mpl
ray.init(num_cpus=8)
accData = md.read_excel(r"Chula\EEW (Data Sci)\Road fatality\accidentsData.xlsx")
accDataDict = accData.to_dict()
popData = md.read_excel(r"Chula\EEW (Data Sci)\Road fatality\populationData.xlsx")
popDataDict = popData.to_dict()

totalPopProv = popDataDict["จำนวนประชากรทั้งหมด"]
provCode = popDataDict["ชื่อจังหวัด"]
totalAccProv = accDataDict["AccProv"]
vehicleType = accDataDict["Vehicle"]

# Select only motorbike
data = {}

for i in vehicleType:
    if vehicleType[i] == "รถจักรยานยนต์":
        data[i] = [vehicleType[i]]


for i in totalAccProv:
    if i in data:
        data[i].append(totalAccProv[i])

prov_vehicle = {}
for i in data:
    if data[i][1] == "nan":
        pass
    elif data[i][1] not in prov_vehicle:
        province = str(data[i][1]).strip()
        prov_vehicle[province] = 1
    else:
        province = str(data[i][1]).strip()
        prov_vehicle[data[i][1]] += 1

# Find Province Code
provCodeNoJungwat = {}
for i in provCode:
    provCodeNoJungwat[i] = provCode[i].removeprefix("จังหวัด").strip()

totalPopProvFinal = {}
for i in totalPopProv:
    totalPopProvFinal[provCodeNoJungwat[i]] = int(totalPopProv[i])

# Find percentage of motorbike accidents per province

percentages = {}
selectedProvinces = ["นครราชสีมา","ชลบุรี", "กรุงเทพมหานคร", "นครศรีธรรมราช", "ระยอง", "สงขลา", "ขอนแก่น", "เชียงราย", "เชียงใหม่", "อุบลราชธานี"]
for i in prov_vehicle:
    if i not in selectedProvinces:
        pass
    else:
        prov = i.strip()
        percentage = prov_vehicle[i]/totalPopProvFinal[prov]
        percentages[i] = round(percentage * 100, 2)

## Plotting graph
mpl.rc("font", family="ChulaCharasNew")
sortedPercentage = dict(sorted(percentages.items(), key=lambda item: item[1], reverse=True))
print("== Calculated Percentages ==")
for i in sortedPercentage:
    text = str(i) +" : " +str(sortedPercentage[i]) +"%"
    print(text)

accProv = list(sortedPercentage.keys())
accCount = list(sortedPercentage.values())
plt.rcParams['font.size'] = '16'
fig = plt.figure(figsize= (10,5))
fig.suptitle('Percentages of Motorcycle death vs total population in each provinces', fontsize=28)
plt.bar(accProv, accCount, color="maroon", width=0.4)

plt.xlabel("Provinces", fontsize=28)
plt.ylabel("Percentages", fontsize=28)
plt.show()