def temp_classifier(temp_celsius) 
    if(temp_celsius <-2):\n",
    returnvalue = 0\n",
    elif(temp_celsius >=-2) and (temp_celsius <2):\n",
    returnvalue = 1\n",
    elif(temp_celsius >=2) and (temp_celsius <15):\n",
    returnvalue = 2\n",
    elif(temp_celsius >=15):\n",
    returnvalue = 3\n",
    return returnvalue"