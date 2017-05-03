
def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
    data = [line.strip() for line in open(changes_file, 'r')]
    return data
    
def countpathlines():
    lines = []
    with open("changes_python.txt") as file:
        for line in file:
            line = line.strip() #or someother preprocessing
            if "/cloud/" in line:
                lines.append(line)
    pathlines = len(lines)
    return pathlines        

def countgradle():
    lines = []
    with open("changes_python.txt") as file:
        for line in file:
            line = line.strip() #or someother preprocessing
            if (".gradle" in line or "/gradle" in line) and "revert settings.gradle" not in line:
                lines.append(line)
    gradle = len(lines)
    return gradle
    
def countmodify():
    lines = []
    with open("changes_python.txt") as file:
        for line in file:
            line = line.strip() #or someother preprocessing
            if "M /" in line:
                lines.append(line)
    modify = len(lines)
    return modify

def countdelete():
    lines = []
    with open("changes_python.txt") as file:
        for line in file:
            line = line.strip() #or someother preprocessing
            if "D /" in line:
                lines.append(line)
    ddelete = len(lines)
    return ddelete
    
def countadd():
    lines = []
    with open("changes_python.txt") as file:
        for line in file:
            line = line.strip() #or someother preprocessing
            if "A /" in line:
                lines.append(line)
    add = len(lines)
    return add
    
def countR():
    lines = []
    with open("changes_python.txt") as file:
        for line in file:
            line = line.strip() #or someother preprocessing
            if "R /" in line:
                lines.append(line)
    r = len(lines)                
    return r
    
# def get_filepath_count():
    # lines = []
    # with open("changes_python.txt") as file:
        # for line in file:
            # line = line.strip() #or someother preprocessing
        # if "/cloud/" in line:
            # lines.append(line) 
            # print len(lines)
    
# x = get_filepath_count()
# print "jb",x
    
# x = countpathlines(data)
# print x
    
# x = countpathlines()
# print "testingpath", x

def get_commits(data):
    sep = 72*'-'
    commits = []
    current_commit = None
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            # the author with spaces at end removed.
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip(),
                'number_of_lines': details[3].strip().split(' ')[1]
            }
            # add details to the list of commits.
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits

if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.txt'
    data = read_file(changes_file)
    commits = get_commits(data)
    # paths = get_filepath_count()
    # print "testing", paths
    # get_filepath_count
    print "testingA"
    # print the number of lines read
    print(len(data))
    #print(commits)
    print(commits[0])
    print(commits[1]['author'])
    print(len(commits))