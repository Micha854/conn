import requests
import subprocess
import datetime
import time

### CONFIG PART
webhook = 'discord webhook'
madmin = 'http://domain.com:5000'
auth_user = 'admin'
auth_pass = 'pass'

# vars
offline = 0
timestamp = 0

while True:
    now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    r = requests.get(madmin + '/settings/devices', auth=(auth_user, auth_pass), timeout=5)

    ### offline
    if not r.status_code == 200 and not offline:
        offline = 1
        timestamp = now
        print(now + ' Disconnection detected...')

    ### online
    if r.status_code == 200 and offline == 1:
        print(now + ' Internet connection back, restart devices!')
        exit_code = subprocess.check_output('./power.sh', shell=True)
        try:
            data = {
                "content": "",
                "username": "Pi!",
                "avatar_url": "https://github.com/GhostTalker/icons/blob/main/rmd/messagebox_critical_256.png?raw=true",
                "embeds": [
                {
                    "title": "The Pi has restarted!",
                    "color": 16711680,
                    "thumbnail": {
                        "url": "https://avatars.githubusercontent.com/u/1294177?s=256&v=4"
                    },
                    "fields": [
                    {
                        "name": "connection lost",
                        "value": str(timestamp),
                        "inline": "true"
                    },
                    {
                        "name": "rebooted",
                        "value": str(now),
                        "inline": "true"
                    }
                    ]
                }
                ]
            }
            send = requests.post(webhook, json=data)
        except:
            print(now + ' could not send webhook!')
        
        offline = 0
        timestamp = 0
        #print(exit_code)


    time.sleep(10)