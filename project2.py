name = str(input("Name of your program: "))
ext = str(input("Extension Used(for eg: py, c, cpp, etc): "))

if ext == 'py':
    print("The file " + name + " is a Python file.")
elif ext == 'c':
    print("The file " + name + " is a C-program.")
elif ext == 'cpp':
    print("The file " + name + " is a C++ program.")
