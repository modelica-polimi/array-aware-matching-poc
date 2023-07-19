#!/usr/bin/env python3

from graph import *


def applyForcedMatches(graph: MatchingGraph, nodes: [MGNode]):
  forcedMatches = []
  for node in nodes:
    forcedMatches += checkPotentialForcedMatch(graph, node)
  print("Forced matches:", forcedMatches)

  feedback = set()
  for node, edge in forcedMatches:
    feedback |= applyForcedMatch(graph, edge, node)

  return feedback


def checkPotentialForcedMatch(graph: MatchingGraph, node: MGNode):
  adjEdges = graph.adjacentEdges(node)
  if len(adjEdges) == 0:
    raise Exception("Error: Invalid model, node " + str(node) + " has no edges")
  edges = [] # len(edges) == unmatchedDegree
  for edge in adjEdges:
    freeEqIndices = graph.freeIndices(edge.equation)
    freeVarIndices = graph.freeIndices(edge.variable)
    freeEdgeIndices = edge.freeIndices().intersectionEq(freeEqIndices).intersectionVar(freeVarIndices)
    if len(freeEdgeIndices) > 0:
      edges += [edge]
  if len(edges) == 1:
    return [(node, edges[0])]
  return []


def applyForcedMatch(graph: MatchingGraph, edge: MGEdge, node: MGNode):
  freeEqIndices = graph.freeIndices(edge.equation)
  freeVarIndices = graph.freeIndices(edge.variable)
  freeEdgeIndices = edge.freeIndices().intersectionEq(freeEqIndices).intersectionVar(freeVarIndices)
  if len(freeEdgeIndices) == 0 and (len(freeVarIndices) > 0 or len(freeEqIndices) > 0):
    raise Exception("Error: Invalid model, single viable edge on " + str(node) + " does not cover all scalar items")
  mappedIndices = freeEdgeIndices.map(graph.freeIndices(node))
  if len(mappedIndices) == 1:
    edge.applyMatch(mappedIndices[0])
    return set(graph.adjacentNodes(edge.opposite(node))) - {node} | {edge.opposite(node)}
  return set()


def simplify(graph: MatchingGraph):
  feedback = graph.equations + graph.variables
  while len(feedback) > 0:
    feedback = applyForcedMatches(graph, feedback)

