# grundfossensor
## General
### Raspberry Pi Water Sensors

### https://shop.frappgmbh.de/AnoPi-Raspberry-Header
## Installation
```
pip install pi-gfs
```
## Get started
### The most important thing is, that you need to activate UART on Raspberry Pi
For further Information have a look at that link
https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/

## Usage
### Read Pressure and Temperatur with RPS
This code example is for the usage of a RPS (relative pressure sensor). The sensor can read the water and air pressure and the temperatur.
```
# import package
from grundfossensor import grundfossensor as gfs

# initilize sensor
rps = gfs(None, '99154122-05-227-00084', 1, 'RPS')

# read values for RPS
print('Pressure {:.2f} bar'.format(rps.get_pressure()))
print('Temperatur {:.2f} bar'.format(rps.get_temperatur()))
```
### Read Flow and Temperatur with VFS
This code example is for the usage of a VFS (vortex flow sensor). The sensor can read the water and water flow and the temperatur.
```
# import package
from grundfossensor import grundfossensor as gfs

# initilize sensor
vfs = gfs(None, '99154122-05-227-00084', 1, 'VFS')

# read values for VFS
print('Pressure {:.2f} bar'.format(vfs.get_flow()))
print('Temperatur {:.2f} bar'.format(vfs.get_temperatur()))
```


### Work with multiple Sensors
The head supports up to 4 Grundfossensor. You can combine Pressure Sensors and Flow sensors as you want. It 
```
from grundfossensor import grundfossensor as gfs

# initilize sensors
rps1 = gfs(None, '99154122-05-227-00084', 1, 'RPS')
rps2 = gfs(None, '99154122-05-227-00215', 2, 'RPS')

# read values for mulitple sensors
print('Temperatur 1 {:.2f} bar'.format(rps1.get_temperatur()))
print('Temperatur 2 {:.2f} bar'.format(rps2.get_temperatur()))

```


## Electrical wiring
### !!!Warning!!! Industrial level voltages and currents can be hazardous, only assemble this if you are a trained expert and know what you are doing.

### Current loop
![current loop wiring](/examples/wiring/Anschluss_Stromschleife.PNG)

### Voltage measurement 

![Voltage measurement  wiring](/examples/wiring/Anschluss_Spannungspegel.PNG)

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

## Contact

info@frappgmbh.de

Project Link: [https://github.com/AndreasScharf/python-anopi](https://github.com/AndreasScharf/python-anopi)

<p align="right">(<a href="#top">back to top</a>)</p>

