#!/usr/bin/env python3
exec(open("/private/tmp/pell_orbit_circuit_search.py").read().replace(
    "            mask = first_dependency(records)\n",
    "            if direct:\n                continue\n            mask = first_dependency(records)\n",
))
