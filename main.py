
import sys
import os 
import argparse
from datetime import datetime

import logging
from logging.handlers import RotatingFileHandler
from os import environ
from os.path import isfile, join, abspath, exists
from sys import argv
from argparse import (ArgumentParser, RawTextHelpFormatter,
                      ArgumentDefaultsHelpFormatter, ArgumentTypeError)

from dotenv import dotenv_values

#from .envctl import parse_env_values
from .proc import start
from .clust import clustering


LOG_FILE_MAX_BYTES = 50e6
LOG_MSG_FMT = "%(asctime)s %(levelname)-8s %(name)s \
%(filename)s#L%(lineno)d %(message)s"
LOG_DT_FMT = "%Y-%m-%d %H:%M:%S"

logger = logging.getLogger("clustering")


class RawDefaultsHelpFormatter(ArgumentDefaultsHelpFormatter, RawTextHelpFormatter):
    """Argparse formatter class"""


def strfile(path):
    """Argparse type checking method
    string path for file should exist"""
    if isfile(path):
        return path
    raise ArgumentTypeError("Input file does not exist")


def strdir(path):
    """Argparse type checking method
    string path for file should exist"""
    if exists(path):
        return path
    raise ArgumentTypeError("Input directory does not exist")



def main():
    """Main method of Parcel Generation Model.
    """

    # command line argument parsing
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawDefaultsHelpFormatter)

    parser.add_argument('ORDERS', type=strfile,
                        help='The path of the orders (xlxs)')

    parser.add_argument('CPs', type=strfile,
                        help='The path of the CPs (xlxs)')

    parser.add_argument('k', type=int,
                        help='number of clusters, k')

    args = parser.parse_args(argv[1:])

    #print(args)
    #print(args.CPs, args.k)
    res = start(args.ORDERS, args.CPs)
    clustering(res,args.k)

if __name__ == "__main__":
    main()


