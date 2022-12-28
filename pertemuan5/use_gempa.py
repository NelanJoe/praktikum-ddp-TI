"""
    * Import Package Gempa
"""
from Gempa import Gempa

palu = Gempa("Palu", 6)
jepang = Gempa("jepang", 8)
cianjur = Gempa("cianjur", 6.5)
aceh = Gempa("aceh", 9)

palu.dampak()
jepang.dampak()
cianjur.dampak()
aceh.dampak()
