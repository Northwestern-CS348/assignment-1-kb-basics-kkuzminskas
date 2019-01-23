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
            print("Input was not a fact or rule ")
            return
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

        print("Asking {!r}".format(fact))
        # check to make sure argument is a fact
        if not isinstance(fact, Fact):
            sys.exit("Error: input was not a Fact")
        else:
            #Terms of the input
            in_predicate = fact.statement.predicate
            list_terms = fact.statement.terms


            for kb_fact in self.facts:
                # binding to be added
                bind = Bindings()

                # index of terms list
                index = 0

                # indicate if the binding is for the wrong fact
                not_bind = True

                # go through each term for the given ask
                for term in list_terms:

                    # if the KB does have a matching predicate, then look for bindings
                    if kb_fact.statement.predicate == in_predicate:

                        # if it is a variable, add a binding
                        if is_var(term):
                            bind.add_binding(term.term, kb_fact.statement.terms[index].term)

                        else:
                            # If a non variable term from the asked fact
                            #doesn't match with the KB term, then do not add the current binding
                            if term != kb_fact.statement.terms[index]:
                                not_bind = False
                                break
                    # if the KB fact doesn't have a matching predicate
                    else:
                        not_bind = False

                    # increasing the index of the knowledge base term being viewed
                    index = index + 1

                if not_bind:
                    list_of_bindings.add_bindings(bind, kb_fact)



        # If there was not a list, then the fact is not in the KB, return false
        if not list_of_bindings:
            return False

        return list_of_bindings
