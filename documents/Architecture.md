# Architecture
```text
Branch A LAN 192.168.10.0/24
        | Gateway A
        +==== Illustrative inter-branch link ====+
                                                |
                                         Gateway B
                                                | Branch B LAN
                                                | 192.168.20.0/24

           JSON topology -> Python simulator -> route lookup
                                          -> simulated result
```
Conceptual only. No router or tunnel is configured.
