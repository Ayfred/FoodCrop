from IndicatorGroup import IndicatorGroup


class Indicator:

    id : str
    frequency : int
    frequencyDesc : str
    geogLocation: str

    def __init__(self, id: int, frequency: int, freqDesc: str, geogLocation: str, indicatorGroup: IndicatorGroup, unit: Unit):
        pass

