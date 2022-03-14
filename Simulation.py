from ArtifactClass import Artifact
import statistics
import os 



#------------------------------------------------

Settings = {

    "WantedArtifactSimulations":1000, #the amount of times you want to find the wanted artifact, the higher the number the more accurate the average days to get it will be  since there is more entries to calculate an average



    "WantedSet":0, # 0,1 or "ANY"
    "WantedType":"Sands", # "Flower", "Plume", "Sands", "Goblet", "Circlet" OR "ANY"
    "WantedMainStat":"DEF%", # "HP","ATK","HP%","ATK%","DEF%","ER","PYR_DMG","ELE_DMG","CRY_DMG","HYD_DMG","ANE_DMG","GEO_DMG","PHY_DMG","EM","CD","CR","HB" OR "ANY"-make sure the main stat is compatible with the piece type
    "WantedSubStats":{"CR":2,"CD":5} #leave empty if you dont want any specific substats  -"WantedSubStats":{}

}




SimulationStats = {
    "TotalArifactsPulled":0,
    "TotalArifactsOfTheCorrectSet":0,
    "TotalArifactsOfTheCorrectType":0,
    "TotalArifactsWithCorrectMainStat":0,
    "TotalArifactsWithCorrectSubStats":0,
    "TotalArifactsWithCorrectSubStatsAndValues":0,

}



#this function will generate artifacts until the one with wanted stats/set etc is found and record the pull stats 
def FindArifact():
    
    Pulls = 0
    FoundArifact = False

    while not FoundArifact:

        SimulationStats["TotalArifactsPulled"] += 1 
        Pulls += 1 
        

        GeneratedArifact = Artifact() #generate an artifact 

        
        if Settings["WantedSet"] == GeneratedArifact.Set or Settings["WantedSet"] == "ANY": #if correct set 
            SimulationStats["TotalArifactsOfTheCorrectSet"] += 1 

            if Settings["WantedType"] == GeneratedArifact.Type or Settings["WantedType"] == "ANY": #if correct type 
                SimulationStats["TotalArifactsOfTheCorrectType"] += 1 

                if Settings["WantedMainStat"] == GeneratedArifact.MainStat or Settings["WantedMainStat"] == "ANY": #if correct main stat 
                    SimulationStats["TotalArifactsWithCorrectMainStat"] += 1


                    GeneratedArifact.LevelUp(4)#level it up to have atleat 4 sub stats 

                    #if it has wanted substats 
                    if all(x in list(GeneratedArifact.SubStats) for x in list(Settings["WantedSubStats"])):
                        SimulationStats["TotalArifactsWithCorrectSubStats"] += 1 

                        GeneratedArifact.LevelUp(16) #max artifact

                        correct_sub_stat_values = [] #temp list to store if each individual stat meets amount req 
                        for wanted_stat in Settings["WantedSubStats"]:
                            
                            if GeneratedArifact.SubStats[wanted_stat] >= Settings["WantedSubStats"][wanted_stat]:
                                correct_sub_stat_values.append(True)
                            else:
                                correct_sub_stat_values.append(False)

                        

                        if False in correct_sub_stat_values: #if sub stats didint level enough 
                            pass
                        else:
                            SimulationStats["TotalArifactsWithCorrectSubStatsAndValues"] += 1 
                            FoundArifact = True

    
    return Pulls #return how many artifacts it took to find the wanted one  




FoundArifacts = [] #list where the amount of artifacts that were pulled to obtain the wanted one is saved, each index is 1 simulation
for i in range(Settings["WantedArtifactSimulations"]):
    
    
    print(f"Simulating artifact farming: {round(i/Settings['WantedArtifactSimulations']*100,1)}%")
    os.system('cls')

    FoundArifacts.append(FindArifact())
    

os.system('cls')
print("#------------------------[WANTED ARTIFACT]--------------------------------#\n")
print(f'[Set]------------({Settings["WantedSet"]})')
print(f'[Type]-----------({Settings["WantedType"]})')
print(f'[Main Stat]------({Settings["WantedMainStat"]})')

for i, stat in enumerate(Settings["WantedSubStats"]):
    print(f'[Substat]--------({list(Settings["WantedSubStats"])[i]}) >= {Settings["WantedSubStats"][stat]}')



print("\n#----------------------[SIMULATION RESULTS]-------------------------------#\n")
print(f'[Total artifact pulls simulated]---------------------------({SimulationStats["TotalArifactsPulled"]:,})')
print(f'[Artifacts of the correct set]-----------------------------({SimulationStats["TotalArifactsOfTheCorrectSet"]:,})<{round(SimulationStats["TotalArifactsOfTheCorrectSet"]/SimulationStats["TotalArifactsPulled"]*100,2)}%>')
print(f'[Artifacts of the correct piece type]----------------------({SimulationStats["TotalArifactsOfTheCorrectType"]:,})<{round(SimulationStats["TotalArifactsOfTheCorrectType"]/SimulationStats["TotalArifactsPulled"]*100,2)}%>')
print(f'[Artifacts of the correct main stat]-----------------------({SimulationStats["TotalArifactsWithCorrectMainStat"]:,})<{round(SimulationStats["TotalArifactsWithCorrectMainStat"]/SimulationStats["TotalArifactsPulled"]*100,2)}%>')
print(f'[Artifacts of the correct substats]------------------------({SimulationStats["TotalArifactsWithCorrectSubStats"]:,})<{round(SimulationStats["TotalArifactsWithCorrectSubStats"]/SimulationStats["TotalArifactsPulled"]*100,2)}%>')
print(f'[Artifacts of the correct substats and wanted values]------({SimulationStats["TotalArifactsWithCorrectSubStatsAndValues"]:,})<{round(SimulationStats["TotalArifactsWithCorrectSubStatsAndValues"]/SimulationStats["TotalArifactsPulled"]*100,2)}%>')

print(f"\n[Average days needed of daily resin farming to get wanted artifact]---({round(statistics.mean(FoundArifacts)/9)})<~{round(statistics.mean(FoundArifacts)/9)*180} Resin>\n\n\n\n")





            