import os
print(os.getcwd())
to_run = True
if to_run:
    os.chdir('..')
    to_run = False
print(os.getcwd())

# Rule 1
from pm4py.objects.dcr.extended.semantics import ExtendedSemantics
from pm4py.objects.dcr.extended.obj import ExtendedDcrGraph
from pm4py.objects.dcr.obj import DcrGraph

testGraph = ExtendedDcrGraph()

events = [
    "A", "B", "C", "D","E","F"
]

testGraph.superActivities = {"A": {"B","E"}}
# Condition from C to A
testGraph.responses = {"A" : {"C"}, "D" : {"A","F"}}

for event in events:
    testGraph.events.add(event)
    testGraph.labels.add(event)
    testGraph.label_map[event] = event

for event in testGraph.events:
        testGraph.marking.included.add(event)
    
print(testGraph)