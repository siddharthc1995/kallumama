from operator import itemgetter

with open ('C:\\Users\\Siddharth Choudhary\\Desktop\\acm_output.txt', 'r', encoding='utf-8') as f:
    string=f.read()
    temp= string.split('\n\n')       #spliting each block on empty line and making list
    #print (temp)

    list_of_papers = list()

    i = 0

    for u in temp:
        co=u.split('\n')                 #spliting each block on next line and making list for each line
        #print ((co))

        count=0
        paper = ()
        for var in co:
        #    print(var)
            if var.startswith('#year'):            #how new the paper is
                #print (2017-int(var[2:]))
                paper = paper + (str(2017-int(var[5:])),)
            if var.startswith('#index'):        #index of the paper
                #print (var[6:])
                paper = paper + (var[6:], )
            if var.startswith('#conf'):            #publication venue
                #print (var[2:])
                paper = paper + (var[5:],)
         #   if var.startswith('#%'):            #no. of citations
         #       count=count+1
            if var.startswith('#citation'):  # no. of citations
                paper = paper + (var[10:],)
        #print(count)
      #  paper = paper + (str(count),)
        list_of_papers.append(paper)
        #print(list_of_papers[i])
        i = i + 1

        if i == 20:
            break

    list_of_papers.sort(key=lambda tup: int(tup[3]),reverse=True)
    #list_of_papers.sort(key=itemgetter(3))
    for paper in list_of_papers:
        print(paper)
        print('-----------------------')

