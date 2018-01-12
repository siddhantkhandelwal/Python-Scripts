# Python Scripts
This repository contains all of my Python scripts made for simplifying tasks.

### Libraries Used:
 - os
 - sys
 - openpyxl
 - hashlib
 - filecmp
 - struct
 - Crypto (in auto-backup)
 - shutil (in auto-backup)

### List of Scripts:
1. Duplicate: 
   - It lists all the duplicate files present at a given path.
   - Gives the option to remove/ not remove any of them.
   - Uses 'filecmp' and 'os' libraries to compare files which are of the same size
   - How to use:
      ```bash
      python filecmp.py /path/to/folder
      ```
2. Excel-Attd: 
   - Fills the attendance of all BITS Students(mathced by ID) in an excel sheet.
   - Created to fill the attendance of Students registered in CP Course at BITS Pilani
   - How to use:
      ```bash
      python update.py /path/to/attendance_list /path/to/excel_sheet <Attd Column No.>
      ```

### Improvement:
Anyone is welcome to contribute and improve/modify the scripts. <br>
Please open an issue if you find any bugs in any of the scripts.