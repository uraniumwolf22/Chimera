    
C9 1x 461 T/S switch relay
C10 1x 15 Main feed

# Driver Headlight

| Pin | Wire # | Function  |
| --- | ------ | --------- |
| 1   | 91     | GND       |
| 2   | 18     | LOW BEAM  |
| 3   | 17     | HIGH BEAM |

# Passenger Headlight

| Pin | Wire # | Function  |
| --- | ------ | --------- |
| 1   | 91     | GND       |
| 2   | 18     | LOW BEAM  |
| 3   | 17     | HIGH BEAM |
# Main headlights wiring scheme
Both sides have one primary connector near the headlight itself.  Both headlights have individual grounds running through the firewall.  Terminated at the grounding block.  The HIGH BEAM and LOW BEAM connections are joined right next to the driver firewall entrance.  After this they both make their way down the wheel well into the HIGH and LOW beam floor switch.  This switch is fed 24v from the Main light switch pin M-Wire#16-"Headlight Dimmer sw" at the dash.  This is an isolated harness from any others.  The passenger headlight has 2 connectors to act as an extension due to wire being too short.

# Passenger turn signal
(Needs revision)

| Pin | Wire # | Function         |
| --- | ------ | ---------------- |
| 1   | 24     | Turn signal      |
| 2   | 22     | Black out marker |
| 3   | 21     | Parking light    |
# Driver turn signal
(Needs revision)

| Pin | Wire # | Function         |
| --- | ------ | ---------------- |
| 1   | 24     | Turn Signal      |
| 2   | 22     | Parking light    |
| 3   | 21     | Black out marker |


# Instrument panel wiring scheme
Each gauge receives its power from a junction originating at the panel itself.  This junction is directly supplied from Pin-B from the ignition switch.  Each switch then has a connection to its sensor.  And currently a chassis connectin to ground.  I will soon implement an additional direct ground from each gauge chassis to the grounding block on the firewall.


# Rear wiring harness

| Wire # | Function              |     |
| ------ | --------------------- | --- |
| 1      | Fuel pump +           |     |
| 2      | Fuel GND              |     |
| 3      | Fuel Sender           |     |
| 4      | Passenger turn signal | 2   |
| 5      | Driver turn signal    | 1   |
| 6      | Service Tail lamps    |     |
| 7      | BO Tail lamp          |     |
# Rear tail lamps

| Pin # | Function          |
| ----- | ----------------- |
| 1     | Service tail lamp |
| 2     | Turn Signal       |
| 3     | BO Marker         |
   