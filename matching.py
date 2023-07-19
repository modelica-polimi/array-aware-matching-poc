#!/usr/bin/env python3

from graph import *


def matching(graph: MatchingGraph):
  paths = augmentingPaths(graph)
  while len(paths) > 0:
    print("augmenting paths:", paths)
    for path in paths:
      applyPath(graph, path)
    paths = augmentingPaths(graph)


def applyPath(graph, path):
  for (node_from, edge_through, delta) in path:
    if not node_from.isVariable:
      edge_through.applyMatch(delta)
    else:
      edge_through.cancelMatch(delta)


class BFSStep:
  def __init__(self, prevStep, takenEdge, node, mapSet, curSet=None):
    self.prevStep = prevStep
    self.takenEdge = takenEdge
    self.node = node
    if mapSet is not None:
      self.mapSet = BiIndexSet(init=mapSet)
    else:
      self.mapSet = None
    if curSet is None:
      self.curSet = self.mapSet.sideOf(node)
    else:
      self.curSet = curSet

  def __repr__(self):
    return '[Step:' + str(id(self)) + \
           ' prev:' + str(id(self.prevStep)) + \
           ' edge:' + repr(self.takenEdge) + \
           ' to:' + repr(self.node) + \
           ' set:' + repr(self.mapSet) + ']'


def augmentingPaths(graph: MatchingGraph):
  # computation of the initial frontier
  startingPoints = []
  for eq in graph.equations:
    outgoingSet = graph.freeIndices(eq)
    if len(outgoingSet) > 0:
      startingPoints += [BFSStep(None, None, eq, None, outgoingSet)]

  # breadth-first search
  # can be replaced with a depth-first-search as long as we check for loops in the residual graph (!)
  frontier = startingPoints
  nextFrontier = []
  foundPaths = []
  while len(foundPaths) == 0 and len(frontier) != 0:
    for step in frontier:
      for edge in graph.adjacentEdges(step.node):
        if not step.node.isVariable:
          options = edge.freeIndices().mapEqToVar(step.curSet)
          for mappedNextSet in options:
            nextNode = edge.opposite(step.node)
            free = graph.freeIndices(nextNode)
            thisStepsMatches = mappedNextSet.intersectionVar(free)
            if len(thisStepsMatches) > 0:
              foundPaths += [BFSStep(step, edge, nextNode, thisStepsMatches)]
            else:
              nextFrontier += [BFSStep(step, edge, nextNode, mappedNextSet)]
        else:
          options = edge.matchedIndices.mapVarToEq(step.curSet)
          for mappedNextSet in options:
            nextNode = edge.opposite(step.node)
            nextFrontier += [BFSStep(step, edge, nextNode, mappedNextSet)]
    frontier = nextFrontier
    nextFrontier = []

  if len(foundPaths) == 0:
    return []
  def pathHeuristic(step):
    return len(step.curSet)
  foundPaths.sort(key=pathHeuristic, reverse=True)

  # restrict the flow based on the path
  # remove multiple overlapping paths (the earlier ones in the list will win)
  paths = []
  touchedNodeIndices = {}
  for pathEnd in foundPaths:
    myTouchedNodeIndices = {}
    curStep = pathEnd
    path = []
    while curStep:
      if curStep.prevStep:
        if len(path) == 0:
          node, edge, map = (curStep.prevStep.node, curStep.takenEdge, curStep.mapSet)
        else:
          _, _, prevMap = path[0]
          map = curStep.mapSet.monoIntersection(prevMap.sideOf(curStep.node))
          node, edge, map = (curStep.prevStep.node, curStep.takenEdge, map)
        path = [(node, edge, map)] + path

      touchedIndices = map.sideOf(curStep.node)
      if curStep.node not in touchedNodeIndices:
        alreadyTouchedIndices = MonoIndexSet(curStep.node.isVariable)
      else:
        alreadyTouchedIndices = touchedNodeIndices[curStep.node]
      if not touchedIndices.isdisjoint(alreadyTouchedIndices):
        path = None
        break
      if curStep.node in myTouchedNodeIndices:
        myTouchedNodeIndices[curStep.node] |= touchedIndices
      else:
        myTouchedNodeIndices[curStep.node] = alreadyTouchedIndices | touchedIndices

      curStep = curStep.prevStep

    if path is not None:
      paths += [path]
      touchedNodeIndices.update(myTouchedNodeIndices)

  return paths
