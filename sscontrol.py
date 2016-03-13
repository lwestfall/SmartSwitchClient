import sscomm
import ssmenus, time

class SmartSwitch:
    """ Object class for the switch devices """

    def __init__(self, address, name):
        self.address = address
        self.name = name
        #self.state = sscomm.get_state(address)
        self.state = False
        self.sync_time()

    def control(self):
        command = 0
        while command != 4:
            options = ["1 - Switch On", 
                        "2 - Switch Off",
                        "3 - Flash", 
                        "4 - Back"]
            command = ssmenus.selectmenu(self.name + " (" + self.address + ")", options)
            #holdon = input("Command given = " + str(command))
            if command == 1:
                self.toggle_on()
            elif command == 2:
                self.toggle_off()
            elif command == 3:
                self.flash()

    def toggle_state(self):
        sscomm.toggle_state(self.address)

    def toggle_on(self):
        sscomm.toggle(self.address, "ON")
    def toggle_off(self):
        sscomm.toggle(self.address, "OFF")
    def current_state(self):
        pass
    def flash(self):
        interval = float(ssmenus.inputmenu(self.name + " (" + self.address + ")",
                                           "Enter a time interval in seconds: "))
        duration = float(ssmenus.inputmenu(self.name + " (" + self.address + ")",
                                           "Enter a duration in seconds: "))
        endtime = time.time() + duration
        currenttime = time.time()
        while currenttime <= endtime:
            sscomm.toggle(self.address,"ON")
            time.sleep(interval)
            sscomm.toggle(self.address,"OFF")
            time.sleep(interval)
            currenttime = time.time()
    def sync_time(self):
        pass    
    def timed_toggle(self, switch_time, on_off_toggle="toggle"):
        pass

