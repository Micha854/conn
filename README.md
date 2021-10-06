# reboot all devices if connection lost

## install
```
git clone https://github.com/Micha854/conn

cp config_example.ini config.ini
```

## setup power.sh
put your reboot commands into the power.sh script

```
#!/bin/bash

#POWER OFF
uhubctl -a off -l 1-1.1.3.4 -p 1
uhubctl -a off -l 1-1.1.3.4 -p 2
uhubctl -a off -l 1-1.1.3.4 -p 3
uhubctl -a off -l 1-1.1.3.4 -p 4
uhubctl -a off -l 1-1.1.3.3 -p 1
uhubctl -a off -l 1-1.1.3.3 -p 2

sleep 10

#POWER ON
uhubctl -a on  -l 1-1.1.3.4 -p 1
uhubctl -a on  -l 1-1.1.3.4 -p 2
uhubctl -a on  -l 1-1.1.3.4 -p 3
uhubctl -a on  -l 1-1.1.3.4 -p 4
uhubctl -a on  -l 1-1.1.3.3 -p 1
uhubctl -a on  -l 1-1.1.3.3 -p 2
```

```
chmod +x power.sh
```


## autostart
```
sudo nano /lib/systemd/system/conn.service
```
```
[Timer]
OnBootSec=1min

[Unit]
Description=CheckConnection Service
After=multi-user.target

[Service]
Type=idle
ExecStart=python3 /home/pi/conn/main.py

[Install]
WantedBy=multi-user.target
```
```
sudo chmod 644 /lib/systemd/system/conn.service
sudo systemctl daemon-reload
sudo systemctl enable sample.service
```


![example](https://raw.githubusercontent.com/Micha854/conn/master/conn.png)
