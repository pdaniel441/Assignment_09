#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: Patrick Danielson, 2021-Mar-14, Modified Code for Assignment 09
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# PDanielson, 2021-Mar-14, Modified code for LabB / Assignment 09
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.


        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """

        cdId, title, artist = CDInfo
        try:
            cdId = int(cdId)
            row = DC.CD(cdId, title, artist)
            table.append(row)
        except ValueError:
            print('VALUE ERROR: Entry ID must be an Integer!')


    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        # TODone add code as required
        try:
            cd_idx = int(cd_idx)
        except ValueError:
            print('VALUE ERROR: CD ID must be an integer!!')
        
        for row in table:
            if cd_idx == row.cd_id:
                return row
        raise Exception('ERROR: ID is not in list of CD\'s')


    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd


        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.

        Raises:
            Exception: DESCraised in case position is not an integer.

        Returns:
            None: DESCRIPTION.

        """

        # TODone add code as required
        track_pos, track_title, track_length = track_info
        
        try:
            track_pos = int(track_pos)
            if track_pos >= 1:
                tmp_track = DC.Track(track_pos, track_title, track_length)
                cd.add_track(tmp_track)
        except ValueError:
            print('VALUE ERROR: Track Postiion must be a positive integer!')
        except:
            raise Exception('General input error.')

