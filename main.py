import os
from BRUTEFORCE import Start_BruteForce as Private

if __name__ == '__main__':
    try:
        os.mkdir('RESULTS')
    except Exception as crot:
        pass
    Private().start()