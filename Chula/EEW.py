# import modin.pandas as md
# import ray
# ray.init(num_cpus=8)
# file = md.read_excel(r"Chula\\eew1.xlsx")
# prov = md.DataFrame(file, columns=["AccProv"])
# count = prov.count()
# print(count)

from pandas import *
xlsx = read_excel('Chula\\eew1.xlsx')
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
for i in percentage:
    print(i, percentage[i])