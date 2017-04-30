####Changes 1
####This stage is mainly a familiarisation stage
#### created breaks and added testcode to see if results are as expected
####Noticed that the code relies on the "object separator" (for want of a better term) containing 72 hyphens
####Thought it would be interesting to test that this is true   -  it is - see row 28





# open the file - and read all of the lines.
changes_file = 'changes_python.txt'
# use strip to strip out spaces and trim the line.

#my_file = open(changes_file, 'r')
#data = my_file.readlines()

data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
# print(len(data))
# print data[1]
# print len(data[1])
sep = 72*'-'


fhand = open(changes_file)

###Check if all hyphen lines are same length and if not is that a problem
###Although there are 17 lines which contain hyphens but not 72 hyphens - they seem ok
###The immediate preceding lines contain data that is in "Changes" section as opposed to "Comment" section
###Therefore code is ok as last item before object separator should be in comments section
for line in fhand:
    line = line.rstrip()
    if not line.startswith('--'):
        prevline = line
    if line.startswith('--'):
        hyphencount = len(line)
        if hyphencount != len(data[0]):
            print "not all hyphen lines are same length"
            print line
            print prevline


        # else:
            # print hyphencount


# create the commit class to hold each of the elements - I am hoping there will be 422
# otherwise I have messed up.
class Commit:
    'class for commits'
   
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment

    def get_commit_comment(self):
        return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
                + self.author + ' with the comment ' + ','.join(self.comment) \
                + ' and the changes ' + ','.join(self.changes)

               



    def get_commit_comment_only(self):
        if "Rename" in str(self.comment):
            print "True"
        else:
            print self.comment




                
commits = []
current_commit = None
index = 0

author = {}
while True:
    try:
        # parse each of the commits and put them into a list of commits
        current_commit = Commit()
        details = data[index + 1].split('|')
        current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index+2:data.index('',index+1)]
        #print(current_commit.changes)
        index = data.index(sep, index + 1)
        current_commit.comment = data[index-current_commit.comment_line_count:index]
        commits.append(current_commit)
    except IndexError:
        break
        
#Check that 422 items in list
# print(len(commits))

commits.reverse()

# for index, commit in enumerate(commits):
    # print(commit.get_commit_comment_only())
    # break
