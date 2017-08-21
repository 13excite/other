import sys
import subprocess as sp
import os
import re


PATH = '/sys/class/enclosure/*/*/device/block/sd*/../../enclosure*/locate'
PATTERN='sd'
def parse_disk_slot(path_to_disk):
    pattern_backplaine = re.compile()
    pattern_slot = re.compile()
    pattern_disk = re.compile()

def get_disk(PATH):
    disk_path = sp.Popen('ls -ld '+PATH, shell=True, stdout=sp.PIPE).communicate()[:-1]
    pass

