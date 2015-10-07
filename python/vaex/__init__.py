# -*- coding: utf-8 -*-
try:
	import version
except:
	import sys
	print >>sys.stderr, "version file not found, please run git/hooks/post-commit or git/hooks/post-checkout and/or install them as hooks (see git/README)"
	raise

__release_name__ = "alpha"
__version_tuple__ = version.versiontuple
__program_name__ = "vaex"
__version__ = "%d.%d.%d" % __version_tuple__
__release__ = version.versiontring[:]
__clean_release__ = "%d.%d.%d" % (__version_tuple__)
__full_name__ = __program_name__ + "-" + __release__
__clean_name__ =  __program_name__ + "-" + __clean_release__

import vaex.dataset
#import vaex.plot

def open(path, *args, **kwargs):
	return vaex.dataset.load_file(path, *args, **kwargs)

def server(hostname, **kwargs):
	return vaex.dataset.ServerRest(hostname, **kwargs)

def example():
	import utils
	return vx.open(vx.utils.get_data_file("helmi-dezeeuw-2000-10p.hdf5"))