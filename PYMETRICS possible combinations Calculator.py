left_list = ["Processing-Planner", "Em-Context Oriented", "Memory-Regular", "Learning-Consistent", "Planning-Planner", "Trust-NonTrusting", "Effort-Outcome Driven", "Altruism-Frugal", "Attension-Overattentive", "Risk-Cautious", "Fairness-Critical", "COGflexibility-Multitasking"]

right_list = ["Processing-Impulsive", "Em-Expression Oriented", "Memory-Great", "Learning-Adaptive", "Planning-Impulsive", "Trust-Trusting", "Effort-Hardworking", "Altruism-Generous", "Attension-Multitasking", "Risk-Adventurous", "Fairness-Accepting", "COGflexibility-Focused"]

possible_match = [(x,y) for x in left_list for y in right_list]
print(possible_match)