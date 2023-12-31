# Copyright 2022 Mabrains LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

########################################################################################################################
# RF DEVICES Generator for skywater130
########################################################################################################################

import pya
from .draw_rf import *
from .globals import *

class rf_mosfet(pya.PCellDeclarationHelper):
    """
    rf mosfet Generator for Skywater130
    """

    def __init__(self):

        # Important: initialize the super class
        super(rf_mosfet, self).__init__()
        self.Type_handle = self.param("Type", self.TypeList, "Type")
       
        for i in RF_MOSFET_DEV :
            self.Type_handle.add_choice(i, i)
        
        
        self.param("Model", self.TypeString, "Model", default="sky130_fd_pr__",readonly=True)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return str(self.Type)

    def produce_impl(self):

        # This is the main part of the implementation: create the layout

        self.percision = 1/self.layout.dbu
        rf_mos_instance = draw_rf_mosfet(layout=self.layout,device_name=self.Type)
       
        write_cells = pya.CellInstArray(rf_mos_instance.cell_index(), pya.Trans(pya.Point(0, 0)),
                              pya.Vector(0, 0), pya.Vector(0, 0),1 , 1)
        self.cell.flatten(1)
        self.cell.insert(write_cells)
        
        self.layout.cleanup()
    
class rf_bjt(pya.PCellDeclarationHelper):
    """
    rf bjt Generator for Skywater130
    """
    
    def __init__(self):

        # Important: initialize the super class
        super(rf_bjt, self).__init__()
        self.Type_handle = self.param("Type", self.TypeList, "Type")
        for i in RF_BJT_DEV :
            self.Type_handle.add_choice(i, i)
        
        
        self.param("Model", self.TypeString, "Model", default="sky130_fd_pr__",readonly=True)
    

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return str(self.Type)

    def produce_impl(self):

        # This is the main part of the implementation: create the layout

        self.percision = 1/self.layout.dbu
        rf_bjt_instance = draw_rf_bjt(layout=self.layout,device_name=self.Type)
       
        write_cells = pya.CellInstArray(rf_bjt_instance.cell_index(), pya.Trans(pya.Point(0, 0)),
                              pya.Vector(0, 0), pya.Vector(0, 0),1 , 1)
        self.cell.flatten(1)
        self.cell.insert(write_cells)
        
        self.layout.cleanup()


class rf_coils(pya.PCellDeclarationHelper):
    """
    rf coils Generator for Skywater130
    """

    def __init__(self):

        # Important: initialize the super class
        super(rf_coils, self).__init__()
        self.Type_handle = self.param("Type", self.TypeList, "Type")
        for i in RF_COILS_DEV :
            self.Type_handle.add_choice(i, i)
        
        
        self.param("Model", self.TypeString, "Model", default="sky130_fd_pr__",readonly=True)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return str(self.Type)

    def produce_impl(self):

        # This is the main part of the implementation: create the layout

        self.percision = 1/self.layout.dbu
        rf_coils_instance = draw_rf_coils(layout=self.layout,device_name=self.Type)
       
        write_cells = pya.CellInstArray(rf_coils_instance.cell_index(), pya.Trans(pya.Point(0, 0)),
                              pya.Vector(0, 0), pya.Vector(0, 0),1 , 1)
        self.cell.flatten(1)
        self.cell.insert(write_cells)
        
        self.layout.cleanup()
    