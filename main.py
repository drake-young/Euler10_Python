from timeit import default_timer
from math import sqrt



# ===========================================================
# FUNCTION -- generate_primes
# ===========================================================
#
# INPUT:    n where n is the largest possible value to be
#           considered in the generation
#
# OUTPUT:   Returns a list containing all prime numbers <=n
#
# TASK:     Generate a list of all prime numbers <= the parameter
#           n. The algorithm acts as a sieve of Eratosthenes,
#           utilizing list slicing and generator functions to
#           replace entire list segments rather than one index
#           at a time
#
# NOTES:
#   Prime algorithm retrieved from:
#       https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
#
#   Algorithm Posted By User: Robert William Hanks
#
#   This algorithm was used because it was claimed to be the
#   most efficient, and after runtime testing, this was confirmed.
#
#   Prior to this algorithm being used, the sieve of Eratosthenes
#   via two nested for loops was programmed instead.
#
#   The use of this external algorithm has no impact on accuracy,
#   only runtime performance
#
# ===========================================================
def generate_primes( n ):
    """ Returns  a list of primes < n """
    sieve  =  [ True ] * n
    for i in range( 3 , int( sqrt( n ) ) + 1 , 2 ):
        if sieve[ i ]:
            sieve[ i * i : : 2 * i ] = [ False ] * ( ( n - ( i * i ) - 1 ) // ( 2 * i ) + 1 )
    return [ 2 ] + [ i for i in range( 3 , n , 2 ) if sieve[ i ] ]



# ===========================================================
# PROBLEM 10 -- Summation of primes
# ===========================================================
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
#
# Find the sum of all primes below two million
#
# ===========================================================
def problem_10( ):
    # Print Problem Context
    print( "Project Euler Problem 10 -- Summation of Primes" )

    # Computation (results and runtime)
    start_time      =  default_timer( )
    result          =  sum( generate_primes( 2000000 ) )
    end_time        =  default_timer( )
    execution_time  =  ( end_time - start_time ) * 1000

    # Display Results
    print( "   Sum of all primes below 2,000,000:   %d"      %  result )
    print( "   Computation Time:                    %.3fms"  %  execution_time )
    return



if __name__ == '__main__':
    problem_10( )