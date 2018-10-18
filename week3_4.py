
# coding: utf-8

# # The results for theory question
# Question1:
# I think the algorithm is a sequence of steps for solving a computational problem which will produce the correct output using basic steps in finite time.
# ScreenPlay:
# (1)Start condition: 
#     I want to see a movie;
#     I have enougth money to buy a ticket;
#     I can get the cinema correctly;
# (2)Roles
#    watcher(I), the ticket seller, the doorman,the projector;the shopkeeper(if I need eating something)
# (3)Props
#    ticket;chairs,money;
# (4)Scenes
#    (a)arriving at the cinema
#     I choose which movies to see, then choose the suitable time and cinema
#     I decide how to get to the cinema,such as taking bus,taxi or subway;
#     I find the entrance to ciname, then find the ticket office;\
#     
#    (b)buying the movie ticket
#     I walk to the ticket office and tell seller which movie to see;
#     then I take out money to seller;
#     the seller give me the ticket and change;
#     I get the ticket;
#     
#    (c)looking for an entrance
#       I will look for the entrance by singals and get into;
#       I give the ticket to the doorman
#       The doorman chech the ticket;
#       I get into the house;
#    (d)waiting for the start of movie
#       I find the right line and chair;
#       I sit down and wait;
#    (e)leaving the cinema
#       I take away the rubbish
#       I leave the cinema from exit
# (5)Result
#    I saw a movie;
#    I am in a good humor;
# 
# Question2
# we should't let corn and duck get together
# The steps to solve the problem below:
# (State1) The rower takes the corn to right side;
# (State2)The rower puts down the corn and returns to left side ;
# (State3) The rower takes the wolf to right side ;
# (State4) The rower puts down the wolf and returns to the left side;
# (State5) The rower takes the farmer to the right side;
# (Satae6) The rower puts down the farmer and returns to the left side;
# (State7) The rower takes the duck to the right side;
# Successly!
# 
# Question3
#  In good formulation,if we know the final goals, it is useful for us to know that which aspects matter and which aspects can be left out. Then we can determine how to manipulate the important aspects and ignore the other aspects.
# 
# Question4
# ![image.png](attachment:image.png)
# 
# Question5
# ![image.png](attachment:image.png)
# 
# (c) The bidirectional search is veryuseful because the only successor of n is ground(n/2); Then the branching factor is 2 in the forward direction and is 1 in the reverse direction.
# (d) Yes, it just need start from the gaol and apply simple reverse sussessor until it searchs 1.
# (e) It just need search from root,left,right.
# 

# # Programming Exercises
# 

# In[1]:

#Question1---solving a classic ancient Chinese puzzle
chicken=0
while chicken<=35:
    rabbit=0
    while rabbit<=35:
        if 2*chicken+4*rabbit==94 and chicken+rabbit==35:
            print("There are",chicken,"chicken; There are" ,rabbit,"rabbits")
        rabbit+=1
    chicken+=1


# In[ ]:

#Question2
def search():  
    socialnet["you"] = ["Alice", "Bob", "Claire"]
    socialnet["Bob"] = ["Anuj", "Peggy"]
    socialnet["Alice"] = ["Peggy"]
    socialnet["Claire"] = ["Thom", "Jonny"]
    socialnet["Anuj"] = []
    socialnet["Peggy"] = []
    socialnet["Thom"] = []
    socialnet["Jonny"] = []

def runDFS():
    
    mark = []
    queue = []
    queue += socialnet["you"]
    
    while queue:
        pop = queue.pop()
        
        if not pop in mark:
            if pop[-1] == 'm':
                print("We found it! "+ pop +" is a mango seller.")
                return
            else:
                queue += socialnet[pop]
                mark.append(pop)
    print("There is no mango seller.")


from collections import deque

def runBFS():
    
    mark = []
    queue = deque()
    queue += socialnet["you"]
    
    while queue:
        pop = queue.popleft()
        
        if not pop in mark:
            if pop[-1] == 'm':
                print("We found it! "+ pop +" is a mango seller.")
                return
            else:
                queue += socialnet[pop]
                mark.append(pop)
    print("There is no mango seller.")

search()
runDFS()
search()
runBFS()


# In[21]:

#Question3_DFS for DLL files on the C disk 

#-*- coding: utf-8 -*-

import os

def dfsStack(path):
    
    filestack=[]
    filestack.append(path)
    while len(filestack)>0:
        filePath=filestack.pop()
        fileList = os.listdir(filePath)
     #   print(fileList)
        for i in fileList:
            fileTypes=os.path.join(filePath, i)
            if os.path.isdir(fileTypes):
                print(i)
                filestack.append(fileTypes)
            else:
                print(i)
path="C:\\Users"       
dfsStack(path)         


# In[25]:

# Question3_Searching for a particular filename

#-*- coding: utf-8 -*-


import os
import sys
 
def searchFile(path,name):
    for root, dirs, files in os.walk(path):  # path is root for filename
        if name in dirs or name in files:
            flag = 1      #tell whether there exists a target filename
            root = str(root)
            dirs = str(dirs)
            return os.path.join(root, dirs)
    return -1

print("Please entry the filename needing searching:")
path=input()
name = sys.stdin.readline().rstrip()  #selecting the rank and Enter Pattern
answer = searchFile(path,name)
if answer == -1:
    print("Not such filename!")
else:
    print(answer)


# In[33]:

#Question4_BFS for DLL files on the C disk 
#-*- coding: utf-8 -*-

import os

def bfsQueue(path, dirCallback = None, fileCallback = None):

    queue = []  
    ret=[]
    queue.append(path,)   
    while len(queue) > 0:       
        tmp = queue.pop()       
        if(os.path.isdir(tmp)):         
            ret.append(tmp)          
            for item in os.listdir(tmp):           
                queue.append(os.path.join(tmp, item))          
            if dirCallback:              
                dirCallback(tmp)     
        elif(os.path.isfile(tmp)):          
            ret.append(tmp)         
            if fileCallback:           
                fileCallback(tmp)   
    return ret 
def printDir(path):  
    print ("dir: " + path)
def printFile(path):  
    print ("file: " + path) 
b = bfsQueue(r'C:\Users', printDir, printFile)


