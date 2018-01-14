####John Butler 10353776
####Overview of script process_changes_class.py
##It creates a class Commit with a constructor which defines many useful attributes including "interesting" ones for analysis

##"interesting" parameters for analysis relate mainly to path type ('countM', 'CountA' or 'CountD') or 
##to task type ('tbldconfig', 'tpixel', 'tgradle', 'tjava', 'txml' or 'toth')
##Also split out date by month and week

##Main function 'def_commit_list'  applies values to the parameters and pulls out detaited reports by author and value for each commit
## The detailed reports all have 422 rows which matches the number of commits

##Further processing is then performed to create summary csv files by author and parameter - intermediate files created during this process
## are deleted at end

##This script also contains functions which support unittesting - see also "test_processing.py" 



import os
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
        commitsm=[]
        commitsd=[]
        commitsb=[]
        commitsu=[]
        commitsa=[]
        commitsp=[]
        commitsg=[]
        commitsj=[]
        commitsx=[]
        commitso=[]
        commitsw=[]
        index = 0    
        while True:
            try:
                count = 1
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
###Creation of suite of csv files supporting reporting by parameter value, author and commit

                u = (author,str(count))
                commitsu.append(u)               
                commitsu.sort(key=lambda s:(s[0],s[1]),reverse=True)
                a = (author,countA)
                commitsa.append(a)               
                commitsa.sort(key=lambda s:(s[0],s[1]),reverse=True)
                d = (author,countD)
                commitsd.append(d)               
                commitsd.sort(key=lambda s:(s[0],s[1]),reverse=True)
                m = (author,countM)
                commitsm.append(m)               
                commitsm.sort(key=lambda s:(s[0],s[1]),reverse=True)
                b = (author,tbldconfig)
                commitsb.append(b)               
                commitsb.sort(key=lambda s:(s[0],s[1]),reverse=True)
                p = (author,tpixel)
                commitsp.append(p)               
                commitsp.sort(key=lambda s:(s[0],s[1]),reverse=True)
                g = (author,tgradle)
                commitsg.append(g)               
                commitsg.sort(key=lambda s:(s[0],s[1]),reverse=True)
                j = (author,tjava)
                commitsj.append(j)               
                commitsj.sort(key=lambda s:(s[0],s[1]),reverse=True)
                x = (author,txml)
                commitsx.append(x)               
                commitsx.sort(key=lambda s:(s[0],s[1]),reverse=True)
                o = (author,toth)
                commitso.append(o)               
                commitso.sort(key=lambda s:(s[0],s[1]),reverse=True)
                w = (week,author)
                commitsw.append(w)               
                commitsw.sort(key=lambda s:(s[0],s[1]),reverse=True)

            except IndexError:
                break

        f1 = open("authordet.csv", "w")
        for c in commitsu:
            f1.write(c[0]+","+str(c[1])+'\n')
        f1.close
        f1 = open("countAdet.csv", "w")
        for c in commitsa:
            f1.write(c[0]+","+str(c[1])+'\n')
        f1.close
        f1 = open("countDdet.csv", "w")
        for c in commitsd:
            f1.write(c[0]+","+str(c[1])+'\n')
        f1.close
        f1 = open("countMdet.csv", "w")
        for c in commitsm:
            f1.write(c[0]+","+str(c[1])+'\n')
        f1.close
        f1 = open("tbldconfigdet.csv", "w")
        for c in commitsb:
            f1.write(c[0]+","+str(c[1])+'\n')
        f1.close
        f1 = open("tpixeldet.csv", "w")
        for c in commitsp:
            f1.write(c[0]+","+str(c[1])+'\n')
        f1.close
        f1 = open("tgradledet.csv", "w")
        for c in commitsg:
            f1.write(c[0]+","+str(c[1])+'\n')
        f1.close
        f1 = open("tjavadet.csv", "w")
        for c in commitsj:
            f1.write(c[0]+","+str(c[1])+'\n')
        f1.close
        f1 = open("txmldet.csv", "w")
        for c in commitsx:
            f1.write(c[0]+","+str(c[1])+'\n')
        f1.close
        f1 = open("tothdet.csv", "w")
        for c in commitso:
            f1.write(c[0]+","+str(c[1])+'\n')
        f1.close
        f1 = open("authorbyweek.csv", "w")
        for c in commitsw:
            f1.write(c[0]+","+str(c[1])+'\n')
        f1.close

######Creation of suite of csv files supporting reporting by parameter cumulative values, author and commit
	with open("authordet.csv") as inf:
	    with open("authorcum.csv", "w") as f1:
                data = []
                author = 'XXXXXXXX'
                countAuthor = 0.0
                for line in inf:
                    line = line.split(",")
                    #print line[0], line[1]
                    if line[0] == author:
                        countAuthor = countAuthor + float(line[1])
                    else:
                        countAuthor = float(line[1])
                        author = line[0]
                    x = line[0]+","+ str(countAuthor)+"\n"
                    f1.write(x)
	with open("countAdet.csv") as inf:
	    with open("countAcum.csv", "w") as f1:
                data = []
                author = 'XXXXXXXX'
                countAuthor = 0.0
                for line in inf:
                    line = line.split(",")
                    #print line[0], line[1]
                    if line[0] == author:
                        countAuthor = countAuthor + float(line[1])
                    else:
                        countAuthor = float(line[1])
                        author = line[0]
                    x = line[0]+","+ str(countAuthor)+"\n"
                    f1.write(x)
	with open("countDdet.csv") as inf:
	    with open("countDcum.csv", "w") as f1:
                data = []
                author = 'XXXXXXXX'
                countAuthor = 0.0
                for line in inf:
                    line = line.split(",")
                    #print line[0], line[1]
                    if line[0] == author:
                        countAuthor = countAuthor + float(line[1])
                    else:
                        countAuthor = float(line[1])
                        author = line[0]
                    x = line[0]+","+ str(countAuthor)+"\n"
                    f1.write(x)
	with open("countMdet.csv") as inf:
	    with open("countMcum.csv", "w") as f1:
                data = []
                author = 'XXXXXXXX'
                countAuthor = 0.0
                for line in inf:
                    line = line.split(",")
                    #print line[0], line[1]
                    if line[0] == author:
                        countAuthor = countAuthor + float(line[1])
                    else:
                        countAuthor = float(line[1])
                        author = line[0]
                    x = line[0]+","+ str(countAuthor)+"\n"
                    f1.write(x)
	with open("tbldconfigdet.csv") as inf:
            with open("tbldconfigcum.csv", "w") as f1:
                data = []
                author = 'XXXXXXXX'
                countAuthor = 0.0
                for line in inf:
            	    line = line.split(",")
                    #print line[0], line[1]
                    if line[0] == author:
                        countAuthor = countAuthor + float(line[1])
            	    else:
                        countAuthor = float(line[1])
                        author = line[0]
                    x = line[0]+","+ str(countAuthor)+"\n"
                    f1.write(x)
	with open("tpixeldet.csv") as inf:
            with open("tpixelcum.csv", "w") as f1:
                data = []
                author = 'XXXXXXXX'
                countAuthor = 0.0
                for line in inf:
            	    line = line.split(",")
                    #print line[0], line[1]
                    if line[0] == author:
                        countAuthor = countAuthor + float(line[1])
            	    else:
                        countAuthor = float(line[1])
                        author = line[0]
                    x = line[0]+","+ str(countAuthor)+"\n"
                    f1.write(x)
	with open("tgradledet.csv") as inf:
            with open("tgradlecum.csv", "w") as f1:
                data = []
                author = 'XXXXXXXX'
                countAuthor = 0.0
                for line in inf:
            	    line = line.split(",")
                    #print line[0], line[1]
                    if line[0] == author:
                        countAuthor = countAuthor + float(line[1])
            	    else:
                        countAuthor = float(line[1])
                        author = line[0]
                    x = line[0]+","+ str(countAuthor)+"\n"
                    f1.write(x)
	with open("tjavadet.csv") as inf:
            with open("tjavacum.csv", "w") as f1:
                data = []
                author = 'XXXXXXXX'
                countAuthor = 0.0
                for line in inf:
            	    line = line.split(",")
                    #print line[0], line[1]
                    if line[0] == author:
                        countAuthor = countAuthor + float(line[1])
            	    else:
                        countAuthor = float(line[1])
                        author = line[0]
                    x = line[0]+","+ str(countAuthor)+"\n"
                    f1.write(x)
	with open("txmldet.csv") as inf:
            with open("txmlcum.csv", "w") as f1:
                data = []
                author = 'XXXXXXXX'
                countAuthor = 0.0
                for line in inf:
            	    line = line.split(",")
                    #print line[0], line[1]
                    if line[0] == author:
                        countAuthor = countAuthor + float(line[1])
            	    else:
                        countAuthor = float(line[1])
                        author = line[0]
                    x = line[0]+","+ str(countAuthor)+"\n"
                    f1.write(x)
	with open("tothdet.csv") as inf:
            with open("tothcum.csv", "w") as f1:
                data = []
                author = 'XXXXXXXX'
                countAuthor = 0.0
                for line in inf:
            	    line = line.split(",")
                    #print line[0], line[1]
                    if line[0] == author:
                        countAuthor = countAuthor + float(line[1])
            	    else:
                        countAuthor = float(line[1])
                        author = line[0]
                    x = line[0]+","+ str(countAuthor)+"\n"
                    f1.write(x)
                    
####Creation of a suite of reports showing parameter values grouped by author 
        with open("authorcum.csv") as f:
            data = []
            for line in f:
                line = line.split(",")
                w = (line[0].strip(),'$',line[1].strip(),'$')
                data.append(w)


        data.sort(key=lambda s:(s[0],float(s[2])),reverse=True)

        f = open("authortemp.csv","w")
        for i in data:
	    delimiter = ''
	    i = delimiter.join(i)
	    f.write(i+'\n')
        f.close

        f = open("authortemp.csv")
        data = []
        for line in f:
            line = line.split("$")
            w = (line[0],",",line[1],',')
            data.append(w)

        f = open("authorsum.csv","w")
        author = "john"
        x = 0 
        for i in data:
            if i[0] == author:
                continue
            else:
                author = i[0]
                f.write(i[0]+","+i[2]+"\n")
        f.close

        with open("countAcum.csv") as f:
            data = []
            for line in f:
                line = line.split(",")
                w = (line[0].strip(),'$',line[1].strip(),'$')
                data.append(w)


        data.sort(key=lambda s:(s[0],float(s[2])),reverse=True)

        f = open("countAtemp.csv","w")
        for i in data:
	    delimiter = ''
	    i = delimiter.join(i)
	    f.write(i+'\n')
        f.close

        f = open("countAtemp.csv")
        data = []
        for line in f:
            line = line.split("$")
            w = (line[0],",",line[1],',')
            data.append(w)

        f = open("countAsum.csv","w")
        author = "john"
        x = 0 
        for i in data:
            if i[0] == author:
                continue
            else:
                author = i[0]
                f.write(i[0]+","+i[2]+"\n")
        f.close
        
        with open("countDcum.csv") as f:
            data = []
            for line in f:
                line = line.split(",")
                w = (line[0].strip(),'$',line[1].strip(),'$')
                data.append(w)


        data.sort(key=lambda s:(s[0],float(s[2])),reverse=True)

        f = open("countDtemp.csv","w")
        for i in data:
	    delimiter = ''
	    i = delimiter.join(i)
	    f.write(i+'\n')
        f.close

        f = open("countDtemp.csv")
        data = []
        for line in f:
            line = line.split("$")
            w = (line[0],",",line[1],',')
            data.append(w)

        f = open("countDsum.csv","w")
        author = "john"
        x = 0 
        for i in data:
            if i[0] == author:
                continue
            else:
                author = i[0]
                f.write(i[0]+","+i[2]+"\n")
        f.close
        
        with open("countMcum.csv") as f:
            data = []
            for line in f:
                line = line.split(",")
                w = (line[0].strip(),'$',line[1].strip(),'$')
                data.append(w)


        data.sort(key=lambda s:(s[0],float(s[2])),reverse=True)

        f = open("countMtemp.csv","w")
        for i in data:
	    delimiter = ''
	    i = delimiter.join(i)
	    f.write(i+'\n')
        f.close

        f = open("countMtemp.csv")
        data = []
        for line in f:
            line = line.split("$")
            w = (line[0],",",line[1],',')
            data.append(w)

        f = open("countMsum.csv","w")
        author = "john"
        x = 0 
        for i in data:
            if i[0] == author:
                continue
            else:
                author = i[0]
                f.write(i[0]+","+i[2]+"\n")
        f.close
        
        with open("tbldconfigcum.csv") as f:
            data = []
            for line in f:
                line = line.split(",")
                w = (line[0].strip(),'$',line[1].strip(),'$')
                data.append(w)


        data.sort(key=lambda s:(s[0],float(s[2])),reverse=True)

        f = open("tbldconfigtemp.csv","w")
        for i in data:
	    delimiter = ''
	    i = delimiter.join(i)
	    f.write(i+'\n')
        f.close

        f = open("tbldconfigtemp.csv")
        data = []
        for line in f:
            line = line.split("$")
            w = (line[0],",",line[1],',')
            data.append(w)

        f = open("tbldconfigsum.csv","w")
        author = "john"
        x = 0 
        for i in data:
            if i[0] == author:
                continue
            else:
                author = i[0]
                f.write(i[0]+","+i[2]+"\n")
        f.close
        
        with open("tpixelcum.csv") as f:
            data = []
            for line in f:
                line = line.split(",")
                w = (line[0].strip(),'$',line[1].strip(),'$')
                data.append(w)


        data.sort(key=lambda s:(s[0],float(s[2])),reverse=True)

        f = open("tpixeltemp.csv","w")
        for i in data:
	    delimiter = ''
	    i = delimiter.join(i)
	    f.write(i+'\n')
        f.close

        f = open("tpixeltemp.csv")
        data = []
        for line in f:
            line = line.split("$")
            w = (line[0],",",line[1],',')
            data.append(w)

        f = open("tpixelsum.csv","w")
        author = "john"
        x = 0 
        for i in data:
            if i[0] == author:
                continue
            else:
                author = i[0]
                f.write(i[0]+","+i[2]+"\n")
        f.close
        
        with open("tgradlecum.csv") as f:
            data = []
            for line in f:
                line = line.split(",")
                w = (line[0].strip(),'$',line[1].strip(),'$')
                data.append(w)


        data.sort(key=lambda s:(s[0],float(s[2])),reverse=True)

        f = open("tgradletemp.csv","w")
        for i in data:
	    delimiter = ''
	    i = delimiter.join(i)
	    f.write(i+'\n')
        f.close

        f = open("tgradletemp.csv")
        data = []
        for line in f:
            line = line.split("$")
            w = (line[0],",",line[1],',')
            data.append(w)

        f = open("tgradlesum.csv","w")
        author = "john"
        x = 0 
        for i in data:
            if i[0] == author:
                continue
            else:
                author = i[0]
                f.write(i[0]+","+i[2]+"\n")
        f.close
        
        with open("tjavacum.csv") as f:
            data = []
            for line in f:
                line = line.split(",")
                w = (line[0].strip(),'$',line[1].strip(),'$')
                data.append(w)


        data.sort(key=lambda s:(s[0],float(s[2])),reverse=True)

        f = open("tjavatemp.csv","w")
        for i in data:
	    delimiter = ''
	    i = delimiter.join(i)
	    f.write(i+'\n')
        f.close

        f = open("tjavatemp.csv")
        data = []
        for line in f:
            line = line.split("$")
            w = (line[0],",",line[1],',')
            data.append(w)

        f = open("tjavasum.csv","w")
        author = "john"
        x = 0 
        for i in data:
            if i[0] == author:
                continue
            else:
                author = i[0]
                f.write(i[0]+","+i[2]+"\n")
        f.close
        
        with open("txmlcum.csv") as f:
            data = []
            for line in f:
                line = line.split(",")
                w = (line[0].strip(),'$',line[1].strip(),'$')
                data.append(w)


        data.sort(key=lambda s:(s[0],float(s[2])),reverse=True)

        f = open("txmltemp.csv","w")
        for i in data:
	    delimiter = ''
	    i = delimiter.join(i)
	    f.write(i+'\n')
        f.close

        f = open("txmltemp.csv")
        data = []
        for line in f:
            line = line.split("$")
            w = (line[0],",",line[1],',')
            data.append(w)

        f = open("txmlsum.csv","w")
        author = "john"
        x = 0 
        for i in data:
            if i[0] == author:
                continue
            else:
                author = i[0]
                f.write(i[0]+","+i[2]+"\n")
        f.close
        
        with open("tothcum.csv") as f:
            data = []
            for line in f:
                line = line.split(",")
                w = (line[0].strip(),'$',line[1].strip(),'$')
                data.append(w)


        data.sort(key=lambda s:(s[0],float(s[2])),reverse=True)

        f = open("tothtemp.csv","w")
        for i in data:
	    delimiter = ''
	    i = delimiter.join(i)
	    f.write(i+'\n')
        f.close

        f = open("tothtemp.csv")
        data = []
        for line in f:
            line = line.split("$")
            w = (line[0],",",line[1],',')
            data.append(w)

        f = open("tothsum.csv","w")
        author = "john"
        x = 0 
        for i in data:
            if i[0] == author:
                continue
            else:
                author = i[0]
                f.write(i[0]+","+i[2]+"\n")
                
###Removal of temporary intermediate csv reports - the *cum ones could be kept as it is possible to create cumulative reports based on these
## However - they can also be generated from detailed reports so chose to remove them
        os.remove ("tothtemp.csv")
        os.remove ("tothcum.csv")
        os.remove ("authortemp.csv")
        os.remove ("authorcum.csv")
        os.remove ("countAtemp.csv")
        os.remove ("countAcum.csv")
        os.remove ("countDtemp.csv")
        os.remove ("countDcum.csv")
        os.remove ("countMtemp.csv")
        os.remove ("countMcum.csv")
        os.remove ("tbldconfigtemp.csv")
        os.remove ("tbldconfigcum.csv")
        os.remove ("tgradletemp.csv")
        os.remove ("tgradlecum.csv")
        os.remove ("tjavatemp.csv")
        os.remove ("tjavacum.csv")
        os.remove ("tpixeltemp.csv")
        os.remove ("tpixelcum.csv")
        os.remove ("txmltemp.csv")
        os.remove ("txmlcum.csv")
        f.close
        
        
####Creation of functions to support unittesting
    def countauthor(self):
		lines = []
		with open("changes_python.txt") as file:
			for line in file:
				line = line.strip() #or someother preprocessing
				if line.startswith("r1"):
					lines.append(line[11:17])
		x = list(set(lines))
		return len(x)

    def countgradle(self):
        lines = []
        with open("changes_python.txt") as file:
            for line in file:
                line = line.strip() #or someother preprocessing
                if (".gradle" in line or "/gradle" in line) and "revert settings.gradle" not in line:
                    lines.append(line)
        gradle = len(lines)
        return gradle

    def countpathlines(self):
        lines = []
        with open("changes_python.txt") as file:
            for line in file:
                line = line.strip() #or someother preprocessing
                if "/cloud/" in line:
                    lines.append(line)
        pathlines = len(lines)
        return pathlines        

    def get_commits(self,data):
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
        return len(commits)
        
    def countmodify(self):
        lines = []
        with open("changes_python.txt") as file:
            for line in file:
                line = line.strip() #or someother preprocessing
                if "M /" in line:
                    lines.append(line)
        modify = len(lines)
        return modify

    def countdelete(self):
        lines = []
        with open("changes_python.txt") as file:
            for line in file:
                line = line.strip() #or someother preprocessing
                if "D /" in line:
                    lines.append(line)
        ddelete = len(lines)
        return ddelete

    def countadd(self):
        lines = []
        with open("changes_python.txt") as file:
            for line in file:
                line = line.strip() #or someother preprocessing
                if "A /" in line:
                    lines.append(line)
        add = len(lines)
        return add
        
    def countR(self):
        lines = []
        with open("changes_python.txt") as file:
            for line in file:
                line = line.strip() #or someother preprocessing
                if "R /" in line:
                    lines.append(line)
        r = len(lines)                
        return r        

commits = Commit()
commits.get_commit_list()
commits.countauthor()
commits.countgradle()
commits.countpathlines()
commits.get_commits(data)
commits.countmodify()
commits.countdelete()
commits.countadd()
commits.countR()

#########################################################



        
