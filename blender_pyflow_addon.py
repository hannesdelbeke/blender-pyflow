bl_info = {
    "name": "PyFlow Integration",
    "blender": (3, 0, 0),
    "category": "Node",
    "location": "Window > PyFlow Node Editor",
    "description": "Launch PyFlow from Blender",
    "version": (1, 0, 0),
    "author": "Your Name"
}

import bpy
import sys
import os
import subprocess

# Ensure PySide6 is used for Qt
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
os.environ["QT_API"] = "pyside6"

# Import necessary PyFlow and Qt modules
from qtpy.QtWidgets import QApplication
from PyFlow.App import PyFlow  # PyFlow main application window

class PyFlowOperator(bpy.types.Operator):
    bl_idname = "wm.launch_pyflow"
    bl_label = "Launch PyFlow"
    
    def execute(self, context):
        # Launch PyFlow within this operator
        self.launch_pyflow()
        self.report({'INFO'}, "PyFlow launched!")
        return {'FINISHED'}
    
    def launch_pyflow(self):
        # Launch PyFlow app
        app = QApplication.instance() or QApplication([])  # Ensure QApplication is only instantiated once
        pyflow_instance = PyFlow.instance(software="standalone")
        pyflow_instance.show()
        app.exec_()

class PyFlowPanel(bpy.types.Panel):
    bl_label = "PyFlow Node Editor"
    bl_idname = "NODE_PT_pyflow"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'PyFlow'
    
    def draw(self, context):
        layout = self.layout
        layout.operator("wm.launch_pyflow", text="Open PyFlow Node Editor")


def menu_func(self, context):
    self.layout.operator(PyFlowOperator.bl_idname, text="PyFlow Node Editor")


def register():
    bpy.utils.register_class(PyFlowOperator)
    bpy.utils.register_class(PyFlowPanel)
    bpy.types.TOPBAR_MT_window.append(menu_func)


def unregister():
    bpy.utils.unregister_class(PyFlowOperator)
    bpy.utils.unregister_class(PyFlowPanel)
    bpy.types.TOPBAR_MT_window.remove(menu_func)


if __name__ == "__main__":
    register()
