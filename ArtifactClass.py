import math
import random


class Artifact:

    #pre-determined stat probabilities obtained from the wiki 
    TYPES = [
        "Flower",
        "Plume",
        "Sands",
        "Goblet",
        "Circlet"
    ]

    ARTIFACT_MAIN_STATS = {
        "Flower":{"HP":100},
        "Plume":{"ATK":100},
        "Sands":{"HP%":26.68,"ATK%":26.66,"DEF%":26.66,"ER":10,"EM":10},
        "Goblet":{"HP%":21.25,"ATK%":21.25,"DEF%":20,"PYR_DMG":5,"ELE_DMG":5,"CRY_DMG":5,"HYD_DMG":5,"ANE_DMG":5,"GEO_DMG":5,"PHY_DMG":5,"EM":2.5},
        "Circlet":{"HP%":22,"ATK%":22,"DEF%":22,"CR":10,"CD":10,"HB":10,"EM":4}
    }

    ARTIFACT_SUB_STATS_ROLL_RANGE = {
        "HP":[209.13,239,268.88,298.75],
        "ATK":[13.62,15.56,17.51,19.45],
        "DEF":[16.20,18.52,20.83,23.15],
        "HP%":[4.08,4.66,5.25,5.83],
        "ATK%":[4.08,4.66,5.25,5.83],
        "DEF%":[5.10,5.83,6.56,7.29],
        "EM":[16.32,18.65,20.98,23.31],
        "ER":[4.53,5.18,5.83,6.48],
        "CR":[2.72,3.11,3.50,3.89],
        "CD":[5.44,6.22,6.99,7.77]
    }

    SUB_STATS_CHANCE = {
        "HP":{"HP":0,"ATK":15.79,"DEF":15.79,"HP%":10.53,"ATK%":10.53,"DEF%":10.53,"ER":10.53,"EM":10.53,"CR":7.89,"CD":7.89},
        "ATK":{"HP":15.79,"ATK":0,"DEF":15.79,"HP%":10.53,"ATK%":10.53,"DEF%":10.53,"ER":10.53,"EM":10.53,"CR":7.89,"CD":7.89},
        "HP%":{"HP":15,"ATK":15,"DEF":15,"HP%":0,"ATK%":10,"DEF%":10,"ER":10,"EM":10,"CR":7.5,"CD":7.5},
        "ATK%":{"HP":15,"ATK":15,"DEF":15,"HP%":10,"ATK%":0,"DEF%":10,"ER":10,"EM":10,"CR":7.5,"CD":7.5},
        "DEF%":{"HP":15,"ATK":15,"DEF":15,"HP%":10,"ATK%":10,"DEF%":0,"ER":10,"EM":10,"CR":7.5,"CD":7.5},
        "ELEM_DMG":{"HP":13.64,"ATK":13.64,"DEF":13.64,"HP%":9.09,"ATK%":9.09,"DEF%":9.09,"ER":9.09,"EM":9.09,"CR":6.82,"CD":6.82},
        "ER":{"HP":15,"ATK":15,"DEF":15,"HP%":10,"ATK%":10,"DEF%":10,"ER":0,"EM":10,"CR":7.5,"CD":7.5},
        "CR":{"HP":14.63,"ATK":14.63,"DEF":14.63,"HP%":9.76,"ATK%":9.76,"DEF%":9.76,"ER":9.76,"EM":9.76,"CR":0,"CD":7.32},
        "CD":{"HP":14.63,"ATK":14.63,"DEF":14.63,"HP%":9.76,"ATK%":9.76,"DEF%":9.76,"ER":9.76,"EM":9.76,"CR":7.32,"CD":0},
        "EM":{"HP":15,"ATK":15,"DEF":15,"HP%":10,"ATK%":10,"DEF%":10,"ER":10,"EM":0,"CR":7.5,"CD":7.5},
        "HB":{"HP":13.64,"ATK":13.64,"DEF":13.64,"HP%":9.09,"ATK%":9.09,"DEF%":9.09,"ER":9.09,"EM":9.09,"CR":6.82,"CD":6.82}
    }


    #generate random stats when artifact is created 
    def __init__(self):

        self.Level = 0
        self.Set = random.randint(0,1)
        self.Type = self.TYPES[random.randint(0,len(self.TYPES)-1)]
        self.MainStat = random.choices(list(self.ARTIFACT_MAIN_STATS[self.Type]), weights=tuple(self.ARTIFACT_MAIN_STATS[self.Type].values()))[0]
        
        #generate sub stats 
        self.SubStats = {}

        for _ in range(4 if random.randint(1,5) == 1 else 3): #generate 4 or 3 substats 

            self.GenerateSubStat()
                
        
        
    #when object is printed print the artifact stats 
    def __str__(self):

        return f'[Level:{self.Level}]-[Set:{self.Set}]-[Type:{self.Type}]-[MainStat:{self.MainStat}]-[SS1: ({round(list(self.SubStats.items())[0][1],1)} {list(self.SubStats.items())[0][0]})]-[SS2: ({round(list(self.SubStats.items())[1][1],1)} {list(self.SubStats.items())[1][0]})]-[SS3: ({round(list(self.SubStats.items())[2][1],1)} {list(self.SubStats.items())[2][0]})]' +(f'-[SS4: ({round(list(self.SubStats.items())[3][1],1)} {list(self.SubStats.items())[3][0]})]' if len(self.SubStats) == 4 else "")


    #function that adds 1 substat to the artifact
    def GenerateSubStat(self):

        stat_generated = False

        while not stat_generated: #generate until substat is not a repeated one 

            generated_stat = random.choices(list(self.SUB_STATS_CHANCE["ELEM_DMG" if self.MainStat[-3:] == "DMG" else self.MainStat]), weights=tuple(self.SUB_STATS_CHANCE["ELEM_DMG" if self.MainStat[-3:] == "DMG" else self.MainStat].values()))[0]

            if generated_stat not in self.SubStats: #if not duplicate 
                
                self.SubStats[generated_stat] = self.ARTIFACT_SUB_STATS_ROLL_RANGE[generated_stat][random.randint(0,len(self.ARTIFACT_SUB_STATS_ROLL_RANGE[generated_stat])-1)]
                
                stat_generated = True
    

    #function to level up artifact by n levels 
    def LevelUp(self, levels):
        
        original_level = self.Level
        self.Level += levels

        if self.Level%4 == 0: #if upgrade substat level 
        
            for _ in range(math.floor( (self.Level-original_level)/4)): #loop amount of stat level ups

                if len(self.SubStats) == 3: #if level up and 3 stats add one 
                    self.GenerateSubStat()
                else: #else level up stat 
                    sub_stat_to_upgrade = list(self.SubStats)[random.randint(0,3)]
                    self.SubStats[sub_stat_to_upgrade] += self.ARTIFACT_SUB_STATS_ROLL_RANGE[sub_stat_to_upgrade][random.randint(0,len(self.ARTIFACT_SUB_STATS_ROLL_RANGE[sub_stat_to_upgrade])-1)]

                    #print(sub_stat_to_upgrade)
