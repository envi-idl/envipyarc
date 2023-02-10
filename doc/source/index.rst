
.. _envipyarc:

************************************
ENVI Py for ArcGIS
************************************

.. include:: <isonum.txt>

ENVI Py for ArcGIS provides a Python client library named envipyarc to run ENVI analytics through ArcMap and ArcGIS Pro.

System Requirements
===================

* ENVI 5.5 Service Pack 2 or later
* ArcMap 10.6 or later and/or ArcGIS Pro 2.2 or later

.. _envipyarc-installation-and-configuration:

Installation and Configuration
==============================

ArcMap
------
ENVI must be installed on the computer before you install ENVI Py. If it is not already installed, you need to install ENVI first. Install ENVI Py from a web download or a DVD as follows:

1. For web downloads, navigate to the envipy*xx*-arcmap.exe file that was downloaded to your computer and run it. For installation from a DVD, navigate to the setup-envipy*xx*-arcmap.exe file in the ENVIPy*xx* folder on the DVD and run it.
2. Follow the prompts to install the software. No further configuration is necessary.


ArcGIS Pro
----------

ENVI must be installed on the computer before you install ENVI Py. If it is not already installed, you need to install ENVI first. Install ENVI Py from a web download or a DVD as follows:

1. For web downloads, navigate to the envipy*xx*-arcgispro.exe file that was downloaded to your computer and run it. For installation from a DVD, navigate to the setup-envipy*xx*-arcgispro.exe file in the ENVIPy*xx* folder on the DVD and run it.
2. Follow the prompts to install the software. No further configuration is necessary.


Usage
=====

ENVI Py for ArcGIS lets you generate an ArcGIS Python Toolbox that contains geoprocessing tools (GPTools). These tools are associated with tasks provided by ENVI. You can create an ArcGIS Python Toolbox in the following ways:

* An ENVI Management Tools toolbox provided as a system toolbox for ArcMap.
* A command-line tool, named createenvitoolbox, provided in the Python scripts directory.
* A Python package named envipyarc.

These options are described next.

Create ENVI Toolbox
===================

ArcMap
------

1. Start ArcMap.
2. In the Catalog window, select **Toolboxes > System Toolboxes > ENVI Management Tools.pyt > Create ENVI Toolbox**.
3. Double-click **Create ENVI Toolbox**.
4. In the required **ENVI Task Name(s)** field, enter one or more ENVI tasks to be wrapped into a GPTool.
5. Click the + button to add the tasks to the Task list.
6. In the required **Output Toolbox** field, specify a location to create the toolbox.

  .. image:: images/create_envi_toolbox.png

5. Click **OK**. After the toolbox is created, navigate to the location specified in **Output Toolbox**.
6. Double-click **ISODATAClassification**. The ISODATA Classification tool appears.

  .. image:: images/envitask.png

7. In the required **Input Raster** field, select an input raster dataset.

  .. image:: images/envitask_input.png

8. Click **OK**. When processing is complete, the result will display in ArcMap.

ArcGIS Pro
----------

If you installed ENVI Py for ArcGIS Pro from a web download or DVD, refer to the `Running ENVI Analytics in ArcGIS Pro Tutorial https://www.l3harrisgeospatial.com/portals/0/pdfs/RunningENVIAnalyticsInArcGISProTutorial.pdf for instructions on creating an ArcGIS Python toolbox that contains ENVI geoprocessing tools. If you did not install from a web download or DVD, follow these instructions:

1. Start ArcGIS Pro.
2. Open the project you created earlier in steps 5-9 of the ArcGIS Pro installation section.
3. In the **Project** pane, select **Toolboxes > ENVI Management Tools.pyt > Create ENVI Toolbox**.
4. Double-click **Create ENVI Toolbox**.
5. In the required **ENVI Task Name(s)** field, enter one or more ENVI tasks to be wrapped into a GPTool.
6.	Click the + button to add the tasks to the Task list.
7.	In the required **Output Toolbox** field, specify a location to create the toolbox.

  .. image:: images/create_envi_toolbox_arcgispro.png

6. Click **Run**. When processing is complete, use the **Project** tab to navigate to the **Output Toolbox** field.
7. Double-click **ISODATAClassification**. The ISODATA Classification tool appears.

  .. image:: images/arcgispro_envitask.png

8. In the required **Input Raster** field, select an input raster dataset.

  .. image:: images/arcgispro_envitask_input.png

9. Click **Run**. When processing is complete, the result will display in ArcGIS Pro.

Command Line
------------

The envipyarc package contains a command-line tool named createenvitoolbox.py. This tool can create a Python toolbox that wraps ENVI tasks. The location of this file differs by product:

* ArcMap: C:\\Python27\\ArcGIS10.x\\scripts
* ArcGIS Pro: C:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\arcgispro-py3\\Scripts

To run the script, go to the Windows Start menu and select **ArcGIS > Python Command Prompt**.

* To display the help, navigate to the scripts directory and run the --help option::

    $ python createenvitoolbox.py --help

* To create a Python toolbox with the ENVI Tasks SpectralIndex and ISODATAClassification, run the following command::

    $ python createenvitoolbox.py SpectralIndex ISODATAClassification --output C:\\ENVITasks.pyt

The toolbox name is the same as the engine name if no option is provided. The output directory defaults to the current directory if no option is provided.


Python
------

1. Use the create_toolbox member method to create a toolbox from a Python module::

    >>> from envipyengine import Engine
    >>> engine = Engine('ENVI')

2. Construct a list of tasks to add to the toolbox::

    >>> task_list = [engine.task('SpectralIndex'), engine.task('ISODATAClassification')]

3. Instantiate a GPToolbox class for creating a toolbox::

    >>> from envipyarc import GPToolbox
    >>> envi_toolbox = GPToolbox(task_list)
    >>> toolbox_file = envi_toolbox.create_toolbox('c:\\my_envi_tools')

4. The create_toolbox method returns the filename of the toolbox, which can then be used by arcpy to import the toolbox::

    >>> import arcpy
    >>> arcpy.ImportToolbox(toolbox_file)

5. Run the toolbox::

    >>> input_raster = 'C:/Program Files/Harris/ENVI55/data/qb_boulder_msi'
    >>> index = 'Normalized Difference Vegetation Index'
    >>> result = arcpy.SpectralIndex_envi(input_raster,index)
    >>> print(result)
