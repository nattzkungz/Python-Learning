# import modin.pandas as md
# import ray
# ray.init(num_cpus=8)
# file = md.read_excel(r"Chula\\eew1.xlsx")
# prov = md.DataFrame(file, columns=["AccProv"])
# count = prov.count()
# print(count)

from pandas import *
xlsx = read_excel(r'Chula\\eew1.xlsx')
xl = xlsx.to_dict()

motorbike_count = xl["Vehicle"]
prov_count = xl["AccProv"]

data = {}

for i in motorbike_count:
    if motorbike_count[i] == "รถจักรยานยนต์":
        data[i] = [motorbike_count[i]]


for i in prov_count:
    if i in data:
        data[i].append(prov_count[i])

prov_vehicle = {}
for i in data:
    if data[i][1] not in prov_vehicle:
        prov_vehicle[data[i][1]] = 1
    else:
        prov_vehicle[data[i][1]] += 1

## Total Accidents in each province

total_acc = {}

for i in prov_count:
    if prov_count[i] not in total_acc:
        total_acc[prov_count[i]] = 1
    else:
        total_acc[prov_count[i]] += 1


percentage = {}
selectedProvinces = ["นครราชสีมา","ชลบุรี", "กรุงเทพมหานคร", "นครศรีธรรมราช", "ระยอง", "สงขลา", "ขอนแก่น", "เชียงราย", "เชียงใหม่", "อุบลราชธานี"]
for i in total_acc:
    if i in selectedProvinces:
        perc = round((prov_vehicle[i]/total_acc[i])*100, 1)
        percentage[i] = perc

print("Calculated Percentages for Motorbikes Accident in each Provinces are: ")

from matplotlib import pyplot as plt
import matplotlib as mpl
# mpl.font_manager.fontManager.addfont("ChulaCharasNewReg.ttf")
mpl.rc("font", family="ChulaCharasNew")
sortedPercentage = dict(sorted(percentage.items(), key=lambda item: item[1], reverse=True))
for i in sortedPercentage:
    text = str(i) +" : " +str(sortedPercentage[i]) +"%"
    print(text)

# accProv = list(sortedPercentage.keys())
# accCount = list(sortedPercentage.values())
# plt.rcParams['font.size'] = '16'
# fig = plt.figure(figsize= (10,5))
# fig.suptitle('Percentages of Motorcycle death vs total death in each provinces', fontsize=28)
# plt.bar(accProv, accCount, color="maroon", width=0.4)

# plt.xlabel("Provinces", fontsize=28)
# plt.ylabel("Percentages", fontsize=28)
# plt.show()