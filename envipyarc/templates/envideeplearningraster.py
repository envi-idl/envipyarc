"""
Maps the ENVI Task data type to a GPTool datatype
"""

from .enviraster import ENVIRASTER

class ENVIDEEPLEARNINGRASTER(ENVIRASTER):
    """
    Defines the ENVIDEEPLEARNINGRASTER parameter template
    """
    def __init__(self, data_type, envi_factory='ENVIDEEPLEARNINGRASTER'):
        super(ENVIDEEPLEARNINGRASTER, self).__init__(data_type, envi_factory=envi_factory)

def template():
    """Returns the template object."""
    return ENVIDEEPLEARNINGRASTER('DERasterDataset')
