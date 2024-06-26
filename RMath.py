# A MATHEMATICAL MODULE FOR PYTHON from scratch
"""you can use this functions for your various projects"""
def degtorad(x):
    pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989
    x = x*(float(pi)/180)
    return x
def fact(x):
    # Helper function to compute factorial
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)
def sin(x):
    # Calculate sine using Taylor series
    result = 0
    xnu= degtorad(x)
    for n in range(85):
        term = ((-1) ** n) * (xnu ** ((2 * n )+ 1)) / fact((2 * n) + 1)
        result += term
    return result
def cos(x):
    result = 0
    xnu= degtorad(x)
    for n in range(85):
        term = ((-1) ** n) * (xnu ** (2 * n )) / fact(2 * n)
        result += term
    return result
def tan(x):
    x = sin(x)/cos(x)
    return x
def cot(x):
    x=1/(tan(x))
    return x
def sec(x):
    x = 1/(cos(x))
    return x
def cosec(x):
    x = 1/sin(x)
    return x
def mod(x):
    #modulus function
    if float(x)>0:
        return x
    if x==0 :
        return 0
    else:
        return -x
def signum(x):
    if float(x) > 0:
        return 1
    if float(x) < 0:
        return -1
    else:
        return 0
#prime checker
def prime_check(y):
   for i in range(2,y):
       if y%i==0:
           print(y,"is composite")
           break
       elif y%i!=0:
           print(y,"is prime")
           break
       else:
           print(y,"is neither prime nor composite")
