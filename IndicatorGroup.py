from enum import Enum

class IndicatorGroup(Enum):
    EXPORT_AND_IMPORT, SUPPLY_AND_USE, PRICES, FEED_PRICE_RATIOS, QUANTITIES_FED, TRANSPORTATION, ANIMAL_UNIT_INDEXES = range(7)