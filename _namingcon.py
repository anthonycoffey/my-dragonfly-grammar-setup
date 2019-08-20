"""
Author:Brandon Lovrien

Command module for programming variable naming conventions
==========================================================


"""

from dragonfly import *


# helper function handling "camelBack"
def camel_back(command):
    someString = str(command)
    lowerString = someString.lower()
    words = lowerString.split()
    finalString = ""
    isFirst = 1
    for word in words:
        if isFirst == 1:
            finalString = finalString + word
            isFirst = 0
        else:
            finalString = finalString + word.title()
    printer = Text(finalString)
    printer.execute()


# Voice command rule for "Camel" naming convention.
def camel_format(command):  # Callback when command is spoken.
    textToPrint = command
    someString = str(textToPrint)
    upperString = someString.title()
    printer = Text(upperString.replace(' ', ''))
    printer.execute()


# Voice command rule for "middle_underscores" naming convention.
def middle_underscores(command):  # Callback when command is spoken.
    textToPrint = command
    someString = str(textToPrint)
    printer = Text(someString.replace(' ', '_'))
    printer.execute()


# Voice command rule for "_BEGINNING_UNDERSCORES" naming convention.
def _BEGINNING_UNDERSCORES(command):  # Callback when command is spoken.
    textToPrint = command
    someString = str(textToPrint)
    upperString = "_" + someString.upper()
    printer = Text(upperString.replace(' ', '_'))
    printer.execute()


# Voice command rule for "middle-slash" naming convention.
def middle_slash_format(command):  # Callback when command is spoken.
    textToPrint = command
    someString = str(textToPrint)
    printer = Text(someString.replace(' ', '-'))
    printer.execute()


# Voice command rule for "spacefree" naming convention.
def SpaceFreeFormat(command):  # Callback when command is spoken.
    textToPrint = command
    someString = str(textToPrint)
    printer = Text(someString.replace(' ', ''))
    printer.execute()


class ProgrammingNamingConventions(MappingRule):
    mapping = {

        # this command capitalizes the 2nd word and on, and removes spaces    example: testValue
        "camel <command>": Function(camel_back),
        "camel <command> <symbol>": Function(camel_back) + Text("%(symbol)s"),
        "<symbol> camel <command>": Text("%(symbol)s") + Function(camel_back),

        # this command capitalizes the 1st letter of each word and removes spaces   example: TestValue
        "pascal <command>": Function(camel_format),
        "pascal <command> <symbol>": Function(camel_format) + Text("%(symbol)s"),
        "<symbol> pascal <command>": Text("%(symbol)s") + Function(camel_format),

        # this command replaces spaces between words with underscores  example:test_value
        "snake case <command>": Function(middle_underscores),
        "snake case <command> <symbol>": Function(middle_underscores) + Text("%(symbol)s"),
        "<symbol> snake case <command>": Text("%(symbol)s") + Function(middle_underscores),

        # example of this command: _TEST_VALUE
        "beginning under <command>": Function(_BEGINNING_UNDERSCORES),
        "beginning under <command> <symbol>": Function(_BEGINNING_UNDERSCORES) + Text("%(symbol)s"),
        "<symbol> beginning under <command>": Text("%(symbol)s") + Function(_BEGINNING_UNDERSCORES),

        # example of this command: test-value
        "kebab case <command>": Function(middle_slash_format),
        "kebab case <command> <symbol>": Function(middle_slash_format) + Text("%(symbol)s"),
        "<symbol> kebab case <command>": Text("%(symbol)s") + Function(middle_slash_format),

        # example of this command: testvalue
        "space free <command>": Function(SpaceFreeFormat),
        "space free <command> <symbol>": Function(SpaceFreeFormat) + Text("%(symbol)s"),
        "<symbol> space free <command>": Text("%(symbol)s") + Function(SpaceFreeFormat),
    }

    extras = [
        Dictation("command"),
        Choice("symbol", {
            "dot": ".",
            "arrow": "->",
            "fat arrow": "=>",
            "parameters": "()",
            "parameters dot": "()."
        }
               )
    ]

# Create a grammar which contains and loads the command rule.


naminggrammar = Grammar("naming conventions")  # Create a grammar to contain the command rule.
naminggrammar.add_rule(ProgrammingNamingConventions())
naminggrammar.load()
