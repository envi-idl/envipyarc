"""
Maps the ENVITIME data type to a GPTool datatype
"""
from __future__ import absolute_import
from string import Template

from envipyarclib.gptool.parameter.template import Template as ParamTemplate


class ENVITIME(ParamTemplate):
    """
    Class template for the datatype
    """
    def get_parameter(self, task_param):
        if task_param['direction'].upper() == 'OUTPUT':
            return Template('''
        $name = arcpy.Parameter(
            displayName="$displayName",
            name="$name",
            datatype="$dataType",
            parameterType="$paramType",
            direction="$direction",
            multiValue=$multiValue
        )
''')
        # Return the input template
        return Template('''
        $name = arcpy.Parameter(
            displayName="$displayName",
            name="$name",
            datatype="$dataType",
            parameterType="$paramType",
            direction="$direction",
            multiValue=$multiValue
        )
''')

    def parameter_names(self, task_param):
        return [Template('$name')]

    def default_value(self):
        return Template('''
        ${name}.value = "$defaultValue"
''')

    def update_parameter(self):
        return Template('')

    def pre_execute(self):
        return Template('''
        # no guarantee datetime is present
        from datetime import datetime as dt 

        date = parameters[self.i${name}].value
        if not date is None:
            # use the most verbose formatting for envi
            date = dt.strftime(date, '%Y-%m-%dT%H:%M:%S.%f%zZ')
            input_params['${name}'] = {'acquisition': date, 'factory':'ENVITime'}
''')

    def post_execute(self):
        return Template('''
        if '${name}' in task_results:
            # no guarantee datetime is present
            from datetime import datetime as dt 

            date = task_results['${name}']['acquisition']

            # ENVITime can come back in one of three ways
            # YYYY-MM-DD
            # YYYY-MM-DDTHH:MM:SS.DZ
            # YYYY-MM-DDTHH:MM:SS:Dooo:mm
            dateFormat = '%Y-%m-%d'
            if 'T' in date:
                dateFormat += 'T%H:%M:%S'
                if '.' in date:
                    dateFormat += '.%f'
                if 'Z' in date:
                    dateFormat += 'Z'
                else:
                    dateFormat += '%z'

            date = dt.strptime(date, dateFormat)
            parameters[self.i${name}].value = date
''')


def template():
    """Returns the template object."""
    return ENVITIME('GPDate')
