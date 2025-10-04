
import copy, os, random
from game_tables import character_tables as ct

def choose_player_race(race_list, player_name):
  for index, race in enumerate(race_list, start = 1):
    print(f" {index:2d} - {race}")
  race = input(f"\nPlease choose a race {player_name}? ")
  race = int(race) - 1
  race_str = race_list[race]
  check = input(f"\nYou have choosen {race_str}, is this correct? [Y|n]: ") or \
"Y"
  if check != "Y" and check != "y":
    choose_player_race(race_list)
  os.system('clear')
  if race_str is race_list[1] or race_str is race_list[2] or race_str is race_list[3] or\
      race_str is race_list[6]:
    for index, subrace in enumerate(ct.racial_attributes[race_str].keys(),start=1):
      print(f"  {index:2d} - {subrace}")
    subrace = int(input(f"Please choose a subrace. [Base]: ") or 1) - 1
    match race_str:
      case "Elf":
        subrace += 2
      case "Gnome":
        subrace += 5
      case "Halfling":
        subrace += 7
  else:
    subrace = 0
  subrace_str = ct.subrace_list[subrace]
  return race_str, subrace_str

def adjust_racial_traits(race,subrace,racial_attributes):
  charisma = racial_attributes[0][0]
  constitution = racial_attributes[0][1]
  dexterity = racial_attributes[0][2]
  intelligence = racial_attributes[0][3]
  strength = racial_attributes[0][4]
  wisdom = racial_attributes[0][5]
  size = racial_attributes[1]
  speed = racial_attributes[2]
  match race:
    case "Half-Elf":
      choice = 2
      ability_list = copy.deepcopy(ct.ability_list)
      ability_list.remove(ability_list[0])
      choices = []
      while choice > 0:
        if choice > 1:
          message = "two abilities"
        else:
          message = "one ability"
        print(f"Please chose {message} to increase by one point.")
        for index,ability in enumerate(ability_list,start=1):
          print(f" {index} - {ability}")
        skills = int(input(f"\n: ")) - 1
        choices.append(ability_list[skills])
        ability_list.remove(ability_list[skills])
        choice -= 1
        os.system('clear')
      for ability in choices:
        match ability:
          case "Constitution":
            constitution += 1
          case "Dexterity":
            dexterity += 1
          case "Intelligence":
            intelligence += 1
          case "Strength":
            strength += 1
          case "Wisdom":
            wisdom += 1
  os.system('clear')
  racial_attributes = [[charisma,constitution,dexterity,intelligence,
      strength,wisdom],size,speed]
  return racial_attributes

def choose_player_class(job_class_list):
  print("")
  for index, job_class in enumerate(job_class_list, start = 1):
    print(f" {index:2d} - {job_class}")
  job_class = input("\nPlease choose a class? ")
  job_class = int(job_class) -1
  job_class_str = job_class_list[job_class]
  check = input(f"\nYou have choosen {job_class_str}, is this correct? [Y|n]: "\
) or "Y"
  if check != "Y" and check != "y":
    choose_player_class(job_class_list)
  os.system('clear')
  specialty_title = ct.class_specialties["Catagories"][job_class]
  specialty_list = ct.class_specialties[job_class_str][ct.class_specialties[\
      "Catagories"][job_class]]
  for index, subclass in enumerate(specialty_list,start=1):
    print(f" {index:2d} - {subclass}")
  job_specialty_int = int(input(f"\nPlease choose a {specialty_title}: ")) - 1
  job_specialty = ct.class_specialties[job_class_str][specialty_title]\
      [job_specialty_int]
  return job_class_str, specialty_title, job_specialty

def choose_skill_proficiencies(number, skill_list):
  print("")
  count = number
  temp_list = copy.deepcopy(skill_list)
  choices = []
  while count > 0:
    for index, skill in enumerate(temp_list,start=1):
      print(f"  {index:2d} - {skill}")
    choice = int(input(f"\nPlease choose {count} skills: ")) - 1
    print()
    choices.append(temp_list[choice])
    temp_list.remove(temp_list[choice])
    count -= 1
  return choices

def choose_player_name(player):
  temp_name = input(f"\nPlease choose a name for {player}: ")
  check = input(f"\nYou have entered the name {temp_name}, is this correct? [Y|\
n]: ") or "Y"
  print("")
  if check != "Y" and check != "y":
    choose_player_name(player)
  os.system('clear')
  return temp_name

def roll_dice(number_of_dice, number_of_sides):
  roll_count = 1
  rolls = []
  sum_of_rolls = 0
  while number_of_dice >= roll_count:
    current_roll = random.randint(1, number_of_sides)
    rolls.append(current_roll)
    roll_count += 1
    sum_of_rolls += current_roll
  rolls.sort(reverse = True)
  return sum_of_rolls, rolls

def roll_ability_scores():
  number_of_rolls = 1
  rolls = []
  while number_of_rolls <= 6:
    temp_roll = roll_dice(4, 6)[1]
    roll = temp_roll[0] + temp_roll[1] + temp_roll[2]
    print(f"You rolled a {roll:3d}.")
    rolls.append(roll)
    number_of_rolls += 1
  rolls.sort(reverse = True)
  return rolls

def assign_ability_rolls(ability_rolls):
  ability_list = copy.deepcopy(ct.ability_list)
  for roll in ability_rolls:
    print(f"\nWhich ability will get the roll of {roll}.\n")
    for index, ability in enumerate(ability_list,start=1):
      print(f"  {index} - {ability}")
    ability = int(input("\n: ")) - 1
    match ability_list[ability]:
      case "Charisma":
        charisma = roll
      case "Constitution":
        constitution = roll
      case "Dexterity":
        dexterity = roll
      case "Intelligence":
        intelligence = roll
      case "Strength":
        strength = roll
      case "Wisdom":
        wisdom = roll
    ability_list.remove(ability_list[ability])
  os.system('clear')
  return charisma, constitution, dexterity, intelligence, strength, wisdom

