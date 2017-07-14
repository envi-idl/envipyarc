

import sys
import os
import shutil

python_install_dir = os.path.dirname(sys.executable)
envipyarc_package_dir = os.path.join(python_install_dir, 'Lib', 'site-packages', 'envipyarc')
shutil.rmtree(envipyarc_package_dir)
envipyarc_templates_package_dir = os.path.join(python_install_dir, 'Lib', 'site-packages', 'envipyarc', 'templates')
shutil.rmtree(envipyarc_templates_package_dir)