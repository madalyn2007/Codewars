#Twice as Old solution
def twice_as_old(dad_years_old, son_years_old): 
    return abs (2 * son_years_old - dad_years_old)
pass

#Volume of A Cuboid solution
def get_volume_of_cuboid(length, width, height):
    return length*width*height
pass

#Grasshopper - Summation solution
def summation(num):
    return sum(range(1, num+1))
pass

#Is the String Uppercase? solution
def is_uppercase(inp):
    if inp == inp.upper():
        return True
    else:
        return False
    
#Remove String Spaces solution
def no_space(x):
    return x.replace(' ', '')