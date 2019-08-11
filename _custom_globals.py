# Author:Brandon Lovrien
# This script includes some commands for various useful symbols used in programming
from dragonfly import (Grammar, CompoundRule, Dictation, Text, Key, AppContext, MappingRule)

# Useful commands for encapsulation of quotes, etc.
class UsefulStuff(MappingRule):
    mapping = {
        "in quotes": Text("\"\"") + Key("left"),
        "in single quotes": Text("\'\'") + Key("left"),
        "dirty bird": Text("()") + Key("left"),
        "in brackets": Text("[]") + Key("left"),
        "in braces": Text("{}") + Key("left"),
        "in angle brackets": Text("<>") + Key("left"),
        "in parameters": Text("()"),
        "arrow": Text("->"),
        "double arrow": Text("=>"),
        "fat arrow": Text("=>"),
    }


class GitCommands(MappingRule):
    mapping = {
        "commit all": Text("git add ."),
        "commit message": Text("git commit -m \"\"") + Key("left"),
        "repo push": Text("git push"),
        "repo pull": Text("git pull")
    }


globalStuff = Grammar("useful custom global commands")  # Create a grammar to contain the command rule.
globalStuff.add_rule(UsefulStuff())
globalStuff.add_rule(GitCommands())
globalStuff.load()
