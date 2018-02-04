#!/usr/bin/python
import subprocess
import os
import socket

hostname = socket.gethostname()


def get_data(filename):
    disk = 'sda'
    dict = { }
    data = subprocess.Popen(['tail', '-40', filename],stdout=subprocess.PIPE)
    (out, err) = data.communicate()
    #print type(out)
    for line in out.splitlines():
        #print line
        if 'Reallocated_Sector_Ct' in line:
            dict[line.split()[1]] = line.split()[-1]
        elif 'Reallocated_Event_Count' in line:
            dict[line.split()[1]] = line.split()[-1]
        elif 'Current_Pending_Sector' in line:
            dict[line.split()[1]] = line.split()[-1]
    return {disk : dict}


    #return data.split()

def parser(data):
    #line = subprocess.check_output(['tail', '-1', filename])
    pass


if __name__ == '__main__':
    #tst = get_data('./data/smart_out')
    dict = get_data('./data/smart_out')
    #print tst
    if dict['sda']['Current_Pending_Sector'] > 0:
        print 'Ipat'
        print hostname