Print["Starting the search for the distance to Halley's Comet"]
Do[
Print[QuantityMagnitude[Entity["Comet", "Comet1PHalley"][EntityProperty["Comet", "DistanceFromEarth"]]]]
,
Infinity]
