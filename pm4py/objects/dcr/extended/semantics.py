from typing import Set

from pm4py.objects.dcr.semantics import DcrSemantics
from pm4py.objects.dcr.obj import DcrGraph


class ExtendedSemantics(DcrSemantics):

    @classmethod
    def enabled(cls, graph) -> Set[str]:
        res = super().enabled(graph)

        for event in set(graph.superActivities.keys()).intersection(graph.marking.pending):
            for e_prime in graph.superActivities[event]:
                graph.marking.pending.add(e_prime)
            graph.marking.pending.remove(event)
            
        # Milestone extension
        for event in set(graph.milestones.keys()).intersection(res):
            if len(graph.milestones[event].intersection(
                    graph.marking.included.intersection(graph.marking.pending))) > 0:
                res.discard(event)
        
        # Nested extension
        # Get all disabled super activities
        '''
        for e in set(graph.superActivities.keys()).difference(res):
            for e_prime in set(graph.superActivities[e]):
            # discard any subevents in those activties
                #if graph.includes[e_prime]
                res.discard(e_prime)
        '''
        # Discard each superActivity from the res
        for super_activity in graph.superActivities.keys():
            res.discard(super_activity)
        graph.marking.included.update(res)
        return res

    @classmethod
    def weak_execute(cls, event, graph):
        if event in graph.noresponses:
            for e_prime in graph.noresponses[event]:
                graph.marking.pending.discard(e_prime)

        return super().weak_execute(event, graph)
    '''
    @classmethod
    def execute(cls, graph:DcrGraph, event):
        super().execute(graph)
'''



