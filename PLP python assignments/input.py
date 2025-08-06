try: #adding a file error handling block so that the program will not crash
    #opening the file in r+ mode so that it can read and update
    with open("PLP python assignments\Week 4 assignment.txt", "r+") as file: 
        content = file.read() #readingd the file
        print(f'Original file content:\n{content}') 
        
        #modifying the file
        modified = file.write(
            "\nI am trying to write into a file\n"
            "I hope this runs successfully\n"
            "Python is fun\n"
        )
        print("File Updated Successfully!") #success message. 

        #writing the modified content to a new file
        with open("assignments/Week 4 assignment/modified_output.txt", "w") as new_file:
            new_file.write(modified)
        print("Modified file written successfully!")

#exception block
except FileNotFoundError:
    print('check your program')