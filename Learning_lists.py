{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[100, 200, 7, 8, 9], [100, 5, 4, 3, 2, 1], [10, 11, 12, 13, 14, 15]]"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = [100,5,4,3,2,1]\n",
    "b = [100,200,7,8,9]\n",
    "c = [10,11,12,13,14,15]\n",
    "d = [b,a,c]\n",
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[100, 200, 7, 8, 9], [100, 5, 4, 3, 2, 1], [10, 11, 12, 13, 14, 15]]"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#sort main list in descending order\n",
    "d.sort(reverse=True)\n",
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[7, 8, 9, 100, 200], [1, 2, 3, 4, 5, 100], [10, 11, 12, 13, 14, 15]]"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#sort lists inside the list\n",
    "for i in d:\n",
    "    i.sort()\n",
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 12, 14]"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#print alternate elements of last list in the list\n",
    "d[-1][0:len(d[-1]):2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[7, 8, 9, 100, 200], [1, 2, 3, 4, 5, 100], [10, 11, 12, 13, 14, 15]]"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[7, 8, 9, 100, 200], [1, 2, 3, 4, 5, 100], [10, 11, 12, 13, 14, 15]]"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#why are this and the below sorts getting same result??\n",
    "d[::1].sort(reverse=True)\n",
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[7, 8, 9, 100, 200], [1, 2, 3, 4, 5, 100], [10, 11, 12, 13, 14, 15]]"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d[::1].sort(reverse=False)\n",
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[7, 8, 9, 100, 200], [1, 2, 3, 4, 5, 100], [10, 11, 12, 13, 14, 15]]"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#reverse lists within the list\n",
    "for i in d:\n",
    "    i.reverse()\n",
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[7, 8, 9, 100, 200]"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d[::1][1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[7, 8, 9, 100, 200], [1, 2, 3, 4, 5, 100], [10, 11, 12, 13, 14, 15]]"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#list comprehension operation\n",
    "[i.reverse() for i in d]\n",
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#find the position of first occurence of pattern in list\n",
    "a = [1,2,3,4,'abc','def','abc',5,6,7,4]\n",
    "a.index(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.index('abc')"
   ]
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
