# first get all lines from file
with open('zdb-win.txt', 'r') as f:
    lines = f.readlines()

# remove spaces
lines = [line.replace(' ', '') for line in lines]

# finally, write lines in the file
with open('rus.txt', 'w') as f:
    f.writelines(lines)
