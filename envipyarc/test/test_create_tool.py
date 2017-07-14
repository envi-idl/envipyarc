"""
Tests the Create Tool GPTool
"""
import os
import unittest

import arcpy

class TestCreateTool(unittest.TestCase):
    """Tests the Create Tool GPTool"""

    workspace_dir = None
    output_toolbox = None

    task_name_iso = 'ISODATAClassification'
    tool_name_iso = 'ISODATAClassification_envi'

    task_name_si = 'SpectralIndex'
    tool_name_si = 'SpectralIndex_envi'

    output_toolbox_name = 'test_createtool'
    toolbox_name = 'ENVI Management Tools'
    tool_name = 'CreateTool'
    alias = 'envi'
    gptool_search = '*_envi'

    @classmethod
    def setUpClass(cls):
        """Class setup imports CreateToolbox."""
        # Import HGS toolbox.
        toolbox_path = os.path.join(os.path.dirname(__file__),
                                    '..',
                                    'esri',
                                    'toolboxes',
                                    cls.toolbox_name + '.pyt')
        arcpy.ImportToolbox(toolbox_path)

        cls.workspace_dir = os.path.join(os.path.dirname(__file__), 'workspace')
        if not os.path.isdir(cls.workspace_dir):
            os.mkdir(cls.workspace_dir)

        cls.output_toolbox = os.path.join(cls.workspace_dir,
                                          cls.output_toolbox_name + '.pyt')


    def tearDown(self):
        # Remove pyt file.
        arcpy.RemoveToolbox(self.output_toolbox)

    def setUp(self):
        if os.path.isfile(self.output_toolbox):
            os.remove(self.output_toolbox)

    def test_create_tool(self):
        """Verify create tool generates a GPTool"""
        result = arcpy.CreateENVIToolbox_envi(self.task_name_iso,
                                              self.output_toolbox)

        self.assertEqual(result[0], self.output_toolbox)
        self.assertTrue(os.path.isfile(self.output_toolbox))

        arcpy.ImportToolbox(self.output_toolbox)
        toolbox_list = arcpy.ListToolboxes()
        toolbox_name = '('.join((self.output_toolbox_name, self.alias)) + ')'
        self.assertTrue(toolbox_name in toolbox_list,
                        'Toolbox failed to import')

        envi_tools_list = arcpy.ListTools('*_envi')
        self.assertTrue(self.tool_name_iso in envi_tools_list,
                        'GPTool not created: ' + self.tool_name_iso)

    def test_create_tool_no_extension(self):
        """Verify create tool generates a toolbox without an extension on input."""
        result = arcpy.CreateENVIToolbox_envi(self.task_name_iso,
                                              os.path.splitext(self.output_toolbox)[0])
        self.assertEqual(result[0], os.path.splitext(self.output_toolbox)[0])
        self.assertTrue(os.path.isfile(self.output_toolbox))

        arcpy.ImportToolbox(self.output_toolbox)
        toolbox_list = arcpy.ListToolboxes()
        toolbox_name = toolbox_name = '('.join((self.output_toolbox_name, self.alias)) + ')'
        self.assertTrue(toolbox_name in toolbox_list,
                        'Toolbox failed to import')

        envi_tools_list = arcpy.ListTools('*_envi')
        self.assertTrue(self.tool_name_iso in envi_tools_list,
                        'GPTool not created: ' + self.tool_name_iso)

    def test_create_multi_tool(self):
        """Verify create tool generates a GPTool with Multiple Tasks"""
        result = arcpy.CreateENVIToolbox_envi([self.task_name_iso,
                                               self.task_name_si],
                                              self.output_toolbox)

        self.assertEqual(result[0], self.output_toolbox)
        self.assertTrue(os.path.isfile(self.output_toolbox))

        arcpy.ImportToolbox(self.output_toolbox)
        toolbox_list = arcpy.ListToolboxes()
        toolbox_name = '('.join((self.output_toolbox_name, self.alias)) + ')'
        self.assertTrue(toolbox_name in toolbox_list,
                        'Toolbox failed to import')

        envi_tools_list = arcpy.ListTools('*_envi')
        self.assertTrue(self.tool_name_iso in envi_tools_list,
                        'GPTool not created: ' + self.tool_name_iso)
        self.assertTrue(self.tool_name_si in envi_tools_list,
                        'GPTool not created: ' + self.tool_name_si)
