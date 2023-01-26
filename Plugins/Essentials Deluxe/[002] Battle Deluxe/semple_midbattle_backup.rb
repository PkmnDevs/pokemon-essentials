# Everything ere is supposed to go in Plugins/Essentials Deluxe/[002] Battle Deluxe/Midbattle_Config.rb
# This file is just a backup for when that file gets updated sometimes. So everything should get duplicated here as well.

##### MID BATTLE SCRIPTS ARE AT THE BOTTOM OF THIS FILE - SEMPLE
# https://www.pokecommunity.com/showthread.php?p=10534994#post10534994


  #-----------------------------------------------------------------------------
  # ^^^ EXAMPLES ^^^
  #
  # vvv  CUSTOM  vvv
  #-----------------------------------------------------------------------------

  ##################################################
  ##########        RIVAL         ##################
  ##################################################

  #-----------------------------------------------------------------------------
  # RIVAL 4 - Water Snake Way
  #-----------------------------------------------------------------------------
  BUTTBUTT4 = {
    "beforeLast_foe" => {
      :speech  => ["My team knows how to work together. You can't beat us!"]
    }
  }

  ##################################################
  ##########     GYM LEADERS      ##################
  ##################################################

  #-----------------------------------------------------------------------------
  # GYM LEADER ASH KETCUM - Oak's Lab
  #-----------------------------------------------------------------------------
  ASH_KETCHUM = {
    "turnCommand" => {
      :playsound  => "Pikachu speaks - Ash dies",
      :text    => "You feel an immense pressure emmanting from the gym leader...",
      :speech  => ["I am Ash Ketchum! From Pallet Town!",
                   "Time to die.  ..For you.  !!"],
      :text_1  => "Ash just turned his hat backwards! This is it! Life or death!"
    },
    "lowhp_foe" => {
      :speech  => ["This is it {1}!",0,"Hit that {1} with everything you've got!"],
      :anim    => [:BULKUP, :Self],
      :playcry => true
    },
    "fainted_foe" => {
      :speech  => ["How can this be happening?!"]
    },
    "afterLast_foe" => {
      :speech  => "Kick his ass, {1}!",
      :playcry => true
    },
    "halfhp_final_foe" => {
      :speech  => ["Daddy, noo!"],
      :text    => "Leader Ash is starting to cry.",
      :playcry => true
    }
  }

  #-----------------------------------------------------------------------------
  # GYM LEADER IVY - Grotto Gym
  #-----------------------------------------------------------------------------
  POISON_IVY = {
    "beforeLast_foe" => {
      :speech  => ["Impressive, but nature always wins. I choose you! Venus!"]
    },
    "mega_foe" => {
      :speech  => ["Scared of a little Sceptile are you? Well that's what you think, but it's not over yet. DIGI-VOLVE!"],
      :anim    => [1,"Shiny"],
      :playcry => true
    },
    "fainted_foe" => {
      :speech  => ["Hmph, only a minor setback."]
    },
    "halfhp_final_foe" => {
      :speech  => ["What if I asked you nicely to give up?"]
    }
  }

  ##################################################
  ##########     ELITE FOUR      ##################
  ##################################################

  #-----------------------------------------------------------------------------
  # ELITE FOUR ROSDALE
  #-----------------------------------------------------------------------------
  ROSDALE = {
    "beforeLast_foe" => {
      :speech  => ["Impressive, but nature always wins. I choose you! Venus!"]
    },
    "mega_foe" => {
      :speech  => ["Scared of a little Sceptile are you? Well that's what you think, but it's not over yet. DIGI-VOLVE!"],
      :anim    => [1,"Shiny"],
      :playcry => true
    },
    "fainted_foe" => {
      :speech  => ["Hmph, only a minor setback."]
    },
    "halfhp_final_foe" => {
      :speech  => ["What if I asked you nicely to give up?"]
    }
  }


  ##################################################
  ##########     MINI BOSSES      ##################
  ##################################################

  #-----------------------------------------------------------------------------
  # EMILY - Route 3
  #-----------------------------------------------------------------------------
  EMILY = {
    "beforeLast_foe" => {
      :speech  => ["There's some Chicken Feets in it for you if you win this, Dovahkiin!"]
    },
    "fainted_foe" => {
      :speech  => ["It's okay Rot, you can rest now (:"]
    }
  }


end

