#!/usr/bin/python3

'''
Resolve the n-queens puzzle

'''

def isSafe(m_queen, n_queen, n):
    '''
    Check if the current position is safe to place a queen
    '''
    for i in range(n):
        if m_queen[i] == n_queen or abs(m_queen[i] - n_queen) == abs(i - n_queen):
            return False
    return True

def print_result(m_queen, n):
    '''
    Print the result
    '''
    for i in range(n):
        for j in range(n):
            if m_queen[i] == j:
                print('Q', end='')
            else:
                print('.', end='')
        print()
    print()

def Queen(m_queen, n_queen, n):
    '''
    Place the queens
    '''
    if n_queen == n:
        print_result(m_queen, n)
        return

    for i in range(n):
        if isSafe(m_queen, i, n):
            m_queen[n_queen] = i
            Queen(m_queen, n_queen + 1, n)
        
def solve_nqueens(n):
    '''
    Solve the n-queens puzzle
    '''
    m_queen = [0] * n
    Queen(m_queen, 0, n)



if __name__ == '__main__':

    import sys

    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)
    
    solve_nqueens(n)
