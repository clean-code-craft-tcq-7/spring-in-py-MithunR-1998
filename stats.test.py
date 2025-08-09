import unittest
import stats as statistics
import math


class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    self.assertTrue(math.isnan(computedStats["avg"]))
    self.assertTrue(math.isnan(computedStats["max"]))
    self.assertTrue(math.isnan(computedStats["min"]))
    # All fields of computedStats (average, max, min) must be
    # nan (not-a-number), as defined in the math package
    # Specify the assert here.
    # Use nan and isnan in https://docs.python.org/3/library/math.html

  def test_avg_ignore_nan_inputs(self):
    #check removal of nan
    computedStats = statistics.calculateStats([1.5, float('nan'), 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 3.067, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 4.5, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_all_values_nan(self):
    #check all nan
    computedStats = statistics.calculateStats([float('nan'),float('nan')])
    self.assertTrue(math.isnan(computedStats["avg"]))
    self.assertTrue(math.isnan(computedStats["max"]))
    self.assertTrue(math.isnan(computedStats["min"]))

  def test_absurd_inputs(self):
    #absurd inputs to be removed
    computedStats = statistics.calculateStats([1e10, -1, 9.2, 1e5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 9.2, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 9.2, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 9.2, delta=epsilon)

  def test_absurd_inputs_1(self):
    #absurd inputs to be removed
    computedStats = statistics.calculateStats([1e10, 8, 9.2, 1e5, -11])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 8.6, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 9.2, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 8, delta=epsilon)

  def test_text_inputs_only(self):
    #text inputs to be removed
    computedStats = statistics.calculateStats(['a', 'b', 'c', 'z'])
    self.assertTrue(math.isnan(computedStats["avg"]))
    self.assertTrue(math.isnan(computedStats["max"]))
    self.assertTrue(math.isnan(computedStats["min"]))

  def test_text_inputs_with_numbers(self):
    #text inputs to be removed
    computedStats = statistics.calculateStats(['a', 'hello', '30', 55, 22.3])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 38.65, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 55, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 22.3, delta=epsilon)

  def test_edge_values(self):
    #range is 0 to 200
    computedStats = statistics.calculateStats([0, 200])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 100, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 200, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 0, delta=epsilon)

  def test_outside_boundary(self):
    #range is 0 to 200
    computedStats = statistics.calculateStats([-0.1, 200.01])
    self.assertTrue(math.isnan(computedStats["avg"]))
    self.assertTrue(math.isnan(computedStats["max"]))
    self.assertTrue(math.isnan(computedStats["min"]))

  def test_only_one_invalid(self):
    #range is 0 to 200
    computedStats = statistics.calculateStats([200.01])
    self.assertTrue(math.isnan(computedStats["avg"]))
    self.assertTrue(math.isnan(computedStats["max"]))
    self.assertTrue(math.isnan(computedStats["min"]))

  def test_only_one_valid(self):
    #range is 0 to 200
    computedStats = statistics.calculateStats([100.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 100.5, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 100.5, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 100.5, delta=epsilon)

  def test_combination_valid_invalid(self):
    computedStats = statistics.calculateStats(['a', 'hello', '30', 55, 22.3, 1e12, -5, 999, float('nan'), 0, 200, 75.256])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 70.511, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 200, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 0, delta=epsilon)


if __name__ == "__main__":
  unittest.main()
