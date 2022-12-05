# Made this plugin so that as we play test different bosses, we don't have to keep going through game menus
# Simply have an event run a script with one of these functions to get that team!
# Use this example below to see how to add your own teams! Map094 Developer Tools is a good place to put these events.

# EXAMPLE:

# def demoteam20
#     party = []
#     species = [:PIKACHU, :PIDGEOTTO, :KADABRA, :GYARADOS, :DIGLETT, :CHANSEY]
#     species.each do |id|
#       party.push(id) if GameData::Species.exists?(id)
#     end
#     $player.party.clear
#     # Generate Pokémon of each species at level 20
#     party.each do |species|
#       pkmn = Pokemon.new(species, 20)
#       $player.party.push(pkmn)
#       $player.pokedex.register(pkmn)
#       $player.pokedex.set_owned(species)
#       case species
#       when :PIDGEOTTO
#         pkmn.learn_move(:FLY)
#       when :KADABRA
#         pkmn.learn_move(:FLASH)
#         pkmn.learn_move(:TELEPORT)
#       when :GYARADOS
#         pkmn.learn_move(:SURF)
#         pkmn.learn_move(:DIVE)
#         pkmn.learn_move(:WATERFALL)
#       when :DIGLETT
#         pkmn.learn_move(:DIG)
#         pkmn.learn_move(:CUT)
#         pkmn.learn_move(:HEADBUTT)
#         pkmn.learn_move(:ROCKSMASH)
#       when :CHANSEY
#         pkmn.learn_move(:SOFTBOILED)
#         pkmn.learn_move(:STRENGTH)
#         pkmn.learn_move(:SWEETSCENT)
#       end
#       pkmn.record_first_moves
#     end
#     pbMessage(_INTL("Filled party with level 20 demo Pokémon."))
# end

# LEADER IVY - Gym 2 - Grotto Gym
def demoteam23
    party = []
    species = [:BELDUM, :PONYTA, :CHESPIN]
    species.each do |id|
      party.push(id) if GameData::Species.exists?(id)
    end
    $player.party.clear
    # Generate Pokémon of each species at level 20
    party.each do |species|
      pkmn = Pokemon.new(species, 23)
      $player.party.push(pkmn)
      $player.pokedex.register(pkmn)
      $player.pokedex.set_owned(species)
      pkmn.record_first_moves
    end
    pbMessage(_INTL("Filled party with level 23 demo Pokémon."))
end

# LEADER SHINO - Gym 3
def demoteam38
  party = []
  species = [:SANDSHREW, :WARTORTLE, :PIDGEOTTO, :LAMPENT]
  species.each do |id|
    party.push(id) if GameData::Species.exists?(id)
  end
  $player.party.clear
  # Generate Pokémon of each species at level 38
  party.each do |species|
    pkmn = Pokemon.new(species, 38)
    $player.party.push(pkmn)
    $player.pokedex.register(pkmn)
    $player.pokedex.set_owned(species)
    case species
    when :SANDSHREW
      pkmn.learn_move(:BULLDOZE)
      pkmn.learn_move(:SLASH)
      pkmn.learn_move(:DIG)
      pkmn.learn_move(:ROLLOUT)
    when :WARTORTLE
      pkmn.learn_move(:WATERPULSE)
      pkmn.learn_move(:BITE)
      pkmn.learn_move(:RAINDANCE)
      pkmn.learn_move(:AQUATAIL)
    when :PIDGEOTTO
      pkmn.learn_move(:FEATHERDANCE)
      pkmn.learn_move(:TWISTER)
      pkmn.learn_move(:WINGATTACK)
      pkmn.learn_move(:SANDATTACK)
    when :LAMPENT
      pkmn.learn_move(:FIRESPIN)
      pkmn.learn_move(:CONFUSERAY)
      pkmn.learn_move(:HEX)
      pkmn.learn_move(:SHADOWBALL)
    end
    pkmn.record_first_moves
  end
  pbMessage(_INTL("Filled party with level 38 demo Pokémon."))
end


# RIVAL 4 - Water Snake Way
def demoteam75
    party = []
    species = [:CHARIZARD, :VENUSAUR, :BLASTOISE, :CORVIKNIGHT, :JOLTEON, :BRONZONG]
    species.each do |id|
      party.push(id) if GameData::Species.exists?(id)
    end
    $player.party.clear
    # Generate Pokémon of each species at level 75
    party.each do |species|
      pkmn = Pokemon.new(species, 75)
      $player.party.push(pkmn)
      $player.pokedex.register(pkmn)
      $player.pokedex.set_owned(species)
      case species
      when :CHARIZARD
        pkmn.learn_move(:DRAGONBREATH)
        pkmn.learn_move(:SUNNYDAY)
        pkmn.learn_move(:SLASH)
        pkmn.learn_move(:FLAMETHROWER)
      when :VENUSAUR
        pkmn.learn_move(:DOUBLETEAM)
        pkmn.learn_move(:TOXIC)
        pkmn.learn_move(:GIGADRAIN)
        pkmn.learn_move(:SOLARBEAM)
      when :BLASTOISE
        pkmn.learn_move(:SHELLSMASH)
        pkmn.learn_move(:ICEBEAM)
        pkmn.learn_move(:SURF)
        pkmn.learn_move(:SKULLBASH)
      when :CORVIKNIGHT
        pkmn.learn_move(:SCARYFACE)
        pkmn.learn_move(:DRILLPECK)
        pkmn.learn_move(:SWAGGER)
        pkmn.learn_move(:BRAVEBIRD)
      when :JOLTEON
        pkmn.learn_move(:DISCHARGE)
        pkmn.learn_move(:HONECLAWS)
        pkmn.learn_move(:THUNDER)
        pkmn.learn_move(:LASTRESORT)
      when :BRONZONG
        pkmn.learn_move(:PSYCHIC)
        pkmn.learn_move(:METALSOUND)
        pkmn.learn_move(:FUTURESIGHT)
        pkmn.learn_move(:EARTHQUAKE)
      end
      pkmn.record_first_moves
    end
    pbMessage(_INTL("Filled party with level 75 demo Pokémon."))
end