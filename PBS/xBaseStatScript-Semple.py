import requests

# ==================
# == TEST GRAB STRINGS ==
# ==================

my_file = """#-------------------------------
[BULBASAUR]
Name = Bulbasaur
Types = GRASS,POISON
BaseStats = 45,49,49,45,65,65
GenderRatio = FemaleOneEighth
GrowthRate = Parabolic
BaseExp = 64
EVs = SPECIAL_ATTACK,1
CatchRate = 45
Happiness = 50
Abilities = OVERGROW
HiddenAbilities = CHLOROPHYLL
Moves = 1,TACKLE,1,GROWL,3,VINEWHIP,6,GROWTH,9,LEECHSEED,12,RAZORLEAF,15,POISONPOWDER,15,SLEEPPOWDER,18,SEEDBOMB,21,TAKEDOWN,24,SWEETSCENT,27,SYNTHESIS,30,WORRYSEED,33,DOUBLEEDGE,36,SOLARBEAM
TutorMoves = AMNESIA,ATTRACT,BODYSLAM,BULLETSEED,CHARM,CUT,DOUBLETEAM,ENDURE,ENERGYBALL,FACADE,FALSESWIPE,FLASH,GIGADRAIN,GRASSKNOT,GRASSPLEDGE,GRASSYGLIDE,GRASSYTERRAIN,HELPINGHAND,HIDDENPOWER,LEAFSTORM,LIGHTSCREEN,MAGICALLEAF,POWERWHIP,PROTECT,REST,ROCKSMASH,ROUND,SAFEGUARD,SEEDBOMB,SLEEPTALK,SLUDGEBOMB,SNORE,SOLARBEAM,STRENGTH,SUBSTITUTE,SUNNYDAY,SWAGGER,SWORDSDANCE,TOXIC,VENOSHOCK,WEATHERBALL,WORKUP
EggMoves = AMNESIA,CHARM,CURSE,GRASSYTERRAIN,INGRAIN,LEAFSTORM,MAGICALLEAF,NATUREPOWER,PETALDANCE,POWERWHIP,SKULLBASH,SLUDGE
EggGroups = Monster,Grass
HatchSteps = 5120
Height = 0.7
Weight = 6.9
Color = Green
Shape = Quadruped
Habitat = Grassland
Category = Seed
Pokedex = Bulbasaur can be seen napping in bright sunlight. There is a seed on its back. By soaking up the sun's rays, the seed grows progressively larger.
Generation = 1
Evolutions = IVYSAUR,Level,16
#-------------------------------
[IVYSAUR]
Name = Ivysaur
Types = GRASS,POISON
BaseStats = 60,62,63,60,80,80
GenderRatio = FemaleOneEighth
GrowthRate = Parabolic
BaseExp = 142
EVs = SPECIAL_ATTACK,1,SPECIAL_DEFENSE,1
CatchRate = 45
Happiness = 50
Abilities = OVERGROW
HiddenAbilities = CHLOROPHYLL
Moves = 1,TACKLE,1,GROWL,1,VINEWHIP,1,GROWTH,9,LEECHSEED,12,RAZORLEAF,15,POISONPOWDER,15,SLEEPPOWDER,20,SEEDBOMB,25,TAKEDOWN,30,SWEETSCENT,35,SYNTHESIS,40,WORRYSEED,45,DOUBLEEDGE,50,SOLARBEAM
TutorMoves = AMNESIA,ATTRACT,BODYSLAM,BULLETSEED,CHARM,CUT,DOUBLETEAM,ENDURE,ENERGYBALL,FACADE,FALSESWIPE,FLASH,GIGADRAIN,GRASSKNOT,GRASSPLEDGE,GRASSYGLIDE,GRASSYTERRAIN,HELPINGHAND,HIDDENPOWER,LEAFSTORM,LIGHTSCREEN,MAGICALLEAF,POWERWHIP,PROTECT,REST,ROCKSMASH,ROUND,SAFEGUARD,SEEDBOMB,SLEEPTALK,SLUDGEBOMB,SNORE,SOLARBEAM,STRENGTH,SUBSTITUTE,SUNNYDAY,SWAGGER,SWORDSDANCE,TOXIC,VENOSHOCK,WEATHERBALL,WORKUP
EggGroups = Monster,Grass
HatchSteps = 5120
Height = 1.0
Weight = 13.0
Color = Green
Shape = Quadruped
Habitat = Grassland
Category = Seed
Pokedex = To support its bulb, Ivysaur's legs grow sturdy. If it spends more time lying in the sunlight, the bud will soon bloom into a large flower.
Generation = 1
Evolutions = VENUSAUR,Level,32
#-------------------------------
[VENUSAUR]
Name = Venusaur
Types = GRASS,POISON
BaseStats = 80,82,83,80,100,100
GenderRatio = FemaleOneEighth
GrowthRate = Parabolic
BaseExp = 263
EVs = SPECIAL_ATTACK,2,SPECIAL_DEFENSE,1
CatchRate = 45
Happiness = 50
Abilities = OVERGROW
HiddenAbilities = CHLOROPHYLL
Moves = 0,PETALBLIZZARD,1,PETALBLIZZARD,1,PETALDANCE,1,TACKLE,1,GROWL,1,VINEWHIP,1,GROWTH,9,LEECHSEED,12,RAZORLEAF,15,POISONPOWDER,15,SLEEPPOWDER,20,SEEDBOMB,25,TAKEDOWN,30,SWEETSCENT,37,SYNTHESIS,44,WORRYSEED,51,DOUBLEEDGE,58,SOLARBEAM
TutorMoves = AMNESIA,ATTRACT,BODYSLAM,BULLDOZE,BULLETSEED,CHARM,CUT,DOUBLETEAM,EARTHPOWER,EARTHQUAKE,ENDURE,ENERGYBALL,FACADE,FALSESWIPE,FLASH,FRENZYPLANT,GIGADRAIN,GIGAIMPACT,GRASSKNOT,GRASSPLEDGE,GRASSYGLIDE,GRASSYTERRAIN,HELPINGHAND,HIDDENPOWER,HYPERBEAM,LEAFSTORM,LIGHTSCREEN,MAGICALLEAF,OUTRAGE,POWERWHIP,PROTECT,REST,ROAR,ROCKCLIMB,ROCKSMASH,ROUND,SAFEGUARD,SEEDBOMB,SLEEPTALK,SLUDGEBOMB,SNORE,SOLARBEAM,STOMPINGTANTRUM,STRENGTH,SUBSTITUTE,SUNNYDAY,SWAGGER,SWORDSDANCE,TERRAINPULSE,TOXIC,VENOSHOCK,WEATHERBALL,WORKUP
EggGroups = Monster,Grass
HatchSteps = 5120
Height = 2.0
Weight = 100.0
Color = Green
Shape = Quadruped
Habitat = Grassland
Category = Seed
Pokedex = Venusaur's flower is said to take on vivid colors if it gets plenty of nutrition and sunlight. The flower's aroma soothes the emotions of people.
Generation = 1
#-------------------------------
[CHARMANDER]
Name = Charmander
Types = FIRE
BaseStats = 39,52,43,65,60,50
GenderRatio = FemaleOneEighth
GrowthRate = Parabolic
BaseExp = 62
EVs = SPEED,1
CatchRate = 45
Happiness = 50
Abilities = BLAZE
HiddenAbilities = SOLARPOWER
Moves = 1,SCRATCH,1,GROWL,4,EMBER,8,SMOKESCREEN,12,DRAGONBREATH,17,FIREFANG,20,SLASH,24,FLAMETHROWER,28,SCARYFACE,32,FIRESPIN,36,INFERNO,40,FLAREBLITZ
TutorMoves = ACROBATICS,AERIALACE,ATTRACT,BEATUP,BODYSLAM,BRICKBREAK,CRUNCH,CUT,DIG,DOUBLETEAM,DRAGONCLAW,DRAGONDANCE,DRAGONPULSE,ENDURE,FACADE,FALSESWIPE,FIREBLAST,FIREFANG,FIREPLEDGE,FIREPUNCH,FIRESPIN,FLAMETHROWER,FLAREBLITZ,FLING,FOCUSPUNCH,HEATWAVE,HELPINGHAND,HIDDENPOWER,IRONTAIL,MEGAKICK,MEGAPUNCH,OUTRAGE,OVERHEAT,PROTECT,REST,ROCKSLIDE,ROCKSMASH,ROCKTOMB,ROUND,SCARYFACE,SHADOWCLAW,SLEEPTALK,SNORE,STRENGTH,SUBSTITUTE,SUNNYDAY,SWAGGER,SWIFT,SWORDSDANCE,THUNDERPUNCH,WEATHERBALL,WILLOWISP,WORKUP
EggMoves = AIRCUTTER,ANCIENTPOWER,BEATUP,BELLYDRUM,BITE,COUNTER,CRUNCH,DRAGONDANCE,DRAGONRUSH,DRAGONTAIL,FLAREBLITZ,METALCLAW,OUTRAGE,WINGATTACK
EggGroups = Monster,Dragon
HatchSteps = 5120
Height = 0.6
Weight = 8.5
Color = Red
Shape = BipedalTail
Habitat = Mountain
Category = Lizard
Pokedex = The flame that burns at the tip of its tail is an indication of its emotions. The flame wavers when Charmander is happy, and blazes when it is enraged.
Generation = 1
Evolutions = CHARMELEON,Level,16
#-------------------------------
[CHARMELEON]
Name = Charmeleon
Types = FIRE
BaseStats = 58,64,58,80,80,65
GenderRatio = FemaleOneEighth
GrowthRate = Parabolic
BaseExp = 142
EVs = SPECIAL_ATTACK,1,SPEED,1
CatchRate = 45
Happiness = 50
Abilities = BLAZE
HiddenAbilities = SOLARPOWER
Moves = 1,SCRATCH,1,GROWL,1,EMBER,1,SMOKESCREEN,12,DRAGONBREATH,19,FIREFANG,24,SLASH,30,FLAMETHROWER,37,SCARYFACE,42,FIRESPIN,48,INFERNO,54,FLAREBLITZ
TutorMoves = ACROBATICS,AERIALACE,ATTRACT,BEATUP,BODYSLAM,BRICKBREAK,CRUNCH,CUT,DIG,DOUBLETEAM,DRAGONCLAW,DRAGONDANCE,DRAGONPULSE,ENDURE,FACADE,FALSESWIPE,FIREBLAST,FIREFANG,FIREPLEDGE,FIREPUNCH,FIRESPIN,FLAMETHROWER,FLAREBLITZ,FLING,FOCUSPUNCH,HEATWAVE,HELPINGHAND,HIDDENPOWER,IRONTAIL,MEGAKICK,MEGAPUNCH,OUTRAGE,OVERHEAT,PROTECT,REST,ROCKSLIDE,ROCKSMASH,ROCKTOMB,ROUND,SCARYFACE,SHADOWCLAW,SLEEPTALK,SNORE,STRENGTH,SUBSTITUTE,SUNNYDAY,SWAGGER,SWIFT,SWORDSDANCE,THUNDERPUNCH,WEATHERBALL,WILLOWISP,WORKUP
EggGroups = Monster,Dragon
HatchSteps = 5120
Height = 1.1
Weight = 19.0
Color = Red
Shape = BipedalTail
Habitat = Mountain
Category = Flame
Pokedex = Without pity, its sharp claws destroy foes. If it encounters a strong enemy, it becomes agitated, and the flame on its tail flares with a bluish white color.
Generation = 1
Evolutions = CHARIZARD,Level,36
#-------------------------------
[CHARIZARD]
Name = Charizard
Types = FIRE,FLYING
BaseStats = 78,84,78,100,109,85
GenderRatio = FemaleOneEighth
GrowthRate = Parabolic
BaseExp = 267
EVs = SPECIAL_ATTACK,3
CatchRate = 45
Happiness = 50
Abilities = BLAZE
HiddenAbilities = SOLARPOWER
Moves = 0,AIRSLASH,1,AIRSLASH,1,DRAGONCLAW,1,HEATWAVE,1,SCRATCH,1,GROWL,1,EMBER,1,SMOKESCREEN,12,DRAGONBREATH,19,FIREFANG,24,SLASH,30,FLAMETHROWER,39,SCARYFACE,46,FIRESPIN,54,INFERNO,62,FLAREBLITZ
TutorMoves = ACROBATICS,AERIALACE,AIRSLASH,ATTRACT,BEATUP,BLASTBURN,BLAZEKICK,BODYSLAM,BREAKINGSWIPE,BRICKBREAK,BRUTALSWING,BULLDOZE,CRUNCH,CUT,DIG,DOUBLETEAM,DRAGONCLAW,DRAGONDANCE,DRAGONPULSE,DUALWINGBEAT,EARTHQUAKE,ENDURE,FACADE,FALSESWIPE,FIREBLAST,FIREFANG,FIREPLEDGE,FIREPUNCH,FIRESPIN,FLAMETHROWER,FLAREBLITZ,FLING,FLY,FOCUSBLAST,FOCUSPUNCH,GIGAIMPACT,HEATCRASH,HEATWAVE,HELPINGHAND,HIDDENPOWER,HURRICANE,HYPERBEAM,IRONTAIL,MEGAKICK,MEGAPUNCH,MYSTICALFIRE,OUTRAGE,OVERHEAT,PROTECT,REST,ROAR,ROCKSLIDE,ROCKSMASH,ROCKTOMB,ROOST,ROUND,SCALESHOT,SCARYFACE,SCORCHINGSANDS,SHADOWCLAW,SLEEPTALK,SNORE,SOLARBEAM,STEELWING,STRENGTH,SUBSTITUTE,SUNNYDAY,SWAGGER,SWIFT,SWORDSDANCE,THUNDERPUNCH,WEATHERBALL,WILLOWISP,WORKUP
EggGroups = Monster,Dragon
HatchSteps = 5120
Height = 1.7
Weight = 90.5
Color = Red
Shape = BipedalTail
Habitat = Mountain
Category = Flame
Pokedex = A Charizard flies about in search of strong opponents. It breathes intense flames that can melt any material. However, it will never torch a weaker foe.
Generation = 1
#-------------------------------
[EEVEE]
Name = Eevee
Types = NORMAL
BaseStats = 55,55,50,55,45,65
GenderRatio = FemaleOneEighth
GrowthRate = Medium
BaseExp = 65
EVs = SPECIAL_DEFENSE,1
CatchRate = 45
Happiness = 50
Abilities = RUNAWAY,ADAPTABILITY
HiddenAbilities = ANTICIPATION
Moves = 1,COVET,1,HELPINGHAND,1,TACKLE,1,GROWL,1,TAILWHIP,5,SANDATTACK,10,QUICKATTACK,15,BABYDOLLEYES,20,SWIFT,25,BITE,30,COPYCAT,35,BATONPASS,40,TAKEDOWN,45,CHARM,50,DOUBLEEDGE,55,LASTRESORT
TutorMoves = ATTRACT,BATONPASS,BODYSLAM,CHARM,DIG,DOUBLETEAM,ENDURE,FACADE,FAKETEARS,FOCUSENERGY,HELPINGHAND,HIDDENPOWER,HYPERVOICE,IRONTAIL,PAYDAY,PROTECT,RAINDANCE,REST,RETALIATE,ROUND,SHADOWBALL,SLEEPTALK,SNORE,STOREDPOWER,SUBSTITUTE,SUNNYDAY,SWAGGER,SWIFT,WEATHERBALL,WORKUP
EggMoves = CHARM,COVET,CURSE,DETECT,DOUBLEKICK,FAKETEARS,FLAIL,MUDSLAP,STOREDPOWER,TICKLE,WISH,YAWN
EggGroups = Field
HatchSteps = 8960
Height = 0.3
Weight = 6.5
Color = Brown
Shape = Quadruped
Habitat = Urban
Category = Evolution
Pokedex = An Eevee has an unstable genetic makeup that suddenly mutates due to its environment. Radiation from various stones causes this Pokémon to evolve.
Generation = 1
Evolutions = VAPOREON,Item,WATERSTONE,JOLTEON,Item,THUNDERSTONE,FLAREON,Item,FIRESTONE,LEAFEON,LocationFlag,MossRock,LEAFEON,Item,LEAFSTONE,GLACEON,LocationFlag,IceRock,GLACEON,Item,ICESTONE,SYLVEON,HappinessMoveType,FAIRY,ESPEON,HappinessDay,,UMBREON,HappinessNight,
#-------------------------------
[ARTICUNO]
Name = Articuno
Types = ICE,FLYING
BaseStats = 90,85,100,85,95,125
GenderRatio = Genderless
GrowthRate = Slow
BaseExp = 290
EVs = SPECIAL_DEFENSE,3
CatchRate = 3
Happiness = 35
Abilities = PRESSURE
HiddenAbilities = SNOWCLOAK
Moves = 1,GUST,1,MIST,5,POWDERSNOW,10,REFLECT,15,ICESHARD,20,AGILITY,25,ANCIENTPOWER,30,TAILWIND,35,FREEZEDRY,40,ROOST,45,ICEBEAM,50,HAIL,55,HURRICANE,60,MINDREADER,65,BLIZZARD,70,SHEERCOLD
TutorMoves = AERIALACE,AGILITY,AIRSLASH,AVALANCHE,BLIZZARD,BRAVEBIRD,DEFOG,DOUBLETEAM,DUALWINGBEAT,ENDURE,FACADE,FLY,GIGAIMPACT,HAIL,HIDDENPOWER,HURRICANE,HYPERBEAM,ICEBEAM,ICICLESPEAR,ICYWIND,PLUCK,PROTECT,RAINDANCE,REFLECT,REST,ROAR,ROCKSMASH,ROOST,ROUND,SANDSTORM,SLEEPTALK,SNORE,STEELWING,SUBSTITUTE,SUNNYDAY,SWAGGER,SWIFT,TRIPLEAXEL,UTURN,WATERPULSE,WEATHERBALL
EggGroups = Undiscovered
HatchSteps = 20480
Height = 1.7
Weight = 55.4
Color = Blue
Shape = Winged
Habitat = Rare
Category = Freeze
Pokedex = Articuno is a legendary bird Pokémon that can control ice. The flapping of its wings chills the air. As a result, it is said that when this Pokémon flies, snow will fall.
Generation = 1
#-------------------------------
[ZAPDOS]
Name = Zapdos
Types = ELECTRIC,FLYING
BaseStats = 90,90,85,100,125,90
GenderRatio = Genderless
GrowthRate = Slow
BaseExp = 290
EVs = SPECIAL_ATTACK,3
CatchRate = 3
Happiness = 35
Abilities = PRESSURE
HiddenAbilities = STATIC
Moves = 1,PECK,1,THUNDERWAVE,5,THUNDERSHOCK,10,LIGHTSCREEN,15,PLUCK,20,AGILITY,25,ANCIENTPOWER,30,CHARGE,35,DRILLPECK,40,ROOST,45,DISCHARGE,50,RAINDANCE,55,THUNDER,60,DETECT,65,MAGNETICFLUX,70,ZAPCANNON
TutorMoves = AERIALACE,AGILITY,BATONPASS,BRAVEBIRD,CHARGEBEAM,DEFOG,DOUBLETEAM,DUALWINGBEAT,EERIEIMPULSE,ENDURE,FACADE,FLASH,FLY,GIGAIMPACT,HAIL,HEATWAVE,HIDDENPOWER,HURRICANE,HYPERBEAM,LIGHTSCREEN,PLUCK,PROTECT,RAINDANCE,REST,RISINGVOLTAGE,ROAR,ROCKSMASH,ROOST,ROUND,SANDSTORM,SHOCKWAVE,SLEEPTALK,SNORE,STEELWING,SUBSTITUTE,SUNNYDAY,SWAGGER,SWIFT,THUNDER,THUNDERBOLT,THUNDERWAVE,UTURN,VOLTSWITCH,WEATHERBALL,WILDCHARGE
EggGroups = Undiscovered
HatchSteps = 20480
Height = 1.6
Weight = 52.6
Color = Yellow
Shape = Winged
Habitat = Rare
Category = Electric
Pokedex = Zapdos is a legendary bird Pokémon that has the ability to control electricity. It usually lives in thunderclouds. It gains power if it is stricken by lightning bolts.
Generation = 1
#-------------------------------
[MOLTRES]
Name = Moltres
Types = FIRE,FLYING
BaseStats = 90,100,90,90,125,85
GenderRatio = Genderless
GrowthRate = Slow
BaseExp = 290
EVs = SPECIAL_ATTACK,3
CatchRate = 3
Happiness = 35
Abilities = PRESSURE
HiddenAbilities = FLAMEBODY
Moves = 1,GUST,1,LEER,5,EMBER,10,SAFEGUARD,15,WINGATTACK,20,AGILITY,25,ANCIENTPOWER,30,INCINERATE,35,AIRSLASH,40,ROOST,45,HEATWAVE,50,SUNNYDAY,55,HURRICANE,60,ENDURE,65,BURNUP,70,SKYATTACK
TutorMoves = AERIALACE,AGILITY,AIRSLASH,BRAVEBIRD,BURNINGJEALOUSY,DEFOG,DOUBLETEAM,DUALWINGBEAT,ENDURE,FACADE,FIREBLAST,FIRESPIN,FLAMETHROWER,FLAREBLITZ,FLY,GIGAIMPACT,HEATWAVE,HIDDENPOWER,HURRICANE,HYPERBEAM,MYSTICALFIRE,OVERHEAT,PLUCK,PROTECT,RAINDANCE,REST,ROAR,ROCKSMASH,ROOST,ROUND,SAFEGUARD,SANDSTORM,SCORCHINGSANDS,SLEEPTALK,SNORE,SOLARBEAM,STEELWING,SUBSTITUTE,SUNNYDAY,SWAGGER,SWIFT,UTURN,WEATHERBALL,WILLOWISP
EggGroups = Undiscovered
HatchSteps = 20480
Height = 2.0
Weight = 60.0
Color = Yellow
Shape = Winged
Habitat = Rare
Category = Flame
Pokedex = Moltres is a legendary bird Pokémon that can control fire. If injured, it is said to dip its body in the molten magma of a volcano to burn and heal itself.
Generation = 1
#-------------------------------
[SNORLAX]
Name = Snorlax
Types = NORMAL
BaseStats = 160,110,65,30,65,110
GenderRatio = FemaleOneEighth
GrowthRate = Slow
BaseExp = 189
EVs = HP,2
CatchRate = 25
Happiness = 50
Abilities = IMMUNITY,THICKFAT
HiddenAbilities = GLUTTONY
Moves = 1,RECYCLE,1,COVET,1,STOCKPILE,1,SWALLOW,1,SCREECH,1,FLING,1,METRONOME,1,FLAIL,1,LASTRESORT,1,LICK,1,TACKLE,1,DEFENSECURL,1,BLOCK,12,YAWN,16,BITE,20,REST,20,SNORE,20,SLEEPTALK,24,CRUNCH,28,BODYSLAM,32,HEAVYSLAM,36,AMNESIA,40,HIGHHORSEPOWER,44,HAMMERARM,48,BELLYDRUM,52,BELCH,56,GIGAIMPACT
TutorMoves = AMNESIA,ATTRACT,BLIZZARD,BODYPRESS,BODYSLAM,BRICKBREAK,BULLDOZE,CHARM,CRUNCH,DARKESTLARIAT,DOUBLETEAM,EARTHQUAKE,ENCORE,ENDURE,FACADE,FIREBLAST,FIREPUNCH,FLAMETHROWER,FLING,FOCUSBLAST,FOCUSPUNCH,GIGAIMPACT,GUNKSHOT,HEATCRASH,HEAVYSLAM,HIDDENPOWER,HIGHHORSEPOWER,HYDROPUMP,HYPERBEAM,HYPERVOICE,ICEBEAM,ICEPUNCH,ICYWIND,IRONHEAD,MEGAKICK,MEGAPUNCH,METRONOME,OUTRAGE,PAYDAY,PROTECT,PSYCHIC,RAINDANCE,RECYCLE,REST,RETALIATE,ROCKCLIMB,ROCKSLIDE,ROCKSMASH,ROCKTOMB,ROUND,SANDSTORM,SCREECH,SEEDBOMB,SELFDESTRUCT,SHADOWBALL,SHOCKWAVE,SLEEPTALK,SNORE,SOLARBEAM,STEELROLLER,STOMPINGTANTRUM,STRENGTH,SUBSTITUTE,SUNNYDAY,SUPERPOWER,SURF,SWAGGER,TERRAINPULSE,THUNDER,THUNDERBOLT,THUNDERPUNCH,UPROAR,WATERPULSE,WHIRLPOOL,WILDCHARGE,WORKUP,ZENHEADBUTT
EggMoves = AFTERYOU,BELCH,CHARM,COUNTER,CURSE,DOUBLEEDGE,FISSURE,GASTROACID,LICK,POWERUPPUNCH,WHIRLWIND
EggGroups = Monster
HatchSteps = 10240
Height = 2.1
Weight = 460.0
Color = Black
Shape = Bipedal
Habitat = Mountain
Category = Sleeping
Pokedex = Snorlax's typical day consists of nothing more than eating and sleeping. It is such a docile Pokémon that there are children who use its big belly as a place to play.
Generation = 1
WildItemCommon = LEFTOVERS
WildItemUncommon = LEFTOVERS
WildItemRare = LEFTOVERS
#-------------------------------
[NIDORANfE]
Name = Nidoran♀
Types = POISON
BaseStats = 55,47,52,41,40,40
GenderRatio = AlwaysFemale
GrowthRate = Parabolic
BaseExp = 55
EVs = HP,1
CatchRate = 235
Happiness = 50
Abilities = POISONPOINT,RIVALRY
HiddenAbilities = HUSTLE
Moves = 1,GROWL,1,POISONSTING,5,SCRATCH,10,TAILWHIP,15,FURYSWIPES,20,TOXICSPIKES,25,DOUBLEKICK,30,BITE,35,HELPINGHAND,40,TOXIC,45,FLATTER,50,CRUNCH,55,EARTHPOWER
TutorMoves = AERIALACE,ATTRACT,BEATUP,BLIZZARD,BODYSLAM,CHARM,CRUNCH,CUT,DIG,DOUBLETEAM,EARTHPOWER,ENDURE,FACADE,FOCUSENERGY,HELPINGHAND,HIDDENPOWER,ICEBEAM,IRONTAIL,POISONJAB,PROTECT,RAINDANCE,REST,ROCKSMASH,ROUND,SHADOWCLAW,SHOCKWAVE,SLEEPTALK,SLUDGEBOMB,SNORE,STRENGTH,SUBSTITUTE,SUNNYDAY,SWAGGER,THIEF,THUNDER,THUNDERBOLT,TOXIC,TOXICSPIKES,VENOMDRENCH,VENOSHOCK,WATERPULSE
EggMoves = BEATUP,CHARM,COUNTER,DISABLE,FOCUSENERGY,POISONFANG,POISONTAIL,SKULLBASH,SUPERSONIC,TAKEDOWN,VENOMDRENCH
EggGroups = Monster,Field
HatchSteps = 5120
Offspring = NIDORANfE,NIDORANmA
Height = 0.4
Weight = 7.0
Color = Blue
Shape = Quadruped
Habitat = Grassland
Category = Poison Pin
Pokedex = Its highly toxic barbs are thought to have developed as protection for this small-bodied Pokémon. When enraged, it releases a horrible toxin from its horn.
Generation = 1
Evolutions = NIDORINA,Level,16
#-------------------------------
[NIDORINA]
Name = Nidorina
Types = POISON
BaseStats = 70,62,67,56,55,55
GenderRatio = AlwaysFemale
GrowthRate = Parabolic
BaseExp = 128
EVs = HP,2
CatchRate = 120
Happiness = 50
Abilities = POISONPOINT,RIVALRY
HiddenAbilities = HUSTLE
Moves = 1,GROWL,1,POISONSTING,1,SCRATCH,1,TAILWHIP,15,FURYSWIPES,22,TOXICSPIKES,29,DOUBLEKICK,36,BITE,43,HELPINGHAND,50,TOXIC,57,FLATTER,64,CRUNCH,71,EARTHPOWER
TutorMoves = AERIALACE,ATTRACT,BEATUP,BLIZZARD,BODYSLAM,CHARM,CRUNCH,CUT,DIG,DOUBLETEAM,EARTHPOWER,ENDURE,FACADE,FOCUSENERGY,HELPINGHAND,HIDDENPOWER,ICEBEAM,IRONTAIL,POISONJAB,PROTECT,RAINDANCE,REST,ROCKSMASH,ROUND,SHADOWCLAW,SHOCKWAVE,SLEEPTALK,SLUDGEBOMB,SNORE,STOMPINGTANTRUM,STRENGTH,SUBSTITUTE,SUNNYDAY,SWAGGER,THIEF,THUNDER,THUNDERBOLT,TOXIC,TOXICSPIKES,VENOMDRENCH,VENOSHOCK,WATERPULSE
EggGroups = Monster,Field
HatchSteps = 5120
Height = 0.8
Weight = 20.0
Color = Blue
Shape = Quadruped
Habitat = Grassland
Category = Poison Pin
Pokedex = When it is with its friends or family, its barbs are tucked away to prevent injury. It appears to become nervous if separated from the others.
Generation = 1
Evolutions = NIDOQUEEN,Item,MOONSTONE
#-------------------------------
[NIDOQUEEN]
Name = Nidoqueen
Types = POISON,GROUND
BaseStats = 90,92,87,76,75,85
GenderRatio = AlwaysFemale
GrowthRate = Parabolic
BaseExp = 253
EVs = HP,3
CatchRate = 45
Happiness = 50
Abilities = POISONPOINT,RIVALRY
HiddenAbilities = SHEERFORCE
Moves = 0,SUPERPOWER,1,SLUDGEWAVE,1,SUPERPOWER,1,FURYSWIPES,1,TOXICSPIKES,1,DOUBLEKICK,1,BITE,1,HELPINGHAND,1,TOXIC,1,FLATTER,1,CRUNCH,1,EARTHPOWER,1,GROWL,1,POISONSTING,1,SCRATCH,1,TAILWHIP
TutorMoves = AERIALACE,ATTRACT,AVALANCHE,BEATUP,BLIZZARD,BODYPRESS,BODYSLAM,BRICKBREAK,BULLDOZE,CHARM,CRUNCH,CUT,DIG,DOUBLETEAM,DRAGONPULSE,DRILLRUN,EARTHPOWER,EARTHQUAKE,ENDURE,FACADE,FIREBLAST,FIREPUNCH,FLAMETHROWER,FLING,FOCUSBLAST,FOCUSENERGY,FOCUSPUNCH,GIGAIMPACT,HELPINGHAND,HEX,HIDDENPOWER,HIGHHORSEPOWER,HYPERBEAM,ICEBEAM,ICEPUNCH,ICYWIND,IRONTAIL,MEGAKICK,MEGAPUNCH,MUDSHOT,OUTRAGE,PAYDAY,POISONJAB,PROTECT,RAINDANCE,REST,ROAR,ROCKBLAST,ROCKCLIMB,ROCKSLIDE,ROCKSMASH,ROCKTOMB,ROUND,SANDSTORM,SANDTOMB,SCORCHINGSANDS,SHADOWBALL,SHADOWCLAW,SHOCKWAVE,SLEEPTALK,SLUDGEBOMB,SLUDGEWAVE,SNORE,STEALTHROCK,STOMPINGTANTRUM,STONEEDGE,STRENGTH,SUBSTITUTE,SUNNYDAY,SUPERPOWER,SURF,SWAGGER,TAUNT,THIEF,THROATCHOP,THUNDER,THUNDERBOLT,THUNDERPUNCH,TORMENT,TOXIC,TOXICSPIKES,UPROAR,VENOMDRENCH,VENOSHOCK,WATERPULSE,WHIRLPOOL
EggGroups = Monster,Field
HatchSteps = 5120
Height = 1.3
Weight = 60.0
Color = Blue
Shape = BipedalTail
Habitat = Grassland
Category = Drill
Pokedex = It is adept at sending foes flying with harsh tackles using its tough, scaly body. This Pokémon is at its strongest when it is defending its young.
Generation = 1
#-------------------------------
[NIDORANmA]
Name = Nidoran♂
Types = POISON
BaseStats = 46,57,40,50,40,40
GenderRatio = AlwaysMale
GrowthRate = Parabolic
BaseExp = 55
EVs = ATTACK,1
CatchRate = 235
Happiness = 50
Abilities = POISONPOINT,RIVALRY
HiddenAbilities = HUSTLE
Moves = 1,LEER,1,POISONSTING,5,PECK,10,FOCUSENERGY,15,FURYATTACK,20,TOXICSPIKES,25,DOUBLEKICK,30,HORNATTACK,35,HELPINGHAND,40,TOXIC,45,FLATTER,50,POISONJAB,55,EARTHPOWER
TutorMoves = AMNESIA,ATTRACT,BEATUP,BLIZZARD,BODYSLAM,CUT,DIG,DOUBLETEAM,DRILLRUN,EARTHPOWER,ENDURE,FACADE,FOCUSENERGY,HELPINGHAND,HIDDENPOWER,ICEBEAM,IRONTAIL,POISONJAB,PROTECT,RAINDANCE,REST,ROCKSMASH,ROUND,SHADOWCLAW,SHOCKWAVE,SLEEPTALK,SLUDGEBOMB,SMARTSTRIKE,SNORE,STRENGTH,SUBSTITUTE,SUNNYDAY,SWAGGER,THIEF,THUNDER,THUNDERBOLT,TOXIC,TOXICSPIKES,VENOMDRENCH,VENOSHOCK,WATERPULSE
EggMoves = AMNESIA,BEATUP,CONFUSION,COUNTER,DISABLE,HEADSMASH,HORNDRILL,POISONTAIL,SUCKERPUNCH,SUPERSONIC,TAKEDOWN,THRASH,VENOMDRENCH
EggGroups = Monster,Field
HatchSteps = 5120
Offspring = NIDORANfE,NIDORANmA
Height = 0.5
Weight = 9.0
Color = Purple
Shape = Quadruped
Habitat = Grassland
Category = Poison Pin
Pokedex = The male Nidoran has developed muscles that freely move its ears in any direction. Even the slightest sound does not escape this Pokémon's notice.
Generation = 1
Evolutions = NIDORINO,Level,16
#-------------------------------
[NIDORINO]
Name = Nidorino
Types = POISON
BaseStats = 61,72,57,65,55,55
GenderRatio = AlwaysMale
GrowthRate = Parabolic
BaseExp = 128
EVs = ATTACK,2
CatchRate = 120
Happiness = 50
Abilities = POISONPOINT,RIVALRY
HiddenAbilities = HUSTLE
Moves = 1,LEER,1,POISONSTING,1,PECK,1,FOCUSENERGY,15,FURYATTACK,22,TOXICSPIKES,29,DOUBLEKICK,36,HORNATTACK,43,HELPINGHAND,50,TOXIC,57,FLATTER,64,POISONJAB,71,EARTHPOWER
TutorMoves = AMNESIA,ATTRACT,BEATUP,BLIZZARD,BODYSLAM,CUT,DIG,DOUBLETEAM,DRILLRUN,EARTHPOWER,ENDURE,FACADE,FOCUSENERGY,HELPINGHAND,HIDDENPOWER,ICEBEAM,IRONTAIL,POISONJAB,PROTECT,RAINDANCE,REST,ROCKSMASH,ROUND,SHADOWCLAW,SHOCKWAVE,SLEEPTALK,SLUDGEBOMB,SMARTSTRIKE,SNORE,STOMPINGTANTRUM,STRENGTH,SUBSTITUTE,SUNNYDAY,SWAGGER,THIEF,THUNDER,THUNDERBOLT,TOXIC,TOXICSPIKES,VENOMDRENCH,VENOSHOCK,WATERPULSE
EggGroups = Monster,Field
HatchSteps = 5120
Height = 0.9
Weight = 19.5
Color = Purple
Shape = Quadruped
Habitat = Grassland
Category = Poison Pin
Pokedex = Its horn is harder than a diamond. If it senses a hostile presence, all the barbs on its back bristle up at once, and it challenges the foe with all its might.
Generation = 1
Evolutions = NIDOKING,Item,MOONSTONE
#-------------------------------
[NIDOKING]
Name = Nidoking
Types = POISON,GROUND
BaseStats = 81,102,77,85,85,75
GenderRatio = AlwaysMale
GrowthRate = Parabolic
BaseExp = 253
EVs = ATTACK,3
CatchRate = 45
Happiness = 50
Abilities = POISONPOINT,RIVALRY
HiddenAbilities = SHEERFORCE
Moves = 0,MEGAHORN,1,SLUDGEWAVE,1,MEGAHORN,1,FURYATTACK,1,TOXICSPIKES,1,DOUBLEKICK,1,HORNATTACK,1,HELPINGHAND,1,TOXIC,1,FLATTER,1,POISONJAB,1,EARTHPOWER,1,LEER,1,POISONSTING,1,PECK,1,FOCUSENERGY
TutorMoves = AMNESIA,ATTRACT,AVALANCHE,BEATUP,BLIZZARD,BODYPRESS,BODYSLAM,BRICKBREAK,BULLDOZE,CUT,DIG,DOUBLETEAM,DRAGONPULSE,DRILLRUN,EARTHPOWER,EARTHQUAKE,ENDURE,FACADE,FIREBLAST,FIREPUNCH,FLAMETHROWER,FLING,FOCUSBLAST,FOCUSENERGY,FOCUSPUNCH,GIGAIMPACT,HELPINGHAND,HEX,HIDDENPOWER,HIGHHORSEPOWER,HYPERBEAM,ICEBEAM,ICEPUNCH,ICYWIND,IRONTAIL,MEGAHORN,MEGAKICK,MEGAPUNCH,MUDSHOT,OUTRAGE,PAYDAY,POISONJAB,PROTECT,RAINDANCE,REST,ROAR,ROCKBLAST,ROCKCLIMB,ROCKSLIDE,ROCKSMASH,ROCKTOMB,ROUND,SANDSTORM,SANDTOMB,SCORCHINGSANDS,SHADOWBALL,SHADOWCLAW,SHOCKWAVE,SLEEPTALK,SLUDGEBOMB,SLUDGEWAVE,SMARTSTRIKE,SNORE,STEALTHROCK,STOMPINGTANTRUM,STONEEDGE,STRENGTH,SUBSTITUTE,SUNNYDAY,SUPERPOWER,SURF,SWAGGER,TAUNT,THIEF,THROATCHOP,THUNDER,THUNDERBOLT,THUNDERPUNCH,TORMENT,TOXIC,TOXICSPIKES,UPROAR,VENOMDRENCH,VENOSHOCK,WATERPULSE,WHIRLPOOL
EggGroups = Monster,Field
HatchSteps = 5120
Height = 1.4
Weight = 62.0
Color = Purple
Shape = BipedalTail
Habitat = Grassland
Category = Drill
Pokedex = A Nidoking's thick tail packs enormously destructive power capable of toppling a metal transmission tower. Once it goes on a rampage, there is no stopping it.
Generation = 1
#-------------------------------"""

### UNCOMMENT THIS TO TEST USING THE TEXT ABOVE, AND THEN COMMENT OUT THE "GRAB STRINGS" & "SAVE TO FILE" SECTIONS BELOW:
# string_list = my_file.split("\n")

### ==================
### ==  READ ME!!!  ==
### ==================
# How to use this script:
# Set the Desired Stat Total variables below.
# Overwrite the /PBS/Pokemon.txt with the original values from the source https://github.com/PkmnDevs/pokemon-essentials (copy all, paste all).
# Use Python v3.10 to run this file. ( $ py PBS\xBaseStatScript-Semple.py )

# Desired Stat Totals:
CHAIN0_BASIC = 530

CHAIN1_BASIC = 320
CHAIN1_STAGE1 = 545
CHAIN1_EVO1 = 28 # Level to evolve from Basic to Stage 1

CHAIN2_BASIC = 290
CHAIN2_STAGE1 = 420
CHAIN2_STAGE2 = 580
CHAIN2_EVO1 = 23 # Level to evolve from Basic to Stage 1
CHAIN2_EVO2 = 40 # Level to evolve from Stage 1 to Stage 2


# ==================
# == GRAB STRINGS ==
# ==================
## See line ~380 above for testing

my_file = open("./PBS/pokemon.txt")
string_list = my_file.readlines()
my_file.close()

# ==================
# ==  VARIABLES   ==
# ==================

name = "" # Current pokemon name from file
newEvoLevel = 0 # New evolution level based on getEvolutionInfo() and Variables above.
uniqueEvos = [] # Store all pokemon names that have unique evolution method. Their evolutions need to be looked-into/updated manually.
cantFind = [] # Store all pokemon names that can't be found in API. Their base stats and evolutions need to be looked-into/updated manually.
skipPkmn = False # If a pkmn name is not in the API, we need to skip lines of the file until we reach the next "InternalName ="
newFileContents = "" # I guess I have to build the new file here?

# =====================
# ==  GET PKMN INFO  ==
# =====================

# Use PokeAPI to:
# - find out how many times a pokemon evolves
#       use "name" against "https://pokeapi.co/api/v2/pokemon-species/{name}"
#       find "evolution chain" url
#       get answer from "https://pokeapi.co/api/v2/evolution-chain/{number}/"
#           which seems to be a chain of "EvolvesTo[1 item]"s
# - find out which stage in the evolution the current pkmn is (Basic, Stage 1, Stage 2)
def getEvolutionInfo(name):
    name = name.lower()
    evoStages = ["BASIC", "STAGE1", "STAGE2"]
    evoStage = ""

    headers = {"Accept": "application/json"}

    # Get pokemon species's json
    pokemonSpeciesURL = "https://pokeapi.co/api/v2/pokemon-species/"
    pokemonSpeciesURL = pokemonSpeciesURL + name
    r = requests.get(url = pokemonSpeciesURL, headers = headers)
    if r.status_code == 404:
        print("Cannot find [" + name + "] in API.")
        cantFind.append(name)
        global skipPkmn
        skipPkmn = True # Skip the rest of the lines of the file until we get to the next pkmn.
        print("\n==============================================\n")
        return ("get","gud")
    data = r.json()

    # Get evolution chain json
    evolutionChainURL = data["evolution_chain"]["url"]
    r = requests.get(url = evolutionChainURL, headers = headers)
    data = r.json()

    # Note the Basic pkmn in evolution chain
    pokemonChain = data["chain"]
    evoChain = 0
    firstSpecies = pokemonChain["species"]["name"]
    if firstSpecies == name : # If it is the pkmn we are searching with, mark its evoStage as BASIC
        evoStage = evoStages[evoChain]
    evolvesTo = pokemonChain["evolves_to"] # "evolves_to" is an empty array if there are no evolutions after current stage.

    # If there is an evolution, check it. (Stage 1)
    while (len(evolvesTo) > 0):
        evolvesTo = evolvesTo[0]
        evoChain = evoChain+1
        speciesName = evolvesTo["species"]["name"]
        if speciesName == name : # If this is the pokemon we are searching for, mark its evoStage as STAGE1 or STAGE2 depending on loop iteration.
            evoStage = evoStages[evoChain]

        # Repeat loop to check if there is another evolution. (Stage 2)
        evolvesTo = evolvesTo["evolves_to"]
    return(evoStage, evoChain)


# ==================
# ==  CALC STATS  ==
# ==================

print("")

for x in string_list:

    if x.startswith("Name ="): # Get Pokemon's name, evolution chain, and evolution stage.
        words = x.split()
        name = words[-1]
        print(name)
        skipPkmn = False
        evoStage, evoChain = getEvolutionInfo(name)

    if skipPkmn == False and x.startswith("BaseStats = "): # Edit the string containing "BaseStats" to use the new, more balanced, base stats. Depends on evoChain and evoStage.
        print("EvoStage (Can be BASIC, STAGE1, STAGE2): " + evoStage)
        print("Total number of evolutions in chain (Can be 0, 1, 2): " + str(evoChain))
        newEvoLevel = 0

        txt = x.split()
        stats = [int(s) for s in txt[-1].split(",") if s.isdigit()] # Get base stats as Ints
        statsTemp = stats.copy() # Some python memory storage thing is F-ing me over. Just gonna use this line a lot instead of learning Python.
        print("\noriginal baseStats:\nHP, Atk, Def, Spe, SpA, SpD")
        print(", ".join(map(str, statsTemp)))

        statsTemp = stats.copy()
        statTotal = sum(statsTemp) # Get current stat total
        print("original statTotal: {0}".format(statTotal))

        match evoChain: # Check how many Pkmn are in the evoultion chain.
            case 0:
                if statTotal < CHAIN0_BASIC: # Buff Weaker Pkmn
                    stats = [(stat + ((CHAIN0_BASIC - statTotal) // 6)) for stat in stats]
                elif statTotal > CHAIN0_BASIC: # Nerf Stronger Pkmn
                    stats = [(stat - ((statTotal - CHAIN0_BASIC) // 12)) for stat in stats]
            case 1:
                match evoStage:
                    case "BASIC":
                        if statTotal < CHAIN1_BASIC: # Buff Weaker Pkmn
                            stats = [(stat + ((CHAIN1_BASIC - statTotal) // 6)) for stat in stats]
                        elif statTotal > CHAIN1_BASIC: # Nerf Stronger Pkmn
                            stats = [(stat - ((statTotal - CHAIN1_BASIC) // 12)) for stat in stats]
                        newEvoLevel = CHAIN1_EVO1 # Value to set Pkmn's evolution level to
                    case "STAGE1":
                        if statTotal < CHAIN1_STAGE1: # Buff Weaker Pkmn
                            stats = [(stat + ((CHAIN1_STAGE1 - statTotal) // 6)) for stat in stats]
                        elif statTotal > CHAIN1_STAGE1: # Nerf Stronger Pkmn
                            stats = [(stat - ((statTotal - CHAIN1_STAGE1) // 12)) for stat in stats]
            case 2:
                match evoStage:
                    case "BASIC":
                        if statTotal < CHAIN2_BASIC: # Buff Weaker Pkmn
                            stats = [(stat + ((CHAIN2_BASIC - statTotal) // 6)) for stat in stats]
                        elif statTotal > CHAIN2_BASIC: # Nerf Stronger Pkmn
                            stats = [(stat - ((statTotal - CHAIN2_BASIC) // 12)) for stat in stats]
                        newEvoLevel = CHAIN2_EVO1
                    case "STAGE1":
                        if statTotal < CHAIN2_STAGE1: # Buff Weaker Pkmn
                            stats = [(stat + ((CHAIN2_STAGE1 - statTotal) // 6)) for stat in stats]
                        elif statTotal > CHAIN2_STAGE1: # Nerf Stronger Pkmn
                            stats = [(stat - ((statTotal - CHAIN2_STAGE1) // 12)) for stat in stats]
                        newEvoLevel = CHAIN2_EVO2
                    case "STAGE2":
                        if statTotal < CHAIN2_STAGE2: # Buff Weaker Pkmn
                            stats = [(stat + ((CHAIN2_STAGE2 - statTotal) // 6)) for stat in stats]
                        elif statTotal > CHAIN2_STAGE2: # Nerf Stronger Pkmn
                            stats = [(stat - ((statTotal - CHAIN2_STAGE2) // 12)) for stat in stats]

        # Ensure no stats go below 1        
        for stat in stats:
            if stat <= 0:
                stat = 1

        statsTemp = stats.copy()
        x = "BaseStats = " + ", ".join(map(str, statsTemp)) + "\n"
        # print("test output: " + x + "\n") # The new string needs to ouput like: BaseStats = 45,49,49,45,65,65

        statsTemp = stats.copy()
        print("\nnew baseStats:\nHP, Atk, Def, Spe, SpA, SpD")
        print(", ".join(map(str, statsTemp)))

        statsTemp = stats.copy()
        statTotal = sum(statsTemp)
        print("new statTotal: {0}".format(statTotal))

        if newEvoLevel == 0:
            print("==============================================\n")

    if skipPkmn == False and x.startswith("Evolutions = "): # Set new evolve level
        print("\noriginal evolution method:\n" + x)
        if newEvoLevel != 0:
            # print("newEvoLevel: {0}".format(newEvoLevel))
            txt = x.split()
            evoMethod = txt[-1].split(",") # Grab and parse the evolution method {Pkmn to evlolve to, method of evolution, parameter like level or helditem or whatever}
            if any(method in evoMethod for method in ["Level", "Happiness", "Trade"]) and (len(evoMethod) == 3):
                evoMethod[1] = "Level"
                evoMethod[2] = "{0}".format(newEvoLevel)
                x = "Evolutions = " + ",".join(evoMethod) + "\n"
                print("new evolution method:\n" + x + "\n")
            else:
                uniqueEvos.append(name)
                print("The original evolution method is unique. Go edit it manually, beautiful.\n")
            print("==============================================\n")

    newFileContents = newFileContents + x

print("Pkmn that need their evolution method looked into, manually:")
print(uniqueEvos)

print("Pkmn that were not in the API and need stats/evolutions to be looked into, manually:")
print(cantFind)


# ==================
# == SAVE TO FILE ==
# ==================

my_file = open("./PBS/pokemon.txt", "w")
new_file_contents = "".join(newFileContents)
my_file.write(new_file_contents)
my_file.close()

## Saving the arrays of pkmn that need to be looked into manually.
content = []
content.append("Pkmn that need their evolution method looked into, manually:\n")
content.append(uniqueEvos)
content.append("\nPkmn that were not in the API and need stats/evolutions to be looked into, manually:\n")
content.append(cantFind)
my_file = open("./PBS/pokemonManualEditing.txt", "w")
new_file_contents = "".join([str(elem) for elem in content]) # Efficient code..? What's that?
my_file.write(new_file_contents)
my_file.close()
