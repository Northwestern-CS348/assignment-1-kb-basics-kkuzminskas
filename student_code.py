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
        if not isinstance(fact, Fact):
            print("Input was not a fact")
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



        fact_list = []
        bind1 = Bindings()
        bind2 = Bindings()
        list_of_bindings = ListOfBindings()

        print("Asking {!r}".format(fact))
        # check to make sure argument is a fact
        if not isinstance(fact, Fact):
            sys.exit("Error: input was not a Fact")
        else:
            #Terms of the input
            in_predicate = fact.statement.predicate
            in_term1 = fact.statement.terms[0]
            in_term2 = fact.statement.terms[1]


            # Are the terms variables: booleans
            var_term1 = is_var(in_term1)
            var_term2 = is_var(in_term2)

            # figuring out bindings
            #for kb_fact in self.facts:
            #    if kb_fact.statement.predicate == in_predicate:
                    #print(b.add_binding(in_term1, kb_fact.statement.terms[0]))

            #print(type(Variable(in_term1).element))
            # First, see if any input terms are variables
            if var_term1 or var_term2:
                if var_term1 and var_term2:
                    print("two vars")
                    for kb_fact in self.facts:
                        if kb_fact.statement.predicate == in_predicate:
                            #bound_to_t1 = bind1.bound_to(Variable(in_term1))
                            #bound_to_t2 = bind2.bound_to(Variable(in_term2))

                            #if bound_to_t1 != kb_fact.statement.terms[0] or bound_to_t2 != kb_fact.statement.terms[1]:
                            bind = Bindings()
                            # Overall list of bindings added
                            bind1.add_binding(Variable(in_term1), Constant(kb_fact.statement.terms[0]))
                            bind2.add_binding(Variable(in_term2), Constant(kb_fact.statement.terms[1]))

                            # Binding to add to the list of bindings
                            bind.add_binding(Variable(in_term1), Constant(kb_fact.statement.terms[0]))
                            bind.add_binding(Variable(in_term2), Constant(kb_fact.statement.terms[1]))

                            list_of_bindings.add_bindings(bind, kb_fact)


                elif var_term1 and not var_term2:
                    print("First term is var")
                    for kb_fact in self.facts:
                        if kb_fact.statement.predicate == in_predicate:

                            if kb_fact.statement.terms[1] == in_term2:
                                #bound_to_t1 = bind1.bound_to(Variable(in_term1))
                                #if bound_to_t1 != kb_fact.statement.terms[0]:
                                bind = Bindings()
                                # Overall list of bindings added
                                bind1.add_binding(Variable(in_term1), Constant(kb_fact.statement.terms[0]))

                                # Binding to add to the list of bindings
                                bind.add_binding(Variable(in_term1), Constant(kb_fact.statement.terms[0]))

                                list_of_bindings.add_bindings(bind, kb_fact)
                elif not var_term1 and var_term2:
                    print("Second term is var")
                    for kb_fact in self.facts:
                        if kb_fact.statement.predicate == in_predicate:

                            if kb_fact.statement.terms[0] == in_term1:
                                #bound_to_t2 = bind1.bound_to(Variable(in_term2))
                                #if bound_to_t2 != kb_fact.statement.terms[1]:
                                bind = Bindings()
                                # Overall list of bindings added
                                bind1.add_binding(Variable(in_term2), Constant(kb_fact.statement.terms[1]))

                                # Binding to add to the list of bindings
                                bind.add_binding(Variable(in_term2), Constant(kb_fact.statement.terms[1]))

                                list_of_bindings.add_bindings(bind, kb_fact)
            else:
                # check to see if the fact is in the knowledge base
                if fact in self.facts:
                    bind = Bindings()
                    print("Fact is in the Knowledge base")
                    list_of_bindings.add_bindings(bind, fact)
                else:
                    return False


        print("Asking {!r}".format(fact))
        if not list_of_bindings:
            return False

        return list_of_bindings
