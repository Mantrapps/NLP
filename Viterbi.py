'''
Homework-2
HMM Decoding: Viterbi Algorithm
Author: Kai Zhu kxz160030@utd
'''


import sys


#contain the state observation likelihood
#         0:hot, 1:cold
#   0  1
#   1  2
#   2  3
bMatrix={'Hot':[0.2,0.4,0.4],'Cold':[0.5,0.4,0.1]}

#Transaction matrix
transDic={('Start','Hot'):0.8,('Start','Cold'):0.2,('Hot','Hot'):0.7,('Hot','Cold'):0.3,('Cold','Hot'):0.4,('Cold','Cold'):0.6};

def viterbi(obs, state):
    '''
    :param obs: observations
    :param state: state [HOT, COLD]
    :return:  best path
    '''
    print ''
    #build viterbiMatrix
    viterbiMaxtrix=list()
    for i in range(len(state)+2):
        row=[0]*(len(obs)+2)
        viterbiMaxtrix.append(row)

    for i in range(1,len(viterbiMaxtrix)-1):
        viterbiMaxtrix[i][0]=state[i-1]

    for i in range(1,len(viterbiMaxtrix[0])-1):
        viterbiMaxtrix[0][i]=int(obs[i-1])

    viterbiMaxtrix[0][0]='Start'


    #initialization step
    for i in range(1,len(viterbiMaxtrix)-1):
        viterbiMaxtrix[i][1]=(transDic[('Start',viterbiMaxtrix[i][0])]*bMatrix[viterbiMaxtrix[i][0]][int(viterbiMaxtrix[0][1])-1],0)
    #recursion step
    #col
    for i in range(2,len(obs)+1):
        #row
        for j in range(1,len(viterbiMaxtrix)-1):
            maxVal = 0
            pre = ''
            for k in range(1,len(viterbiMaxtrix)-1):
            # get the max
                tempVal=transDic[(viterbiMaxtrix[k][0],viterbiMaxtrix[j][0])]*bMatrix[viterbiMaxtrix[j][0]][int(viterbiMaxtrix[0][i])-1]
                tempVal*=viterbiMaxtrix[k][i-1][0]
                if tempVal>maxVal:
                    maxVal=tempVal
                    pre=k
            viterbiMaxtrix[j][i]=(maxVal,pre)

    #termination
    finsihVal=0
    pre=''
    for k in range(1, len(viterbiMaxtrix)-1):
        tempVal=viterbiMaxtrix[k][len(viterbiMaxtrix[0])-2]
        if tempVal>maxVal:
            maxVal=tempVal
            pre=k
    viterbiMaxtrix[len(viterbiMaxtrix)-1][len(viterbiMaxtrix[0])-1]=(maxVal,pre)

    #return
    col=len(viterbiMaxtrix[0])-1
    row=len(viterbiMaxtrix)-1
    result=[]

    while col>0:
        pre=viterbiMaxtrix[row][col][1]
        print pre
        result.insert(0,viterbiMaxtrix[pre][0])
        row=pre
        col-=1

    return result

s
def main(arg):
    #input could be any length from 0 to 10;
    print arg[1]
    #output
    print "Observation(input):", arg[1]
    print "Weather(output):", viterbi(arg[1],["Hot","Cold"]);
    pass





if __name__ == '__main__':
   main(sys.argv)

