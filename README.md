# Pokemon Accord:

Creating our own game: Multiple Small Regions each with their own protagonist that meet up in the end.

### Plugins used

<!-- [Gen 8 Project](https://reliccastle.com/threads/3829/)  
[Following Pokemon EX](https://reliccastle.com/resources/516/)  
[Elite Battle: DX](https://luka-sj.com/res/ebdx)   -->
[Gen 8 Move Animation Project](https://www.pokecommunity.com/showthread.php?t=446303)  
[FL Unreal Time](https://www.pokecommunity.com/showthread.php?t=285831)  
<!-- [EVs and IVs Summary](https://reliccastle.com/resources/703/)  
[Relearn Moves](https://reliccastle.com/resources/933/)  

### Assets

[Voltseon's Pause Menu](https://reliccastle.com/resources/692/)  
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

**Resources:**  
[Wiki](https://essentialsdocs.fandom.com/wiki/Essentials_Docs_Wiki)  
[Forum](https://reliccastle.com)  
[Reddit](https://www.reddit.com/r/PokemonRMXP/)  
[Youtube Tutorial](https://www.youtube.com/watch?v=mlnzaEhH5cI&list=PLuIp7Uf7pllmpcFOHbj4r8cVQYywpRZB5)  

## Workflow

There will be a _master_ branch and a _develop_ branch.

_develop_ will be were we push up changes.

Periodically, we will force all Work In Progress branches into _develop_ and then change all the _MapInfo_ (names, grouping) in the dev branch and push it to master.

================
==  __WORKFLOW__  ==
================

1. Create a new branch off of _develop_. Naming Pattern: `your-first-name/whatever-you-want`

2. If you are going to edit a new map, find a blank map in the list. Note it's ID. Post in the Map Claiming discord channel: `Claiming MapXXX for <map name> [in <parent map name + ID>]` (Make sure no one else has already claimed it!)

3. Then, when you are going to edit a WIP map, post a comment in Map Communication discord channel: `Working on MapXXX".` (Make sure no one else is also working on it!)

4. Make your edits. __DO NOT MOVE THE MAPS AROUND__. Commit and Push up changes to your own branch as much as you want.

5. When you are ready to push your branch to dev, first Pull from dev. (In Github Remote Desktop App: While on your branch, click on the "Branch" tab in the taskbar. Select "Compare to Branch". Select the dev branch. Choose to make a merge commit to pull dev into your branch. If there are merge conflicts, they should only be on MapInfo.rxdata and/or Systems.rxdata. Select to keep your branch's version for both resolution steps.

6. Push your branch up to the origin and create a Pull Request to merge your branch into the dev branch.

7. Edit your comment step (3) to say `NOT working on MapXXX` so that others know they can touch it now.

Periodically steps 5 and 6 may be forced through even when you're not ready, so that dev can contain all WIP maps, and then we can name and group  some for:

8. Merge the dev branch into the master branch. Keep all the dev MapInfo.


# Pokémon Essentials

Based on Essentials v20.

You can build your fangame on top of a fork of this repository. Doing so will let you update your fangame with improvements made to this repo as soon as they are made.

## Pulling in updates to PokemonAccord

1. On Github dev branch, "fetch" the changes from the "upstream" to pull in new updates.
2. Then pull the changes of the dev branch into the pkmn-accord-dev branch.

## Usage

1. Fork this repo.
2. Get a copy of Essentials v20 (a download link cannot be provided here).
3. Clone your forked repo into the Essentials v19 folder, replacing the existing files with the ones from the repo.

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
