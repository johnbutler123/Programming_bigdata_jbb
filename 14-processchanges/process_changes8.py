changes_file = 'changes_python.txt'
data = [line.strip() for line in open(changes_file, 'r')]
sep = 72*'-'


class Commit:
    'class for commits'
   
    def __init__(self, revision=None, author=None, fulldate=None, month=None, week=None, date=None, comment_line_count=None, changes=None,
            comment=None, tbldconfig=0, tpixel=0, tgradle=0, tjava=0, txml=0, toth=0, countM=0, countA=0, countD=0):
        self.revision = revision
        self.author = author
        self.fulldate = fulldate
        self.month = month
        self.week = week
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment
        self.tbldconfig = tbldconfig
        self.tpixel = tpixel
        self.tgradle = tgradle
        self.tjava = tjava
        self.txml = txml
        self.toth = toth
        self.countM = countM
        self.countA = countA
        self.countD = countD
    def get_commit_list(self):
        import time
        import datetime
        changes_file = 'changes_python.txt'
        my_file = open(changes_file, 'r')
        data = [line.strip() for line in open(changes_file, 'r')]
        sep = 72*'-'
        commits = []
        index = 0    
        while True:
            try:
                tbldconfig=0
                tpixel=0
                tgradle=0
                tjava=0
                txml=0
                toth=0
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
                        tbldconfig = tbldconfig + 1
                        # print typebldconfig, revision, change
                    elif "dpi" in str(change):
                        tpixel = tpixel + 1
                    elif "600dp" in str(change):
                        tpixel = tpixel + 1
                    elif "gradle" in str(change):
                        tgradle = tgradle + 1
                    elif "java" in str(change):
                        tjava = tjava + 1
                    elif "xml" in str(change):
                        txml = txml + 1
                    else:
                        toth = toth+1
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
                w = (author,countD)
                commits.append(w)               
                commits.sort(key=lambda s:(s[0],s[1]),reverse=True)
            except IndexError:
                break
        # print "finished"
        f1 = open("testingtesting8.csv", "w")
        for c in commits:
            #print c[1]
            #f1.write(c[0]+","+str(c[1]))
            f1.write(c[0]+","+str(c[1])+'\n')
        f1.close


commits = Commit()
commits.get_commit_list()


#########################################################



        
