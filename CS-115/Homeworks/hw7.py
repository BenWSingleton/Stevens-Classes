''' Created on: 10/17/2019
          Name: Benjamin Singleton
        Pledge: I pledge my honor that I have abided by the Stevens Honor System'''

from cs115 import *

def numToBaseB(N,B):
    answer=nTBBhelper(N,B)
    if N==0:
        return '0'
    else:
        return answer
    
def nTBBhelper(N,B):
    if int(N)==0:
        return ''
    else:
        return nTBBhelper(N//B, B)+str(N%B)

def baseBToNum(S, B):
    if S=='':
        return 0
    elif S[-1]==0:
        return 0
    else:
        return B*(baseBToNum(S[:-1], B))+int(S[-1])

def baseToBase(B1,B2,SinB1):
    value=baseBToNum(SinB1, B1)
    return numToBaseB(value, B2)

def add(S,T):
    val1=baseBToNum(S, 2)
    val2=baseBToNum(T, 2)
    val3=val2+val1
    return numToBaseB(val3, 2)

def addZeros(S1, S2):
    if len(S1)!=len(S2):
        if len(S1)>len(S2):
            diff=len(S1)-len(S2)
            return (S1, ('0'*diff)+S2)            
        else:
            diff=len(S2)-len(S1)
            return (('0'*diff)+S1, S2)
    else:
        return (S1, S2)

def removeZeros(S1):
    if S1[0]=='1':
        return S1
    else:
        return removeZeros(S1[1:])

def addB(S1, S2):
    (S1, S2)=addZeros(S1, S2)
    def helper(S1, S2, carry):
        if S1=='':
            return carry
        else:
            total=FullAdder[S1[-1], S2[-1], carry]
            return helper(S1[:-1], S2[:-1], total[1])+total[0] 
    return removeZeros(helper(S1, S2, carry='0'))

FullAdder ={ ('0','0','0') : ('0','0'),('0','0','1') : ('1','0'),('0','1','0') : ('1','0'),('0','1','1') : ('0','1'),('1','0','0') : ('1','0'),('1','0','1') : ('0','1'),('1','1','0') : ('0','1'),('1','1','1') : ('1','1') }
    
