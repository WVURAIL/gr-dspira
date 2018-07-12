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
from gnuradio import gr
#import h5py
#import time

class spectrometer_output(gr.sync_block):
    """
    docstring for block spectrometer_output
    """

    #def __init__(self, intype, vec_length, filename = "filename", pointing = "AZ,EL", freq_start=1419.0, freq_step=0.002 , notes = 'notes'):

    def __init__(self, f0_gui, samp_rate, ampl_gui, text_gui, save_button_gui):
        self.i = 0
        self.f0 = f0_gui
        self.samp_rate = samp_rate
        self.ampl = ampl_gui
        self.text = text_gui
        self.save_button = save_button_gui
        gr.sync_block.__init__(self,
            name="spectrometer_output",
            in_sig=None,
            out_sig=[np.float32])


    def work(self, input_items, output_items):
        out0 = output_items[0]

        # <+signal processing here+>
        self.i += 1
        out0[:] = self.ampl*np.sin(2*np.pi*self.f0*self.i/self.samp_rate)
        return len(output_items[:])
    
    def set_save_button(self, f0_gui, ampl_gui, text_gui, save_button_gui):
        if save_button_gui == True:
            print(text_gui)
            self.f0 = f0_gui
            self.ampl = ampl_gui
            self.text = text_gui
            self.save_button = False


    #        self.h5.attrs["file_name"] = filename
    #        self.h5.attrs["pointing"] = pointing
    #        self.h5.attrs['freq_start'] = freq_start
    #        self.h5.attrs["freq_step"] = freq_step            
    #        self.h5.attrs["notes"] = notes

        #current_time = time.time()
        
        #if intype == complex:
        #    datatype = np.complex64
        #elif intype == float:
        #    datatype = np.float32
        #elif intype == int:
        #    datatype = np.int32
        #else:
        #    raise
        
        # Not sure how to implement the following:
        # Note: .create_dataset() is an hdf5 command.
        #self.h5 = h5py.File(filename, 'w')
        #self.h5.attrs["file_name"] = filename
        #self.h5.attrs["pointing"] = pointing
        #self.h5.attrs['freq_start'] = freq_start
        #self.h5.attrs["freq_step"] = freq_step
        #self.h5.attrs["notes"] = notes
        #self.h5.attrs["start_time"] = current_time
        
        #self.timeDataset = self.h5.create_dataset('timestamp', (1,1), dtype=np.float64, maxshape=(None,1))
        #self.inputDataset = self.h5.create_dataset('input', (1,1), dtype=np.float64, maxshape=(None,1))
        #self.spectrumDataset = self.h5.create_dataset('spectrum', (1,vec_length), dtype=datatype, maxshape=(None,vec_length))
        #self.n_times = 1
        #self.n = 0
        #self.vec_size = vec_length

        #gr.sync_block.__init__(self,
        #    name="spectrometer_output",
        #    in_sig=[(datatype, vec_length)],
        #    out_sig=None)


    #def work(self, input_items, output_items):
    #    in0 = input_items[0]
    #    in_num = input_items[1]
    #    self.n_times = self.n+1
    #    current_time = time.time()
        #out = output_items[0]
        # <+signal processing here+>
        #out[:] = in0

        #self.timeDataset.resize((self.n_times,1))
    #    self.inputDataset.resize((self.n_times, 1))
    #    self.spectrumDataset.resize((self.n_times,self.vec_size))
    
        #self.timeDataset[self.n] = current_time
    #    self.inputDataset[self.n] = in_num
    #    self.spectrumDataset[self.n] = in0
    #    self.n += 1
    #    return len(output_items[0])

    #def set_filename(self, filename):
    #    if self.filename != filename:
    #        self.h5.attrs["file_name"] = filename
    #        self.h5.attrs["pointing"] = pointing
    #        self.h5.attrs['freq_start'] = freq_start
    #        self.h5.attrs["freq_step"] = freq_step            
    #        self.h5.attrs["notes"] = notes

