#!/usr/bin/env python3

'''Entry point'''

from graph import *
from matching import matching
from simplify import simplify


def testcase1():
  var_x = MGNode(True, range(0, 3), "x")
  eq_1 = MGNode(False, range(0, 2), "e1")
  eq_2 = MGNode(False, range(0, 1), "e2")
  edge_1_x = MGEdge(eq_1, var_x, [lambda i: i, lambda i: i + 1])
  edge_2_x = MGEdge(eq_2, var_x, [lambda i: 2])
  return MatchingGraph([eq_1, eq_2], [var_x], [edge_1_x, edge_2_x])


def testcase2():
  var_x = MGNode(True, range(0, 4), "x")
  eq_1 = MGNode(False, range(0, 2), "e1")
  eq_2 = MGNode(False, range(2, 4), "e2")
  edge_1_x = MGEdge(eq_1, var_x, [lambda i: i])
  edge_2_x = MGEdge(eq_2, var_x, [lambda i: i])
  return MatchingGraph([eq_1, eq_2], [var_x], [edge_1_x, edge_2_x])


def testcase3():
  var_l = MGNode(True, range(0, 1), "l")
  var_h = MGNode(True, range(0, 1), "h")
  var_fl = MGNode(True, range(0, 1), "fl")
  var_fh = MGNode(True, range(0, 1), "fh")
  var_x = MGNode(True, range(0, 5), "x")
  var_y = MGNode(True, range(0, 5), "y")
  var_f = MGNode(True, range(0, 5), "f")

  eq_1 = MGNode(False, range(0, 1), "e1")
  eq_2 = MGNode(False, range(0, 1), "e2")
  eq_3 = MGNode(False, range(0, 1), "e3")
  eq_4 = MGNode(False, range(0, 1), "e4")
  eq_5 = MGNode(False, range(0, 5), "e5")
  eq_6 = MGNode(False, range(0, 5), "e6")
  eq_7 = MGNode(False, range(0, 5), "e7")

  edge_1_l = MGEdge(eq_1, var_l, [lambda i: 0])
  edge_1_fl = MGEdge(eq_1, var_fl, [lambda i: 0])
  edge_2_fl = MGEdge(eq_2, var_fl, [lambda i: 0])
  edge_3_h = MGEdge(eq_3, var_h, [lambda i: 0])
  edge_3_fh = MGEdge(eq_3, var_fh, [lambda i: 0])
  edge_4_fh = MGEdge(eq_4, var_fh, [lambda i: 0])
  edge_5_fl = MGEdge(eq_5, var_fl, [lambda i: 0])
  edge_5_f = MGEdge(eq_5, var_f, [lambda i: i])
  edge_5_x = MGEdge(eq_5, var_x, [lambda i: i])
  edge_6_fh = MGEdge(eq_6, var_fh, [lambda i: 0])
  edge_6_f = MGEdge(eq_6, var_f, [lambda i: i])
  edge_6_y = MGEdge(eq_6, var_y, [lambda i: i])
  edge_7_f = MGEdge(eq_7, var_f, [lambda i: i])
  return MatchingGraph([eq_1, eq_2, eq_3, eq_4, eq_5, eq_6, eq_7],
                       [var_l, var_h, var_fl, var_fh, var_x, var_y, var_f],
                       [edge_1_l, edge_1_fl, edge_2_fl, edge_3_h, edge_3_fh, edge_4_fh, edge_5_fl, edge_5_f, edge_5_x,
                 edge_6_fh, edge_6_f, edge_6_y, edge_7_f])


def testcase4():
  var_l = MGNode(True, range(0, 1), "l")
  var_h = MGNode(True, range(0, 1), "h")
  var_x = MGNode(True, range(0, 5), "x")
  var_f = MGNode(True, range(0, 6), "f")

  eq_1 = MGNode(False, range(0, 1), "e1")
  eq_2 = MGNode(False, range(0, 1), "e2")
  eq_3 = MGNode(False, range(0, 5), "e3")
  eq_4 = MGNode(False, range(1, 5), "e4")
  eq_5 = MGNode(False, range(0, 1), "e5")
  eq_6 = MGNode(False, range(0, 1), "e6")

  edge_1_l = MGEdge(eq_1, var_l, [lambda i: 0])
  edge_1_f = MGEdge(eq_1, var_f, [lambda i: 0])
  edge_2_f = MGEdge(eq_2, var_f, [lambda i: 0])
  edge_3_x = MGEdge(eq_3, var_x, [lambda i: i])
  edge_3_f1 = MGEdge(eq_3, var_f, [lambda i: i])
  edge_3_f2 = MGEdge(eq_3, var_f, [lambda i: i + 1])
  edge_4_f = MGEdge(eq_4, var_f, [lambda i: i])
  edge_5_h = MGEdge(eq_5, var_h, [lambda i: 0])
  edge_5_f = MGEdge(eq_5, var_f, [lambda i: 5])
  edge_6_f = MGEdge(eq_6, var_f, [lambda i: 5])
  return MatchingGraph([eq_1, eq_2, eq_3, eq_4, eq_5, eq_6],
                       [var_l, var_h, var_x, var_f],
                       [edge_1_l, edge_1_f, edge_2_f, edge_3_x, edge_3_f1, edge_3_f2, edge_4_f, edge_5_h, edge_5_f, edge_6_f])


def testcase5():
  var_x = MGNode(True, range(0, 5), "x")
  var_y = MGNode(True, range(0, 4), "y")
  var_z = MGNode(True, range(0, 5), "z")
  eq_1 = MGNode(False, range(0, 5), "e1")
  eq_2 = MGNode(False, range(0, 4), "e2")
  eq_3 = MGNode(False, range(0, 4), "e3")
  eq_4 = MGNode(False, range(0, 1), "e4")
  edge_1_x = MGEdge(eq_1, var_x, [lambda i: i])
  edge_2_y = MGEdge(eq_2, var_y, [lambda i: i])
  edge_2_x = MGEdge(eq_2, var_x, [lambda i: i + 1])
  edge_3_z = MGEdge(eq_3, var_z, [lambda i: i])
  edge_3_x = MGEdge(eq_3, var_x, [lambda i: i])
  edge_3_y = MGEdge(eq_3, var_y, [lambda i: i])
  edge_4_z = MGEdge(eq_4, var_z, [lambda i: 4])
  edge_4_x = MGEdge(eq_4, var_x, [lambda i: 4])
  return MatchingGraph([eq_1, eq_2, eq_3, eq_4], [var_x, var_y, var_z],
                       [edge_1_x, edge_2_y, edge_2_x, edge_3_z, edge_3_x, edge_3_y, edge_4_z, edge_4_x])


def testcase6():
  var_x = MGNode(True, range(0, 6), "x")
  var_y = MGNode(True, range(0, 3), "y")
  eq_1 = MGNode(False, range(0, 3), "e1")
  eq_2 = MGNode(False, range(0, 6), "e2")
  edge_1_x = MGEdge(eq_1, var_x, [lambda i: i])
  edge_1_y = MGEdge(eq_1, var_y, [lambda i: i])
  edge_2_x = MGEdge(eq_2, var_x, [lambda i: i])
  edge_3_y = MGEdge(eq_2, var_y, [lambda i: 0])
  return MatchingGraph([eq_1, eq_2], [var_x, var_y], [edge_1_x, edge_1_y, edge_2_x, edge_3_y])


def testcase7():
  var_x = MGNode(True, range(0, 2), "x")
  var_y = MGNode(True, range(0, 1), "y")
  var_z = MGNode(True, range(0, 1), "z")
  eq_1 = MGNode(False, range(0, 1), "e1")
  eq_2 = MGNode(False, range(0, 1), "e2")
  eq_3 = MGNode(False, range(0, 1), "e3")
  eq_4 = MGNode(False, range(0, 1), "e4")
  edge_1_x = MGEdge(eq_1, var_x, [lambda i: 0])
  edge_2_x = MGEdge(eq_2, var_x, [lambda i: 1])
  edge_2_y = MGEdge(eq_2, var_y, [lambda i: 0])
  edge_3_y = MGEdge(eq_3, var_y, [lambda i: 0])
  edge_3_z = MGEdge(eq_3, var_z, [lambda i: 0])
  edge_4_y = MGEdge(eq_4, var_y, [lambda i: 0])
  edge_4_z = MGEdge(eq_4, var_z, [lambda i: 0])
  return MatchingGraph([eq_1, eq_2, eq_3, eq_4], [var_x, var_y, var_z],
                       [edge_1_x, edge_2_x, edge_2_y, edge_3_y, edge_3_z, edge_4_y, edge_4_z])


def testcase8():
  var_x = MGNode(True, range(0, 9), "x")
  var_y = MGNode(True, range(0, 3), "y")
  eq_1 = MGNode(False, range(0, 3), "e1")
  eq_2 = MGNode(False, range(3, 7), "e2")
  eq_3 = MGNode(False, range(7, 9), "e3")
  eq_4 = MGNode(False, range(0, 3), "e4")
  edge_1_x = MGEdge(eq_1, var_x, [lambda i: i])
  edge_1_y = MGEdge(eq_1, var_y, [lambda i: 0])
  edge_2_x = MGEdge(eq_2, var_x, [lambda i: i])
  edge_2_y = MGEdge(eq_2, var_y, [lambda i: 1])
  edge_3_x = MGEdge(eq_3, var_x, [lambda i: i])
  edge_3_y = MGEdge(eq_3, var_y, [lambda i: 2])
  edge_4_y = MGEdge(eq_4, var_y, [lambda i: i])
  return MatchingGraph([eq_1, eq_2, eq_3, eq_4], [var_x, var_y],
                       [edge_1_x, edge_1_y, edge_2_x, edge_2_y, edge_3_x, edge_3_y, edge_4_y])


def testcase8a():
  # too many equations
  var_x = MGNode(True, range(0, 9), "x")
  var_y = MGNode(True, range(0, 3), "y")
  eq_1 = MGNode(False, range(0, 3), "e1")
  eq_2 = MGNode(False, range(2, 7), "e2")
  eq_3 = MGNode(False, range(5, 9), "e3")
  eq_4 = MGNode(False, range(0, 3), "e4")
  edge_1_x = MGEdge(eq_1, var_x, [lambda i: i])
  edge_1_y = MGEdge(eq_1, var_y, [lambda i: 0])
  edge_2_x = MGEdge(eq_2, var_x, [lambda i: i])
  edge_2_y = MGEdge(eq_2, var_y, [lambda i: 1])
  edge_3_x = MGEdge(eq_3, var_x, [lambda i: i])
  edge_3_y = MGEdge(eq_3, var_y, [lambda i: 2])
  edge_4_y = MGEdge(eq_4, var_y, [lambda i: i])
  return MatchingGraph([eq_1, eq_2, eq_3, eq_4], [var_x, var_y],
                       [edge_1_x, edge_1_y, edge_2_x, edge_2_y, edge_3_x, edge_3_y, edge_4_y])


def testcase9():
  var_x = MGNode(True, range(0, 5), "x")
  var_y = MGNode(True, range(0, 5), "y")
  eq_1 = MGNode(False, range(0, 5), "e1")
  eq_2 = MGNode(False, range(0, 1), "e2")
  eq_3 = MGNode(False, range(0, 1), "e3")
  eq_4 = MGNode(False, range(0, 1), "e4")
  eq_5 = MGNode(False, range(0, 1), "e5")
  eq_6 = MGNode(False, range(0, 1), "e6")
  return MatchingGraph([eq_1, eq_2, eq_3, eq_4, eq_5, eq_6], [var_x, var_y], [
    MGEdge(eq_1, var_x, [lambda i: i]),
    MGEdge(eq_1, var_y, [lambda i: i]),
    MGEdge(eq_2, var_x, [lambda i: 0, lambda i: 1, lambda i: 2, lambda i: 3, lambda i: 4]),
    MGEdge(eq_3, var_y, [lambda i: 0, lambda i: 1, lambda i: 2, lambda i: 3, lambda i: 4]),
    MGEdge(eq_4, var_x, [lambda i: 0, lambda i: 1, lambda i: 2, lambda i: 3, lambda i: 4]),
    MGEdge(eq_5, var_y, [lambda i: 0, lambda i: 1, lambda i: 2, lambda i: 3, lambda i: 4]),
    MGEdge(eq_6, var_x, [lambda i: 0, lambda i: 1, lambda i: 2, lambda i: 3, lambda i: 4])
  ])


def testcase10():
  var_x = MGNode(True, range(0, 2), "x")
  var_y = MGNode(True, range(0, 2), "y")
  eq_1 = MGNode(False, range(0, 2), "e1")
  eq_2 = MGNode(False, range(0, 1), "e2")
  eq_3 = MGNode(False, range(0, 1), "e3")
  edge_1_x = MGEdge(eq_1, var_x, [lambda i: i])
  edge_1_y = MGEdge(eq_1, var_y, [lambda i: i])
  edge_2_x = MGEdge(eq_2, var_x, [lambda i: 0, lambda i: 1])
  edge_3_y = MGEdge(eq_3, var_y, [lambda i: 0, lambda i: 1])
  return MatchingGraph([eq_1, eq_2, eq_3], [var_x, var_y], [edge_1_x, edge_1_y, edge_2_x, edge_3_y])


def testcase11():
  var_a = MGNode(True, range(0, 4), "a")
  var_b = MGNode(True, range(0, 4), "b")
  var_c = MGNode(True, range(0, 4), "c")
  var_d = MGNode(True, range(0, 4), "d")
  eq_1 = MGNode(False, range(0, 4), "e1")
  eq_2 = MGNode(False, range(0, 4), "e2")
  eq_3 = MGNode(False, range(0, 4), "e3")
  eq_4 = MGNode(False, range(0, 4), "e4")
  return MatchingGraph([eq_1, eq_2, eq_3, eq_4], [var_a, var_b, var_c, var_d], [
    MGEdge(eq_1, var_a, [lambda i: i]),
    MGEdge(eq_2, var_a, [lambda i: i]),
    MGEdge(eq_2, var_b, [lambda i: i]),
    MGEdge(eq_3, var_b, [lambda i: i]),
    MGEdge(eq_3, var_c, [lambda i: i]),
    MGEdge(eq_4, var_c, [lambda i: i]),
    MGEdge(eq_4, var_d, [lambda i: i])
  ])

def testcase12():
  var_x = MGNode(True, range(0, 2), "x")
  var_y = MGNode(True, range(0, 2), "y")
  eq_1 = MGNode(False, range(0, 2), "e1")
  eq_2 = MGNode(False, range(0, 1), "e2")
  eq_3 = MGNode(False, range(0, 1), "e3")
  return MatchingGraph([eq_1, eq_2, eq_3], [var_x, var_y], [
    MGEdge(eq_1, var_x, [lambda i: i]),
    MGEdge(eq_1, var_y, [lambda i: i]),
    MGEdge(eq_2, var_x, [lambda i: 1]),
    MGEdge(eq_3, var_y, [lambda i: 0]),
  ])


def testcase13():
  # Test should fail to match (variable y has no edges
  # even though the number of equation is equal to the number
  # of variables)
  var_x = MGNode(True, range(0, 3), "x")
  var_y = MGNode(True, range(0, 1), "y")
  eq_1 = MGNode(False, range(0, 2), "e1")
  eq_2 = MGNode(False, range(1, 3), "e2")
  return MatchingGraph([eq_1, eq_2], [var_x, var_y], [
    MGEdge(eq_1, var_x, [lambda i: i]),
    MGEdge(eq_2, var_x, [lambda i: i]),
  ])


def testcase14():
  # Test should fail to match (x[1] referenced twice
  # while x[2] never referenced)
  var_x = MGNode(True, range(0, 3), "x")
  eq_1 = MGNode(False, range(0, 2), "e1")
  eq_2 = MGNode(False, [0], "e2")
  return MatchingGraph([eq_1, eq_2], [var_x], [
    MGEdge(eq_1, var_x, [lambda i: i]),
    MGEdge(eq_2, var_x, [lambda i: 1]),
  ])


def testcase15():
  var_x = MGNode(True, range(0, 4), "x")
  eq_1 = MGNode(False, range(0, 1), "e1")
  eq_2 = MGNode(False, range(0, 3), "e2")
  return MatchingGraph([eq_1, eq_2], [var_x], [
    MGEdge(eq_1, var_x, [lambda i: 0]),
    MGEdge(eq_1, var_x, [lambda i: 4]),
    MGEdge(eq_2, var_x, [lambda i: i]),
    MGEdge(eq_2, var_x, [lambda i: i+1]),
  ])


def testcase16():
  var_x = MGNode(True, range(0, 5), "x")
  eq_1 = MGNode(False, range(0, 1), "e1")
  eq_2 = MGNode(False, range(0, 4), "e2")
  return MatchingGraph([eq_1, eq_2], [var_x], [
    MGEdge(eq_1, var_x, [lambda i: 1]),
    MGEdge(eq_1, var_x, [lambda i: 3]),
    MGEdge(eq_2, var_x, [lambda i: i]),
    MGEdge(eq_2, var_x, [lambda i: i + 1]),
  ])


def testcase17():
  var_x = MGNode(True, range(0, 5), "x")
  eq_1 = MGNode(False, range(0, 1), "e1")
  eq_2 = MGNode(False, range(0, 4), "e2")
  return MatchingGraph([eq_1, eq_2], [var_x], [
    MGEdge(eq_1, var_x, [lambda i: 0]),
    MGEdge(eq_1, var_x, [lambda i: 3]),
    MGEdge(eq_2, var_x, [lambda i: i]),
    MGEdge(eq_2, var_x, [lambda i: i + 1]),
  ])


def main():
  #
  # Change the following line to modify the test case being run.
  #
  graph = testcase17()

  print("*** simplify")
  simplify(graph)
  print("State after simplify:")
  graph.dump()
  print("valid:", graph.matchingValid())
  if graph.matchingValid():
    print("Simplify was enough to solve the problem")
  else:
    print()
    print("*** matching")
    # TODO: remove parts matched by simplify as in paper
    matching(graph)
    print("State after matching:")
    graph.dump()
    print("valid:", graph.matchingValid())


if __name__ == '__main__':
  main()


