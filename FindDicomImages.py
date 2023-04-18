"""
When outside discs/usb keys are received with outside studies, the conventions of
file naming are not always followed.  This program asks for a directory which contains
dicom images, and replaces any extension with ".dcm".  It will search all files in the
directory, and any files in included subdirectories.  The test for a valid dicom file
is based on reading files over 10K in size using pydicom.dcmread.  If the file is
not a valid dicom file, then dcmread raises an exception.  That exception is captured
in the try: except: block.
"""

from tkinter.filedialog import askdirectory
import os
import pydicom

dirname = askdirectory()

for dirpath, dirnames, filenames in os.walk(dirname):
    with os.scandir(dirpath) as dir_entries:
        for entry in dir_entries:
            test = os.path.splitext(entry.path)
            info = entry.stat()
            if entry.is_file():
                if info.st_size > 10000: # Most lossless compressed dicom images are more than 10K.
                    try:
                        dataset = pydicom.dcmread(entry)
                        print(test[0])
                        fnsplit = os.path.splitext(test[0])
                        new_filename = fnsplit[0] + '.dcm'
                        print(new_filename)
                    except:
                        continue

exit()
