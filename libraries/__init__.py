import sys
import os
modules = ['requests', 'envoy']

for module in modules:
    sys.path.insert(0, os.path.abspath('libraries/%s/' % module))