# Lan Play Switch WebUI for Raspberry Pi
![Screenshot of GUI](https://github.com/arthurkoch/switch-lan-play-raspi/blob/main/screenshot.png)
Small WebApp to manage Lan Play for Switch  on a Raspberry Pi created with Flask.
Compiled lan-play for ARM64 is included.
It's still very much WIP.
The goal is to have an executable file + a config file

## Notes

FULL DISCLAIMER: I have almost no coding experience, I taught myself all of this while trying to find a solution, so this comes with no gaurantee. 

After a lot of research and testing, I found that you must use v0.1.0 of the original switch-lan-play file in order for it to work on Raspberry Pi. Any newer version will not work. I have included my copy of that file in this repo.

I have updated config.ini to reflect current active lan-play servers, the original one was very out of date. You can obviously still edit it to your personal needs.

I made some changes to the app code to replace the `ping` command with `nc` when looking up server activity. This runs much quicker and allows for checking specific ports for different IPs


## Config

You can add additional servers in the config.ini file.
Currently only the servers are configurable. 


## Running
As Root:

    git clone https://github.com/RareCandyMan/switch-lan-play-raspi.git
    cd switch-lan-play-raspi
    python3 -m venv myvenv
    source myvenv/bin/activate
    pip3 install -r requirements.txt
    flask run --host <ip of raspberry>
    

It'll run on port 5000 - you probably have to open the port.

## Thanks to
spacemeowx2 for creating lan-play
https://github.com/spacemeowx2/switch-lan-play

