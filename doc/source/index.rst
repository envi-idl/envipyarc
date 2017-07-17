.. _envipyarc:

******************
ENVI Py for ArcGIS
******************

.. include:: <isonum.txt>

ENVI Py for ArcGIS provides a Python client library, named envipyarc, to run ENVI analytics through ArcMap and ArcGIS Pro.

See http://www.harrisgeospatial.com/ for more details on product offerings.

System Requirements
===================

To operate, ENVI Py for Arcgis requires the following:

* ENVI 5.3SP2 or later
* ArcMap 10.4 or later and/or ArcGIS Pro 1.3 or later

Installation and Configuration
==============================

For ArcMap
----------

* Launch a windows command prompt in administrator module
* Issue following commands:
  >>> cd c:\\python27\\ArcGIS10.5\\Scripts
  >>> pip install envipyarc
* Close the windows command prompt
* Launch ArcMap
* Navigate in the Catalog window to Toolboxes |rarr| System Toolboxes |rarr| ENVI Management Tools.pyt |rarr| Configure ENVI Environment.  Note: If ENVI Management Tools.pyt does not appear in System Toolboxes, connect to the folder located at C:\\Python27\\ArcGIS10.x\\Lib\\site-packages\\envipyarc\\esri\\toolboxes\\ and ENVI Management Tools.pyt can be run from there.
* Double-click on Configure ENVI Environment, and a tool is opened that you can use to configure ENVI Py

.. image:: images/configure_envi_environment.png

* The first field - Engine Location - is required. This must be the full path of the 'taskengine.exe' in your ENVI distribution. This file is located at <ENVI_INSTALL_DIR>\\IDLXX\\bin\\bin.x86_64\\taskengine.exe
* Next, you may specify whether ENVI will have the ability to compile .pro files. This will depend on what your ENVI license allows. If this is not checked, the ENVI code you wish to run must be packaged as .sav files.
* Finally, if you wish to specify one or more directories that contain custom ENVI code, you can do so here. If you wish to specify more than one directory be sure to use a semi-colon to separate the individual directory paths.


For ArcGIS Pro
--------------

* Select from Windows start menu ArcGIS |rarr| Python Command Prompt. Note: Make sure to run as administrator
* Issue following command:
  >>> pip install envipyarc
* Close the Python Command Prompt
* Launch ArcGIS Pro
* Click on Select another project template 
* Select New |rarr| Computer and click Browse button 
* Browse to the following location, C:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\arcgispro-py3\\lib\\site-packages\\envipyarc\\esri\\projecttemplates\\, and select ENVIPyManagement.aptx
* Enter a name for your project and click OK
* Navigate in the Project pane to Toolboxes |rarr| ENVI Management Tools.pyt 
* Expand the ENVI Management Tools toolbox, and double-click on Configure ENVI Environment tool.

.. image:: images/configure_envi_environment_arcgispro.png

* The first field - Engine Location - is required. This must be the full path of the 'taskengine.exe' in your ENVI distribution. This file is located at <ENVI_INSTALL_DIR>\\IDLXX\\bin\\bin.x86_64\\taskengine.exe
* Next, you may specify whether ENVI will have the ability to compile .pro files. This will depend on what your ENVI license allows. If this is not checked, the ENVI code you wish to run must be packaged as .sav files.
* Finally, if you wish to specify one or more directories that contain custom ENVI code, you can do so here. If you wish to specify more than one directory be sure to use a semi-colon to separate the individual directory paths.


Usage
=====

ENVI Py for ArcGIS allows users to generate an ArcGIS Python Toolbox containing 
geoprocessing tools (GPTools) associated with tasks provided by ENVI Desktop.

There are multiple ways to create an ArcGIS Python Toolbox:  

* Through a ENVI Management Tools toolbox provided as a system toolbox for ArcMap.
* Through a ENVI Py Management project template containing the ENVI Management Tools toolbox for ArcGIS Pro.
* Through a command-line tool, named createenvitoolbox, provided in the Python scripts directory.
* Through Python using the Python package, envipyarc.


Create ENVI Toolbox
===================

From ArcMap
-----------

* Launch ArcMap
* Navigate in the Catalog window to Toolboxes |rarr| System Toolboxes |rarr| ENVI Management Tools.pyt |rarr| Create ENVI Toolbox.
* Double-click on Create ENVI Toolbox, and the tool appears with two required input parameters.
* The first parameter is used to specify the names of one or more ENVI tasks to be wrapped in a GPTool. The second parameter is the location where the toolbox is created. 

.. image:: images/create_envi_toolbox.png

* Click OK, and when the tool finishes generating the new toolbox, navigate to the location specified in Output Toolbox. 
* Double-click on ISODATAClassification, and the tool appears with one required input parameter. 

.. image:: images/envitask.png

* Select an input raster dataset for the first input parameter.

.. image:: images/envitask_input.png

* Click OK, and when the tool finishes processing, the result will appear in ArcMap.



From ArcGIS Pro
---------------

* Launch ArcGIS Pro
* Open the project you created in the Installation section above 
* Navigate in the Project pane to Toolboxes |rarr| ENVI Management Tools.pyt |rarr| Create ENVI Toolbox. 
* Double-click on Create ENVI Toolbox, and the tool appears with two required input parameters.
* The first parameter is used to specify the names of one or more ENVI tasks to be wrapped in a GPTool. The second parameter is the location where the toolbox is created. 

.. image:: images/create_envi_toolbox_arcgispro.png

* Click run and when the tool finishes generating a new toolbox, navigate in the Project tab to the location specified in Output Toolbox. 
* Double-click on ISODATAClassification. The tool will appear with one required input parameter. 

.. image:: images/arcgispro_envitask.png

* Select an input raster dataset for the first input parameter. 

.. image:: images/arcgispro_envitask_input.png

* Click Run, and when the tool finishes processing, a result will appear in ArcGIS Pro.


From Command-line
=================

createenvitoolbox.py is a command-line tool in the envipyarc package used to create a Python toolbox that wraps ENVI tasks.

For ArcMap the script is located at C:\\Python27\\ArcGIS10.x\\scripts.

For ArcGIS Pro the script is located at C:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\arcgispro-py3\\Scripts.  Launch the ArcGIS |rarr| Python Command Prompt to run the script.

To display the help, navigate to the scripts directory and run the --help option::

    $ python createenvitoolbox.py --help

To create a Python toolbox with the ENVI Tasks SpectralIndex and ISODATAClassification, run this command.::

    $ python createenvitoolbox.py SpectralIndex ISODATAClassification --output C:\\ENVITasks.pyt

The toolbox name is the same as the engine name if no option is provided.
The output directory defaults to the current directory if no option is provided.


From Python
===========

The create_toolbox member method is the first way to create a toolbox from a Python module::

    >>> from envipyengine import Engine
    >>> engine = Engine('ENVI')

Now, construct a list of tasks to add to the toolbox::

    >>> task_list = [engine.task('SpectralIndex'), engine.task('ISODATAClassification')]

Next, instantiate a GPToolbox class for creating a toolbox::

    >>> from envipyengine import GPToolbox
    >>> envi_toolbox = GPToolbox(task_list)
    >>> toolbox_file = envi_toolbox.create_toolbox('c:\\my_envi_tools')

The create_toolbox method returns the filename of the toolbox, which can then be used by arcpy to import the toolbox::

    >>> import arcpy
    >>> arcpy.ImportToolbox(toolbox_file)
	
Run the toolbox.

    >>> input_raster = 'C:/Program Files/Harris/ENVI54/data/qb_boulder_msi'
    >>> index = 'Normalized Difference Vegetation Index'
    >>> result = arcpy.SpectralIndex_envi(input_raster,index)
    >>> print(result)


API Documentation
=================

.. toctree::
   :maxdepth: 2

   api




