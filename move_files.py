import os

folder_original = '/folder/'
folder_destination = '/new_folder/'

location_original = os.path.join(folder_original, 'file.txt')
location_destination = os.path.join(folder_destination, 'new_file.txt')

# this method moves the file to a new location
os.rename(location_original, location_destination)
