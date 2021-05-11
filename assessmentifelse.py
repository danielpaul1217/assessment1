def f():
  #creating a boolean identifier and setting it to A
	bool valid = A 
	if valid:
	    z()
	else:
	    s()
	    return False
  #cross checking resulting boolean value with B
	valid = valid and B  		
	if valid:
	    y()
	else:
	    t()
	    return False
  #cross checking resulting boolean value with C
	valid = valid and C  		
	if valid:
	    x()
	else:
	    u()
	    return False
  #cross checking resulting boolean value with D
	valid = valid and D  		
	if valid:
	    w()
	else:
	    v()
  #returning result value of valid
	return valid
