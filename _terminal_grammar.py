# Author: Anthony Coffey
# This script includes some commands for various useful symbols used in programming
from dragonfly import (Grammar, CompoundRule, Dictation, Text, Key, AppContext, MappingRule)


# Useful commands for encapsulation of quotes, etc.
class TerminalCommands(MappingRule):
    mapping = {
        "node install": Text("npm install "),
        "start dev server": Text("npm run serve"),
        "restart server": Text("npm run restart"),
        "run production": Text("npm run prod"),
        "build production": Text("vue-cli-service build -modern --report")
    }


globalStuff = Grammar("useful custom terminal commands")  # Create a grammar to contain the command rule.
globalStuff.add_rule(TerminalCommands())
globalStuff.load()
