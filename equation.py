import sys
import numpy


def linear():
    A = numpy.matrix([
        [2, 3, 1],
        [4, 2, 3],
        [7, 1, -1]
    ])
    B = numpy.matrix([4, 17, 1]).T
    print A.I * B
    
    
    # A = numpy.array([
    #     [1, 2, 1],
    #     [2, -1, 3],
    #     [3, 1, 2]
    #     ])

    # B = numpy.array([7, 7, 18])

    print numpy.linalg.solve(A, B)

    return

def test():
    C = numpy.matrix([
        [1, 2, 3],
        [2, 2, 1],
        [3, 4, 3]
        ])

    D = numpy.matrix([
        [2, 1],
        [5, 3]
        ])

    E = numpy.matrix([
        [1, 3],
        [2, 0],
        [3, 1]
        ])

    print C.I * E * D.I
    return

if __name__ == '__main__':
    linear()