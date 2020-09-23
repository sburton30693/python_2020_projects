# Spencer Burton
# Text is from Star Wars Episode IV Opening Crawl

text = """Rebel {0}'s, {1}ing from a {2} base, have won
their first victory against the {3} Galactic {4}. During
the battle, Rebel {5}s managed to steal secret plans to the {4}’s
ultimate weapon, the {6}, an armored space station with enough
power to {7} an entire planet. Pursued by the {4}’s sinister agents,
{8} races home aboard their {9}, custodian of the stolen
plans that can save their people and restore {10} to the galaxy."""

# Get words from user
noun_1      = input("Enter a noun (occupation): ")
verb_1      = input("Enter a verb: ")
adjective_1 = input("Enter an adjective: ")
adjective_2 = input("Enter an adjective: ")
noun_2      = input("Enter a proper noun: ")
noun_3      = input("Enter a noun (occupation): ")
noun_4      = input("Enter a noun: ")
verb_2      = input("Enter a verb: ")
name_1      = input("Enter a name: ")
noun_5      = input("Enter a noun (vehicle): ")
noun_6      = input("Enter a noun (objects or idea): ")

# Insert words into the text with formatting
replaced_text = str.format(text, noun_1, verb_1, adjective_1, adjective_2, noun_2, \
                           noun_3, noun_4, verb_2, name_1, noun_5, noun_6)
	
print("\n" + replaced_text)
