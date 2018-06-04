# Python Scripts
**Repository containing Python scripts made for simplifying common tasks.** :sunglasses:

## Libraries Used:
 - os
 - sys
 - openpyxl
 - hashlib
 - filecmp
 - struct
 - Crypto           (in auto-backup)
 - shutil           (in auto-backup)
 - vlc              (in alarm-clock)
 - mutagen          (in alarm-clock)
 - python-crontab   (in alarm-clock)

## Scripts:
1. [Duplicate](https://github.com/Pro-Panda/Python-Scripts/tree/master/Duplicate): 
   - It lists all the duplicate files present at a given path.
   - Gives the option to remove/ not remove any of them.
   - Uses 'filecmp' and 'os' libraries to compare files which are of the same size
   
2. [Excel-Attd](https://github.com/Pro-Panda/Python-Scripts/tree/master/Excel-Attd): 
   - Fills the attendance of all BITS Students(mathced by ID) in an excel sheet.
   - Created to fill the attendance of Students registered in CP Course at BITS Pilani
   
3. [Alarm-Clock](https://github.com/siddhantkhandelwal/Python-Scripts/tree/master/alarm-clock):
   - Plays the file 'alarm.mp3' in the cwd once the alarm expires.
   - Can be used to schedule alarms weekly, daily.
   
## How to use:
 - Duplicate

   ```bash
   python filecmp.py /path/to/folder
   ```
 - Excel-Attd

    ```bash
    python update.py /path/to/attendance_list /path/to/excel_sheet <Attd Column No.>
    ```
 - Alarm-Clock

    ```bash
    python alarm-clock-cli.py option h m s
    ```

## Improvements:
*Anyone is welcome to contribute and improve/modify the scripts.*

- [Alarm-Clock](https://github.com/siddhantkhandelwal/Python-Scripts/tree/master/alarm-clock):
  - Add an option to snooze the alarm.
  - Add an option to delete/modify scheduled alarms.
  - Add an option for custom alarm sounds.
  - Create logs specific to the script. Will help in keeping track of alarms independent of the cron-tab.

*Please open an issue if you find any bugs in any of the scripts.*
