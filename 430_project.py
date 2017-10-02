from os import listdir #importing os.path module

def cutLink(line,link,VERT=True):
    x=line
    y=x
    x1=link[0][0]
    y1=link[0][1]
    x2=link[1][0]
    y2=link[1][1]
    if VERT:
        if(x < x1 and x>x2)or (x >x1 and x<x2):
            return True
        else:
            return False
    else:
        if (y <y1 and y>y2) or (y>y1 and y<y2):
            return True
        else:
            return False

def func(line,lineCur,vertical):
    cut = 0
    cutMax = 0
    for link in links:
        if link is not None:
            if cutLink(line, link, VERT=vertical):
                # print("hello")
                cut = cut + 1
    if (cut >= cutMax):
        cutMax = cut
        lineCur = line
    return(cutMax)

def Findlinewithmostcut(links,left,right,down,up):
    cutMax=0 #records the max cuts
    lineCur_h=0
    lineCur_v = 0
    lineCur = 0
    line_orientation ="h"
    h_cutmax = 0
    v_cutmax = 0
    h1 = down +0.5
    v1 = left + 0.5
    while (True):
        if h1 > up:
            break
        h_line_cutmax = func(h1, lineCur, vertical=False)
        if h_cutmax<h_line_cutmax:
            h_cutmax = h_line_cutmax
            lineCur_h = h1
        h1 = h1 + 1

    while(True):
        if v1 > right:
            break
        v_line_cutmax = func(v1,lineCur,vertical=True)
        if v_cutmax < v_line_cutmax:
            v_cutmax = v_line_cutmax
            lineCur_v = v1
        v1 = v1 +1
    lineCur = lineCur_h
    cutMax = h_cutmax
    if h_cutmax <= v_cutmax:
        cutMax = v_cutmax
        line_orientation = "v"
        lineCur = lineCur_v
    return(lineCur,cutMax,line_orientation)



if __name__ == '__main__':
    file = listdir("input")  # array
    # this is used to load each instance file given for further use
    for t in file:  # from variable name to name of the list
        points = []  # stores (x,y) for all points
        # for file object to read, use open
        fobj = open("input/" + t, 'r')  # read is r, read and write is rw
        fobj.readline()  # reading the first line of the file
        for L in fobj:
            pnt = L.split(" ")
            points.append([int(pnt[0]), int(pnt[1])])
            # print(L)

        res = []  # stores the number of lines chosen
        links = []  # stores pair( p1,p2) for all pair of points
        # NOTE: Order does not matter here. (p1,p2) and (p2,p1) are the same
        left, right, up, down = 0, 0, 0, 0  # bounds

        for p in points:
            left = min(left, p[0])  # 0 since it is minimum and is stored as that
            right = max(right, p[1])  # 1 since it is maximum and is stored as that
            up = max(up, p[1])
            down = min(down, p[0])

        for i,p1 in enumerate(points):
            for j in range(i,len(points)):
                if p1 is not points[j]:
                    links.append((p1, points[j]))  # tuple is appended

        #print(len(links))  # to find length of links

        sum =0
        while((len(links)-sum) is not 0):
            line,cutMax,line_orientation=Findlinewithmostcut(links,left,right,down,up)
            res.append((line,line_orientation))

            if line_orientation == 'v':
                vertical = True
            else:
                vertical = False

            sum = sum + cutMax
            for s in range(len(links)):
                if links[s] is not None:
                    # print(cutLink(line,links[s],VERT=vertical))
                    if cutLink(line,links[s],VERT=vertical):
                        links[s] = None

        print(len(res),res)

        #This part of the code write the output we get here to the output files
        t=t.split(".")
        write_t = "output_greedy/greedy_solution" + t[0][-2]+t[0][-1]
        write_object=open(write_t,'w')
        write_object.write("%d \n"%(len(res)))
        for line in res:
            write_object.write("%s %f\n"%(line[1],line[0]))
        write_object.close()







