{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1c1a82c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "All values should be numbers\n",
      "\n",
      "What is the year? 1700\n",
      "What is the month? 1\n",
      "What is the day? 4\n",
      "\n",
      "2341975.5\n"
     ]
    }
   ],
   "source": [
    "print(\"All values should be numbers\")\n",
    "print()\n",
    "\n",
    "# Getting the values for the year, month and day\n",
    "Y = eval(input(\"What is the year? \"))\n",
    "M = eval(input(\"What is the month? \"))\n",
    "D = eval(input(\"What is the day? \"))\n",
    "\n",
    "# Using the JD formula\n",
    "JD = 367 * Y - 7 * (Y + (M + 9)//12)//4 - 3 * ((Y + (M - 9)//7)//100 + 1)//4 + (275 * M)//9 + D + 1721029 - 0.5\n",
    "\n",
    "print()\n",
    "print(JD)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "901ec419",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
