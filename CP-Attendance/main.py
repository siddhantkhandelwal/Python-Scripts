#Pro-Panda
#to ease the burden of filling attendance sheets for CP Lectures for CP Lab TAs
import sys,openpyxl

wb = openpyxl.load_workbook(sys.argv[2])
sheet = wb.active
xl_file = open(sys.argv[1],'rw')

while(1):
    ID_present = (xl_file.readline()).strip()
    if (ID_present=='' or len(ID_present)>4):
        break
    if (len(ID_present)<4):
        ID_present=((4-len(ID_present))*'0')+ID_present
    runner=1
    while(1):
        runner=runner+1
        ID_sheet = (sheet['B'+str(runner)].value)
        if (ID_sheet==None):
            break
        ID_sheet = ID_sheet[8:12]
        if(ID_sheet==ID_present):
            sheet[sys.argv[3]+str(runner)] = 1
	    break
wb.save(sys.argv[2])
