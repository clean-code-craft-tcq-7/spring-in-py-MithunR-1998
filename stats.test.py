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

if __name__ == "__main__":
  unittest.main()
