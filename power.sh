#!/bin/bash

#POWER OFF
uhubctl -a off -l 1-1.1.3.4 -p 1
uhubctl -a off -l 1-1.1.3.4 -p 2
uhubctl -a off -l 1-1.1.3.4 -p 3
uhubctl -a off -l 1-1.1.3.4 -p 4
uhubctl -a off -l 1-1.1.3.3 -p 1
uhubctl -a off -l 1-1.1.3.3 -p 2

sleep(10)

#POWER ON
uhubctl -a on  -l 1-1.1.3.4 -p 1
uhubctl -a on  -l 1-1.1.3.4 -p 2
uhubctl -a on  -l 1-1.1.3.4 -p 3
uhubctl -a on  -l 1-1.1.3.4 -p 4
uhubctl -a on  -l 1-1.1.3.3 -p 1
uhubctl -a on  -l 1-1.1.3.3 -p 2
