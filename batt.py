#!/usr/bin/env python

import subprocess

batt = {}
total_energy = 0.0

for battery in range(2):
    print("")
    print("Battery " + str(battery))
    print("=======================")
    try:
        process = subprocess.Popen("upower -i /org/freedesktop/UPower/devices/battery_BAT"+str(battery), shell=True, stdout=subprocess.PIPE)
        result = process.communicate()[0].split('\n')
    except:
        print("error getting BAT" + str(battery))

    for line in result:
        if 'state:' in line:
            batt['state'] = line.split()[1]
        if 'time to empty:' in line:
            batt['time_left'] = line.split()[3] + ' ' + line.split()[4]
        if 'percentage:' in line:
            batt['percentage'] = line.split()[1]
        if 'energy:' in line:
            batt_energy = float(line.split()[1])
            total_energy = total_energy + batt_energy
        if 'energy-rate:' in line:
            energy_rate = line.split()[1]

    for k,v in batt.items():
        print(k +  "      " + v)

print("")
print("TOTAL ENERGY: " + str(total_energy) + ' wh')
total_time = total_energy / float(energy_rate)
total_time = ("%.2f" % total_time)
print("TOTAL TIME:   " + str(total_time) + ' hours')
print("")