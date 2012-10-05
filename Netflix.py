#!/usr/bin/env python

# ---------------------------
# projects/Netflix/Netflix.py
# Copyright (C) 2012
# Darby Perez & Newman Willis
# ---------------------------

# ------------
# Netflix_read
# ------------


def Netflix_read_parameters (r, a) :
    """
    reads two ints that represent tasks and rules into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] >= 0
    return True

def Netflix_read_node (r, a, cache) :
    """
    modifies cache based on rules of successive lines of r
    r is a  reader
    a is an array of int
    cache is a 2 dimensional array of int
    """
    
    for i in range(0, a[1]) :
        s = r.readline()
        l = s.split()
        task = int(l[0])
        if(task <= a[0]) :
            rules = int(l[1])
            for j in range (0, rules) :
                independent = int(l[2 + j])
                cache[task][independent] = 1               
    return cache                 
    assert a[0] > 0
    assert a[1] > 0 
          
          

# ------------
# Netflix_eval
# ------------

def Netflix_eval (tasks, cache) :
    """
    tasks is an int
    cache is a 2 dimsensional array
    return array containing tasks in output order 
    """
    assert tasks > 0
    output = [0] * tasks
    count = 0
    while(count < tasks) :
        for x in range(1, tasks + 1) :
            if (Netflix_no_prereqs(x, tasks, cache)) :
                output[count] = x
                count += 1
                Netflix_remove_tasks(x, tasks, cache)
                cache[x][x] = 1
                break
    assert len(output) > 0
    return output
    
# ------------
# Netflix_remove_tasks
# ------------    

def Netflix_remove_tasks (job, tasks, cache):  
    """
    job is an int
    tasks is an int
    cache is a 2 dimensional array
    """
    assert job > 0
    assert tasks > 0
    for x in range(1, tasks + 1) :
        cache[x][job] = 0
    return cache    

# ------------
# Netflix_no_prereqs
# ------------   
    
def Netflix_no_prereqs (job, tasks, cache) :
    """
    job is an int
    tasks is an int
    cache is a 2 dimensional array
    returns true if no tasks point to job
    """
    assert job > 0
    assert tasks > 0
    for x in range(1, tasks + 1) :
        if(cache[job][x] == 1) :
            return False
    return True
        

# -------------
# Netflix_print
# -------------

def Netflix_print (w, v) :
    """
    prints the value of v
    w is a writer
    v is the order in which the jobs should be executed
    """
    for x in range(0, len(v) - 1) :
        w.write(str(v[x]) + " ")
    w.write(str(v[len(v) - 1]) + "\n")

# -------------
# Netflix_solve
# -------------

def Netflix_solve (r, w) :
    """
    read the parameters of the graph, read the rules pertaining to each node, eval, print loop
    r is a reader
    w is a writer
    """
    
    a = [0, 0]
    while Netflix_read_parameters(r, a) :
        cache = [[0 for x in xrange(a[0] + 1)] for x in xrange(a[0] + 1)]
        cache = Netflix_read_node(r, a, cache)
        v = Netflix_eval(a[0], cache)
        Netflix_print(w, v)