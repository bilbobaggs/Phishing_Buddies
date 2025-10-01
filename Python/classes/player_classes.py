
import math
from functions import player_functions as pf
from game_tables import character_tables as ct

class player_character:
  def __init__(self, level, proficiency_bonus, name, race, job_class):

    race = pf.choose_player_race(race, name)
    racial_attributes = ct.racial_attributes[race[0]][race[1]]
    racial_profile = pf.adjust_racial_traits(race[0],race[1],racial_attributes)
    jclass = pf.choose_player_class(job_class)
    class_profile = ct.class_attributes[jclass]
    skill_proficiencies = pf.choose_skill_proficiencies(class_profile[5],\
        class_profile[6])

    ability_rolls = pf.roll_ability_scores()
    ability_rolls = pf.assign_ability_rolls(ability_rolls)

    self.level = level
    self.proficiency_bonus = proficiency_bonus
    self.race = race[0]
    self.subrace = race[1]
    self.job_class = jclass
    self.name = pf.choose_player_name(name)
    self.hit_dice = class_profile[0]
    self.speed = racial_profile[2]
    self.size = racial_profile[1]

  # Charisma attribute list.
    self.charisma = ability_rolls[0]
    self.charisma_mod = ((int(ability_rolls[0])-10)//2)+racial_profile[0][0]

    if "Charisma" in class_profile[4]:
      self.charisma_save = self.charisma_mod + self.proficiency_bonus
    else:
      self.charisma_save = self.charisma_mod

    if "Deception" in skill_proficiencies:
      self.deception = self.charisma_save + self.proficiency_bonus
    else:
      self.deception = self.charisma_save

    if "Intimidation" in skill_proficiencies:
      self.intimidation = self.charisma_save + self.proficiency_bonus
    else:
      self.intimidation = self.charisma_save

    if "Performance" in skill_proficiencies:
      self.performance = self.charisma_save + self.proficiency_bonus
    else:
      self.performance = self.charisma_save

    if "Persuasion" in skill_proficiencies:
      self.persuasion = self.charisma_save + self.proficiency_bonus
    else:
      self.persuasion = self.charisma_save

  # Constitution attribute list.
    self.constitution = ability_rolls[1]
    self.constitution_mod = ((int(ability_rolls[1])-10)//2)+racial_profile[0][1]
    self.hit_points = self.constitution_mod + int(self.hit_dice)

    if "Constitution" in class_profile[4]:
      self.constitution_save = self.constitution_mod + self.proficiency_bonus
    else:
      self.constitution_save = self.constitution_mod

  # Dexterity attribute list
    self.dexterity = ability_rolls[2]
    self.dexterity_mod = ((int(ability_rolls[2])-10)//2)+racial_profile[0][2]

    if "Dexterity" in class_profile[4]:
      self.dexterity_save = self.dexterity_mod + self.proficiency_bonus
    else:
      self.dexterity_save = self.dexterity_mod

    self.armor_class = 10 + self.dexterity_save

    if "Acrobatics" in skill_proficiencies:
      self.acrobatics = self.dexterity_save + self.proficiency_bonus
    else:
      self.acrobatics = self.dexterity_save

    if "Sleight of Hand" in skill_proficiencies:
      self.sleight_of_hand = self.dexterity_save + self.proficiency_bonus
    else:
      self.sleight_of_hand = self.dexterity_save

    if "Stealth" in skill_proficiencies:
      self.stealth = self.dexterity_save + self.proficiency_bonus
    else:
      self.stealth = self.dexterity_save

  # Intelligence attribute list
    self.intelligence = ability_rolls[3]
    self.intelligence_mod = ((int(ability_rolls[3])-10)//2)+racial_profile[0][3]

    if "Intelligence" in class_profile[4]:
      self.intelligence_save = self.intelligence_mod + self.proficiency_bonus
    else:
      self.intelligence_save = self.intelligence_mod

    if "Arcana" in skill_proficiencies:
      self.arcana = self.intelligence_save + self.proficiency_bonus
    else:
      self.arcana = self.intelligence_save

    if "History" in skill_proficiencies:
      self.history = self.intelligence_save + self.proficiency_bonus
    else:
      self.history = self.intelligence_save

    if "Investigation" in skill_proficiencies:
      self.investigation = self.intelligence_save + self.proficiency_bonus
    else:
      self.investigation = self.intelligence_save

    if "Nature" in skill_proficiencies:
      self.nature = self.intelligence_save + self.proficiency_bonus
    else:
      self.nature = self.intelligence_save

    if "Religion" in skill_proficiencies:
      self.religion = self.intelligence_save + self.proficiency_bonus
    else:
      self.religion = self.intelligence_save

  # Strength attributes list
    self.strength = ability_rolls[4]
    self.strength_mod = ((int(ability_rolls[4])-10)//2)+racial_profile[0][4]

    if "Strength" in class_profile[4]:
      self.strength_save = self.strength_mod + self.proficiency_bonus
    else:
      self.strength_save = self.strength_mod

    if "Athletics" in skill_proficiencies:
      self.athletics = self.strength_save + self.proficiency_bonus
    else:
      self.athletics = self.strength_save

  # Wisdom attribute list
    self.wisdom = ability_rolls[5]
    self.wisdom_mod = ((int(ability_rolls[5])-10)//2)+racial_profile[0][5]

    if "Wisdom" in class_profile[4]:
      self.wisdom_save = self.wisdom_mod + self.proficiency_bonus
    else:
      self.wisdom_save = self.wisdom_mod

    if "Animal Handling" in skill_proficiencies:
      self.animal_handling = self.wisdom_save + self.proficiency_bonus
    else:
      self.animal_handling = self.wisdom_save

    if "Insight" in skill_proficiencies:
      self.insight = self.wisdom_save + self.proficiency_bonus
    else:
      self.insight = self.wisdom_save

    if "Medicine" in skill_proficiencies:
      self.medicine = self.wisdom_save + self.proficiency_bonus
    else:
      self.medicine = self.wisdom_save

    if "Perception" in skill_proficiencies:
      self.perception = self.wisdom_save + self.proficiency_bonus
    else:
      self.perception = self.wisdom_save

    if "Survival" in skill_proficiencies:
      self.survival = self.wisdom_save + self.proficiency_bonus
    else:
      self.survival = self.wisdom_save

class ability_list:
    def __init__(self, ability, value):
        self.ability = ability
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, ability):
        return hash(ability) % self.capacity

    def insert(self, ability, value):
        index = self._hash(ability)

        if self.table[index] is None:
            self.table[index] = ability_list(ability, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.ability == ability:
                    current.value = value
                    return
                current = current.next
            new_node = ability_list(ability, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, ability):
        index = self._hash(ability)

        current = self.table[index]
        while current:
            if current.ability == ability:
                return current.value
            current = current.next

        raise KeyError(ability)

    def remove(self, ability):
        index = self._hash(ability)

        previous = None
        current = self.table[index]

        while current:
            if current.ability == ability:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

        raise KeyError(ability)

    def __len__(self):
        return self.size

    def __contains__(self, ability):
        try:
            self.search(ability)
            return True
        except KeyError:
            return False
