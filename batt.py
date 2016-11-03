#!/usr/bin/env python

import subprocess

batt = {}
total_energy = 0.0
total_time = 0.0
cmd = "upower -i /org/freedesktop/UPower/devices/battery_BAT"

for b in range(2):
    print("")
    print("Battery " + str(b))
    print("=======================")
    try:
        p = subprocess.Popen(cmd + str(b), shell=True, stdout=subprocess.PIPE)
        result = p.communicate()[0].split('\n')
    except:
        print("error getting BAT" + str(b))

    for line in result:
        if 'state:' in line:
            batt['status   '] = line.split()[1]
        if 'time to empty:' in line:
            batt['time_left'] = line.split()[3] + ' ' + line.split()[4]
        if 'percentage:' in line:
            batt['percentage'] = line.split()[1]
        if 'energy:' in line:
            batt_energy = float(line.split()[1])
            total_energy = total_energy + batt_energy
            batt['energy'] = '   ' + str(batt_energy) + 'wh'
        if 'energy-rate:' in line:
            energy_rate = line.split()[1]
            batt['power rate'] = energy_rate + ' w'

    for k, v in batt.items():
        print(k + "      " + v)

print("")
print("TOTAL ENERGY: " + str(total_energy) + ' wh')
if total_time > 0:
    total_time = total_energy / float(energy_rate)
else:
    total_time = total_energy / 7.0
total_time = ("%.2f" % total_time)
print("TOTAL TIME:   " + str(total_time) + ' hours')
print("")
