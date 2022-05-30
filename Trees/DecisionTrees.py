__author__ = 'Luis Moniz'
""" An object oriented implementation of a decision tree
"""


class Node(object):
    """ Abstract Tree Root implementation
    """

    def __init__(self):
        self._information = {}

    def decide(self, _):
        self._child.decide(self._information)

    def value(self):
        return self._information[self._attribute]


class Decision(Node):
    """ Abstract interior node implementation
    """

    def __init__(self, attr):
        super(Decision, self).__init__()
        self._attribute = attr

    def decide(self, _):
        pass

    def getBranch(self):
        pass


class Action(Node):
    """ Abstract leaf node implementation
    """

    def __init__(self):
        super(Node, self).__init__()

    def decide(self, _):
        # self.run()
        return self

    def run(self):
        pass


class Boolean(Decision):
    """ Abstract boolean decision node implementation
    """

    def __init__(self, attr):
        super(Boolean, self).__init__(attr)

    def addYesNode(self, other):
        self._yesNode = other

    def addNoNode(self, other):
        self._noNode = other

    def value(self):
        return self._information[self._attribute]

    def decide(self, info):
        self._information = info
        return self.getBranch().decide(self._information)

    def getBranch(self):
        if self.value():
            return self._yesNode
        else:
            return self._noNode


class MinMax(Boolean):
    """ Abstract range decision node implementation,extending Boolean node
    """

    def __init__(self, attr, min, max):
        super(MinMax, self).__init__(attr)
        self.minValue = min
        self.maxValue = max

    def value(self):
        return self.maxValue >= super(Boolean, self).value() >= self.minValue

# class PrintAction(Action):
#     def __init__(self,msg):
#         super(PrintAction,self).__init__()
#         self.message = msg
#     def decide(self,_):
#         print self.message+"\n"
#
#
#
#
# attack = PrintAction("Attack")
# creep = PrintAction("Creep")
# move = PrintAction("Move")
# patrol = PrintAction("Patrol")
#
# visible = Boolean("visible?")
# audible = Boolean("audible?")
# close = MinMax("distance",20,40)
# flank = Boolean("flank?")
#
# visible.addNoNode(audible)
# visible.addYesNode(close)
# audible.addNoNode(patrol)
# audible.addYesNode(creep)
# close.addNoNode(flank)
# close.addYesNode(attack)
# flank.addNoNode(attack)
# flank.addYesNode(move)
#
# root=visible
#
# root.decide({"visible?":False,"audible?":False,"flank?":True,"distance":30})
