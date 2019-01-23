import read, copy
from util import *
from logical_classes import *
import sys


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """

        # check to make sure fact is a fact
        if isinstance(fact, Rule):
            print("Sorry, rules are not implented in Assignment 1. Wait for Assignment 2")
            return
        elif not isinstance(fact, Fact):
            sys.exit("Error: Input was not a fact or rule. Try inputting a fact or rule")

        else:
            if fact in self.facts:
                print("Fact already in Knowledge Base.")
            else:
                fact.asserted = True
                self.facts.append(fact)
                print("Asserting {!r}".format(fact))

    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """

        # list of bindings to be returned
        list_of_bindings = ListOfBindings()
        no_fact = False

        print("Asking {!r}".format(fact))
        # check to make sure argument is a fact
        if not isinstance(fact, Fact):
            sys.exit("Error: input to kb_ask was not a Fact. Try inputting a fact")
        else:
            #Terms of the input
            fact_statement = fact.statement

            # indicator of if there is a fact
            fact_exist = False

            for kb_fact in self.facts:
                # Result of the function match which produces False if no match is found
                # and the bindings for the match if any are found in the knowledge base
                #     Note: See util.py for description of the function
                match_result = match(fact_statement, kb_fact.statement)

                if match_result != False:
                    # add the binding to the list of bindings
                    list_of_bindings.add_bindings(match_result, kb_fact)

                    # change the indicator to show a fact exists
                    fact_exist = True



            if fact_exist:
                return list_of_bindings
            else:
                return False
