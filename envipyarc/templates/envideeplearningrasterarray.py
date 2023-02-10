"""
Maps the ENVI Task data type to a GPTool datatype
"""

from .envirasterarray import ENVIRASTERARRAY

class ENVIDEEPLEARNINGRASTERARRAY(ENVIRASTERARRAY):
    """
    Defines the ENVIDEEPLEARNINGRASTERARRAY parameter template
    """
    def __init__(self, data_type, envi_factory='ENVIDEEPLEARNINGRASTER'):
        super(ENVIDEEPLEARNINGRASTERARRAY, self).__init__(data_type, envi_factory=envi_factory)

def template():
    """Returns the template object."""
    return ENVIDEEPLEARNINGRASTERARRAY('DERasterDataset')
