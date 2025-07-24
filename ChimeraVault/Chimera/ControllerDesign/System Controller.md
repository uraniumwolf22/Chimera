
# Required Relays
PV Disconnect
Main Battery Disconnect Remote
Truck Battery Disconnect Remote
12V Regulator Disconnect
AC Inverter Disconnect
Shore power disconnect
# Inputs/Outputs
Shore 12V DC+/DC-    --Provides Power to onboard systems from vehicle battery's or 120v plug
PV DC+/DC-    -Provides power from solar panels
Habitat battery +/-    --Used for charging and discharging Habitat battery
Truck battery DC+/DC- --Used for jumping truck or backup habitat power
Inverter output DC+/DC-    --Used to power AC inverter
12V Regulator output DC+/DC-    --Used to power Auxiliary 12v systems
24V Output
I2C Bus out +5V
SPI Bus out
DB9 serial connector

# Connector requirements
4x 14 Gauge wires Shore power
4x 14 Gauge wires 12v PV
4x 14 Gauge wires Truck battery connection

4x 14 Gauge wires 12v Battery output
4x 14 Gauge wires Habitat Battery

4x I2C Bus with power gauge can be any
1x DB9 connector
# Primary Vehicle Monitoring
- Primary Systems
	- Monitor Battery voltage
	- Monitor Oil pressure
	- Monitor Coolant Temperature
	- Monitor Engine RPM


- Secondary Systems
	- Monitor AFR
	- Monitor Head Temperature
	- Monitor Oil Temperature
	- Fuel level

- General Recording
	- Engine Hours
	- Miles Traveled
	- Maintenance counters Oil/Bearings/General Lubrication based on TM



# Shelter monitoring
- Primary systems
	- Monitor Habitat Battery Voltage
	- Control Charging from Main Batteries
	- Control Charging From Photovoltaic System
	- Control power flow to devices

- Secondary Systems
	- Diesel Level
	- PV Voltage Monitoring
	- Hab Temperature Control
	- Hab temperature Monitoring