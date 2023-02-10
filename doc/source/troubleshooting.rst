
***************
Troubleshooting
***************


No option engine in section: envipyengine
=========================================

This error means the ENVI Py installation has not been configured to point to your ENVI/IDL taskengine executable.  Before running any task or GPTool, make sure you have completed the steps in the :ref:`envipyarc-installation-and-configuration` section which sets the path to the ENVI taskengine.



Invalid task definition: Unknown task schema
============================================

This error occurs when running task not supported by the ENVI version connected to ENVI Py.  To fix this error make sure that ENVI Py is configured to use the latest version of ENVI installed on your machine.