#! /usr/bin/python

import os
from classes import player_classes as pc
from functions import player_functions as pf
from game_tables import character_tables as ct

os.system('clear')

ability_scores = []

player_list = []

print("Welcome to Fantasy Quest!\n")

players = input("How many players are there? ")

print()
count = 1
while int(players) >= count:
    player_name = "Player " + str(count)
    player_list.append(pc.player_character(1, 2, player_name, ct.race_list,
                                           ct.class_list))
    count += 1

os.system('clear')
for player in player_list:
  player_name = "| " + player.name + " |"
  name = f"|-{player_name:-^77}-|"
  width = len(name)
  print("")
  print(f"_" * width)
  print(name)
  print("|" + " " * int(width - 2) + "|")
  race = player.race + " |"
  subrace = player.subrace + " |"
  left_padding = "|" + "-" * 2 + "|"
  center_padding = "-" * 1 + "|"
  right_padding = "-" * 29 + "|"
  census = f"{left_padding} Race: {race:-<12}{center_padding} Subrace: {subrace\
:-<16}{right_padding}"
  print(census)
  job_class = player.job_class + " |"
  job_title = "| " + player.specialty_title
  job_specialty = job_title + ": " + player.job_specialty + " |"
  n = 2
  left_padding = "|" + "-" * n + "|"
  right_padding = "-" * int(n + 1) + "|"
  job_class_info = f"{left_padding} Class: {job_class:-<11}-{job_specialty:-<53\
}{right_padding}"
  print(job_class_info)
  print("|" + (" " * (width - 2))  + "|")
  stats = f"|--| Armor Class: {player.armor_class:^3} |-| Hit Points: {player.\
      hit_points:^3} |-| Hit Die: {player.hit_dice:2d} x d{player.\
      hit_die:^2d} |-| Level: {player.level:>2} |-|"
  print(stats)
  print(f"|" + ("#" * (width - 2)) + "|")
  row = f"|  Proficiency Bonus: {player.proficiency_bonus:2d}"
  row = row + (" " * (width - len(row) - 1)) + "|"
  print(row)
  print(f"|" + (" " * (width - 2)) + "|")
# Row for strength and wisdom
  if player.strength_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  save = player.strength_save
  roll = player.strength
  row = f"| {bubble}Strength Mod: {save:>2d} ({roll:>2d})  "

  if player.wisdom_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  save = player.wisdom_save
  roll = player.wisdom
  row = row + f"    {bubble}Wisdom Mod: {save:>2d} ({roll:>2d})"
  row = row + (" " * (width - len(row) - 1)) + "|"
  print(row)

# Row for athletics and animal handling
  if player.athletics_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = f"|   {bubble}Athletics: {player.athletics:2d}  "
  if player.animal_handling_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = row + " " * 12 + f"{bubble}Animal Handling: {player.animal_handling:2d}"
  row = row + (" " * (width - len(row) - 1)) + "|"
  print(row)

# Row for insight
  if player.insight_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = "|" + " " * 32 + f"{bubble}Insight: {player.insight:2d}"
  row = row + (" " * (width - len(row) - 1)) + "|"
  print(row)

# Row for dexterity and medicine
  if player.dexterity_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  save = player.dexterity_save
  roll = player.dexterity
  row = f"| {bubble}Dexerity Mod: {save:>2d} ({roll:>2d})  "
  if player.medicine_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = row + " " * 6 + f"{bubble}Medicine: {player.medicine:2d}"
  row = row + (" " * (width - len(row) - 1)) + "|"
  print(row)

# Row for acrobatics and perception
  if player.acrobatics_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = f"|   {bubble}Acrobatics: {player.acrobatics:2d}"
  if player.perception_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = row + " " * 13 + f"{bubble}Perception: {player.perception:2d}"
  row = row + (" " * (width - len(row) - 1)) + "|"
  print(row)

# Row for sleight of hand and survival
  if player.sleight_of_hand_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = f"|   {bubble}Sleight of Hand: {player.sleight_of_hand:2d}   "
  if player.survival_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = row + " " * 5 + f"{bubble}Survival: {player.survival:2d}"
  row = row + (" " * (width - len(row) - 1)) + "|"
  print(row)

# Row for stealth
  if player.stealth_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = f"|   {bubble}Stealth: {player.stealth:2d}"
  row = row + (" " * (width - len(row) - 1)) + "|"
  print(row)

# Row for charisma
  if player.charisma_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  save = player.charisma_save
  roll = player.charisma
  row = "|" + " " * 30 + f"{bubble}Charisma Mod: {save:>2d} ({roll:<2d})"
  row = row + (" " * (width - len(row) - 1)) + "|"
  print(row)

# Row for intelligence and deception
  if player.intelligence_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  save = player.intelligence_save
  roll = player.intelligence
  row = f"| {bubble}Intelligence Mod: {save:>2d} ({roll:>2d})"
  if player.deception_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = row + " " * 4 + f"{bubble}Deception: {player.deception:2d}"
  row = row + (" " * (width - len(row) - 1)) + "|"
  print(row)

# Row for arcana and intimidation
  if player.arcana_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = f"|   {bubble}Arcana: {player.arcana:2d}"
  if player.intimidation_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = row + " " * 17 + f"{bubble}Intimidation: {player.intimidation:2d}"
  row = row + (" " * (width - len(row) - 1)) + "|"
  print(row)

# Row for history and performance
  if player.history_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = f"|   {bubble}History: {player.history:2d}"
  if player.performance_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = row + " " * 16 + f"{bubble}Performance: {player.performance:2d}"
  row = row + (" " * (width - len(row) - 1)) + "|"
  print(row)

# Row for investigation and persuasion
  if player.investigation_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = f"|   {bubble}Investigation: {player.investigation:2d}"
  if player.persuasion_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = row + " " * 10 + f"{bubble}Persuasion: {player.persuasion:2d}"
  row = row + (" " * (width - len(row) - 1)) + "|"
  print(row)

# Row for nature
  if player.nature_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = f"|   {bubble}Nature: {player.nature:2d}"
  row = row + (" " * (width - len(row) - 1)) + "|"
  print(row)

# Row for religion and constitution
  if player.religion_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  row = f"|   {bubble}Religion: {player.religion:2d}"
  if player.constitution_proficiency:
    bubble = "\u25CF "
  else:
    bubble = "\u25CB "
  save = player.constitution_save
  roll = player.constitution
  row = row + " " * 13 + f"{bubble}Constitution Mod: {save:>2d} ({roll:>2d})"
  row = row + (" " * (width - len(row) - 1)) + "|"
  print(row)

