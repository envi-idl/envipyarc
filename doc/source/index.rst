
.. _envipyarc:

************************************
ENVI :sup:`®` Py for ArcGIS :sup:`®`
************************************

.. include:: <isonum.txt>

ENVI Py for ArcGIS provides a Python client library named envipyarc to run ENVI analytics through ArcMap™ and ArcGIS Pro.

System Requirements
===================

* ENVI 5.3 Service Pack 2 or later
* ArcMap 10.4 or later and/or ArcGIS Pro 1.3 or later

To use ENVI for ArcGIS full interoperability, ENVI 5.4 is required.

.. _envipyarc-installation-and-configuration:

Installation and Configuration
==============================

ArcMap
------

1. Start a Windows command prompt in administrator mode.
2. Issue the following commands::

    $ cd c:\Python27\ArcGIS10.5\Scripts
    $ pip install envipyarc

3. Close the windows command prompt.
4. Start ArcMap.
5. In the Catalog window, select **Toolboxes > System Toolboxes > ENVI Management Tools.pyt > Configure ENVI Environment**. If this file does not appear in System Toolboxes, connect to the folder located at C:\\Python27\\ArcGIS10.x\\Lib\\site-packages\\envipyarc\\esri\\toolboxes\\ and run it from there.
6. Double-click **Configure ENVI Environment**.

  .. image:: images/configure_envi_environment.png

7. In the required **Engine Location** field, enter the full path of the 'taskengine.exe' in your ENVI distribution. The default path is <ENVI_INSTALL_DIR>\\IDLXX\\bin\\bin.x86_64\\taskengine.exe
8. Enable the **Run Engine in Compile Mode** option if you want to compile .pro files. This depends on what your ENVI license allows. If you disable this option, the ENVI code you want to run must be packaged as IDL SAVE files (.sav).
9. Enable the **Use Custom ENVI Library Path** option to specify one or more directories that contain custom ENVI code. Then enter the path to the directories in the **Configure ENVI Library Path** field. Use a semicolon to separate individual directory paths.
10. Click **OK** to run the tool and save the environment.

ArcGIS Pro
----------

1. From the Windows start menu, select **ArcGIS > ArcGIS Pro > Python Command Prompt**. Be sure to run this as an administrator.
2. Issue following command::

    $ pip install envipyarc

3. Close the **Python Command Prompt**.
4. Start ArcGIS Pro.
5. Click **Select another project template**.
6. Select **New > Computer** and click the **Browse** button.
7. Navigate to C:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\arcgispro-py3\\lib\\site-packages\\envipyarc\\esri\\projecttemplates\\.
8. Select ENVIPyManagement.aptx.
9. Enter a name for your project and click **OK**.
10. In the Project pane, select **Toolboxes > ENVI Management Tools.pyt**.
11. Expand the **ENVI Management Tools** toolbox, and double-click the **Configure ENVI Environment** tool.

  .. image:: images/configure_envi_environment_arcgispro.png

11. In the required **Engine Location** field, enter the full path of the 'taskengine.exe' in your ENVI distribution. The default path is <ENVI_INSTALL_DIR>\\IDLXX\\bin\\bin.x86_64\\taskengine.exe.
12. Enable the **Run Engine in Compile Mode** option if you want to compile .pro files. This depends on what your ENVI license allows. If you disable this option, the ENVI code you want to run must be packaged as IDL SAVE files (.sav).
13. Enable the **Use Custom ENVI Library Path** option to specify one or more directories that contain custom ENVI code. Then enter the path to the directories in the **Configure ENVI Library Path** field. Use a semicolon to separate individual directory paths.
14. Click **OK** to run the tool and save the environment.

Usage
=====

ENVI Py for ArcGIS lets you generate an ArcGIS Python Toolbox that contains geoprocessing tools (GPTools). These tools are associated with tasks provided by ENVI. You can create an ArcGIS Python Toolbox in the following ways:

* An ENVI Management Tools toolbox provided as a system toolbox for ArcMap.
* An ENVI Py Management project template containing the ENVI Management Tools toolbox for ArcGIS Pro.
* A command-line tool, named createenvitoolbox, provided in the Python scripts directory.
* A Python package named envipyarc.

The options are described next.

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

1. Start ArcGIS Pro.
2. Open the project you created earlier in the Installation section.
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

    >>> input_raster = 'C:/Program Files/Harris/ENVI54/data/qb_boulder_msi'
    >>> index = 'Normalized Difference Vegetation Index'
    >>> result = arcpy.SpectralIndex_envi(input_raster,index)
    >>> print(result)
