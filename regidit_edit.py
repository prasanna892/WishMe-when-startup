# Python code to add current script to the registry

# module to edit the windows registry
import winreg as reg	

def AddToRegistry():
	# path of the python file with extension
	address="enter_file_path_with_file_name_and_extension"
	
	# key we want to change is HKEY_CURRENT_USER
	# key value is Software\Microsoft\Windows\CurrentVersion\Run
	key = reg.HKEY_CURRENT_USER
	key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
	
	# open the key to make changes to
	open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)
	
	# modify the opened key
	reg.SetValueEx(open,"enter_the_key_name",0,reg.REG_SZ,address)
	
	# now close the opened key
	reg.CloseKey(open)
	


# calling function
if __name__=="__main__":
	AddToRegistry()
	print("successfully added")
