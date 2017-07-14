"""
Tests the ENVI Py config module
"""

import os
import unittest

import arcpy

import envipyengine
import envipyengine.config


class TestConfigTool(unittest.TestCase):
    """Tests the Create Tool GPTool"""

    output_toolbox = None
    toolbox_name = 'ENVI Management Tools'
    tool_name = 'ConfigureENVI'
    alias = 'envi'
    engine_value = ''
    path_value = '+C:\\mycode'
    compile = '--compile'

    _ENGINE = 'engine'
    _ENGINE_ARGS = 'engine-args'
    _IDL_PATH = 'IDL_PATH'

    @classmethod
    def setUpClass(cls):
        """Class setup backs up the config files and loads the toolbox."""
        # Import HGS toolbox.
        toolbox_path = os.path.join(os.path.dirname(__file__),
                                    '..',
                                    'esri',
                                    'toolboxes',
                                    cls.toolbox_name + '.pyt')
        arcpy.ImportToolbox(toolbox_path)

        # Need to use a valid path for the engine or the tests will fail
        cls.engine_value = toolbox_path

        cls.user_file = envipyengine.config._USER_CONFIG_FILE
        if os.path.exists(cls.user_file):
            os.rename(cls.user_file, cls.user_file + '.bak')

        cls.sys_file = envipyengine.config._SYSTEM_CONFIG_FILE
        if os.path.exists(cls.sys_file):
            os.rename(cls.sys_file, cls.sys_file + '.bak')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.user_file + '.bak'):
            os.rename(cls.user_file + '.bak', cls.user_file)

        if os.path.exists(cls.sys_file + '.bak'):
            os.rename(cls.sys_file + '.bak', cls.sys_file)

    def _clean_files(self, filenames):
        """ Convenience method for cleaning up config files """
        for _file in filenames:
            if os.path.exists(_file):
                os.remove(_file)

    def setUp(self):
        self._clean_files([self.user_file, self.sys_file])

    def tearDown(self):
        self._clean_files([self.user_file, self.sys_file])

    def test_config_all_simple(self):
        """ Verify that simple values are saved to the config file """
        result = arcpy.ConfigureENVIEnvironment_envi(self.engine_value, True, True, self.path_value)

        result_engine = envipyengine.config.get(self._ENGINE)
        result_engine_args = envipyengine.config.get(self._ENGINE_ARGS)
        result_environment = envipyengine.config.get_environment()

        self.assertEqual(self.engine_value, result_engine)
        self.assertEqual(self.compile, result_engine_args)
        self.assertTrue(self._IDL_PATH in result_environment)
        self.assertEquals(self.path_value, result_environment[self._IDL_PATH])

    def test_config_turn_off_compile(self):
        """ Verify compile is turned off properly """
        result = arcpy.ConfigureENVIEnvironment_envi(self.engine_value, True, False, None)
        result_engine_args = envipyengine.config.get(self._ENGINE_ARGS)
        self.assertEqual(self.compile, result_engine_args)

        result = arcpy.ConfigureENVIEnvironment_envi(self.engine_value,
                                                     False, False, None)
        result_engine_args = envipyengine.config.get(self._ENGINE_ARGS)
        self.assertEqual('', result_engine_args)

    def test_config_remove_path(self):
        """ Verify library path is cleared properly """
        result = arcpy.ConfigureENVIEnvironment_envi(self.engine_value,
                                                     False, True,
                                                     self.path_value)

        result_environment = envipyengine.config.get_environment()
        self.assertTrue(self._IDL_PATH in result_environment)
        self.assertEquals(self.path_value, result_environment[self._IDL_PATH])

        result = arcpy.ConfigureENVIEnvironment_envi(self.engine_value,
                                                     False, False, None)
        result_environment = envipyengine.config.get_environment()
        self.assertFalse(self._IDL_PATH in result_environment)
