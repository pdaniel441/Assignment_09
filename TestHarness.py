#------------------------------------------#
# Title: Test Harness
# Desc: A Module to test the Modules
# Change Log: Patrick Danielson, 2021-Mar-14, Modified Code for Assignment 09
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# PDanielson, 2021-Mar-14, Modified Code for LabB / Assignment 09
#------------------------------------------#


import DataClasses as DC
import ProcessingClasses as PC
import IOClasses as IO

lstOfCDObjects = []
file_name = ['TestCD.txt', 'TestTrack.txt']

# Test DataClasses.py
print('\n\nTesting Track class')
print(DC.Track.__doc__)
# Create 2 Tracks
trk1 = DC.Track(1, 'test.track1', '01:59')
trk2 = DC.Track(2, 'test.track2', '02:59')
print(trk1)
print('record for file:', trk1.get_record())

print('\n\nTesting CD class')
# Create 1 CD
print(DC.CD.__doc__)
cd1 = DC.CD(1, 'test_title', 'cd_artist')
print(cd1)
print('record for file:', cd1.get_record())
# Add Tracks to CD 1
print('adding tracks...')
cd1.add_track(trk1)
cd1.add_track(trk2)
print('get tracks:\n', cd1.get_tracks())
print('get long record:\n', cd1.get_long_record())
# Remove Track 1 and Sort Tracks
print('removing track 1...')
cd1.rmv_track(1)
print('get long record:\n', cd1.get_long_record())
lstOfCDObjects.append(cd1)

# Test IOClasses.py
print('\n\nTesting of class FileIO')
IO.FileIO.save_inventory(file_name, lstOfCDObjects) # Only saves 2nd track
print(IO.FileIO.load_inventory(file_name))  # Load in and have empty 1st track on CD1

print('\n\nTesting ScreenIO class')
print('Main menu:')
IO.ScreenIO.print_menu()
print('selection in menu: {}'.format(IO.ScreenIO.menu_choice()))
print('**Inventory:')
IO.ScreenIO.show_inventory(lstOfCDObjects)
cd2 = DC.CD(2, 'test_title_2', 'cd_artist_2')
lstOfCDObjects.append(cd2)

print('\n**Inventory:')
for item in lstOfCDObjects:
    print(item)

print('\n**New Inventory:')
IO.ScreenIO.show_inventory(lstOfCDObjects)
cd_idx = 1
cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)

print('\nSub Menu')
IO.ScreenIO.print_CD_menu()
print('selection in sub menu: {}'.format(IO.ScreenIO.menu_CD_choice()))
print('Tracks:')
IO.ScreenIO.show_tracks(cd) # should only have 1 track in Position 2

# Test ProcessingClasses.py
print('\n\nTesting Processing Classes')
PC.DataProcessor.add_CD((3, 'Foreigner', 'Foreigner'), lstOfCDObjects)
print('Inventory:')
for item in lstOfCDObjects:
    print(item)