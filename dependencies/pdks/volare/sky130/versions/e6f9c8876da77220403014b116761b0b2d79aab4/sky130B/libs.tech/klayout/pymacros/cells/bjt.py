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
# BJT Generator for skywater130
########################################################################################################################


import pya
from .draw_bjt import *
from .globals import *



class npn_bjt(pya.PCellDeclarationHelper):
    """
    NPN BJT Generator for Skywater130
    """

    def __init__(self):

        # Important: initialize the super class
        super(npn_bjt, self).__init__()
        self.Type_handle = self.param("type", self.TypeList, "type")
        
        for i in BJT_NPN_DEV :
            self.Type_handle.add_choice(i, i)

        
        
        self.param("Model", self.TypeString, "Model", default="sky130_fd_pr__npn",readonly=True)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return str(self.type)
    
    def produce_impl(self):

        # This is the main part of the implementation: create the layout

        self.percision = 1/self.layout.dbu
        #self.cell.flatten(1)
        npn_instance = draw_npn(layout=self.layout,device_name=self.type)
        write_cells = pya.CellInstArray(npn_instance.cell_index(), pya.Trans(pya.Point(0, 0)),
                              pya.Vector(0, 0), pya.Vector(0, 0),1 , 1)
        self.cell.flatten(1)
        self.cell.insert(write_cells)
        self.layout.cleanup()
     
class pnp_bjt(pya.PCellDeclarationHelper):
    """
    PNP BJT Generator for Skywater130
    """

    def __init__(self):

        # Important: initialize the super class
        super(pnp_bjt, self).__init__()
        self.Type_handle = self.param("Type", self.TypeList, "Type")

        for i in BJT_PNP_DEV : 
            self.Type_handle.add_choice(i, i)


        self.param("Model", self.TypeString, "Model", default="sky130_fd_pr__pnp",readonly=True)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return str(self.Type)
    
    def produce_impl(self):

        # This is the main part of the implementation: create the layout

        self.percision = 1/self.layout.dbu
        pnp_instance = draw_pnp(layout=self.layout,device_name=self.Type)
        write_cells = pya.CellInstArray(pnp_instance.cell_index(), pya.Trans(pya.Point(0, 0)),
                              pya.Vector(0, 0), pya.Vector(0, 0),1 , 1)
        self.cell.flatten(1)
        self.cell.insert(write_cells)

        self.layout.cleanup()
