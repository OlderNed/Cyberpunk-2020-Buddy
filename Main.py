#Made by Exanimem, Ned, and Snowfish
"""Cyberpunk 2020 Buddy"""

import tkinter as tk
from tkinter import ttk
import random

MASTER = tk.Tk()
# Creates window

MASTER.title('Exanimem\'s Cyberpunk 2020 Buddy')

NB = ttk.Notebook(MASTER)
# Notebook handles tabs
GENERAL_PAGE_1 = ttk.Frame(NB)
GEAR_PAGE_2 = ttk.Frame(NB)
CYBERNETICS_PAGE_3 = ttk.Frame(NB)
WEAPONS_PAGE_4 = ttk.Frame(NB)
LIFEPATH_PAGE_5 = ttk.Frame(NB)
DICE_PAGE_6 = ttk.Frame(NB)
NB.add(GENERAL_PAGE_1, text='General')
NB.add(GEAR_PAGE_2, text='Gear')
NB.add(CYBERNETICS_PAGE_3, text='Cybernetics')
NB.add(WEAPONS_PAGE_4, text='Weapons')
NB.add(LIFEPATH_PAGE_5, text='Lifepath')
NB.add(DICE_PAGE_6, text='Dice')
NB.pack()

ttk.Style().theme_use('clam')
# Tkinter theme



#SELECTED_ROLE = tk.StringVar(MASTER)
#SELECTED_ROLE.set("Solo")

#def career_skills():
#    role = SELECTED_ROLE.get()
#    if role == "Solo":
#        tk.Label(GENERAL_PAGE_1, text="Combat Sense").grid(row=1)
#
#        COMBAT_SENSE = tk.Entry(GENERAL_PAGE_1, width=5)
#
#        COMBAT_SENSE.grid(row=1, column=2)
#
#        COMBAT_SENSE.insert(1, "1")

# PAGE 1 START - GENERAL
#ROLE_MENU = tk.OptionMenu(GENERAL_PAGE_1, SELECTED_ROLE, "Solo", "Rocker", "Netrunner", "Media", "Nomad", "Fixer", "Cop", "Corp", "Techie", command=career_skills)
#ROLE_MENU.grid(row=0, column=2)
tk.Label(GENERAL_PAGE_1, text="Handle").grid(row=0)
tk.Label(GENERAL_PAGE_1, text="Age").grid(row=1)

HANDLE = tk.Entry(GENERAL_PAGE_1, width=30)
AGE = tk.Entry(GENERAL_PAGE_1, width=3)

HANDLE.grid(row=0, column=1)
AGE.grid(row=1, column=1)

AGE.insert(1, "16")

tk.Label(GENERAL_PAGE_1, text="Intelligence (INT)").grid(row=0, column=2)
tk.Label(GENERAL_PAGE_1, text="Reflexes (REF)").grid(row=1, column=2)
tk.Label(GENERAL_PAGE_1, text="Technical Ability (TECH)").grid(row=2, column=2)
tk.Label(GENERAL_PAGE_1, text="Cool").grid(row=3, column=2)
tk.Label(GENERAL_PAGE_1, text="Attractiveness (ATTR)").grid(row=4, column=2)
tk.Label(GENERAL_PAGE_1, text="Luck").grid(row=5, column=2)
tk.Label(GENERAL_PAGE_1, text="Movement Allowance (MA)").grid(row=6, column=2)
tk.Label(GENERAL_PAGE_1, text="Body Type").grid(row=7, column=2)
tk.Label(GENERAL_PAGE_1, text="Empathy (EMP)").grid(row=8, column=2)
tk.Label(GENERAL_PAGE_1, text="Run").grid(row=9, column=2)
tk.Label(GENERAL_PAGE_1, text="Leap").grid(row=10, column=2)
tk.Label(GENERAL_PAGE_1, text="Carry").grid(row=11, column=2)
tk.Label(GENERAL_PAGE_1, text="Lift").grid(row=12, column=2)
tk.Label(GENERAL_PAGE_1, text="Rep").grid(row=13, column=2)
tk.Label(GENERAL_PAGE_1, text="Current IP").grid(row=14, column=2)
tk.Label(GENERAL_PAGE_1, text="Humanity").grid(row=15, column=2)

# Label that goes next to the text field / entry box

INTELLIGENCE = tk.Entry(GENERAL_PAGE_1, width=5)
REFLEXES = tk.Entry(GENERAL_PAGE_1, width=5)
TECHNICAL_ABILITY = tk.Entry(GENERAL_PAGE_1, width=5)
COOL = tk.Entry(GENERAL_PAGE_1, width=5)
ATTRACTIVENESS = tk.Entry(GENERAL_PAGE_1, width=5)
LUCK = tk.Entry(GENERAL_PAGE_1, width=5)
MOVEMENT_ALLOWANCE = tk.Entry(GENERAL_PAGE_1, width=5)
BODY_TYPE = tk.Entry(GENERAL_PAGE_1, width=5)
EMPATHY = tk.Entry(GENERAL_PAGE_1, width=5)
RUN = tk.Entry(GENERAL_PAGE_1, width=5)
LEAP = tk.Entry(GENERAL_PAGE_1, width=5)
CARRY = tk.Entry(GENERAL_PAGE_1, width=5)
LIFT = tk.Entry(GENERAL_PAGE_1, width=5)
REP = tk.Entry(GENERAL_PAGE_1, width=5)
CURRENT_IP = tk.Entry(GENERAL_PAGE_1, width=5)
HUMANITY = tk.Entry(GENERAL_PAGE_1, width=5)
# Links variable to entry box and creates entry box. Width is in characters

INTELLIGENCE.grid(row=0, column=3)
REFLEXES.grid(row=1, column=3)
TECHNICAL_ABILITY.grid(row=2, column=3)
COOL.grid(row=3, column=3)
ATTRACTIVENESS.grid(row=4, column=3)
LUCK.grid(row=5, column=3)
MOVEMENT_ALLOWANCE.grid(row=6, column=3)
BODY_TYPE.grid(row=7, column=3)
EMPATHY.grid(row=8, column=3)
RUN.grid(row=9, column=3)
LEAP.grid(row=10, column=3)
CARRY.grid(row=11, column=3)
LIFT.grid(row=12, column=3)
REP.grid(row=13, column=3)
CURRENT_IP.grid(row=14, column=3)
HUMANITY.grid(row=15, column=3)
# Defines where the the entry box is

INTELLIGENCE.insert(1, "1")
REFLEXES.insert(1, "1")
TECHNICAL_ABILITY.insert(1, "1")
COOL.insert(1, "1")
ATTRACTIVENESS.insert(1, "1")
LUCK.insert(1, "1")
MOVEMENT_ALLOWANCE.insert(1, "1")
BODY_TYPE.insert(1, "1")
EMPATHY.insert(1, "1")

def calculate_misc():
    RUN.insert(1, MOVEMENT_ALLOWANCE.get()*3)

tk.Button(GENERAL_PAGE_1, text='Calculate Misc.', command=calculate_misc()).grid(row=3, column=1, pady=4)

# PAGE 2 START - GEAR

GEAR_TYPE_LABEL = tk.Label(GEAR_PAGE_2, text="Type")
GEAR_COST_LABEL = tk.Label(GEAR_PAGE_2, text="Cost")

GEAR_TYPE_LABEL.grid(row=0, column=1)
GEAR_COST_LABEL.grid(row=0, column=2)

for i in range(30):
    GEAR_TYPE = tk.Entry(GEAR_PAGE_2, width=40)
    GEAR_COST = tk.Entry(GEAR_PAGE_2, width=5)

    GEAR_TYPE.grid(row=i+1, column=1)
    GEAR_COST.grid(row=i+1, column=2)


# PAGE 3 START - CYBERNETICS

CYBERNETIC_TYPE_LABEL = tk.Label(CYBERNETICS_PAGE_3, text="Type")
CYBERNETIC_HUMANITY_LOSS_LABEL = tk.Label(CYBERNETICS_PAGE_3, text="HL")
CYBERNETIC_COST_LABEL = tk.Label(CYBERNETICS_PAGE_3, text="Cost")

CYBERNETIC_TYPE_LABEL.grid(row=0, column=1)
CYBERNETIC_HUMANITY_LOSS_LABEL.grid(row=0, column=2)
CYBERNETIC_COST_LABEL.grid(row=0, column=3)

for i in range(30):
    CYBERNETIC_TYPE = tk.Entry(CYBERNETICS_PAGE_3, width=40)
    CYBERNETIC_HUMANITY_LOSS = tk.Entry(CYBERNETICS_PAGE_3, width=2)
    CYBERNETIC_COST = tk.Entry(CYBERNETICS_PAGE_3, width=5)
    CYBERNETIC_TYPE.grid(row=i+1, column=1)
    CYBERNETIC_HUMANITY_LOSS.grid(row=i+1, column=2)
    CYBERNETIC_COST.grid(row=i+1, column=3)


# PAGE 4 START - WEAPONS

WEAPON_NAME_LABEL = tk.Label(WEAPONS_PAGE_4, text="Name")
WEAPON_TYPE_LABEL = tk.Label(WEAPONS_PAGE_4, text="Type")
WEAPON_ACCURACY_LABEL = tk.Label(WEAPONS_PAGE_4, text="WA")
WEAPON_CONCEALABILITY_LABEL = tk.Label(WEAPONS_PAGE_4, text="Con")
WEAPON_AVAILABILITY_LABEL = tk.Label(WEAPONS_PAGE_4, text="Avail")
WEAPON_DAMAGE_LABEL = tk.Label(WEAPONS_PAGE_4, text="Damage")
WEAPON_AMMO_LABEL = tk.Label(WEAPONS_PAGE_4, text="Ammo")
WEAPON_NOS_LABEL = tk.Label(WEAPONS_PAGE_4, text="NoS")
WEAPON_ROF_LABEL = tk.Label(WEAPONS_PAGE_4, text="RoF")
WEAPON_RELIABILITY_LABEL = tk.Label(WEAPONS_PAGE_4, text="Rel")

WEAPON_NAME_LABEL.grid(row=0, column=0)
WEAPON_TYPE_LABEL.grid(row=0, column=1)
WEAPON_ACCURACY_LABEL.grid(row=0, column=2)
WEAPON_CONCEALABILITY_LABEL.grid(row=0, column=3)
WEAPON_AVAILABILITY_LABEL.grid(row=0, column=4)
WEAPON_DAMAGE_LABEL.grid(row=0, column=5)
WEAPON_AMMO_LABEL.grid(row=0, column=6)
WEAPON_NOS_LABEL.grid(row=0, column=7)
WEAPON_ROF_LABEL.grid(row=0, column=8)
WEAPON_RELIABILITY_LABEL.grid(row=0, column=9)

for i in range(30):
    WEAPON_NAME = tk.Entry(WEAPONS_PAGE_4, width=30)
    WEAPON_TYPE = tk.Entry(WEAPONS_PAGE_4, width=4)
    WEAPON_ACCURACY = tk.Entry(WEAPONS_PAGE_4, width=2)
    WEAPON_CONCEALABILITY = tk.Entry(WEAPONS_PAGE_4, width=1)
    WEAPON_AVAILABILITY = tk.Entry(WEAPONS_PAGE_4, width=1)
    WEAPON_DAMAGE = tk.Entry(WEAPONS_PAGE_4, width=6)
    WEAPON_AMMO = tk.Entry(WEAPONS_PAGE_4, width=4)
    WEAPON_NOS = tk.Entry(WEAPONS_PAGE_4, width=1)
    WEAPON_ROF = tk.Entry(WEAPONS_PAGE_4, width=1)
    WEAPON_RELIABILITY = tk.Entry(WEAPONS_PAGE_4, width=2)

    WEAPON_NAME.grid(row=i+1, column=0)
    WEAPON_TYPE.grid(row=i+1, column=1)
    WEAPON_ACCURACY.grid(row=i+1, column=2)
    WEAPON_CONCEALABILITY.grid(row=i+1, column=3)
    WEAPON_AVAILABILITY.grid(row=i+1, column=4)
    WEAPON_DAMAGE.grid(row=i+1, column=5)
    WEAPON_AMMO.grid(row=i+1, column=6)
    WEAPON_NOS.grid(row=i+1, column=7)
    WEAPON_ROF.grid(row=i+1, column=8)
    WEAPON_RELIABILITY.grid(row=i+1, column=9)

# PAGE 5 START - LIFEPATH

def life_events(age):
    event_types = ["Big Problems, Big Wins", "Friends & Enemies", "Romantic Involvement"]
    age_int = int(age)
    life_event_amount = age_int - 16
    for i in range(life_event_amount):
        life_event_age = tk.Entry(LIFEPATH_PAGE_5, width=3)
        life_event_event = tk.Entry(LIFEPATH_PAGE_5, width=50)
        life_event_age.grid(row=12+i, column=0)
        life_event_event.grid(row=12+i, column=1)
        life_event = random.choice(event_types)
        if life_event == "Big Problems, Big Wins":
            big_problems_big_wins = ["Big Problems", "Big Wins"]
            big_choice = random.choice(big_problems_big_wins)
            if big_choice == "Big Problems":
                big_problems = ["Test 2", "Test 3"]
                big_problems_result = random.choice(big_problems)
                life_event_age.insert(1, "{}".format(16+i))
                life_event_event.insert(1, "{}".format(big_problems_result))
            if big_choice == "Big Wins":
                big_wins = ["Test 2", "Test 3"]
                big_wins_result = random.choice(big_wins)
                life_event_age.insert(1, "{}".format(16+i))
                life_event_event.insert(1, "{}".format(big_wins_result))
        if life_event == "Friends & Enemies":
            friends_n_enemies = ["Test 1", "Test 2"]
            friends_n_enemies_result = random.choice(friends_n_enemies)
            life_event_age.insert(1, "{}".format(16+i))
            life_event_event.insert(1, "{}".format(friends_n_enemies_result))
        if life_event == "Romantic Involvement":
            romantic_involvement = ["Test 1", "Test 2"]
            romantic_involvement_result = random.choice(romantic_involvement)
            life_event_age.insert(1, "{}".format(16+i))
            life_event_event.insert(1, "{}".format(romantic_involvement_result))

tk.Button(LIFEPATH_PAGE_5, text="Roll Life Events", command=life_events(AGE.get())).grid(row=12, column=1, pady=4)

SELECTED_CLOTHES = tk.StringVar(MASTER)
SELECTED_CLOTHES.set("Biker leathers")
SELECTED_HAIR = tk.StringVar(MASTER)
SELECTED_HAIR.set("Mohawk")
SELECTED_AFFECTATIONS = tk.StringVar(MASTER)
SELECTED_AFFECTATIONS.set("Tatoos")
SELECTED_ETHNICITY = tk.StringVar(MASTER)
SELECTED_ETHNICITY.set("English")
SELECTED_FAMILY_RANKING = tk.StringVar(MASTER)
SELECTED_FAMILY_RANKING.set("Corporate Executive")
SELECTED_PARENTS = tk.StringVar(MASTER)
SELECTED_PARENTS.set("Both parents are living")
SELECTED_TRAITS = tk.StringVar(MASTER)
SELECTED_TRAITS.set("Shy and secretive")
SELECTED_VALUED_PERSON = tk.StringVar(MASTER)
SELECTED_VALUED_PERSON.set("A parent")
SELECTED_VALUE_MOST = tk.StringVar(MASTER)
SELECTED_VALUE_MOST.set("Money")
SELECTED_FEEL_ABOUT_PEOPLE = tk.StringVar(MASTER)
SELECTED_FEEL_ABOUT_PEOPLE.set("Neutral")
SELECTED_VALUED_POSESSION = tk.StringVar(MASTER)
SELECTED_VALUED_POSESSION.set("A weapon")

CLOTHES = tk.OptionMenu(LIFEPATH_PAGE_5, SELECTED_CLOTHES, "Biker leathers", "Blue jeans", "Corporate Suits", "Jumpsuits", "Miniskits", "High Fashion", "Cammos", "Normal clothes", "Nude", "Bag Lady chic")
HAIR = tk.OptionMenu(LIFEPATH_PAGE_5, SELECTED_HAIR, "Mohawk", "Long & Ratty", "Short & Spiked", "Wild & all over", "Bald", "Striped", "Tinted", "Neat, short", "Short, curly", "Long, straight")
AFFECTATIONS = tk.OptionMenu(LIFEPATH_PAGE_5, SELECTED_AFFECTATIONS, "Tatoos", "Mirrorshades", "Ritual Scars", "Spiked gloves", "Nose Rings", "Earrings", "Longer fingernails", "Spiked heeled boots", "Weird Contact Lenses", "Fingerless Gloves")
ETHNICITY = tk.OptionMenu(LIFEPATH_PAGE_5, SELECTED_ETHNICITY, "English", "Bantu", "Fante", "Kongo", "Ashanti", "Zulu","Swahili", "Japanese", "Korean", "Bulgarian", "Russian", "Czech", "Polish", "Ukranian", "Slovak", "Micronesian", "Tagalog", "Polynesian","Malayan","Sudanese","Indonesian","Hawaiian","Burmese","Cantonese","Mandarin","Thai","Tibetan","Vietnamese","Blackfolk","Spanish","Portuguese","French","German","Italian","Greek","Danish","Dutch","Norwegian","Swedish","Finnish")
FAMILY_RANKING = tk.OptionMenu(LIFEPATH_PAGE_5, SELECTED_FAMILY_RANKING, "Corporate Executive", "Corporate Manager", "Corporate Technician", "Nomad Pack", "Pirate Fleet", "Gang Family", "Crime Lord", "Combat Zone Poor", "Urban homeless", "Arcology family")
PARENTS = tk.OptionMenu(LIFEPATH_PAGE_5, SELECTED_PARENTS, "Both parents are living", "Your parent(s) died in warfare", "Your parent(s) died in an accident", "Your parent(s) were murdered", "Your parent(s) have amnesia and don't remember you", "You never knew your parent(s)", "Your parent(s) are in hiding to protect you", "You were left with relatives for safekeeping", "You grew up on the Street and never had parents", "Your parent(s) gaveyour up for adoption", "Your parent(s) sold you for money")
TRAITS = tk.OptionMenu(LIFEPATH_PAGE_5, SELECTED_TRAITS, "Shy and secretive", "Rebellious, antisocial, violent", "Arrogant, proud and aloof", "Moody, rash and headstrong", "Picky, fussy and nervous", "Silly and fluffheaded", "Sneaky and deceptive", "Intellectual and detached", "Friendly and outgoing")
VALUED_PERSON = tk.OptionMenu(LIFEPATH_PAGE_5, SELECTED_VALUED_PERSON, "A parent")
VALUE_MOST = tk.OptionMenu(LIFEPATH_PAGE_5, SELECTED_VALUE_MOST, "Money")
FEEL_ABOUT_PEOPLE = tk.OptionMenu(LIFEPATH_PAGE_5, SELECTED_FEEL_ABOUT_PEOPLE, "Neutral")
VALUED_POSESSION = tk.OptionMenu(LIFEPATH_PAGE_5, SELECTED_VALUED_POSESSION, "A weapon")

CLOTHES.grid(row=0, column=0)
HAIR.grid(row=1, column=0)
AFFECTATIONS.grid(row=2, column=0)
ETHNICITY.grid(row=3, column=0)
FAMILY_RANKING.grid(row=4, column=0)
PARENTS.grid(row=5, column=0)
TRAITS.grid(row=6, column=0)
VALUED_PERSON.grid(row=7, column=0)
VALUE_MOST.grid(row=8, column=0)
FEEL_ABOUT_PEOPLE.grid(row=9, column=0)
VALUED_POSESSION.grid(row=10, column=0)


# PAGE 6 START - ROLL DICE
AMOUNT_D4 = tk.Entry(DICE_PAGE_6, width=5)
AMOUNT_D6 = tk.Entry(DICE_PAGE_6, width=5)
AMOUNT_D8 = tk.Entry(DICE_PAGE_6, width=5)
AMOUNT_D10 = tk.Entry(DICE_PAGE_6, width=5)
AMOUNT_D12 = tk.Entry(DICE_PAGE_6, width=5)
AMOUNT_D20 = tk.Entry(DICE_PAGE_6, width=5)
AMOUNT_DCUSTOM = tk.Entry(DICE_PAGE_6, width=5)
AMOUNT_DSIDES = tk.Entry(DICE_PAGE_6, width=5)

AMOUNT_D4.grid(row=0, column=1)
AMOUNT_D6.grid(row=1, column=1)
AMOUNT_D8.grid(row=2, column=1)
AMOUNT_D10.grid(row=3, column=1)
AMOUNT_D12.grid(row=4, column=1)
AMOUNT_D20.grid(row=5, column=1)
AMOUNT_DCUSTOM.grid(row=6, column=1)
AMOUNT_DSIDES.grid(row=6, column=2)

AMOUNT_D4.insert(1, "1")
AMOUNT_D6.insert(1, "1")
AMOUNT_D8.insert(1, "1")
AMOUNT_D10.insert(1, "1")
AMOUNT_D12.insert(1, "1")
AMOUNT_D20.insert(1, "1")
AMOUNT_DCUSTOM.insert(1, "1")
AMOUNT_DSIDES.insert(1, "1")
# Without this, the value would be nothing so roll_dice would throw an error
# about it not being able to use nothing as an interger when it first ran. This is to prevent that.

tk.Label(DICE_PAGE_6, text="Result:").grid(row=7, column=1)
label_variable = tk.StringVar()
ROLL_RESULT_LABEL = tk.Label(DICE_PAGE_6, text=label_variable)
ROLL_RESULT_LABEL.grid(row=7, column=2)

def roll_dice(amount, sides):
    """Rolls dice."""
    amount = int(amount)
    amount = int(sides)
    total_roll_result = 0
    for i in range(1, amount):
        roll_result = random.randint(1, sides)
        total_roll_result += roll_result
    label_variable.set(total_roll_result)

tk.Button(DICE_PAGE_6, text='d4', command=lambda: roll_dice(AMOUNT_D4.get(), 4)).grid(row=0, column=2, pady=4)
tk.Button(DICE_PAGE_6, text='d6', command=roll_dice(AMOUNT_D6.get(), 6)).grid(row=1, column=2, pady=4)
tk.Button(DICE_PAGE_6, text='d8', command=roll_dice(AMOUNT_D8.get(), 8)).grid(row=2, column=2, pady=4)
tk.Button(DICE_PAGE_6, text='d10', command=roll_dice(AMOUNT_D10.get(), 10)).grid(row=3, column=2, pady=4)
tk.Button(DICE_PAGE_6, text='d12', command=roll_dice(AMOUNT_D12.get(), 12)).grid(row=4, column=2, pady=4)
tk.Button(DICE_PAGE_6, text='d20', command=roll_dice(AMOUNT_D20.get(), 20)).grid(row=5, column=2, pady=4)
tk.Button(DICE_PAGE_6, text='dCustom', command=roll_dice(AMOUNT_DCUSTOM.get(), AMOUNT_DSIDES.get())).grid(row=6, column=3, pady=4)

MASTER.mainloop()
