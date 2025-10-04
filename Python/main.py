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
while count <= int(players):
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
  census = f"|--------| Race: {player.race:^12} |-------| Subrace: \
      {player.subrace:^16} |-------|"
  print(census)
  job_class_info = f"|-| Class: {player.job_class:^11} |-| {\
      player.specialty_title:^21}: {player.job_specialty:^27} |-|"
  print(job_class_info)
  stats = f"|----| Armor Class: {player.armor_class:^3} |-| Hit Points: \
{player.hit_points:^3} |-| Hit Die: d{player.hit_dice:^2d} |-| Level: \
{player.level:^2} |----|"
  print(stats)
  print(f"|" + ("#" * (width - 2)) + "|")
  print(f"| Cha Roll: {player.charisma:2d} |--| Mod: {player.charisma_save:2d} |")
  print(f"| Con Roll: {player.constitution:2d} |--| Mod: {player.constitution_save:2d} |")
  print(f"| Dex Roll: {player.dexterity:2d} |--| Mod: {player.dexterity_save:2d} |")
  print(f"| Int Roll: {player.intelligence:2d} |--| Mod: {player.intelligence_save:2d} |")
  print(f"| Str Roll: {player.strength:2d} |--| Mod: {player.strength_save:2d} |")
  print(f"| Wis Roll: {player.wisdom:2d} |--| Mod: {player.wisdom_save:2d} |")
  print(f"| {player.proficiency_bonus:2d} :Proficiency Bonus |")
  print(f"| {player.acrobatics:2d} :Acrobatics |")
  print(f"| {player.animal_handling:2d} :Animal Handling |")
  print(f"| {player.arcana:2d} :Arcana |")
  print(f"| {player.athletics:2d} :Athletics |")
  print(f"| {player.deception:2d} :Deception |")
  print(f"| {player.history:2d} :History |")
  print(f"| {player.insight:2d} :Insight |")
  print(f"| {player.intimidation:2d} :Intimidation |")
  print(f"| {player.investigation:2d} :Investigation |")
  print(f"| {player.medicine:2d} :Medicine |")
  print(f"| {player.nature:2d} :Nature |")
  print(f"| {player.perception:2d} :Perception |")
  print(f"| {player.performance:2d} :Performance |")
  print(f"| {player.persuasion:2d} :Persuasion |")
  print(f"| {player.religion:2d} :Religion |")
  print(f"| {player.sleight_of_hand:2d} :Sleight of Hand |")
  print(f"| {player.stealth:2d} :Stealth |")
  print(f"| {player.survival:2d} :Survival |")
