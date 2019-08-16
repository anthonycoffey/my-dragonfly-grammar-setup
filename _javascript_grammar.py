# Author:Brandon Lovrien
# This script includes commands that are to be used for JavaScript programming

from dragonfly import *


def doSomethingToCommand(command):
    newCommand = Sequence(command)
    newCommand.execute()


class JavaScriptEnabler(CompoundRule):
    spec = "Enable JavaScript"  # Spoken form of command.

    def _process_recognition(self, node, extras):  # Callback when command is spoken.
        JavaScriptBootstrap.disable()
        JavaScriptGrammar.enable()
        print("JavaScript grammar enabled")


class JavaScriptDisabler(CompoundRule):
    spec = "switch language"  # Spoken form of command.

    def _process_recognition(self, node, extras):  # Callback when command is spoken.
        JavaScriptGrammar.disable()
        JavaScriptBootstrap.enable()
        print("JavaScript grammar disabled")


class JavaScriptTestRule(CompoundRule):
    spec = "test JavaScript"  # Spoken form of command.

    def _process_recognition(self, node, extras):  # Callback when command is spoken.
        print("JavaScript grammar tested")


class JavaScriptControlStructures(MappingRule):
    mapping = {
        "variable": Text("var "),
        "function": Text("function functionName() {") + Key("enter"),
        "code block": Text("{") + Key("enter") + Key("enter"),
        "if": Text("if() {") + Key("enter") + Key("enter"),
        "if else": Text("if() {") + Key("enter") + Key("enter") + Text("}") + Key("enter") + Text("else {") + Key(
            "enter"),
        "else if": Text("else if() {") + Key("enter"),
        "while loop": Text("while() {") + Key("enter"),
        "do while loop": Text("do {") + Key("enter") + Key("down") + Text("while()"),
        "for loop": Text("for(let i = 0; i < arr.length; i++) {") + Key("enter"),
        "switch statement": Text("switch() {") + Key("enter"),

    }


class JavaScriptES6Syntax(MappingRule):
    mapping = {
        "constant": Text("const "),
        "let": Text("let "),
        "import statement": Text("import {} from \"\";") + Key("left") + Key("left"),
        "export statement": Text("export default {}"),
        "template literal": Text("``") + Key("left"),
        "string interpolation": Text("${}") + Key("left")
    }


class JavaScriptCommentsSyntax(MappingRule):
    mapping = {
        "comment": Text("// "),
        "multiline comment": Text("/**") + Key("enter")  # + Key("enter") + Text("*/") + Key("up")
    }


class JavaScriptMiscellaneousStuff(MappingRule):
    mapping = {
        "equals": Text(" = "),
        "new": Text("new "),
        "return statement": Text("return "),
        "log statement": Text("console.log({});") + Key("left") + Key("left") + Key("left"),
        "bang": Text("!"),

    }


class JavaScriptVueCommands(MappingRule):
    mapping = {
        "view tag": Text("<v-"),
        "view equals": Text("=\"\""),
        "view flex": Text("<v-flex "),
        "view layout": Text("<v-layout "),
        "view card": Text("<v-card "),
        "close tag": Text("</"),
        "print variable": Text("{{}}") + Key("left") + Key("left")
    }


class JavaScriptComparisonOperators(MappingRule):
    mapping = {
        "equal to": Text("=="),
        "exactly equal to": Text("==="),
        "not equal to": Text("!="),
        "greater than": Text(">"),
        "less than": Text("<"),
        "greater than or equal to": Text(">="),
        "less than or equal to": Text("<="),

    }


class JavaScriptArithmeticOperators(MappingRule):
    mapping = {
        "plus": Text(" + "),
        "plus plus": Text("++"),
        "minus minus": Text("--"),
        "multiply by": Text(" * "),
        "divide by": Text(" / "),
        "modulus": Text(" % ")

    }


class JavaScriptAssignmentOperators(MappingRule):
    mapping = {
        "plus equals": Text("+="),
        "minus equals": Text("-="),
        "multiply equals": Text("*="),
        "divide equals": Text("/="),
        "modulus equals": Text("%="),

    }


JavaScriptBootstrap = Grammar("JavaScript bootstrap")  # Create a grammar to contain the command rule.
JavaScriptBootstrap.add_rule(JavaScriptEnabler())
JavaScriptBootstrap.load()

JavaScriptGrammar = Grammar("JavaScript grammar")
JavaScriptGrammar.add_rule(JavaScriptTestRule())
JavaScriptGrammar.add_rule(JavaScriptControlStructures())
JavaScriptGrammar.add_rule(JavaScriptCommentsSyntax())
JavaScriptGrammar.add_rule(JavaScriptMiscellaneousStuff())
JavaScriptGrammar.add_rule(JavaScriptComparisonOperators())
JavaScriptGrammar.add_rule(JavaScriptArithmeticOperators())
JavaScriptGrammar.add_rule(JavaScriptAssignmentOperators())
JavaScriptGrammar.add_rule(JavaScriptDisabler())
JavaScriptGrammar.add_rule(JavaScriptES6Syntax())
JavaScriptGrammar.add_rule(JavaScriptVueCommands())
JavaScriptGrammar.load()
JavaScriptGrammar.disable()


# Unload function which will be called by natlink at unload time.
def unload():
    global JavaScriptGrammar
    if JavaScriptGrammar: JavaScriptGrammar.unload()
    JavaScriptGrammar = None
