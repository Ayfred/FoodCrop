**REPORT**

Python project: FoodCrop, data management from a csv table

By Aydar Yunus, Mu Maxime, Foray Leo-Paul

We developed on the Pycharm IDE because we were already using it and its use is intuitive.
The code was shared in git via the school gitlab, and we used the version of Python 3.10.

Regarding the use of our program, it must be run on the Main class.
This contains by default the instructions:

     dataframe = pandas.read_csv("FeedGrains.csv")
     fcd = FoodCropsDataset()
     fcd.load("FeedGrains.csv")

that allow you to load the dataset.

If you want to perform a search on the result of this loading, all you have to do is call the findMeasurement() method of FoodCropsDataset, whose first parameter is the CommodityGroup id, then the indicatorGroup id, then the id of the geographical position and finally the id of the unit. Each of these parameters is optional, if none is present the method returns all the recorded measurements.
The call is made as follows:

     print(fcd.findMeasurements(commodityGroupId, indicatorGroupId, geographicalLocationId, unitId))


If you want the display to be more readable, add this instead:

     result = fcd.findMeasurements(commodityGroupId, indicatorGroupId, geographicalLocationId, unitId)
     for measurement in result:
         print(measurement.describe())

Regarding the distribution of work in the group, after an in-depth analysis of the subject and the class diagram that illustrated it,
we found a way to separate the different tasks into three distinct groups to take advantage of everyone's skills while maintaining a balance between the workloads.
Thus, Maxime was responsible for the instantiation of the API model and the proper functioning of the load method.
The different dictionaries were created by Léo-Paul, as well as the methods allowing the call to them for the reuse of instances or for the find() method of foodCropDataset.
All the describe() methods and their nestings were done by Yunus, who took care to comment the methods of the whole project and to make the code clearer when necessary, notably by implementing the PEP conventions of python.

In our work, we encountered several problems of varying importance. For example, the use of git and changing branches sometimes caused us some small problems. For example, pieces of code that appear on one pc and not the other, a restriction preventing pushes to the main branch, but being used to this technology, these were quickly resolved. We also had trouble understanding the class diagram and applying it, because we weren't used to doing it that way. To know where the dictionaries should be created or what the enums are for, we had to ask the teacher or other students for help. The main problem was to understand how to perform searches whose complexity remains in O(1), but with some research on specialized python sites whose javadoc we were able to solve them.

-----------------------------------------------------------------------------------------------------
