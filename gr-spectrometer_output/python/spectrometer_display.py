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

class spectrometer_display(gr.sync_block):
    """
Spectrometer Display.  A single vector stream comes into the block from the spectrometer.
        In:  Data stream of spectra
    Several vectors are output:
        Out: Latest Spectrum - either raw or with calibration, depending on user's choice.
             
        The output streams have different possible calibration units????.
            Counts (linear)
            Counts (db)
            Kelvins
    Parameters are
    1) Vector length in Channels
    2) Notes about observation
    3) Integration Time 
    4) 
    9) Brightness units; one of [Counts (linear), Counts(dB), Kelvins]
    """
    def __init__(self, vec_length, integration, collect):
        gr.sync_block.__init__(self,
            name="spectrometer_display",
            in_sig=[(np.float32, int(vec_length))],
            out_sig=[(np.float32, int(vec_length))])
        
        self.vec_length = int(vec_length)
        #self.notes = notes
        self.integration = integration
        #self.filename = filename
        #self.calibration = calibration
        self.collect = collect
        #self.stop_button = stop_button
        #self.save_button = save_button
        #self.write_to_file = write_to_file

        self.hot = 1
        self.cold = 0

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        print(np.shape(in0))
        
        #out1 = output_items[1]
       
        # <+signal processing here+>

        if self.collect == "cal":
            out[:] = in0*(self.hot)/(self.cold+5)
        elif self.collect == "hot":
            out[:] = 5
            self.hot = 5
            #print(self.hot)
        elif self.collect == "cold":
            out[:] = 2
            self.cold = 2
        else:
            out[:] = in0 
        
        return len(output_items[0])

    def set_parameters(self, integration, collect):
        self.integration = integration
        #self.calibration = calibration
        self.collect = collect
        #self.stop_button = stop_button

        #if self.calibration == "No":
        #    filename = self.filename + "." + str(current_time)
        #elif self.calibration == "hot":
        #    self.filename = filename + "." +"hot"
        #else:
        #    self.filename + "." +"cold"

     
        #if self.save_button == True:
        #    if self.calibration == "No":
        #        filename = self.filename + "." + str(current_time)
        #    elif self.calibration == "hot":
        #        self.filename = filename + "." + "hot"
        #    else:
        #        self.filename + "." + "cold"
        #    self.save_button = False