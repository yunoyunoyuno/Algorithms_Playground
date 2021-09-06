{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "Event = [[0,1,0,1,0,0],\n",
    "         [0,0,0,1,0,1],\n",
    "         [1,0,0,1,0,1],\n",
    "         [0,0,0,0,0,0],\n",
    "         [1,0,0,1,0,0],\n",
    "         [0,1,0,1,0,0]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Person 4 is a celebrity.\n"
     ]
    }
   ],
   "source": [
    "#Brute Force\\\n",
    "def ans(E):\n",
    "    a = CelebCheck(E);\n",
    "    if(a >= 0) : print(\"Person\",a+1,\"is a celebrity.\");\n",
    "    else: print(\"There is no Celebrity in this event.\")\n",
    "        \n",
    "def CelebCheck(E):\n",
    "    n = len(E);\n",
    "    for i in range(n):\n",
    "        for j in range(n):\n",
    "            if(i != j and (E[i][j] == 1 or E[j][i] == 0)): break\n",
    "        if(j == n-1): return i;\n",
    "    return -1\n",
    "\n",
    "ans(Event)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Person 4 is a celebrity.\n"
     ]
    }
   ],
   "source": [
    "#Devide and Conquer n/2 , n/2\n",
    "\n",
    "def ans(E):\n",
    "    a = FindCelebRecursive(E,0,len(E)-1);\n",
    "    if(a >= 0) : print(\"Person\",a+1,\"is a celebrity.\");\n",
    "    else: print(\"There is no Celebrity in this event.\")\n",
    "\n",
    "def celeb_check(E,k,L,R):\n",
    "    for i in range(L,R+1): \n",
    "        if E[i][k] == 0 or E[k][i] == 1: return -1;\n",
    "    return k;\n",
    "\n",
    "def FindCelebRecursive(E,l,r):\n",
    "    if(l == r): return l;\n",
    "    n = len(E); mid = (l+r)//2;\n",
    "    lc = FindCelebRecursive(E,l,mid);\n",
    "    if(lc >= 0): lc = celeb_check(E,lc,mid+1,r);\n",
    "    if(lc >= 0): return lc;\n",
    "    rc = FindCelebRecursive(E,mid+1,r);\n",
    "    if(rc >= 0): rc = celeb_check(E,rc,l,mid);\n",
    "    return rc;\n",
    "\n",
    "ans(Event)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Person 4 is a celebrity.\n"
     ]
    }
   ],
   "source": [
    "# Devide and Conquer 1, n-2, 1\n",
    "def ans(E):\n",
    "    a = check(E);\n",
    "    if(a >= 0) : print(\"Person\",a+1,\"is a celebrity.\");\n",
    "    else: print(\"There is no Celebrity in this event.\")\n",
    "        \n",
    "def isCeleb(E,left,right):\n",
    "    if (left == right) : return left;\n",
    "    if(E[left][right] == 1):\n",
    "        return isCeleb(E,left+1,right);\n",
    "    return isCeleb(E,left,right-1)\n",
    "\n",
    "def check(E):\n",
    "    k = isCeleb(E,0,len(E)-1)\n",
    "    for i in range(len(E)):\n",
    "        if(i != k and E[k][i] == 1 and E[i][k] == 0): return -1\n",
    "    return k\n",
    "ans(Event)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
