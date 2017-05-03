with open("testingtesting6a.csv") as inf:
    with open("testingtesting6b.csv", "w") as f1:
        data = []
        author = 'XXXXXXXX'
        countAuthor = 0.0
        for line in inf:
            line = line.split(",")
            if line[0] == author:
                countAuthor = countAuthor + float(line[1])
            else:
                countAuthor = float(line[1])
                author = line[0]
            x = line[0]+","+ str(countAuthor)+"\n"
            f1.write(x)
            #print x



