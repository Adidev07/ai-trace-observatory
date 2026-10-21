import unittest, json
from pathlib import Path
from logic import run
class LogicTests(unittest.TestCase):
    def setUp(self):
        self.records=json.loads(Path(__file__).with_name("sample_data.json").read_text())
    def test_aggregates(self):
        result=run({},self.records)
        self.assertEqual(result['count'],4)
        self.assertEqual(result['error_rate'],.25)
        self.assertEqual(result['p95_latency_ms'],3000)
        self.assertAlmostEqual(result['estimated_cost_usd'],.00588)
    def test_filter(self):
        self.assertEqual(run({'model':'demo-small'},self.records)['count'],2)
    def test_empty(self):
        self.assertIsNone(run({'model':'missing'},self.records)['p95_latency_ms'])
    def test_threshold(self):
        for v in (0,-1,'nan','inf'):
            with self.assertRaises(ValueError): run({'latency_threshold_ms':v},self.records)
