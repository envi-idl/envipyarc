"""
Maps the ENVI Task data type to a GPTool datatype
"""

from .envideeplearningraster import ENVIDEEPLEARNINGRASTER

class ENVIDEEPLEARNINGLABELRASTER(ENVIDEEPLEARNINGRASTER):
    """
    Defines the ENVIDEEPLEARNINGLABELRASTER parameter template
    """
    def __init__(self, data_type, envi_factory='ENVIDEEPLEARNINGLABELRASTER'):
        super(ENVIDEEPLEARNINGLABELRASTER, self).__init__(data_type, envi_factory=envi_factory)

def template():
    """Returns the template object."""
    return ENVIDEEPLEARNINGLABELRASTER('DERasterDataset')
