import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description='Splits an interleaved FASTQ (input in STDIN) into first and second read files')
    parser.add_argument('first')
    parser.add_argument('second')
    args = parser.parse_args()

    pipeForward = os.open(args.first, os.O_WRONLY)
    pipeReverse = os.open(args.second, os.O_WRONLY)

    i = 0
    forward = True
    for line in sys.stdin:
        if forward:
            os.write(pipeForward, line)
        else:
            os.write(pipeReverse, line)
        i += 1
        if i == 4:
            forward = not forward
            i = 0
    
if __name__ == '__main__':
    main()
