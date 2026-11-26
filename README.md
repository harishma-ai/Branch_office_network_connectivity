# Branch Office Network Connectivity Simulator
Python project simulating routing between two branch LANs. Educational only: it does not configure routers, create VPNs, or send real traffic.

## Topology
- Branch A (Coimbatore): `192.168.10.0/24`, gateway `192.168.10.1`
- Branch B (Chennai): `192.168.20.0/24`, gateway `192.168.20.1`
- Illustrative inter-branch link: `10.10.10.0/30`

## Features
- Branch/subnet mapping and IP validation
- Static route table simulation and longest-prefix matching
- Bidirectional simulated reachability tests
- Route lookup explanations and unit tests

## Requirements
Python 3.9+; no extra packages.

## Run (Windows)
Extract ZIP, open folder, type `cmd` in the Explorer address bar and Enter:
```bash
python src/main.py
```
If needed: `py src/main.py`

## Run tests
```bash
python -m unittest discover -s tests -v
```
