inf = 'y_input.xml'

INF = open(inf,'r')
c = 0
outstring = ''
for x in INF:
    if x.strip() == '<phrase>':
        c += 1
        #print "new phrase ", c;
        
    elif x.strip() == '</phrase>':
        print outstring
        outstring = ''

    elif '<yid>' in x:
        outstring = x[6:-7]
    elif '<eng>' in x:
        outstring += '\t'+x[6:-7]

    else:
        #print "miss:"+x.strip()+"|"
        pass
    





    
