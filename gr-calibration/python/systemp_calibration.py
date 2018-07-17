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

import numpy as np
import datetime
import h5py
from gnuradio import gr

class systemp_calibration(gr.sync_block):
    """
    Horn Calibration.  A single vector stream comes into the block from the spectrometer.
        In:  Data stream of spectra
        Several vectors are output:
        out0: Latest Spectrum - either raw or with calibration, depending on user's choice.
        out1: gain for displaying
        out2: system temperature
             
        The output streams have different possible calibration units????.
            Counts (linear)
            Counts (db)
            Kelvins
    
    Parameters are
    (1) Vector length in Channels
    (3) Collect: user indicates what is to be displayed in live time - uncalibrated spectrum, calibrated spectrum, hot calibration run, cold calibration run
    """
    def __init__(self, vec_length, collect):
        gr.sync_block.__init__(self,
            name="systemp_calibration",
            in_sig=[(np.float32, int(vec_length))],
            out_sig=3*[(np.float32, int(vec_length))])
        
        self.vec_length = int(vec_length)
        self.collect = collect
        self.hot = 2*np.ones(vec_length)   
        self.cold = 1*np.ones(vec_length)
        self.gain = np.ones(vec_length)
        self.tsys = 50*np.ones(vec_length)
        self.thot = 300
        self.tcold = 10
    
    def work(self, input_items, output_items):
        in0 = input_items[0]
        out0 = output_items[0]
        out1 = output_items[1]
        out2 = output_items[2]

        # <+signal processing here+>
        if self.collect == "cal":
            out0[:] = in0/(self.gain) - self.tsys
        elif self.collect == "hot":
            out0[:] = in0
            self.hot[:] = in0
            self.y = self.hot/self.cold
            self.y[self.y == 1] = 2
            self.tsys = (self.thot - self.y*self.tcold)/(self.y-1)
            self.gain = self.cold/(self.tcold + self.tsys)
            self.gain[self.gain <= 0] = 1
            
        elif self.collect == "cold":
            out0[:] = in0
            self.cold[:] = in0
            self.y = self.hot/self.cold
            self.y[self.y == 1] = 2
            self.tsys = (self.thot - self.y*self.tcold)/(self.y-1)
            self.gain = self.cold/(self.tcold + self.tsys)
            self.gain[self.gain <= 0] = 1
        else:
            out0[:] = in0 
        
        out1[:] = self.gain
        out2[:] = self.tsys

        return len(output_items[0])

    def set_parameters(self, collect):
        self.collect = collect
