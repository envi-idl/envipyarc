"""
Maps the ENVIMACHINELEARNINGMODEL data type to a GPTool datatype
"""
from __future__ import absolute_import
from string import Template

from envipyarclib.gptool.parameter.template import Template as ParamTemplate


class ENVIMACHINELEARNINGMODEL(ParamTemplate):
    """
    Class template for the datatype
    """

    def get_parameter(self, task_param):
        if task_param['direction'].upper() == 'OUTPUT':
            return Template(
                '''
        $name = arcpy.Parameter(
            displayName="$displayName",
            name="$name",
            datatype="GPString",
            parameterType="$paramType",
            direction="$direction",
            multiValue=$multiValue
        )
                '''
            )
        # Return the input template
        return Template(
            '''
        $name = arcpy.Parameter(
            displayName="$displayName",
            name="$name",
            datatype="$dataType",
            parameterType="$paramType",
            direction="$direction",
            multiValue=$multiValue
        )
        $name.filter.list = ['json']
            '''
        )

    def parameter_names(self, task_param):
        return [Template('$name')]

    def default_value(self):
        return Template(
            '''
        ${name}.value = "$defaultValue"
            '''
        )

    def update_parameter(self):
        return Template('')

    def pre_execute(self):
        return Template(
            '''
        path = parameters[self.i${name}].valueAsText
        if not path is None:
            input_params['${name}'] = {'url':path, 'factory':'ENVIMACHINELEARNINGMODEL'}
            '''
        )

    def post_execute(self):
        return Template(
            '''
        if '${name}' in task_results:
            model = task_results['${name}']
            parameters[self.i${name}].value = model['url']
            '''
        )


def template():
    """Returns the template object."""
    return ENVIMACHINELEARNINGMODEL('DEFile')
