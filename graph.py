#!/usr/bin/env python3

'''Functions and classes implementing a matching graph.
Note: does not implement the MCIM data structure. Matrices and vectors
are represented as set of indices (sparse matrices and vectors).'''


class MonoIndexSet(set):
  def __init__(self, isVariable, vafs=None, rng=None, init=None):
    if vafs is None:
      vafs = []
    if init is None:
      init = []
    if len(vafs) == 0:
      super().__init__(init)
    else:
      super().__init__(set(init).union(set([vaf(i) for vaf in vafs for i in rng])))
    self.isVariable = isVariable


class BiIndexSet(set):
  def __init__(self, vafs=None, rng=None, init=None):
    if vafs is None:
      vafs = []
    if init is None:
      init = []
    super().__init__(set(init).union(set([(i, vaf(i)) for vaf in vafs for i in rng])))

  def equationSet(self):
    return MonoIndexSet(False, init=[a for (a, b) in self])

  def variableSet(self):
    return MonoIndexSet(True, init=[b for (a, b) in self])

  def sideOf(self, node):
    return self.variableSet() if node.isVariable else self.equationSet()

  def monoIntersection(self, idx: MonoIndexSet):
    return self.intersectionVar(idx) if idx.isVariable else self.intersectionEq(idx)

  def intersectionEq(self, eq: set):
    return BiIndexSet(init=[(a, b) for (a, b) in self if a in eq])

  def intersectionVar(self, var: set):
    return BiIndexSet(init=[(a, b) for (a, b) in self if b in var])

  def map(self, idx: MonoIndexSet):
    # solveLocalMatchingProblem
    return self.mapVarToEq(idx) if idx.isVariable else self.mapEqToVar(idx)

  def mapEqToVar(self, eq: set):
    eq_uniq = set(eq)
    var = [(a, b) for (a, b) in self if a in eq_uniq]
    return [BiIndexSet(init=l) for l in unmerge(var)]

  def mapVarToEq(self, var: set):
    var_uniq = set(var)
    eq = [(a, b) for (a, b) in self if b in var_uniq]
    return [BiIndexSet(init=l) for l in unmerge(eq)]


def unmerge(l):
  lol = scatter(l, lambda t: t[0])
  res = []
  for i in lol:
    j = scatter(i, lambda t: t[1])
    res += j
  return res


def scatter(l, key):
  l = sorted(l)
  if len(l) == 0:
    return []
  previ = l[0]
  res = [[previ]]
  j = 0
  for curi in l[1:]:
    if key(previ) == key(curi):
      j += 1
    else:
      j = 0
    if j < len(res):
      res[j] += [curi]
    else:
      res += [[curi]]
    previ = curi
  return res


class MGNode:
  def __init__(self, isVar, rng, name=None):
    self.name = name
    self.isVariable = isVar
    self.indices = MonoIndexSet(isVar, [lambda i: i], rng)
    self.matchedIndices = None

  def __repr__(self):
    return '(' + self.name + ')'


class MGEdge:
  def __init__(self, eq: MGNode, var: MGNode, vafs):
    self.indices = BiIndexSet(vafs, eq.indices)
    self.matchedIndices = BiIndexSet([], None)
    self.equation = eq
    self.variable = var

  def __repr__(self):
    return '(' + self.equation.name + '--' + self.variable.name + ')'

  def freeIndices(self):
    return BiIndexSet(init=(self.indices - self.matchedIndices))

  def isUnmatched(self):
    return len(self.matchedIndices) == 0

  def opposite(self, node):
    assert node == self.equation or node == self.variable
    return self.equation if node == self.variable else self.variable

  def applyMatch(self, indexSet: BiIndexSet):
    assert len(self.matchedIndices.intersection(indexSet)) == 0
    self.matchedIndices |= indexSet

  def cancelMatch(self, indexSet: BiIndexSet):
    assert len(self.matchedIndices.intersection(indexSet)) == len(indexSet)
    self.matchedIndices -= indexSet


class MatchingGraph:
  def __init__(self, eqs: [MGNode], vars: [MGNode], edges: [MGEdge]):
    self.equations = list(eqs)
    self.variables = list(vars)
    self.edges = list(edges)

  def nodes(self):
    return self.equations + self.variables

  def adjacentEdges(self, node: MGNode) -> [MGEdge]:
    return [edge for edge in self.edges if edge.variable == node or edge.equation == node]

  def adjacentNodes(self, node: MGNode) -> [MGNode]:
    return [edge.opposite(node) for edge in self.adjacentEdges(node)]

  def matchedIndices(self, node: MGNode) -> MonoIndexSet:
    res = BiIndexSet()
    for e in self.adjacentEdges(node):
      res |= e.matchedIndices
    return res.equationSet() if not node.isVariable else res.variableSet()

  def freeIndices(self, node: MGNode) -> MonoIndexSet:
    res = BiIndexSet()
    for e in self.adjacentEdges(node):
      res |= e.matchedIndices
    return MonoIndexSet(node.isVariable, init=node.indices - (res.equationSet() if not node.isVariable else res.variableSet()))

  def outgoingPaths(self, node: MGNode, rng: MonoIndexSet) -> [(MonoIndexSet, MGEdge)]:
    edges = self.adjacentEdges(node)
    res = []
    for edge in edges:
      validIndices = edge.freeIndices().sideOf(node) if not node.isVariable else edge.matchedIndices.sideOf(node)
      validIndices = validIndices.intersection(rng)
      if len(validIndices) > 0:
        res += [(validIndices, edge)]
    return res

  def matchingValid(self):
    for e1 in self.edges:
      m = e1.matchedIndices
      for e2 in self.adjacentEdges(e1.equation):
        if e1 != e2:
          assert len(m.intersectionEq(e2.matchedIndices)) == 0
      for e2 in self.adjacentEdges(e1.variable):
        if e1 != e2:
          assert len(m.intersectionVar(e2.matchedIndices)) == 0
    return sum([len(self.freeIndices(e)) for e in self.equations]) + sum([len(self.freeIndices(v)) for v in self.variables]) == 0

  def dump(self):
    print("MatchingGraph:")
    print("  Equations:", self.equations)
    print("  Variables:", self.variables)
    print("  Edges:    ", self.edges)
    print("  Matching:")
    for edge in self.edges:
      print("    Edge", edge, "indices", edge.indices, "matched", edge.matchedIndices)
