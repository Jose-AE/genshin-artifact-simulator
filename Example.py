from ArtifactClass import Artifact


#in here you will see how to use the artifact class that I made 



#to generate an artifact just create the object with its class
my_artifact = Artifact()

#to show the stats of the artifact, just print it (stats are generated randomly when created)
print(my_artifact) #-[Set:1]-[Type:Plume]-[MainStat:ATK]-[SS1: (23.1 DEF)]-[SS2: (7.0 CD)]-[SS3: (268.9 HP)]

#to level it up use the level up function 
my_artifact.LevelUp(4) #this will level it up by 4 levels, so 1 new substat or a substat upgrade if already at 4 substats
print(my_artifact)

my_artifact.LevelUp(16)#since its now at level 4 add another 16 levels to max it 
print(my_artifact)


#accesing stats
print(my_artifact.Level) #level  
print(my_artifact.Set) #set 
print(my_artifact.Type) #type 
print(my_artifact.MainStat) #main stat 
print(my_artifact.SubStats) #sub stats (saved as a dictionary )

