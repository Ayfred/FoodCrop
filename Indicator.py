import Unit
from IndicatorGroup import IndicatorGroup


class Indicator:


    def __init__(self, id: int, frequency: int, freqDesc: str, geogLocation: str, indicatorGroup: IndicatorGroup, unit: Unit):
        self.id = id
        self.frequency = frequency
        self.freqDesc = freqDesc
        self.geoLocation = geogLocation
        self.indicatorGroup = indicatorGroup
        self.unit = unit

