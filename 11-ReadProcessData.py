######Changes 2
#Read in datafile and breakup into groupings which will eventally become objects
#For each grouping create standard attributes "revision", "author", "fulldate","comment_line_count","changes" and "comment"

#Also added some other attributes which would support extracting "interesting" information from data
#For each grouping derived total number of Adds, Modifications and Deletes in the "changes" section ("CountA", "CountM" and "CountD")

##Also derived for each grouping count by path of key tasks performed - see below:
#typebldconfig  - build_config
#typepixeldensity -  pixel density for screen and items related tasks
#typegradle  -  work done in relation to open source build model "gradle"
#typejava   - java type tasks
#typexml - xml type tasks
#typeoth  - other tasks

#Derived week from date as this could be useful going forward eg sum commits by week or by author and week

#Checked that total items in final list = 422 (this will eventually become total objects in class)
#Also spot checked some items to ensure code is working as expected - see row 96



# open the file - and read all of the lines.
changes_file = 'changes_python.txt'
# use strip to strip out spaces and trim the line.

my_file = open(changes_file, 'r')


###Testing to ensure that file can be read
# for line in my_file:
    # print line
# data = my_file.readlines()

data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
# print(len(data))
# print data[1]
# print len(data[1])
sep = 72*'-'

import time
import datetime

commits = []
index = 0
while True:
    try:
        typebldconfig=0
        typepixeldensity=0
        typegradle=0
        typejava=0
        typexml=0
        typeoth=0
        countM = 0
        countA = 0
        countD = 0
        details = data[index + 1].split('|')
        revision = int(details[0].strip().strip('r'))
        author = details[1].strip()
        fulldate = details[2].strip()
        year = int((details[2][0:5]).strip())
        month = int((details[2][6:8]).strip())
        date = int((details[2][9:11]).strip())
        mydate = datetime.date(year,month, date)  #year, month, day
        week = (mydate.strftime("%W"))
        comment_line_count = int(details[3].strip().split(' ')[0])
        changes = data[index+2:data.index('',index+1)]
        for change in changes:
            if "build-config" in str(change):
                typebldconfig = typebldconfig + 1
                # print typebldconfig, revision, change
            elif "dpi" in str(change):
                typepixeldensity = typepixeldensity + 1
            elif "600dp" in str(change):
                typepixeldensity = typepixeldensity + 1
            elif "gradle" in str(change):
                typegradle = typegradle + 1
            elif "java" in str(change):
                typejava = typejava + 1
            elif "xml" in str(change):
                typexml = typexml + 1
            else:
                typeoth = typeoth+1
        for change in changes:
            if change[0] == "M":
                countM = countM+1
            elif change[0] == "A":
                countA = countA+1
            elif change[0] == "D":
                countD = countD +1
        index = data.index(sep, index + 1)
        comment = data[index-comment_line_count:index]
        # print type(comment)
        # The object which contains the conveniently misspelt word "Foother" can be used for testing
        # It has two lines of comments so can check that both are captured
        # It contains three references to 'Modify' changes so this can also be checked
        # Contains two paths in the changes section  that relate to xml type and one that relates to java
        # if "Foother" in str(comment):
            # print comment
            # print typexml
            # print typejava
            # print countA
            # print countM
            # print countD
            # break
        w = (author)
        commits.append(w)


    except IndexError:
        break

print len(commits)  ###Great - 422 as expected

        
