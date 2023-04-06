def ship_class(ship):  # package function to be imported
    if ship == "falcon":
        name = "Millenium Falcon"
        falcon = {
            print(f"{name} secure data: Level 1 Access"),
            print("Captain: Han Solo"),
            print("Commissioned: 60BBY"),
            print("Product line: YT-Series"),
            print(
                "Armament: Laser cannons, blaster cannon, concussion missile,lightning gun"
            ),
        }
    elif ship == "executor":
        name = "Imperial Executor"
        executor = {
            print(f"{name} secure data: Level 1 Access"),
            print("Captain:Lord Darth Vader"),
            print("Product line: Modified Executor-class Star Dreadnought"),
            print(
                "Armament: 5000 turbolasers, 750 turbolaser batteries, 100 twin ion cannons, 125 assault concussion missile launchers, 250 turret-mounted quad laser cannons"
            ),
            print(
                "Complement: 1000+ ships, 144 TIE starfighters, 200 assault shuttles including transport shuttles and support craft, 74 walkers"
            ),
        }

    else:
        name = "United Space Ship Enterprise NCC-1701-D"
        enterprise = {
            print(f"{name} secure data: Level 1 Access"),
            print("Captain: Jean-Luc Picard"),
            print("Class: Galaxy class"),
            print("Operator: Starfleet"),
            print(
                "Defense systems: 10 phaser banks, 250 photon torpedoes and high capacity shield grid"
            ),
        }
