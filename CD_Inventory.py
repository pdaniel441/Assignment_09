#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: Patrick Danielson, 2021-Mar-14, Modified Code for Assignment 09
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# PDanielson, 2021-Mar-14, Modified Code for LabB / Assignment 09
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO
import os.path

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
# Check if Files exist and Create if not found
for file in lstFileNames:
    if os.path.exists(file): 
        pass
    else:
        objFile = open(file,'w')
        objFile.close()

lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album index: ')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        # TODone add code to handle tracks on an individual CD
        while True:
            IO.ScreenIO.print_CD_menu()
            cd_strChoice = IO.ScreenIO.menu_CD_choice()  
            if cd_strChoice == 'x':
                break
            if cd_strChoice == 'a':
                tplTrackInfo = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(tplTrackInfo,cd)
                IO.ScreenIO.show_tracks(cd)
                continue
            elif cd_strChoice == 'd':
                IO.ScreenIO.show_tracks(cd)
                continue
            elif cd_strChoice == 'r':
                IO.ScreenIO.show_tracks(cd)
                track_id = input('Please enter ID for track you want to remove: ')
                cd.rmv_track(track_id)
            else: print('Invalid Menu selection.')
                
    
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
   
    else:
        print('General Error')