#!/usr/bin/env python3

#python script that will loop through and unzip

import zipfile
import os
import glob


i = 1

while i <= 1000:
	#finding latest file in directory
	list_of_files = glob.glob('/path/to/directory/*.zip') 
	latest_file = max(list_of_files, key=os.path.getctime)
	print(f"Latest file is pwd = {latest_file}")

	# specifying the zip file name
	file_name = latest_file
	split_latest_file = os.path.basename(latest_file)



	print(f"Try {i}") 
	# if not split_latest_file.endswith("*.zip"):
	# 	break
	# opening the zip file in READ mode
	with zipfile.ZipFile(file_name, 'r') as f:
	    # printing all the contents of the zip file
	    names = f.namelist()
	    split_name = names[0].split('.')
	    print(split_name[0])

	    #extract zip with password as filename
	    f.setpassword(bytes(f"{split_name[0]}","utf-8"))
	    f.extractall()
	    print(f"Extracted zip file {file_name} with password {split_name[0]} and new file is {split_name[0]}.zip ")
	    i += 1
