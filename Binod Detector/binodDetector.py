import os

os.chdir('D:\Work\VS Code program\Python\Mini Projects\Binod Detector')     # setting current folder as current directory
contents = os.listdir()     # lists all the files available in current directory

n = 0

# print(contents)
for file in contents:
    if file.endswith('txt'):    # only searchs in .txt files
        file2 = file
        print(f"Detecting binod in '{file}'")

        with open(f"{file}",'r') as file:       # opening file to read contents
            data = file.read()              # fetching data of text files
            if 'binod' in data.lower():
                print(f"File '{file2}' contains binod\n")
                n += 1
            elif 'binod' not in data.lower():
                print(f"File '{file2}' do not contains binod\n")

print(f"Binod found in {n} files")