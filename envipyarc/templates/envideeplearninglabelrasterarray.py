"""
Maps the ENVI Task data type to a GPTool datatype
"""

from .envideeplearningrasterarray import ENVIDEEPLEARNINGRASTERARRAY

class ENVIDEEPLEARNINGLABELRASTERARRAY(ENVIDEEPLEARNINGRASTERARRAY):
    """
    Defines the ENVIDEEPLEARNINGLABELRASTERARRAY parameter template
    """
    def __init__(self, data_type, envi_factory='ENVIDEEPLEARNINGLABELRASTER'):
        super(ENVIDEEPLEARNINGLABELRASTERARRAY, self).__init__(data_type,
                                                               envi_factory=envi_factory)

def template():
    """Returns the template object."""
    return ENVIDEEPLEARNINGLABELRASTERARRAY('DERasterDataset')
