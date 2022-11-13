**RAPPORT**

Projet Python : FoodCrop, gestion de données à partir d'un tableau csv

By Aydar Yunus, Mu Maxime, Foray Léo-Paul

Nous avons développé sur l'IDE Pycharm car nous l'utilisions déjà et son utilisation est intuitive. 
Le code était partagé en git via le gitlab de l'école, et nous avons utilisé la version de Python 3.10.

Concernant l'utilisation de notre programme, il faut le faire tourner sur la classe Main.
Celle ci contient par défaut les instructions :

    dataframe = pandas.read_csv("FeedGrains.csv")
    fcd = FoodCropsDataset()
    fcd.load("FeedGrains.csv")

qui permettent de charger le jeux de données.

Si vous souhaitez effectuer une recherche sur le résultat de ce chargement, il suffit de faire appel à la méthode findMeasurement() de FoodCropsDataset, dont le premier parametre est l'id du CommodityGroup, puis l'id de l'indicatorGroup, puis l'id de la position géographique et pour finir l'id de l'unité. Chacun de ces paramètre est optionnel, si aucun n'est présent la méthode renvoie toutes les mesures enregistrées.
L'appel se fait ainsi :

    print(fcd.findMeasurements(commodityGroupId, indicatorGroupId, geographicalLocationId, unitId))


Si vous souhaitez que l'affichage soit plus lisible, ajoutez plutôt ceci :

    result = fcd.findMeasurements(commodityGroupId, indicatorGroupId, geographicalLocationId, unitId)
    for measurement in result:
        print(measurement.describe())

Concernant la répartition du travail dans le groupe, après une analyse poussée du sujet et du diagramme de classe qui l'illustrait, 
nous avons trouvé une manière de séparer les différentes tâches en trois groupes distincts pour tirer profit des compétences de chacun tout en préservant un équilibre entre les charges de travail. 
Ainsi, Maxime s'est chargé de l'instanciation du modèle API et du bon fonctionnement de la méthode load. 
Les différents dictionnaires ont été créés par Léo-Paul, ainsi que les méthodes permettant l'appel à ceux-ci pour la réutilisation d'instances ou encore pour la méthode find() de foodCropDataset. 
L'ensemble des méthodes describe() et leurs imbriquements ont été réalisés par Yunus, qui a pris soin de commenter les méthodes de l'ensemble du projet et de rendre le code plus clair lorsque nécessaire, notemment en implémentant les conventions PEP de python.

Dans notre travail, nous avons rencontré plusieurs problèmes d'importance diverses. Par exemple, l'utilisation du git et les changement de branches nous ont parfois posé quelques petits problèmes. Par exemple, des morceaux de codes qui apparaissent sur un pc et pas l'autre, une restriction empechant d'effectuer des push sur la branche principale, mais étant habitués à cette technologie ceux-ci ont été rapidement réglés. Nous avons aussi eu du mal à comprendre le diagramme de classe et à l'appliquer, car nous n'étions pas habitués à procéder dans ce sens la. Pour savoir ou les dictionnaires devait être créés ou à quoi servent les enums, nous avons du demandé de l'aide au professeur ou dautres élèves. Le principal problème a été de comprendre comment effectuer des recherches dont la complexité reste en O(1), mais avec quelques recherches sur des sites spécialisés python dont la javadoc nous avons put les résoudre.

-----------------------------------------------------------------------------------------------------
