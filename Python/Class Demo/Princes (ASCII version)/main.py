from Prince import Prince

nick = Prince("Nick", son_of="Ken")
nick.name = "Nicolas"
nick.announce()

tom = Prince("Matthew", son_of="Nick")
tom.announce()

matthew = Prince("Thomas", son_of="Nick")
matthew.add_sibling("Matthew")
matthew.announce()
