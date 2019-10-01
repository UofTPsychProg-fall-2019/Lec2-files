#!/usr/bin/env python3

#%% FOR LOOPS: a gentle introduction

# task: print out each value of nums in sequence
nums = [1,3,5,8]


# try 1: lots of repeated code
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])


# try 2: repeated code, but now is exactly the same
x = 0
print(nums[x])
x = 1
print(nums[x])
x = 2
print(nums[x])
x = 3
print(nums[x])


# try 3: FOR LOOP with indexing
for x in range(4):
    print('x:',x)
    print('nums[x]:',nums[x])



# try 4: FOR LOOP with iterable
for x in nums:
    print(x)
    

for x in range(25,10,-3):
    print(x)

#%%
# YOUR TURN #1: sum a list of numbers

nums = [1,3,5,8]
sumnums = 0
for n in nums:
    sumnums+=n
print(sumnums)


#%%
# YOUR TURN #2: use a for loop to decide whether or not to 
# exclude subject due to bad RTs

subject_rt = [508,423,80,15,2389,987,758,466,772,1203]
nrt = len(subject_rt)
nbad = 0
for rt in subject_rt: 
    print(rt)
    if rt<150 or rt>2000:
        nbad+=1
if nbad>(nrt*0.15):
    print('EXCLUDE!')

#%%
# YOUR TURN #3: excluding subjects due to bad RTs
# use a for loop inside a for loop! 

# list of RTs, each list is from a separate subject
subject_rts = [[508,423,80,15,2389,987,758,466,772,1203],
               [765,563,433,833,398,486,546,557,2109,983],
               [432,543,299,359,348,413,321,524,580,418]]
nsbj = len(subject_rts)   # number of subjects
nrt = len(subject_rts[0]) # number of RTs per subject
exc_crit = 0.15           # max proportion of RTs to keep subject
exc_sbj = []
nbads = []
for s in range(nsbj): # loop through subjects, i.e. [0,1,2] 
    subject_rt = subject_rts[s]
    nbad = 0
    for rt in subject_rt: 
        if rt<150 or rt>2000:
            nbad+=1
    nbads.append(nbad)
    if nbad>(nrt*0.15):
        exc_sbj.append(1)
    else:
        exc_sbj.append(0)
print(exc_sbj)



#%%
# WHILE LOOPS

x = 0
while x<10:
    print(x)
    x = x+1

    
        
#%%
# Using break and continue within loops
    
even = []
x = 0
while True:
    x = x+1
    if x%2 is not 0:
        print('GROSS!',x,'is odd, skipping!')
        continue
    
    print('YAY!',x,'is even, keeping!')
    even.append(x)
    
    if x>=21:
        break
print(even)



#%%
# indexing multidimensional numpy arrays
#
import numpy as np
data = np.array([[1,1,2,3],[1,4,5,6],[2,7,8,9],[2,10,11,12]])
# select second row
data[1]
# select second column
data[:,1]
# select rows that begin with 2 (i.e., logical indexing)
data[data[:,0]==2,:]



#%%
# YOUR TURN #4: median RT for each subject using numpy

# list of RTs, each list is from a separate subject
subject_rts = [[508,423,80,15,2389,987,758,466,772,1203],
               [765,563,433,833,398,486,546,557,2109,983],
               [432,543,299,359,348,413,321,524,580,418]]
np.median(subject_rts,axis=1)


#%%
# data file columns: subject, trial, condition, correct, RT
#
data = np.empty((0,5))
for x in ['1','2','3']:
    filename = 'datafile'+x+'.csv'
    print(filename)
    tmp = sp.loadtxt(filename,delimiter=',')
    data = np.vstack([data,tmp])



#%%
# finding and copying files    
import os
import shutil
# find and copy important_file.txt from directory1 to directory2
filepath = os.path.join('directory1','important_file.txt')
newpath = os.path.join('directory2','important_file.txt')
shutil.copyfile(filepath,newpath)



#%%
# formatting strings for output

acc = np.array([0.87,0.95])
mrt = np.array([486.5, 407.0])

# just numbers
print('subject 1:',str(acc[0]),str(mrt[0]),str(acc[1]),str(mrt[1]))

# formatted! but that was a lot of work
print('subject 1: '+str(100*acc[0])+'% '+str(mrt[0])+'ms '+
                    str(100*acc[1])+'% '+str(mrt[1])+'ms')

# oh easier formatting
print('subject 1: {}% {}ms {}% {}ms'.format(100*acc[0],mrt[0],100*acc[1],mrt[1]))

# all inline!
print(f'subject 1: {100*acc[0]}% {mrt[0]}ms {100*acc[1]}% {mrt[1]}ms')


#%%
# formatting specific notation for output

cond1 = 'blocked'
rep1 = 4
acc1 = 0.7872395342
rt1 = 482.333333333

# some many numbers after the decimal
print('{}, {} reps: {}% {}ms'.format(cond1,rep1,100*acc1,rt1))

# just the right amount
print('{:s}, {:d} reps: {:.2f}% {:.1f}ms'.format(cond1,rep1,100*acc1,rt1))

# all inline!
print(f'{cond1:s}, {rep1:d} reps: {100*acc1:.2f}% {rt1:.1f}ms')


#%%
# writing output to a file
sbj = np.array([1,2,1,2])
cond = np.array([1,1,2,2])
acc = np.array([0.873,0.945,0.761,0.724])
mrt = np.array([486.5,407.0,545.0,608.5])
alldata = np.vstack([sbj,cond,acc,mrt]).T
np.savetxt('subject_summary.txt',alldata,fmt='%d %d %.3f %.1f')


#%% 
# writing a custom function
def mike(ate_lunch=True,cats=2):
    """
    Super helpful function about Mike.
    
    Parameters
    ----------
    ate_lunch : Did Mike eat lunch? The default is True.
    cats : How many cats does Mike own. The default is 2.    
    """
    if not ate_lunch:
        print('Mike is hungry.')
    else:
        print('Mike ate lunch. He is still hungry.')
        
    print('Mike has {} cats'.format(cats))
 
    
#%%
# using a custom function
mike()
mike(ate_lunch=False)    
mike(cats=48)
help(mike)
