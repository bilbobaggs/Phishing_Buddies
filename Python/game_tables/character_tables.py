
ability_list = ["Charisma","Constitution","Dexterity","Intelligence","Strength",
                "Wisdom"]

skill_list ={"Charisma":["Deception","Intimidation","Performance","Persuasion"],
             "Dexterity":["Acrobatics","Sleight of Hand","Stealth"],
             "Intelligence":["Arcana","History","Investigation","Nature",\
                 "Religion"],
             "Strength":["Athletics"],
             "Wisdom":["Animal Handling","Insight","Medicine","Perception",\
                 "Survival"]}

armor_catagories = ["Light Armor","Medium Armor","Heavy Armor","Shields"]

armor_table = {"Light Armor":["Padded","Leather","Studded Leather"],
               "Medium Armor":["Hide","Chain Shirt","Scale Mail","Breastplate",
                               "Half Plate"],
               "Heavy Armor":["Ring Mail","Chain Mail","Splint","Plate"],
               "Shields":"Shield"}

weapon_catagories = ["All","Martial Weapons","Melee","Ranged","Simple Weapons"]

weapon_table = {"All":["Battleaxe","Blowgun","Club","Crossbow, Hand",\
    "Crossbow, Heavy",
                  "Crossbow, Light","Dagger","Dart","Flail","Glaive","Greataxe",
                  "Greatclub","Greatsword","Halberd","Handaxe","Lance",
                  "Light Hammer","Longsword","Javelin","Mace","Maul",
                  "Morningstar","Pike","Quarterstaff","Rapier","Scimitar",
                  "Shortsword","Shortbow","Sickle","Sling","Spear","Trident",
                  "War Pick","Warhammer","Whip"],
           "Martial Weapons":{"All":["Club","Crossbow, Light","Dagger","Dart",
                                     "Greatclub","Handaxe", "Javelin",
                                     "Light Hammer","Mace", "Quarterstaff",
                                     "Shortbow","Sickle","Sling","Spear"],
                              "Melee":["Club","Dagger","Greateclub","Handaxe",
                                       "Javelin","Light Hammer","Mace",
                                       "Quarterstaff","Sickle","Spear"],
                              "Ranged":["Crossbow, Light","Dart","Shortbow",\
                                  "Sling"]},
           "Simple Weapons":{"All":["Battleaxe","Blowgun","Crossbow, Hand",
                                    "Crossbow, Heavy","Flail","Glaive",
                                    "Greataxe","Greatsword","Halberd","Lance",
                                    "Longsword","Maul","Morningstar","Pike",
                                    "Rapier","Scimitar","Shortsword","Trident",
                                    "War Pick","Warhammer","Whip"],
                             "Melee":["Battleaxe","Flail","Glaive","Greataxe",
                                     "Greatsword","Halberd","Lance","Longsword",
                                     "Maul","Morningstar","Pike","Rapier",
                                     "Scimitar","Shortsword","Trident",\
                                         "War Pick",
                                     "Warhammer","Whip"],
                             "Ranged":["Blowgun","Crossbow, Hand",\
                                 "Crossbow, Heavy",
                                      "Longbow","Net"]}}


class_list = ["Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin",
              "Ranger", "Rogue","Sorcerer","Warlock","Wizard"]

class_specialties = {"Catagories":["Primal Path","Bard College","Devine Domain",
                                   "Druid Circle","Martial Archtype",
                                   "Monastic Tradition","Sacred Oath",
                                   "Ranger Archtype","Roguish Archetype",
                                   "Sorcerous Origin","Otherwordly Patron",
                                   "Arcane Tradition"],
                     "Barbarian":{"Primal Path":["Path of the Berserker",
                                                  "Path of the Totem Warrior"]},
                     "Bard":{"Bard College":["College of Lore",
                                             "College of Valor"]},
                     "Cleric":{"Devine Domain":["Knowledge Domain",
                                                "Life Domain","Light Domain",
                                                "Nature Domain","Tempest Domain",
                                                "Trickery Domain","War Domain"]},
                     "Druid":{"Druid Circle":["Circle of the Land",
                                              "Circle of the Moon"]},
                     "Fighter":{"Martial Archtype":["Champion","Battle Master",
                                                     "Eldritch Knight"]},
                     "Monk":{"Monastic Tradition":["Way of the Open Hand",
                                                   "Way of the Shadow",
                                                   "Way of the Four Elements"]},
                     "Paladin":{"Sacred Oath":["Oath of Devotion",
                                               "Oath of the Ancients",
                                               "Oath of Vengeance"]},
                     "Ranger":{"Ranger Archtype":["Hunter","Beast Master"]},
                     "Rogue":{"Roguish Archetype":["Thief","Assassian",
                                                   "Arcane Trickster"]},
                     "Sorcerer":{"Sorcerous Origin":["Draconic Bloodline",
                                                      "Wild Magic"]},
                     "Warlock":{"Otherwordly Patron":["The Archfey","The Fiend"]},
                     "Wizard":{"Arcane Tradition":["School of Abjuration",
                                                   "School of Conjuration",
                                                   "School of Enchantment",
                                                   "School of Evocation",
                                                   "School of Illusion",
                                                   "School of Necromancy",
                                                   "School of Transmutation"]}
                     }

race_list = ["Dragonborn","Dwarf","Elf","Gnome","Half-Elf","Half-Orc","Halfling",
             "Human","Tiefling"]

subrace_list = ["Base","Hill Dwarf","Moutain Dwarf","High Elf","Wood Elf",
                "Dark Elf","Forest Gnome","Rock Gnome","Lightfoot","Stout"]

racial_attributes = {"Dragonborn":{"Base":[[1,0,0,0,2,0],"Medium",30]},
                     "Dwarf":{"Base":[[0,2,0,0,0,0],"Medium",25],
                              "Hill Dwarf":[[0,2,0,0,0,1],"Medium",25],
                              "Moutain Dwarf":[[0,2,0,0,2,0],"Medium",25]},
                     "Elf":{"Base":[[0,0,2,0,0,0],"Medium",30],
                            "High Elf":[[0,0,2,1,0,0],"Medium",30],
                            "Wood Elf":[[0,0,2,0,0,1],"Medium",35],
                            "Dark Elf":[[1,0,2,0,0,0],"Medium",30]},
                     "Gnome":{"Base":[[0,0,0,2,0,0],"Small",25],
                              "Forest Gnome":[[0,0,1,2,0,0],"Small",25],
                              "Rock Gnome":[[0,1,0,2,0,0],"Small",25]},
                     "Half-Elf":{"Base":[[2,0,0,0,0,0],"Medium",30]},
                     "Half-Orc":{"Base":[[1,0,0,0,2,0],"Medium",30]},
                     "Halfling":{"Base":[[0,0,2,0,0,0],"Small",25],
                                 "Lightfoot":[[1,0,2,0,0,0],"Small",25],
                                 "Stout":[[0,1,2,0,0,0],"Small",25]},
                     "Human":{"Base":[[1,1,1,1,1,1],"Medium",30]},
                     "Tiefling":{"Base":[[2,0,0,1,0,0],"Medium",30]}}

barbarian_armor = armor_table[armor_catagories[0]] \
                  + armor_table[armor_catagories[1]] \
                  + [armor_table[armor_catagories[3]]]
barbarian_weapons = weapon_table[weapon_catagories[0]]
barbarian_saving = [ability_list[1],ability_list[4]]
barbarian_skills = [skill_list[ability_list[5]][0],skill_list[ability_list[4]][0],
                    skill_list[ability_list[0]][1],skill_list[ability_list[3]][3],
                    skill_list[ability_list[5]][3],skill_list[ability_list[5]][4]]

bard_armor = armor_table[armor_catagories[0]]
bard_weapons = weapon_table[weapon_catagories[4]][weapon_catagories[0]] \
               + [weapon_table[weapon_catagories[0]][3],
                weapon_table[weapon_catagories[0]][17],
                weapon_table[weapon_catagories[0]][24],
                weapon_table[weapon_catagories[0]][26]]
bard_saving = [ability_list[0],ability_list[2]]
bard_skills = skill_list[ability_list[0]] + skill_list[ability_list[2]] \
              + skill_list[ability_list[3]] + skill_list[ability_list[4]] \
              + skill_list[ability_list[5]]

cleric_armor = armor_table[armor_catagories[0]] \
               + armor_table[armor_catagories[1]] \
               + [armor_table[armor_catagories[3]]]
cleric_weapons = weapon_table[weapon_catagories[4]][weapon_catagories[0]]
cleric_saving = [ability_list[0],ability_list[5]]
cleric_skills = [skill_list[ability_list[3]][1],skill_list[ability_list[5]][1],
                 skill_list[ability_list[5]][2],skill_list[ability_list[0]][3],
                 skill_list[ability_list[3]][4]]

druid_armor = armor_table[armor_catagories[0]] \
              + armor_table[armor_catagories[1]] \
              + [armor_table[armor_catagories[3]]]
druid_weapons = [weapon_table[weapon_catagories[0]][2],
                weapon_table[weapon_catagories[0]][6],
                weapon_table[weapon_catagories[0]][7],
                weapon_table[weapon_catagories[0]][18],
                weapon_table[weapon_catagories[0]][19],
                weapon_table[weapon_catagories[0]][23],
                weapon_table[weapon_catagories[0]][25],
                weapon_table[weapon_catagories[0]][28],
                weapon_table[weapon_catagories[0]][29],
                weapon_table[weapon_catagories[0]][30]]
druid_saving = [ability_list[3],ability_list[5]]
druid_skills = [skill_list[ability_list[3]][0],skill_list[ability_list[5]][0],
                skill_list[ability_list[5]][1],skill_list[ability_list[5]][2],
                skill_list[ability_list[3]][3],skill_list[ability_list[5]][3],
                skill_list[ability_list[3]][4],skill_list[ability_list[5]][4]]

fighter_armor = armor_table[armor_catagories[0]] \
                + armor_table[armor_catagories[1]] \
                + armor_table[armor_catagories[2]] \
                + [armor_table[armor_catagories[3]]]
fighter_weapons = weapon_table[weapon_catagories[0]]
fighter_saving = [ability_list[1],ability_list[4]]
fighter_skills = [skill_list[ability_list[2]][0],skill_list[ability_list[5]][0],
                  skill_list[ability_list[4]][0],skill_list[ability_list[3]][1],
                  skill_list[ability_list[5]][1],skill_list[ability_list[0]][1],
                  skill_list[ability_list[5]][3],skill_list[ability_list[5]][4]]

monk_armor = None
monk_weapons = weapon_table[weapon_catagories[4]][weapon_catagories[0]] \
               + [weapon_table[weapon_catagories[0]][26]]
monk_saving = [ability_list[2],ability_list[4]]
monk_skills = [skill_list[ability_list[2]][0],skill_list[ability_list[4]][0],
               skill_list[ability_list[3]][1],skill_list[ability_list[5]][1],
               skill_list[ability_list[3]][4],skill_list[ability_list[2]][2]]

paladin_armor = armor_table[armor_catagories[0]] \
                + armor_table[armor_catagories[1]] \
                + armor_table[armor_catagories[2]] \
                + [armor_table[armor_catagories[3]]]
paladin_weapons = weapon_table[weapon_catagories[0]]
paladin_saving = [ability_list[0],ability_list[5]]
paladin_skills = [skill_list[ability_list[4]][0],skill_list[ability_list[5]][1],
                  skill_list[ability_list[0]][1],skill_list[ability_list[5]][2],
                  skill_list[ability_list[0]][3],skill_list[ability_list[3]][4]]

ranger_armor = armor_table[armor_catagories[0]] \
               + armor_table[armor_catagories[1]] \
               + [armor_table[armor_catagories[3]]]
ranger_weapons = weapon_table[weapon_catagories[0]]
ranger_saving = [ability_list[2],ability_list[4]]
ranger_skills = [skill_list[ability_list[5]][0],skill_list[ability_list[4]][0],
                 skill_list[ability_list[5]][1],skill_list[ability_list[3]][2],
                 skill_list[ability_list[3]][3],skill_list[ability_list[5]][3],
                 skill_list[ability_list[2]][2],skill_list[ability_list[5]][4]]

rogue_armor = armor_table[armor_catagories[0]]
rogue_weapons = weapon_table[weapon_catagories[4]][weapon_catagories[0]] \
                + [weapon_table[weapon_catagories[0]][3]]
rogue_saving = [ability_list[2],ability_list[3]]
rogue_skills = [skill_list[ability_list[2]][0],skill_list[ability_list[4]][0],
                skill_list[ability_list[0]][0],skill_list[ability_list[5]][1],
                skill_list[ability_list[0]][1],skill_list[ability_list[3]][2],
                skill_list[ability_list[5]][3],skill_list[ability_list[0]][2],
                skill_list[ability_list[0]][3],skill_list[ability_list[2]][1],
                skill_list[ability_list[5]][2]]

sorcerer_armor = None
sorcerer_weapons = [weapon_table[weapon_catagories[0]][5],
                    weapon_table[weapon_catagories[0]][6],
                    weapon_table[weapon_catagories[0]][7],
                    weapon_table[weapon_catagories[0]][23],
                    weapon_table[weapon_catagories[0]][29]]
sorcerer_saving = [ability_list[0],ability_list[1]]
sorcerer_skills = [skill_list[ability_list[3]][0],skill_list[ability_list[0]][0],
                   skill_list[ability_list[5]][1],skill_list[ability_list[0]][1],
                   skill_list[ability_list[0]][3],skill_list[ability_list[3]][4]]

warlock_armor = armor_table[armor_catagories[0]]
warlock_weapons = weapon_table[weapon_catagories[4]][weapon_catagories[0]]
warlock_saving = [ability_list[0],ability_list[5]]
warlock_skills = [skill_list[ability_list[3]][0],skill_list[ability_list[0]][0],
                  skill_list[ability_list[3]][1],skill_list[ability_list[0]][1],
                  skill_list[ability_list[3]][2],skill_list[ability_list[3]][3],
                  skill_list[ability_list[3]][4]]

wizard_armor = None
wizard_weapons = [weapon_table[weapon_catagories[0]][5],
                  weapon_table[weapon_catagories[0]][6],
                  weapon_table[weapon_catagories[0]][7],
                  weapon_table[weapon_catagories[0]][23],
                  weapon_table[weapon_catagories[0]][29]]
wizard_saving = [ability_list[3],ability_list[5]]
wizard_skills = [skill_list[ability_list[3]][0],skill_list[ability_list[3]][1],
                 skill_list[ability_list[5]][1],skill_list[ability_list[3]][2],
                 skill_list[ability_list[5]][2],skill_list[ability_list[3]][4]]

class_attributes = {"Barbarian":[12,barbarian_armor,barbarian_weapons,None,
                                 barbarian_saving,2,barbarian_skills],
                    "Bard":[8,bard_armor,bard_weapons,None,bard_saving,3,
                            bard_skills],
                    "Cleric":[8,cleric_armor,cleric_weapons,None,cleric_saving,
                              2,cleric_skills],
                    "Druid":[8,druid_armor,druid_weapons,None,druid_saving,2,
                             druid_skills],
                    "Fighter":[10,fighter_armor,fighter_weapons,None,
                               fighter_saving,2,fighter_skills],
                    "Monk":[8,monk_armor,monk_weapons,None,monk_saving,2,
                            monk_skills],
                    "Paladin":[10,paladin_armor,paladin_weapons,None,
                               paladin_saving,2,paladin_skills],
                    "Ranger":[10,ranger_armor,ranger_weapons,None,ranger_saving,
                              3,ranger_skills],
                    "Rogue":[8,rogue_armor,rogue_weapons,None,rogue_saving,4,
                             rogue_skills],
                    "Sorcerer":[6,sorcerer_armor,sorcerer_weapons,None,
                              sorcerer_saving,2,sorcerer_skills],
                    "Warlock":[8,warlock_armor,warlock_weapons,None,
                               warlock_saving,2,warlock_skills],
                    "Wizard":[6,wizard_armor,wizard_weapons,None,wizard_saving,2,
                              wizard_skills]}
