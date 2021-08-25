import os
import ntpath
import fnmatch
from PIL import Image
from datetime import datetime

def GetDateTaken(ImagePath):
    #Ref http://stackoverflow.com/questions/23064549/get-date-and-time-when-photo-was-taken-from-exif-data-using-pil
    sDateTaken = Image.open(ImagePath)._getexif()[36867]
    return datetime.strptime(sDateTaken[:10], "%Y:%m:%d")

def MountNASVolume(VolumeName):
    #Ref http://stackoverflow.com/questions/27598313/mounting-smb-network-share-on-desktop
    Command = "osascript -e 'mount volume \"smb://NicksNas/{0}\"'".format(VolumeName)
    os.system(Command)

def GetOrganisedPath(OrganisedRootPath, ImagePath):
    DateTaken = GetDateTaken(ImagePath)
    FolderPath = os.path.join(
        OrganisedRootPath,
        DateTaken.strftime('%Y-%m-%d'))
    FilePath = os.path.join(
        FolderPath,
        ntpath.basename(ImagePath))
    return FolderPath, FilePath

def MoveIfMatched(SourceImagePath, SourceFileName, ImageFileMask):
    if os.path.isfile(SourceImagePath) and fnmatch.fnmatch(SourceFileName.lower(), ImageFileMask):
        try:
            print (SourceImagePath)
            DestinationFolderPath, DestinationFilePath = GetOrganisedPath(OrganisedRootPath, SourceImagePath)
            os.makedirs(DestinationFolderPath, exist_ok=True)
            os.rename(SourceImagePath, DestinationFilePath)
        except Exception:
            raise
            #pass

def OrganiseImages(SourceFolder, OrganisedRootPath, Recursive = False, ImageFileMask = "*.jpg"):
    ImageFileMask = ImageFileMask.lower()

    if Recursive:
        for RootPath, Dirs, Files in os.walk(SourceFolder):
            for SourceFileName in Files:
                SourceImagePath = os.path.join(RootPath, SourceFileName)
                MoveIfMatched(SourceImagePath, SourceFileName, ImageFileMask)
    else:
        for SourceFileName in os.listdir(SourceFolder):
            SourceImagePath = os.path.join(SourceFolder, SourceFileName)
            MoveIfMatched(SourceImagePath, SourceFileName, ImageFileMask)

MountNASVolume("Multimedia")
SourceFolder = os.path.normpath("/Volumes/Multimedia/Our Pictures/snow/")
OrganisedRootPath = os.path.normpath("/Volumes/Multimedia/Our Pictures/Nick's Pictures/Organised/")
OrganiseImages(SourceFolder, OrganisedRootPath, Recursive=True)


