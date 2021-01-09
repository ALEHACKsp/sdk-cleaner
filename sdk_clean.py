'''
<< SDK Cleaner by rdbo >>
https://github.com/rdbo/sdk-cleaner
'''

import os
import platform

def get_file_list(path):
	path_separator = "/"
	if(platform.system() == "Windows"):
		path_separator = "\\"
	file_list = []
	for path, names, filenames in os.walk(path):
		for file in filenames:
			abs_file = f"{path}{path_separator}{file}"
			file_list.append(abs_file)
	return file_list

def main():
	sdk_folder = os.path.dirname(os.path.realpath(__file__))
	file_list = get_file_list(sdk_folder)
	print("[*] Cleaning SDK up ...")
	for file in file_list:
		if not (file.endswith(__file__) or file.endswith(".h") or file.endswith(".hpp")):
			os.remove(file)

	print("[*] The SDK has been successfully cleaned up")

	return 1

if __name__ == "__main__":
	main()
