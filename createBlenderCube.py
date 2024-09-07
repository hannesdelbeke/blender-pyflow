# a custom node to create a cube
# couldn't figure out how to easily do multi input slots for e.g. positions (int, int, int)
# standard nodes are manually hooked up in PyFlow\Packages\PyFlowBase\__init__.py

import bpy  # Import Blender Python API to create the cube
from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *

class createBlenderCube(NodeBase):
    def __init__(self, name):
        super(createBlenderCube, self).__init__(name)

        # Exec pins
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, "ExecPin", None, self.compute)
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, "ExecPin")

        # Input pin for cube name
        self.cubeName = self.createInputPin("name", "StringPin")

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType("ExecPin")
        helper.addInputDataType("StringPin")
        helper.addOutputDataType("ExecPin")
        return helper

    @staticmethod
    def category():
        return "Blender"

    @staticmethod
    def keywords():
        return ["create", "cube", "blender"]

    @staticmethod
    def description():
        return "Creates a cube in Blender with the specified name."

    def compute(self, *args, **kwargs):
        # Fetch cube name
        name = self.cubeName.getData()
        if not name:
            name = "Cube"

        # Create a new cube in Blender with default parameters
        bpy.ops.mesh.primitive_cube_add()
        cube = bpy.context.object  # The newly created cube

        # Set cube name
        cube.name = name

        # Move execution to the next node
        self.outExec.call()
