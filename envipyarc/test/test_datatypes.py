"""
Tests the supported datatypes for ENVI Tasks running as GPTools
"""
import os
from envipyarclib.test.config import Config
from envipyarclib.test.datatype.bool import TestDataTypeBool
from envipyarclib.test.datatype.boolean import TestDataTypeBoolean
from envipyarclib.test.datatype.byte import TestDataTypeByte
from envipyarclib.test.datatype.bytearray import TestDataTypeByteArray
from envipyarclib.test.datatype.double import TestDataTypeDouble
from envipyarclib.test.datatype.doublearray import TestDataTypeDoubleArray
from envipyarclib.test.datatype.enviraster import TestDataTypeENVIRaster
from envipyarclib.test.datatype.enviuri import TestDataTypeENVIURI
from envipyarclib.test.datatype.envivector import TestDataTypeENVIVector
from envipyarclib.test.datatype.float import TestDatatypeFloat
from envipyarclib.test.datatype.floatarray import TestDataTypeFloatArray
from envipyarclib.test.datatype.int import TestDataTypeInt
from envipyarclib.test.datatype.intarray import TestDataTypeIntArray
from envipyarclib.test.datatype.long import TestDatatypeLong
from envipyarclib.test.datatype.long64 import TestDatatypeLong64
from envipyarclib.test.datatype.long64array import TestDataTypeLong64Array
from envipyarclib.test.datatype.string import TestDatatypeString
from envipyarclib.test.datatype.stringarray import TestDataTypeStringArray
from envipyarclib.test.datatype.uint import TestDataTypeUInt
from envipyarclib.test.datatype.uintarray import TestDataTypeUIntArray
from envipyarclib.test.datatype.ulong import TestDataTypeULong
from envipyarclib.test.datatype.ulong64 import TestDatatypeULong64
from envipyarclib.test.datatype.ulong64array import TestDataTypeULong64Array
from envipyarclib.test.datatype.ulongarray import TestDataTypeULongArray

import arcpy

from envipyengine import Engine
from .. import GPToolbox



class ENVIConfig(Config):
    """
    Implementation of the data type config for ENVI task engine
    """
    def __init__(self):
        self._workspace = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                       'workspace')
        os.environ['ENVI_CUSTOM_CODE'] = self.test_task_dir
        os.environ['IDL_PATH'] = ';'.join(('<IDL_DEFAULT>', self.test_task_dir))
        self.setup_workspace(self._workspace)
    
    def setup_toolbox(self, engine_name, task_name, toolbox_name):
        """
        Implementation of abstract method
        """
        task = Engine(engine_name).task(task_name)
        toolbox = GPToolbox([task], alias='TEST')
        tbx_file = os.path.join(arcpy.env.scratchFolder, toolbox_name)

        # Remove the old toolbox if it exists
        self.remove_toolbox(tbx_file)
        tbx_file = toolbox.create_toolbox(tbx_file)
        arcpy.ImportToolbox(tbx_file)

CONFIG = ENVIConfig()

TESTS = [
    TestDataTypeBool,
    TestDataTypeBoolean,
    TestDataTypeByte,
    TestDataTypeByteArray,
    TestDataTypeDouble,
    TestDataTypeDoubleArray,
    TestDataTypeENVIRaster,
    TestDataTypeENVIURI,
    TestDataTypeENVIVector,
    TestDatatypeFloat,
    TestDataTypeFloatArray,
    TestDataTypeInt,
    TestDataTypeIntArray,
    TestDatatypeLong,
    TestDatatypeLong64,
    TestDataTypeLong64Array,
    TestDatatypeString,
    TestDataTypeStringArray,
    TestDataTypeUInt,
    TestDataTypeUIntArray,
    TestDataTypeULong,
    TestDatatypeULong64,
    TestDataTypeULong64Array,
    TestDataTypeULongArray
]

# attach the ENVI Config to the tests
for testcls in TESTS:
    testcls.config = CONFIG
