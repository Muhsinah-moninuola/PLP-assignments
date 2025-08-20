#getting the name of the file from the user
filename = input('Enter the name of the file you want to view?: ').strip()

try: #exception block to handle filename errors
    with open (filename, 'r') as file:  #opens the file that the user provided
        content = file.read() #reading the file
        #printing the original content from the file
        print(f'Original file content:\n{content}')

    #modifying the file
    modified_content = "\nThis is to modify the content of the file\nThank you for using the program"
    

    modified_output = content + modified_content

       
    with open("new_file.txt", "w") as new_file:
        new_file.write(modified_output)
        print('File modified Successfully')

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
except IOError:
    print("There was an error reading or writing the file.")

