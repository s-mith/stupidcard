import sys

def run_pyx(filename):
    code = ""
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('#'):
                code += line
            else:
                if line.startswith("#import"):
                    line = line[1:]
                    line = line.split(" ")
                    if "\n" in line[1]:
                        line[1] = line[1].replace("\n", "")
                    with open(line[1], 'r') as importfile:
                        thing  = importfile.read()
                        if "#imports" in thing:
                            code += thing.split("#imports")[1]
                        else:
                            code += thing
                    code += "\n"

    # write the code to a file called compiled.py
    with open("compiled.py", 'w') as file:
        file.write(code)
    # run compiled.py
    
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: pyx <filename.pyx>")
    else:
        filename = sys.argv[1]
        run_pyx(filename)
