# import package
from grundfossensor import grundfossensor as gfs

# initilize sensor
rps = gfs(None, '99154122-05-227-00084', 1, 'RPS')

# read values for RPS
print('Pressure {:.2f} bar'.format(rps.get_pressure()))
print('Temperatur {:.2f} bar'.format(rps.get_temperatur()))
