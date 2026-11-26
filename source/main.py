from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from config_loader import load_config
from network_model import NetworkModel

SAMPLES=[
("Branch A PC -> Branch B PC","192.168.10.25","192.168.20.25"),
("Branch B PC -> Branch A server","192.168.20.30","192.168.10.100"),
("Same Branch A subnet","192.168.10.25","192.168.10.100"),
("Unknown destination subnet","192.168.10.25","172.16.5.10"),
]
def main():
    cfg=load_config(ROOT/"config"/"topology.json")
    model=NetworkModel(cfg)
    print("="*70+"\n TWO BRANCH OFFICE NETWORK CONNECTIVITY SIMULATOR\n"+"="*70)
    print("Simulation only: no real network, router, or VPN configuration.\nTOPOLOGY")
    for b in cfg["branches"]:
        print(f" {b['name']} ({b['city']}): {b['subnet']} | gateway {b['gateway']}")
    print(f" Inter-branch link: {cfg['inter_branch_link']}\nTEST RESULTS\n"+"-"*70)
    for title,src,dst in SAMPLES:
        result=model.simulate_connectivity(src,dst)
        route=model.lookup_route(dst)
        print(f"{title}\n Source: {src} | Destination: {dst}\n Result: {result['status']}\n Reason: {result['reason']}")
        if route: print(f" Route: {route['route_id']} | {route['destination']} | next hop {route['next_hop']}")
        print("-"*70)
    print("Demo complete. Modify config/topology.json to customize.")
if __name__=="__main__": main()
