from typing import Set

from pm4py.objects.dcr.semantics import DcrSemantics


class ExtendedSemantics(DcrSemantics):

    @classmethod
    def enabled(cls, graph) -> Set[str]:
        res = super().enabled(graph)
        # Milestone extension
        for e in set(graph.milestones.keys()).intersection(res):
            if len(graph.milestones[e].intersection(
                    graph.marking.included.intersection(graph.marking.pending))) > 0:
                res.discard(e)
        # Nested extension
        # Get all disabled super activities
        for e in set(graph.superActivities.keys()).difference(res):
            for e_prime in set(graph.superActivities[e]):
            # discard any subevents in those activties
                #if graph.includes[e_prime]
                res.discard(e_prime)
        return res

    @classmethod
    def weak_execute(cls, event, graph):
        if event in graph.noresponses:
            for e_prime in graph.noresponses[event]:
                graph.marking.pending.discard(e_prime)

        return super().weak_execute(event, graph)


