# Siralim-Ultimate-Treasure-Booster
A low involvement script that edits your save to make the realm modifiers go outside their normal values, resulting in a bunch of extra treasure.

After downloading both the realm_prop_adjust.py and encrypt_decrypt.js, put them both in your folder with your Siralim Save files. 

You'll then neeed to open the realm_prop_adjust.py in a text editor like notepad, and edit the path of the file you want it to operate on. 

These are lines 5 and 6 of the realm_prop_adjust.py

Example : "C:\Users\admin\AppData\Local\SiralimUltimate\save\slot1.sav"
SAVE_FILE_PATH = r"Save File Path Here"

You just have to put the path for your save file you want modified in the quotation marks and save your changes.

How I use this is, double click the realm_prop_adjust.py to execute it, and then start playing. After I finish a realm, I go to Save & Restart in game, and while it's restarting, I double click to run the .py file again, and presto! The next realm has its modifiers changed.



Most of the credit should go to Gurgalex as I used the code from his SiralimUltimateSaver in order to create this project. If you want to do this same kind of thing with a more step-by-step and hands on approach, head over to his at https://github.com/gurgalex/SiralimUltimateSaver.git
