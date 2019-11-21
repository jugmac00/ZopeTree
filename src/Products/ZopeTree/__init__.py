#
# ZopeTree
#
# Copyright (c) 2001-2003 by Philipp "philiKON" von Weitershausen
#
# This software is distributed under the terms of the Mozilla Public License
# (MPL)
#

from AccessControl import allow_module

__allow_access_to_unprotected_subobjects__ = 1
__roles__ = None

# make ZopeTree module accessible from PythonScript and ZPT
from Products.ZopeTree.ZopeTree import ZopeTree, Node  # noqa
from Products.ZopeTree.TreeObjectWrapper import TreeObjectWrapper  # noqa
allow_module('Products.ZopeTree')
