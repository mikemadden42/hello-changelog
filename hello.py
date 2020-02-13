#!/usr/bin/env python3

import os
import sys


def hello():
    print("Hello %s on %s." % (os.getlogin(), sys.platform))


if __name__ == "__main__":
    hello()
