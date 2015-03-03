

.. _batinfo:

===================
Batinfo
===================


.. seealso::

   - http://blog.nicolargo.com/2013/06/6934.html
   - https://github.com/nicolargo/batinfo


.. contents::
   :depth: 3

Description
============

Is a simple Python lib to retreive battery information on Linux based 
operating system.

No ACPI or external software is needed.

Only the Linux kernel and its /sys/class/power_supply folder.

A simple example says better than words:

    In [1]: import batinfo
    In [2]: bat = batinfo.batteries()
    In [3]: bat
    Out[3]: <batinfo.battery.batteries at 0x31c87d0>
    In [4]: bat.stat
    Out[4]: [{"status": "Full", "capacity": 50, "name": "CMB1", "uevent": "POWER_SUPPLY_NAME=CMB1\nPOWER_SUPPLY_STATUS=Full\nPOWER_SUPPLY_PRESENT=1\nPOWER_SUPPLY_TECHNOLOGY=Li-ion\nPOWER_SUPPLY_CYCLE_COUNT=0\nPOWER_SUPPLY_VOLTAGE_MIN_DESIGN=10800000\nPOWER_SUPPLY_VOLTAGE_NOW=12496000\nPOWER_SUPPLY_CURRENT_NOW=0\nPOWER_SUPPLY_CHARGE_FULL_DESIGN=5800000\nPOWER_SUPPLY_CHARGE_FULL=5800000\nPOWER_SUPPLY_CHARGE_NOW=3900000\nPOWER_SUPPLY_CAPACITY=100\nPOWER_SUPPLY_MODEL_NAME=CP293550-01\nPOWER_SUPPLY_MANUFACTURER=Fujitsu\nPOWER_SUPPLY_SERIAL_NUMBER=01A-Z100320001158Z", "alarm": 0, "charge_full": 5800000, "voltage_now": 12496000, "serial_number": "01A-Z100320001158Z", "cycle_count": 0, "current_now": 0, "charge_now": 3900000, "voltage_min_design": 10800000, "path": "/sys/class/power_supply/CMB1", "technology": "Li-ion", "manufacturer": "Fujitsu", "type": "Battery", "model_name": "CP293550-01", "present": 1, "charge_full_design": 5800000}]
    In [6]: bat.stat[0]
    Out[6]: {"status": "Full", "capacity": 100, "name": "CMB1", "uevent": "POWER_SUPPLY_NAME=CMB1\nPOWER_SUPPLY_STATUS=Full\nPOWER_SUPPLY_PRESENT=1\nPOWER_SUPPLY_TECHNOLOGY=Li-ion\nPOWER_SUPPLY_CYCLE_COUNT=0\nPOWER_SUPPLY_VOLTAGE_MIN_DESIGN=10800000\nPOWER_SUPPLY_VOLTAGE_NOW=12496000\nPOWER_SUPPLY_CURRENT_NOW=0\nPOWER_SUPPLY_CHARGE_FULL_DESIGN=5800000\nPOWER_SUPPLY_CHARGE_FULL=5800000\nPOWER_SUPPLY_CHARGE_NOW=3900000\nPOWER_SUPPLY_CAPACITY=100\nPOWER_SUPPLY_MODEL_NAME=CP293550-01\nPOWER_SUPPLY_MANUFACTURER=Fujitsu\nPOWER_SUPPLY_SERIAL_NUMBER=01A-Z100320001158Z", "alarm": 0, "charge_full": 5800000, "voltage_now": 12496000, "serial_number": "01A-Z100320001158Z", "cycle_count": 0, "current_now": 0, "charge_now": 3900000, "voltage_min_design": 10800000, "path": "/sys/class/power_supply/CMB1", "technology": "Li-ion", "manufacturer": "Fujitsu", "type": "Battery", "model_name": "CP293550-01", "present": 1, "charge_full_design": 5800000}
    In [7]: bat.stat[0].capacity
    Out[7]: 50
    In [8]: print bat.stat[0]
    100
    In [9]: bat.stat[0].manufacturer
    Out[9]: 'Fujitsu'
    In [9]: bat.stat[0].technology
    Out[9]: 'Li-ion'
    In [11]: bat.stat[0].charge_full
    Out[11]: 5800000
    In [12]: bat.stat[0].charge_now
    Out[12]: 3900000
    In [12]: bat.update()
    > Refresh the stats

Have fun...


Source code
===========

.. seealso::

   - https://github.com/nicolargo/batinfo


::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #
    # Batinfo
    # A simple Python lib to retreive battery information
    #
    # Copyright (C) 2013 Nicolargo <nicolas@nicolargo.com>
    #
    # BatInfo is free software; you can redistribute it and/or modify
    # it under the terms of the GNU Lesser General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.
    #
    # BatInfo is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    # GNU Lesser General Public License for more details.
    #
    # You should have received a copy of the GNU Lesser General Public License
    # along with this program. If not, see <http://www.gnu.org/licenses/>.

    import os
    import logging
    import json

    logging.basicConfig()
    log = logging.getLogger(__name__)


    class battery(object):
        """
        Battery stats
        """

        def __init__(self, path="/sys/class/power_supply", name="BAT0"):
            self.path = os.path.join(path, name)
            self.name = name
            self.__update__()

        def __str__(self):
            self.__update__()
            return str(self.capacity)

        def __repr__(self):
            self.__update__()
            return json.dumps(self, default=lambda o: o.__dict__)

        def __getattr__(self, stat):
            """
            Catch message if attribute did not exist
            """
            log.critical("Attribute %s did not exist" % stat)
            return ""

        def __get_stat__(self, stat):
            """
            Read stat from the Linux kernel
            """
            try:
                with open(os.path.join(self.path, stat), 'r') as f:
                    return f.read().strip()
            except Exception:
                log.critical("Can not read file %s" % stat)
                return ""

        def __update__(self):
            """
            Update the stats
            """
            # Get all file in the battery system folder
            stats = [f for f in os.listdir(self.path)
                     if os.path.isfile(os.path.join(self.path, f))]
            for stat in stats:
                # print("%s = %s" % (stat, self.__get_stat__(stat)))
                value = self.__get_stat__(stat)
                try:
                    # Try to convert to integer
                    value = int(value)
                except ValueError:
                    # Not possible, not a problem
                    pass
                setattr(self, stat, value)


    class batteries(object):
        """
        Class to retreive stats of all the batteries
        List of battery (class)
        """

        def __init__(self, bat_root_path="/sys/class/power_supply"):
            # Root path for batteries stats
            self.bat_root_path = bat_root_path
            # Update stat
            self.update()

        def update(self):
            # Init the batteries stat list
            self.stat = []
            # and update it...
            # Find all the batteries in the bat_root_path folder
            # It's a battery if the file "type" exist
            # and contain "Battery"
            for dirname in os.listdir(self.bat_root_path):
                type_file = os.path.join(self.bat_root_path, dirname, "type")
                if (os.path.isfile(type_file)):
                    try:
                        with open(type_file, 'r') as f:
                            is_bat = (f.read().strip() == "Battery")
                    except Exception:
                        log.critical("Can not read file %s" % type_file)
                    if (is_bat):
                        # It is a battery, let's add it to the list
                        # print("Add the battery %s to the list" % dirname)
                        self.stat.append(battery(self.bat_root_path, dirname))

        def __len__(self):
            return len(self.stat)
