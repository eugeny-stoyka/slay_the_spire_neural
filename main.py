# -*- coding: utf-8 -*-

import sys

from common.support.parser import parser

if sys.version[0] == '2':
    raise Exception("Только для третьей версии python, сейчас используется: \n" + str(sys.version))

if __name__ == "__main__":
    options, _ = parser.parse_args()
    print(options)