import sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from config_loader import load_config
from network_model import NetworkModel

class Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.model=NetworkModel(load_config(ROOT/"config"/"topology.json"))
 def test_a_to_b(self):
  self.assertEqual(self.model.simulate_connectivity("192.168.10.25","192.168.20.25")["status"],"SIMULATED REACHABLE")
 def test_b_to_a(self):
  self.assertEqual(self.model.simulate_connectivity("192.168.20.30","192.168.10.100")["status"],"SIMULATED REACHABLE")
 def test_local(self):
  self.assertEqual(self.model.simulate_connectivity("192.168.10.25","192.168.10.100")["status"],"REACHABLE (LOCAL)")
 def test_unknown_network(self):
  self.assertEqual(self.model.simulate_connectivity("192.168.10.25","172.16.5.10")["status"],"UNREACHABLE")
 def test_route_lookup(self):
  self.assertEqual(self.model.lookup_route("192.168.20.25")["route_id"],"ROUTE-A-B")
if __name__=="__main__":unittest.main()
