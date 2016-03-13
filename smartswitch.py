import sscomm, ssmenus
import time
import sscontrol
import sys, re

PORT = 5750

if "__name__" != "__main__":
    print('SmartSwitch: Connecting your home to you.\nCreated by Luke Westfall 2016\n')

    subnet = sscomm.get_subnet()
    
    while True:
        deviceIPs = []
        switches = []

        while len(deviceIPs) == 0:
            deviceIPs, deviceNames = sscomm.scan_switches(subnet)

            if len(deviceIPs) > 0:
                print("%i devices found:\n" % len(deviceIPs))
                for i in range(0, len(deviceIPs)):
                    switches.append(sscontrol.SmartSwitch(deviceIPs[i],deviceNames[i]))
                    # print(deviceIPs[i] + " : \"" + deviceNames[i] + "\"\n")
            else:
                pass
        while True:
            if len(switches) >= 1:
                options = []
                for i in range(0, len(switches)):
                    options.append(str(i + 1) + " - " + switches[i].name + " (" + switches[i].address + ")")
                options.append(str(len(switches) + 1) + " - Exit")
                command = ssmenus.selectmenu("Home", options)
                if command == len(switches) + 1:
                    sys.exit("Goodbye!")
                else:
                    switches[command - 1].control()
            else:

                rescan = raw_input("Lost connection with all devices. Rescan? (Y/n): ")

                if rescan.upper() == "N":
                    sys.exit("Goodbye!")
                else:
                   break

                print("No devices found in network on that port.\nTrying again in 5 seconds.\n\n")
                time.sleep(5)
