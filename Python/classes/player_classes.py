
import math
from functions import player_functions as pf
from game_tables import character_tables as ct

class player_character:
  def __init__(self, level, proficiency_bonus, name, race, job_class):

    race = pf.choose_player_race(race, name)
    racial_attributes = ct.racial_attributes[race[0]][race[1]]
    racial_profile = pf.adjust_racial_traits(race[0],race[1],racial_attributes)
    jclass = pf.choose_player_class(job_class)
    class_profile = ct.class_attributes[jclass[0]]
    skill_proficiencies = pf.choose_skill_proficiencies(class_profile[5],\
        class_profile[6])

    ability_rolls = pf.roll_ability_scores()
    ability_rolls = pf.assign_ability_rolls(ability_rolls)

    self.level = level
    self.proficiency_bonus = proficiency_bonus
    self.race = race[0]
    self.subrace = race[1]
    self.job_class = jclass[0]
    self.specialty_title = jclass[1]
    self.job_specialty = jclass[2]
    self.name = pf.choose_player_name(name)
    self.hit_die = class_profile[0]
    self.hit_dice = level
    self.speed = racial_profile[2]
    self.size = racial_profile[1]

  # Charisma attribute list.
    self.charisma = ability_rolls[0] + racial_profile[0][0]
    self.charisma_mod = ((int(self.charisma) - 10) // 2)

    if "Charisma" in class_profile[4]:
      self.charisma_proficiency = True
      self.charisma_save = self.charisma_mod + self.proficiency_bonus
    else:
      self.charisma_proficiency = False
      self.charisma_save = self.charisma_mod

    if "Deception" in skill_proficiencies:
      self.deception_proficiency = True
      self.deception = self.charisma_mod + self.proficiency_bonus
    else:
      self.deception_proficiency = False
      self.deception = self.charisma_mod

    if "Intimidation" in skill_proficiencies:
      self.intimidation_proficiency = True
      self.intimidation = self.charisma_mod + self.proficiency_bonus
    else:
      self.intimidation_proficiency = False
      self.intimidation = self.charisma_mod

    if "Performance" in skill_proficiencies:
      self.performance_proficiency = True
      self.performance = self.charisma_mod + self.proficiency_bonus
    else:
      self.performance_proficiency = False
      self.performance = self.charisma_mod

    if "Persuasion" in skill_proficiencies:
      self.persuasion_proficiency = True
      self.persuasion = self.charisma_mod + self.proficiency_bonus
    else:
      self.persuasion_proficiency = False
      self.persuasion = self.charisma_mod

  # Constitution attribute list.
    self.constitution = ability_rolls[1] + racial_profile[0][1]
    self.constitution_mod = ((int(self.constitution) - 10) // 2)
    self.hit_points = self.constitution_mod + int(self.hit_die)

    if "Constitution" in class_profile[4]:
      self.constitution_proficiency = True
      self.constitution_save = self.constitution_mod + self.proficiency_bonus
    else:
      self.constitution_proficiency = False
      self.constitution_save = self.constitution_mod

  # Dexterity attribute list
    self.dexterity = ability_rolls[2] + racial_profile[0][2]
    self.dexterity_mod = ((int(self.dexterity) - 10) // 2)

    if "Dexterity" in class_profile[4]:
      self.dexterity_proficiency = True
      self.dexterity_save = self.dexterity_mod + self.proficiency_bonus
    else:
      self.dexterity_proficiency = False
      self.dexterity_save = self.dexterity_mod

    self.armor_class = 10 + self.dexterity_mod

    if "Acrobatics" in skill_proficiencies:
      self.acrobatics_proficiency = True
      self.acrobatics = self.dexterity_mod + self.proficiency_bonus
    else:
      self.acrobatics_proficiency = False
      self.acrobatics = self.dexterity_mod

    if "Sleight of Hand" in skill_proficiencies:
      self.sleight_of_hand_proficiency = True
      self.sleight_of_hand = self.dexterity_mod + self.proficiency_bonus
    else:
      self.sleight_of_hand_proficiency = False
      self.sleight_of_hand = self.dexterity_mod

    if "Stealth" in skill_proficiencies:
      self.stealth_proficiency = True
      self.stealth = self.dexterity_mod + self.proficiency_bonus
    else:
      self.stealth_proficiency = False
      self.stealth = self.dexterity_mod

  # Intelligence attribute list
    self.intelligence = ability_rolls[3] + racial_profile[0][3]
    self.intelligence_mod = ((int(self.intelligence) - 10) // 2)

    if "Intelligence" in class_profile[4]:
      self.intelligence_proficiency = True
      self.intelligence_save = self.intelligence_mod + self.proficiency_bonus
    else:
      self.intelligence_proficiency = False
      self.intelligence_save = self.intelligence_mod

    if "Arcana" in skill_proficiencies:
      self.arcana_proficiency = True
      self.arcana = self.intelligence_mod + self.proficiency_bonus
    else:
      self.arcana_proficiency = False
      self.arcana = self.intelligence_mod

    if "History" in skill_proficiencies:
      self.history_proficiency = True
      self.history = self.intelligence_mod + self.proficiency_bonus
    else:
      self.history_proficiency = False
      self.history = self.intelligence_mod

    if "Investigation" in skill_proficiencies:
      self.investigation_proficiency = True
      self.investigation = self.intelligence_mod + self.proficiency_bonus
    else:
      self.investigation_proficiency = False
      self.investigation = self.intelligence_mod

    if "Nature" in skill_proficiencies:
      self.nature_proficiency = True
      self.nature = self.intelligence_mod + self.proficiency_bonus
    else:
      self.nature_proficiency = False
      self.nature = self.intelligence_mod

    if "Religion" in skill_proficiencies:
      self.religion_proficiency = True
      self.religion = self.intelligence_mod + self.proficiency_bonus
    else:
      self.religion_proficiency = False
      self.religion = self.intelligence_mod

  # Strength attributes list
    self.strength = ability_rolls[4] + racial_profile[0][4]
    self.strength_mod = ((int(self.strength) - 10) // 2)

    if "Strength" in class_profile[4]:
      self.strength_proficiency = True
      self.strength_save = self.strength_mod + self.proficiency_bonus
    else:
      self.strength_proficiency = False
      self.strength_save = self.strength_mod

    if "Athletics" in skill_proficiencies:
      self.athletics_proficiency = True
      self.athletics = self.strength_mod + self.proficiency_bonus
    else:
      self.athletics_proficiency = False
      self.athletics = self.strength_mod

  # Wisdom attribute list
    self.wisdom = ability_rolls[5] + racial_profile[0][5]
    self.wisdom_mod = ((int(self.wisdom) - 10) // 2)

    if "Wisdom" in class_profile[4]:
      self.wisdom_proficiency = True
      self.wisdom_save = self.wisdom_mod + self.proficiency_bonus
    else:
      self.wisdom_proficiency = False
      self.wisdom_save = self.wisdom_mod

    if "Animal Handling" in skill_proficiencies:
      self.animal_handling_proficiency = True
      self.animal_handling = self.wisdom_mod + self.proficiency_bonus
    else:
      self.animal_handling_proficiency = False
      self.animal_handling = self.wisdom_mod

    if "Insight" in skill_proficiencies:
      self.insight_proficiency = True
      self.insight = self.wisdom_mod + self.proficiency_bonus
    else:
      self.insight_proficiency = False
      self.insight = self.wisdom_mod

    if "Medicine" in skill_proficiencies:
      self.medicine_proficiency = True
      self.medicine = self.wisdom_mod + self.proficiency_bonus
    else:
      self.medicine_proficiency = False
      self.medicine = self.wisdom_mod

    if "Perception" in skill_proficiencies:
      self.perception_proficiency = True
      self.perception = self.wisdom_mod + self.proficiency_bonus
    else:
      self.perception_proficiency = False
      self.perception = self.wisdom_mod

    if "Survival" in skill_proficiencies:
      self.survival_proficiency = True
      self.survival = self.wisdom_mod + self.proficiency_bonus
    else:
      self.survival_proficiency = False
      self.survival = self.wisdom_mod

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
