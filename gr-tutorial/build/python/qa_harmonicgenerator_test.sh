#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/dspira/gr-tutorial/python
export PATH=/home/dspira/gr-tutorial/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/dspira/gr-tutorial/build/swig:$PYTHONPATH
/usr/bin/python2 /home/dspira/gr-tutorial/python/qa_harmonicgenerator.py 
