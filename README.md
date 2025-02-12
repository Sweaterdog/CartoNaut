# CartoNaut
This repository is about CartoNaut, an AI-driven robot which uses vision and text-to-speech to explore the surroundings and attempt to reach goals and targets set by the user.

CartoNaut is currently powered by Gemini 2.0 Flash Thinking Experimental 01-21.

The name CartoNaut comes from "Carto" - from Cartographer, and "Naut" - from Astronaut. The name is designed to showcase the bot's visual mapping and exploration skills.

## Instructions to build and set up
### What you'll need

| Item | Price |
| ---- | ----- |
| [Google Account](https://accounts.google.com/) | N/A |
| [elevenlabs](https://elevenlabs.io) OR [PlayHT](https://play.ht) account (you can sign up with google) | N/A |
| Another Computer (Windows, Mac, or Linux) | N/A |
| A Wi-Fi network | N/A |
| [Raspberry Pi Zero 2WH](https://thepihut.com/products/raspberry-pi-zero-2?variant=43855634497731) | £16.98 |
| [CamJam EduKit 3 - Robotics](https://thepihut.com/products/camjam-edukit-3-robotics) | £20 |
| [Micro-USB OTG Adapter](https://thepihut.com/products/micro-usb-otg-adapter-for-raspberry-pi-zero) | £2 |
| [microSD card](https://thepihut.com/products/sandisk-microsd-card-class-10-a1) | £8.00 |
| USB Webcam | £6 |
| Powerbank | £15 |
| Total | £67.98 |

### Setting up

1. Unpack the CamJam Edukit. Keep the box safe.
2. Set up your robot according to the instructions found [here](https://github.com/CamJam-EduKit/EduKit3/blob/master/CamJam%20Edukit%203%20-%20RPi.GPIO/CamJam%20EduKit%203%20-%20Robotics%20Worksheet%202%20(RPi.GPIO)%20-%20Building%20a%20Robot.pdf). Use the box as the chassis.
3. Download Raspberry Pi Imager on your computer. You can use [Windows](https://downloads.raspberrypi.org/imager/imager_latest.exe), [Mac](https://downloads.raspberrypi.org/imager/imager_latest.dmg) or [Linux](https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb).
4. Plug in the microSD card to your computer
5. Open Raspberry Pi Imager and configure it as shown below:
   
   ![image](https://github.com/user-attachments/assets/84a921ee-ff1e-426b-9d9b-9068a6bc1f6d)
6. Configure OS Customisation as shown below:
   
   ![image](https://github.com/user-attachments/assets/5bdddabe-707f-4a53-894e-84cdbaae7af2)
   
   _(set the password to "raspberry")_

7. Make sure to enable SSH in the SERVICES tab.
8. Flash the SD Card.
9. Unplug the SD Card from your computer, and plug it in to the Pi.
10. Connect the USB Webcam to the Pi via the OTG cable.
11. Power the Pi using the powerbank and a USB cable.
12. On your computer, open a new CMD/Powershell/Terminal window and type: "ssh pi@zero.local"
13. If prompted, accept fingerprint warnings with "yes" and type "raspberry" as the password. You may not be able to see it as you are typing.
14. If not already installed on the Pi, install Python and Git.
    
    ```sudo apt install python3 python-is-python3 git```
    
    These should be installed on both the Pi and your local computer.
16. On both the existing command window and a brand new one, enter
    ```git clone https://github.com/uukelele-scratch/CartoNaut.git```
    Then, `cd CartoNaut`.
17. On the ssh-connected command window, run
    ```pip install opencv-python flask flask-socketio```
    then
    ```python server.py```
19. To verify everything is working correctly, in your browser on your local computer, go to `http://zero.local:5000`. You should see the latest frame from the connected webcam.
20. On your local PC, go to https://mpv.io/installation/ and follow the installation instructions.
    For Windows, download a version suitable for your PC (e.g. https://github.com/shinchiro/mpv-winbuild-cmake/releases/download/20250210/mpv-dev-x86_64-20250210-git-73b8459.7z) and unzip the file. Then, move the folder to a location such as C:\ and add it your PATH - type "path" in the Start menu and open "Edit the system environment variables", then click "Environment Variables" at the bottom. Double-click "Path" at the top, then click New and paste the location of the **folder** that the unzipped files are in (containing mpv.exe and mpv.com)
22. On your local PC, run
    ```pip install google-generativeai python-socketio requests pillow elevenlabs pyht```
23. Grab yourself a Google API Key at https://aistudio.google.com/apikey. Also, get an ElevenLabs or PlayHT API Key at their respective websites.
24. In a text editor on your local PC, open `client.py`. For example, on Windows, run `notepad client.py`.
25. Near the top, you will find a config area. Here, you can put config data. To start, put your Google API Key opposite "GEMINI_API_KEY" (enclosed in quotes), and do the same for either ElevenLabs or PlayHT (+ userid if using PlayHT), depending on which you are using. Set the "AUDIO" to either "ElevenLabs" or "PlayHT", or leave it as "" (empty) if you don't want your robot to talk.
26. Set your GOAL, TARGET, and SUCCESS_CRITERIA as you wish.
27. Run `python client.py` on your local computer. Then, make sure the system volume isn't muted, and enjoy!

## Find any issues?
If you find any issues with CartoNaut, or the building process, I'd love to know! Please file an issue at the "Issues" section near the top of this page.

## Want to contribute?
This repo is open to pull requests!
