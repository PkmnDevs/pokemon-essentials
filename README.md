# Pokemon Accord:

Creating our own game: Multiple Small Regions each with their own protagonist that meet up in the end.

## WARNING !!!!! !!!!! !!!!!

I broke something when adding plugins I guess :shrug: . The branch "emily-initialize-2" lets you load up for the first time and start a new game. But the branch "ryan-adding-plugins" will crash when you hit new game...\n
Emily's branch was built off of Ryan's branch at one point, so whatever he added after that point is the thing that caused the issue. I need to look into it later.\n
BUT, in the meantime, since everything worked fine on Ryan's computer, I realized the fact that he had a saved game was somehow bypassing the error?\n
So the workaround for now is to:

1) In GitHub desktop, click the menu-bar drop-down for "Repository".

2) Select "Show in Explorer".

3) Copy the folder called "Pokemon Accord".

4) Now, in the search bar, type in %appdata%

5) This should bring you inside a folder called your "Roaming" folder.

6) Paste the folder you copied into here. This is where the saved games live, so now you will have a dummy saved-game and should be able to bypass the error!

### Plugins used

[Gen 8 Project](https://reliccastle.com/threads/3829/)  
[Following Pokemon EX](https://reliccastle.com/resources/516/)
[Gen 8 Move Animation Project](https://www.pokecommunity.com/showthread.php?t=446303)  
[FL Unreal Time](https://www.pokecommunity.com/showthread.php?t=285831)  
[EVs and IVs Summary](https://reliccastle.com/resources/703/)  
[Relearn Moves](https://reliccastle.com/resources/933/)  
<!-- [Elite Battle: DX](https://luka-sj.com/res/ebdx)   - This is super cool but was causing a lot of strange errors. Might be best to avoid using it.  -->

### Assets

<!-- [Voltseon's Pause Menu](https://reliccastle.com/resources/692/)  
[Ekat's Public Gen 3 Tilesets](https://reliccastle.com/threads/3669/)  
[The Darkest Resource Pack](https://reliccastle.com/resources/897/)  
[Ghosts of Knowledge Knesho Resource Pack](https://reliccastle.com/resources/900/)  
[Platinum Battle Transitions](https://reliccastle.com/resources/898/)  
[Pokeball Animations](https://reliccastle.com/resources/909/)   -->
[ENL's Pre-Looped Music Library](https://reliccastle.com/resources/663/)  
[Kyle Dove Tileset](https://reliccastle.com/resources/15/)  

### Developer Tools

[Trello](https://trello.com/pkmndevs)  
[Miro](https://miro.com/welcome/eDN0TW1zSmtiZ1A5NUtiYjBKaUNxZnlzYU9EUlBxaHhGZmpiTk42RjVIbVFrd2J0M0RUMjVZd1NBTUpWWlpYY3wzNDU4NzY0NTIyNzcxODAzNzE4?invite_link_id=295639398454)  
[How to contribute to our project](https://youtu.be/z1mddjl06Bc)
Any custom images you add __MUST__ be compressed in [TinyPNG](https://tinypng.com/). This strips the image of some "image profile" thing that puts annoying warnings in the console.

**Resources:**  
[Wiki](https://essentialsdocs.fandom.com/wiki/Essentials_Docs_Wiki)  
[Forum](https://reliccastle.com)  
[Reddit](https://www.reddit.com/r/PokemonRMXP/)  
[Youtube Tutorial](https://www.youtube.com/watch?v=mlnzaEhH5cI&list=PLuIp7Uf7pllmpcFOHbj4r8cVQYywpRZB5)  

## Workflow

__Branches:__

* _master_ :: This is a branch we do not intend to manage. It is from the repo we forked: Maruno's. Occasionally we will pull Maruno's changes down into _pkmn-accord-dev_. (Well, pull changes into a diff branch first, test what broke, then push to _pkmn-accord-dev_)

* _dev_ :: Same as above, but with newer changes from Maruno. Occasionally we will pull down this branch into _pkmn-accord-dev_. (Same clarification as above).

* _POKEMON\_ACCORD_ :: The master branch. Should be a stable build of the game that anyone can play. (Just a copy of _pkmn-accord-dev_ when it's in best condition). Should tag this branch with release version numbers when we have significant progress on the game.

* _pkmn-accord-dev_ :: The most up to date changes that are hopefully in decent condition. May sometimes be in bad condition as we use this branch to organize/name all our WIP Maps. Otherwise, fingers crossed that it is stable. Should get pushed up to _POKEMON\_ACCORD_ when we want to make a "new release".

* _{your name}/{anything}_ :: These branches are your personal branches. Make all the changes you want. Just don't fuck up the Map organization! This will get pushed into _pkmn-accord-dev_ either when the changes made are ready, or when we need to do some map organization.

Periodically, we will force all Work In Progress branches into _develop_ and then change all the _MapInfo_ (names, grouping) in the dev branch and push it to master.

================
==  __WORKFLOW__  ==
================

1. Create a new branch off of _pkmn-accord-dev_. Naming Pattern: `your-first-name/whatever-you-want`

2. If you are going to edit a new map, find a blank map in the list. Note it's ID. Post in the Map Claiming discord channel: `Claiming MapXXX for <map name> [in <parent map ID + name>]` (Make sure no one else has already claimed it! Ex: "Claiming Map069 for PokeCenter in Map050 - Pallet Town")

3. Make your edits. __DO NOT MOVE THE MAPS AROUND OR NAME THEM__. (Like, in the editor, do not drag them and organize them) (However, you CAN change the Tileset, Width/Height, and BGM/BGS in the Map Properties.). Commit and Push up changes to your own branch as much as you want.

4. When you are ready to push your personal branch to _pkmn-accord-dev_, first Pull from _pkmn-accord-dev_. (In Github Remote Desktop App: While on your branch, click on the "Branch" tab in the taskbar. Select "Compare to Branch". Select the _pkmn-accord-dev_ branch. Choose to make a merge commit to pull dev into your branch. If there are merge conflicts, they should only be on MapInfo.rxdata and/or Systems.rxdata. Select to keep your branch's version for both resolution steps.)

5. After that, push your personal branch up to the origin and create a Pull Request to merge your personal branch into the _pkmn-accord-dev_ branch.

Periodically steps 4 and 5 may be forced through even when you're not ready, so that _pkmn-accord-dev_ branch can contain all WIP maps, and then we can name and group some the sake of organization. To help keep communication clear on who is messing around with what map, we may want to make these discord posts: (Imagine the scenario where Emily made a map, but Ryan wants to fix some broken NPC dialogue on it while he has time. If they both edit the map on different branches, everything will break. So Emily has to either let Ryan make edits on her personal branch, or they need to take turns and not edit at the same time. These steps are to help enforce the latter, when needed.)

6. When you are going to edit a WIP map, post a comment in Map Communication discord channel: `Working on MapXXX".`

7. Edit your comment step (3) to say `NOT working on MapXXX` so that others know they can touch it now.

When we have a stable build in _pkmn-accord-dev_, we will push it to our master branch: _POKEMON\_ACCORD_

8. Merge the _pkmn-accord-dev_ branch into the _POKEMON\_ACCORD_ branch. Keep all the dev MapInfo.

__WHEN PULLING IN LATEST MARUNO CHANGES:__

1. Navigate to "our" _dev_ branch.

2. Sync it with Maruno's _dev_ branch.

3. Create a new branch off of _pkmn-accord-dev_

4. Pull "our" _dev_ branch into the new branch you just made.

5. Play-Test changes.

6. If it's good stuff, push your new branch up into _pkmn-accord-dev_.

====================
==  __From Maruno:__  ==
====================

# Pokémon Essentials

Based on Essentials v20.1.

You can build your fangame on top of a fork of this repository. Doing so will let you update your fangame with improvements made to this repo as soon as they are made.

## Pulling in updates to PokemonAccord

1. On Github dev branch, "fetch" the changes from the "upstream" to pull in new updates.
2. Then pull the changes of the dev branch into the pkmn-accord-dev branch.

## Usage

1. Fork this repo.
2. Get a copy of Essentials v20.1 (a download link cannot be provided here).
3. Clone your forked repo into the Essentials v20.1 folder, replacing the existing files with the ones from the repo.

From here, you can edit this project to turn it into your fangame/develop mods. When this repo is updated, you can pull the changes to update your fork and get the updates into your fangame/modding environment.

## Scripts

The scripts no longer live in the Scripts.rxdata file. They have been extracted into separate files and placed in the Data/Scripts/ folder (and subfolders within). This makes it easier to work with other people and keep track of changes.

The scripts are loaded into the game alphanumerically, starting from the top folder (Data/Scripts/) and going depth-first. That is, all scripts in a given folder are loaded, and then each of its subfolder is checked in turn (again in alphanumerical order) for files/folders to load/check.

### Extracting and reintegrating scripts

This repo contains two script files in the main folder:

* scripts_extract.rb - Run this to extract all scripts from Scripts.rxdata into individual .rb files (any existing individual .rb files are deleted).
  * Scripts.rxdata is backed up to ScriptsBackup.rxdata, and is then replaced with a version that reads the individual .rb files and does nothing else.
* scripts_combine.rb - Run this to reintegrate all the individual .rb files back into Scripts.rxdata.
  * The individual .rb files are left where they are, but they no longer do anything.

You will need Ruby installed to run these scripts. The intention is to replace these with something more user-friendly.

## Files not in the repo

The .gitignore file lists the files that will not be included in this repo. These are:

* The Audio/, Graphics/ and Plugins/ folders and everything in them.
* Everything in the Data/ folder, except for:
  * The Data/Scripts/ folder and everything in there.
  * Scripts.rxdata (a special version that just loads the individual script files).
* A few files in the main project folder (two of the Game.xxx files, and the RGSS dll file).
* Temporary files.
