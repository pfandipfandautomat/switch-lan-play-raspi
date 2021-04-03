# Lan Play Switch WebUI for Raspberry Pi
![Screenshot of GUI](https://github.com/arthurkoch/switch-lan-play-raspi/blob/main/screenshot.png)
Small WebApp to manage Lan Play for Switch  on a Raspberry Pi created with Flask.
Compiled lan-play for ARM64 is included.
It's still very much WIP.
The goal is to have an executable file + a config file


## Config

You can add additional servers in the config.ini file.
Currently only the servers are configurable. 


## Running
As Root:


    python3 -m venv myvenv
    source myvenv/bin/activate
    pip3 install -r requirements.txt
    flask run --host <ip of raspberry>
    

It'll run on port 5000 - you probably have to open the port.

## Thanks to
spacemeowx2 for creating lan-play
https://github.com/spacemeowx2/switch-lan-play

