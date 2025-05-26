#!/usr/bin/env python3

'''Free Disk Space Funtion'''

# Author ID: 137013231

import os

def free_space():
    cmd = "df -h | grep '/$' | awk '{print $4}'"
    result = os.popen(cmd).read()
    return result.strip()

if __name__ == '__main__':
    print(free_space())
