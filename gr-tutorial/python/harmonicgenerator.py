#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class harmonicgenerator(gr.sync_block):
    """
    docstring for block harmonicgenerator
    """
    def __init__(self, n_outputs, vec_length, ampl, f0, n_harmonics, samprate):
        self.i = numpy.arange(vec_length)
        self.n_outputs = n_outputs
        self.vec_length = vec_length
        self.ampl = ampl
        self.f0 = f0
        self.n_harmonics = n_harmonics
        self.samprate = samprate
        gr.sync_block.__init__(self,
            name="harmonicgenerator",
            in_sig=None,
            out_sig=n_outputs*[(numpy.float32, vec_length)])

    def work(self, input_items, output_items):
        self.i += self.vec_length
        for m in range(self.n_outputs):
            out = output_items[m]
            out[:] = self.ampl[m]*numpy.sin(2*numpy.pi*self.n_harmonics[m]*self.f0*self.i/self.samprate)
            # out[0] = output_items[0]
            # out[1] = output_items[1]
            # out[0] = numpy.sin(2*numpy.pi*self.f0*self.i/self.samprate)
            # out[1] = numpy.sin(2*numpy.pi*self.n*self.f0*self.i/self.samprate)
        return len(output_items[:])

    def set_amplitude(self, amplitude):
        self.ampl = amplitude
