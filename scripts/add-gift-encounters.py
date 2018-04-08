#!/usr/bin/env python2
"""
This is an unmaintained one-shot script, only included in the repo for
reference.
"""

from pokedex.db import connect, identifier_from_name
from pokedex.db.tables import Encounter, EncounterSlot, LocationArea
from pokedex.db.tables import EncounterMethod, Location, Pokemon, Version

session = connect()

def get_version(name):
    return session.query(Version).filter_by(identifier=identifier_from_name(name)).one()

def gift_data():
    R = get_version(u'red')
    B = get_version(u'blue')
    Y = get_version(u'yellow')
    G = get_version(u'gold')
    S = get_version(u'silver')
    C = get_version(u'crystal')
    RU = get_version(u'ruby')
    SA = get_version(u'sapphire')
    EM = get_version(u'emerald')
    FR = get_version(u'firered')
    LG = get_version(u'leafgreen')

    DI = get_version(u'diamond')
    PE = get_version(u'pearl')
    PT = get_version(u'platinum')
    HG = get_version(u'heartgold')
    SS = get_version(u'soulsilver')

    BL = get_version(u'black')
    WH = get_version(u'white')
    B2 = get_version(u'black-2')
    W2 = get_version(u'white-2')

    return [
        # Gen I
        [ u'bulbasaur',   [ R, B ],  5, u'pallet-town' ],
        [ u'charmander',  [ R, B ],  5, u'pallet-town' ],
        [ u'squirtle',    [ R, B ],  5, u'pallet-town' ],
        [ u'pikachu',     [ Y    ],  5, u'pallet-town' ],
        [ u'bulbasaur',   [ Y    ], 10, u'cerulean-city'  ],
        [ u'charmander',  [ Y    ], 10, u'kanto-route-24' ],
        [ u'squirtle',    [ Y    ], 10, u'vermilion-city' ],

        [ u'aerodactyl', [ R, B, Y ], 30, u'pewter-city',   u'museum-of-science' ],
        [ u'magikarp',   [ R, B, Y ],  5, u'kanto-route-4', u'pokemon-center' ],
        [ u'omanyte',    [ R, B, Y ], 30, u'mt-moon',       u'b2f' ],
        [ u'kabuto',     [ R, B, Y ], 30, u'mt-moon',       u'b2f' ],
        [ u'hitmonlee',  [ R, B, Y ], 30, u'saffron-city',  u'fighting-dojo' ],
        [ u'hitmonchan', [ R, B, Y ], 30, u'saffron-city',  u'fighting-dojo' ],
        [ u'eevee',      [ R, B, Y ], 25, u'celadon-city',  u'celadon-mansion' ],
        [ u'lapras',     [ R, B, Y ], 15, u'saffron-city',  u'silph-co-7f' ],

        # Gen II
        [ u'chikorita', [ G, S, C ],  5, u'new-bark-town' ],
        [ u'cyndaquil', [ G, S, C ],  5, u'new-bark-town' ],
        [ u'totodile',  [ G, S, C ],  5, u'new-bark-town' ],
        [ u'togepi',    [ G, S, C ],  0, u'violet-city'   ],
        [ u'pichu',     [       C ],  0, u'johto-route-34' ],
        [ u'cleffa',    [       C ],  0, u'johto-route-34' ],
        [ u'igglybuff', [       C ],  0, u'johto-route-34' ],
        [ u'tyrogue',   [       C ],  0, u'johto-route-34' ],
        [ u'smoochum',  [       C ],  0, u'johto-route-34' ],
        [ u'elekid',    [       C ],  0, u'johto-route-34' ],
        [ u'magby',     [       C ],  0, u'johto-route-34' ],
        [ u'spearow',   [ G, S, C ], 10, u'goldenrod-city', u'north-gate' ],
        [ u'eevee',     [ G, S, C ], 20, u'goldenrod-city' ],
        [ u'shuckle',   [ G, S, C ], 15, u'cianwood-city'  ],
        [ u'dratini',   [       C ], 15, u'dragons-den'    ],
        [ u'tyrogue',   [ G, S, C ], 10, u'mt-mortar',      u'b1f' ],

        # Gen III
        # Note Lileep + Anorith are not listed because they are not *gifts*
        # They're note quite encounters either
        # but that's outta scope of gift logic
        [ u'treecko',   [ RU, SA, EM ],  5, u'hoenn-route-101' ],
        [ u'torchic',   [ RU, SA, EM ],  5, u'hoenn-route-101' ],
        [ u'mudkip' ,   [ RU, SA, EM ],  5, u'hoenn-route-101' ],
        [ u'wynaut',    [ RU, SA, EM ],  0, u'lavaridge-town'  ],
        [ u'castform',  [ RU, SA, EM ], 25, u'hoenn-route-119', u'weather-center' ],
        [ u'beldum',    [ RU, SA, EM ],  5, u'mossdeep-city',   u'stevens-house'  ],
        [ u'chikorita', [         EM ],  5, u'littleroot-town' ],
        [ u'cyndaquil', [         EM ],  5, u'littleroot-town' ],
        [ u'totodile',  [         EM ],  5, u'littleroot-town' ],

        [ u'bulbasaur',  [ FR, LG ],  5, u'pallet-town' ],
        [ u'charmander', [ FR, LG ],  5, u'pallet-town' ],
        [ u'squirtle',   [ FR, LG ],  5, u'pallet-town' ],
        [ u'aerodactyl', [ FR, LG ],  5, u'pewter-city',   u'museum-of-science' ],
        [ u'magikarp',   [ FR, LG ],  5, u'kanto-route-4', u'pokemon-center' ],
        [ u'omanyte',    [ FR, LG ],  5, u'mt-moon',       u'b2f' ],
        [ u'kabuto',     [ FR, LG ],  5, u'mt-moon',       u'b2f' ],
        [ u'hitmonlee',  [ FR, LG ], 25, u'saffron-city',  u'fighting-dojo' ],
        [ u'hitmonchan', [ FR, LG ], 25, u'saffron-city',  u'fighting-dojo' ],
        [ u'eevee',      [ FR, LG ], 25, u'celadon-city',  u'celadon-mansion' ],
        [ u'lapras',     [ FR, LG ], 25, u'saffron-city',  u'silph-co-7f' ],
        [ u'togepi',     [ FR, LG ],  0, u'water-labyrinth' ],

        # Gen IV
        [ u'turtwig',  [ DI, PE     ],  5, u'lake-verity', u'before-galactic-intervention' ],
        [ u'chimchar', [ DI, PE     ],  5, u'lake-verity', u'before-galactic-intervention' ],
        [ u'piplup',   [ DI, PE     ],  5, u'lake-verity', u'before-galactic-intervention' ],
        [ u'turtwig',  [         PT ],  5, u'sinnoh-route-201' ],
        [ u'chimchar', [         PT ],  5, u'sinnoh-route-201' ],
        [ u'piplup',   [         PT ],  5, u'sinnoh-route-201' ],
        [ u'togepi',   [ DI, PE, PT ],  0, u'eterna-city' ],
        [ u'eevee',    [ DI, PE,    ],  5, u'hearthome-city' ],
        [ u'eevee',    [         PT ], 20, u'hearthome-city' ],
        [ u'happiny',  [ DI, PE,    ],  0, u'hearthome-city' ],
        [ u'porygon',  [         PT ], 25, u'veilstone-city' ],
        [ u'riolu',    [ DI, PE, PT ],  0, u'iron-island', u'b2f-left' ],

        [ u'chikorita',  [ HG, SS ],  5, u'new-bark-town' ],
        [ u'cyndaquil',  [ HG, SS ],  5, u'new-bark-town' ],
        [ u'totodile',   [ HG, SS ],  5, u'new-bark-town' ],
        [ u'togepi',     [ HG, SS ],  0, u'violet-city'   ],
        [ u'spearow',    [ HG, SS ], 20, u'goldenrod-city', u'north-gate' ],
        [ u'eevee',      [ HG, SS ],  5, u'goldenrod-city' ],
        [ u'shuckle',    [ HG, SS ], 15, u'cianwood-city'  ],
        [ u'dratini',    [ HG, SS ], 15, u'dragons-den'    ],
        [ u'tyrogue',    [ HG, SS ], 10, u'mt-mortar',      u'b1f' ],
        [ u'mareep',     [ HG, SS ],  0, u'violet-city'   ],
        [ u'wooper',     [ HG, SS ],  0, u'violet-city'   ],
        [ u'slugma',     [ HG, SS ],  0, u'violet-city'   ],
        [ u'bulbasaur',  [ HG, SS ],  5, u'pallet-town'   ],
        [ u'charmander', [ HG, SS ],  5, u'pallet-town'   ],
        [ u'squirtle',   [ HG, SS ],  5, u'pallet-town'   ],
        [ u'treecko',    [ HG, SS ],  5, u'saffron-city',   u'silph-co-7f' ],
        [ u'torchic',    [ HG, SS ],  5, u'saffron-city',   u'silph-co-7f' ],
        [ u'mudkip' ,    [ HG, SS ],  5, u'saffron-city',   u'silph-co-7f' ],

        # Gen V
        [ u'snivy',      [ BL, WH ],  5, u'nuvema-town'   ],
        [ u'tepig',      [ BL, WH ],  5, u'nuvema-town'   ],
        [ u'oshawott',   [ BL, WH ],  5, u'nuvema-town'   ],
        [ u'pansage',    [ BL, WH ], 10, u'dreamyard'     ], # not the basement
        [ u'pansear',    [ BL, WH ], 10, u'dreamyard'     ],
        [ u'panpour',    [ BL, WH ], 10, u'dreamyard'     ],
        [ u'zorua',      [ BL, WH ], 10, u'castelia-city' ],
        [ u'tirtouga',   [ BL, WH ], 25, u'relic-castle', u'a' ],
        [ u'archen',     [ BL, WH ], 25, u'relic-castle', u'a' ],
        [ u'larvesta',   [ BL, WH ],  0, u'unova-route-18'     ],
        [ u'omanyte',    [ BL, WH ], 25, u'twist-mountain'     ],
        [ u'kabuto',     [ BL, WH ], 25, u'twist-mountain'     ],
        [ u'aerodactyl', [ BL, WH ], 25, u'twist-mountain'     ],
        [ u'lileep',     [ BL, WH ], 25, u'twist-mountain'     ],
        [ u'anorith',    [ BL, WH ], 25, u'twist-mountain'     ],
        [ u'cranidos',   [ BL, WH ], 25, u'twist-mountain'     ],
        [ u'shieldon',   [ BL, WH ], 25, u'twist-mountain'     ],
        [ u'magikarp',   [ BL, WH ],  5, u'marvelous-bridge'   ],

        [ u'snivy',      [ B2, W2 ],  5, u'aspertia-city'    ],
        [ u'tepig',      [ B2, W2 ],  5, u'aspertia-city'    ],
        [ u'oshawott',   [ B2, W2 ],  5, u'aspertia-city'    ],
        [ u'zorua',      [ B2, W2 ], 25, u'driftveil-city'   ],
        [ u'deerling',   [ B2, W2 ], 30, u'unova-route-6'    ],
        [ u'eevee',      [ B2, W2 ], 10, u'castelia-city'    ],
        [ u'omanyte',    [ B2, W2 ], 25, u'join-avenue'      ],
        [ u'kabuto',     [ B2, W2 ], 25, u'join-avenue'      ],
        [ u'aerodactyl', [ B2, W2 ], 25, u'join-avenue'      ],
        [ u'lileep',     [ B2, W2 ], 25, u'join-avenue'      ],
        [ u'anorith',    [ B2, W2 ], 25, u'join-avenue'      ],
        [ u'cranidos',   [ B2, W2 ], 25, u'join-avenue'      ],
        [ u'shieldon',   [ B2, W2 ], 25, u'join-avenue'      ],
        [ u'tirtouga',   [ B2, W2 ], 25, u'join-avenue'      ],
        [ u'archen',     [ B2, W2 ], 25, u'join-avenue'      ],
        [ u'magikarp',   [ B2, W2 ],  5, u'marvelous-bridge' ],
        [ u'happiny',    [ B2, W2 ],  0, u'nacrene-city'     ],
        [ u'tirtouga',   [ B2, W2 ], 25, u'nacrene-city'     ],
        [ u'archen',     [ B2, W2 ], 25, u'nacrene-city'     ],
        [ u'omanyte',    [ B2, W2 ], 25, u'twist-mountain'   ],
        [ u'kabuto',     [ B2, W2 ], 25, u'twist-mountain'   ],
        [ u'aerodactyl', [ B2, W2 ], 25, u'twist-mountain'   ],
        [ u'lileep',     [ B2, W2 ], 25, u'twist-mountain'   ],
        [ u'anorith',    [ B2, W2 ], 25, u'twist-mountain'   ],
        [ u'cranidos',   [ B2, W2 ], 25, u'twist-mountain'   ],
        [ u'shieldon',   [ B2, W2 ], 25, u'twist-mountain'   ],
        # These are shiny...
        [ u'dratini',    [     W2 ],  1, u'floccesy-town'    ],
        [ u'gible',      [ B2     ],  1, u'floccesy-town'    ],
    ]


gift_method = session.query(EncounterMethod).filter_by(identifier=u'gift').one()

for gift_data in gift_data():
    pokemon_name  = identifier_from_name(gift_data[0])
    versions      = gift_data[1]
    level         = identifier_from_name(str(gift_data[2]))
    location_name = identifier_from_name(gift_data[3])
    area_name       = None
    if len(gift_data) > 4:
        area_name     = identifier_from_name(gift_data[4])


    pokemon       = session.query(Pokemon     ).filter_by(identifier=pokemon_name                      ).one()
    location      = session.query(Location    ).filter_by(identifier=location_name                     ).one()
    location_area = session.query(LocationArea).filter_by(identifier=area_name, location_id=location.id).first()
    # Some of these don't exist yet
    if not location_area:
        location_area = LocationArea(
            location_id = location.id,
            game_index  = 0, # cause who knows what this means
            identifier  = area_name
        )
        session.add(location_area)
        session.commit()

    for version in versions:
        encounter_slot = session.query(EncounterSlot).filter_by(
            version_group_id    = version.version_group_id,
            encounter_method_id = gift_method.id
        ).first()

        if not encounter_slot:
            encounter_slot = EncounterSlot(
                version_group_id = version.version_group_id,
                encounter_method_id = gift_method.id,
                # No priority over or under other events/conditions
                slot                = None,
                # Rarity is meaningless for gifts
                rarity              = None,
            )
            session.add(encounter_slot)
            session.commit()

        encounter_info = {
            'version_id':        version.id,
            'location_area_id':  location_area.id,
            'encounter_slot_id': encounter_slot.id,
            'pokemon_id':        pokemon.id,
            'min_level':         level,
            'max_level':         level
        }
        encounter = session.query(Encounter).filter_by(**encounter_info).first()
        if not encounter:
            encounter = Encounter(**encounter_info)
            session.add(encounter)

    session.commit()
