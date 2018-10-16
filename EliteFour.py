## CSCI 1300
## Semester Project
## Adam Grabwoski
## Pokemon Elite Four Challenge


import random
hyper_check = False


### How the player and opponents fight each other. 
def take_turn(player_active, enemy_active, Moves):
    global hyper_check
    print()
    ## Asks the player which move they would like to use from their active pokemon
    print("Which move do you want to use? \n")
    print(" "+player_active["Moves"][0]+"\n", player_active["Moves"][1]+"\n",player_active["Moves"][2]+"\n",player_active["Moves"][3]+"\n")    
    move = str(input("Enter name of move: "))
    print()
    x = True
    while x:
        if move in Moves:
            x = False
        else:
            move = str(input("Enter name of move: ")) 
            print()
            
    ## Player's Turn or enemy's turn first, based on higher speed
    if player_active["Speed"] >= enemy_active["Speed"]:
        player_went = True
        enemy_went = False
        player_turn = True
        print()
        globals()[move](player_turn, player_active, enemy_active)
        
        if enemy_active["HP"]<=0:
            return 
          
    else:
        player_turn = False
        player_went = False
        enemy_went = True
        enemy_move = random.randint(0,3)
        if hyper_check == True:
            print(enemy_active["Name"], "needs a turn to recharge.")
            print()
            hyper_check = False
        else:    
            enemy_move2 = enemy_active["Moves"][enemy_move]
            globals()[enemy_move2](player_turn, player_active, enemy_active)
            if player_active["HP"]<=0:
                return
            
    ## Player's turn if enemy went first
    if player_went != True:
        player_turn = True
        globals()[move](player_turn, player_active, enemy_active)
        if enemy_active["HP"]<=0:
            return 
                
    ## Enemy's Turn if player went first            
    if enemy_went != True:
        player_turn = False
        enemy_move = random.randint(0,3)
        if hyper_check == True:
            print(enemy_active["Name"], "needs a turn to recharge.")
            hyper_check = False
        else:    
            enemy_move2 = enemy_active["Moves"][enemy_move]
            globals()[enemy_move2](player_turn, player_active, enemy_active)
            if player_active["HP"]<=0:
                return
                
    else:
        player_turn = False
        enemy_move = random.randint(0,3)
        if hyper_check == True:
            print(enemy_active["Name"], "needs a turn to recharge.")
            hyper_check = False
        else:    
            enemy_move2 = enemy_active["Moves"][enemy_move]
            globals()[enemy_move2](player_turn, player_active, enemy_active)
            if player_active["HP"]<=0:
                return
        
        
############################################################
##################### Defining all the moves   
############################################################        

### There is a lot of the same here, basically all of the moves that deal damage
### Have a damage calculation, then they check and see if the type of the move 
### matches that of the user for a damage bonus, then compares the type of the move
### to the type(s) of the Pokemon getting hit by the move to see if it deals
### any bonus damage or reduced damage. 
### Finally, some moves have extra effects besides just dealing damage, and
### some moves do not deal damage at all, but rather modify stats in some way.


def Flamethrower(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used Flamethrower!")
        print()
        damage = int(((22*90*player_active["Special"]/enemy_active["Special"])/50)+random.randint(1,6))
        if "Fire" in player_active["Type"]:
            damage = damage*1.5
        if "Rock" in enemy_active["Type"] or"Dragon" in enemy_active["Type"]:
            damage = damage*0.5
            print()
            print("It's not very effective.")
            print()
        if "Grass" in enemy_active["Type"] or "Bug" in enemy_active["Type"] or "Ice" in enemy_active["Type"]:
            damage = damage*2
            print()
            print("It's Super Effective!")
            print()
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from Flamethrower!")
        print()
    else:
        print(enemy_active["Name"], "used Flamethrower!")
        print()
        damage = int(((22*90*enemy_active["Special"]/player_active["Special"])/50)+random.randint(1,6))
        if "Fire" in enemy_active["Type"]:
            damage = damage*1.5
        if "Rock" in player_active["Type"] or"Dragon" in player_active["Type"]:
            damage = damage*0.5
            print()
            print("It's not very effective.")
            print()
        if "Grass" in player_active["Type"] or "Bug" in player_active["Type"] or "Ice" in player_active["Type"]:
            damage = damage*2
            print()
            print("It's Super Effective!")
            print()
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from IceBeam!")

def Slash(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used Slash!")
        print()
        if random.randint(1,100)>=50:
            print("Critical hit!")
            print()
            damage = int(2*((22*70*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
            if "Rock" in enemy_active["Type"]:
                print()
                print("It's not very effective.")
                print()
                damage = damage*0.5
            enemy_active["HP"] = enemy_active["HP"] - damage
            print(enemy_active["Name"], "took", damage, "damage from Slash!")
            print()
        else:
            print(player_active["Name"], "used Slash!")
            print()
            damage = int(((22*70*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
            if "Rock" in enemy_active["Type"]:
                print()
                print("It's not very effective.")
                print()
                damage = damage*0.5
            enemy_active["HP"] = enemy_active["HP"] - damage
            print(enemy_active["Name"], "took", damage, "damage from Slash!") 
            print()
    else:
        if random.randint(1,100)>=50:
            print(enemy_active["Name"], "used Slash!")
            print()
            print("Critical hit!")
            print()
            damage = int(2*((22*70*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
            if "Rock" in player_active["Type"]:
                damage = damage*0.5
                print()
                print("It's not very effective.")
                print()
            player_active["HP"] = player_active["HP"] - damage
            print(player_active["Name"], "took", damage, "damage from Slash!")
            print()
        else:
            print(enemy_active["Name"], "used Slash!")
            print()
            damage = int(((22*70*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
            player_active["HP"] = player_active["HP"] - damage
            print(player_active["Name"], "took", damage, "damage from Slash!")
            print()
            
def FireBlast(player_turn, player_active, enemy_active):
        if player_turn:
            print(player_active["Name"], "used FireBlast!")
            print()
            hit_chance = random.randint(1,100)
            if hit_chance >30:
                damage = int(((22*120*player_active["Special"]/enemy_active["Special"])/50)+random.randint(1,6))
                if "Fire" in player_active["Type"]:
                    damage = damage*1.5
                if "Rock" in enemy_active["Type"] or"Dragon" in enemy_active["Type"]:
                    damage = damage*0.5
                    print()
                    print("It's not very effective.")
                    print()
                if "Grass" in enemy_active["Type"] or "Bug" in enemy_active["Type"] or "Ice" in enemy_active["Type"]:
                    damage = damage*2
                    print()
                    print("It's Super Effective!")
                    print()
                enemy_active["HP"] = enemy_active["HP"] - damage
                print(enemy_active["Name"], "took", damage, "damage from FireBlast!")
                print()
            else:
                print("Uh-oh! Looks like FireBlast missed!")   
                print()
        else:
            print(enemy_active["Name"], "used FireBlast!")
            print()
            hit_chance = random.randint(1,100)
            if hit_chance >30:
                damage = int(((22*120*enemy_active["Special"]/player_active["Special"])/50)+random.randint(1,6))
                if "Fire" in enemy_active["Type"]:
                    damage = damage*1.5
                if "Rock" in player_active["Type"] or"Dragon" in player_active["Type"]:
                    damage = damage*0.5
                    print()
                    print("It's not very effective.")
                    print()
                if "Grass" in player_active["Type"] or "Bug" in player_active["Type"] or "Ice" in player_active["Type"]:
                    damage = damage*2
                    print()
                    print("It's Super Effective!")
                    print()
                player_active["HP"] = player_active["HP"] - damage
                print(player_active["Name"], "took", damage, "damage from FireBlast!")
                print()
            else:
                print("Uh-oh! Looks like FireBlast missed!")
                print()
            
def Strength(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used Strength!")
        print()
        damage = int(((22*80*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
        if "Rock" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from Strength!")
        print()
    else:
        print(enemy_active["Name"], "used Strength!")
        print()
        damage = int(((22*80*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
        if "Rock" in player_active["Type"]:
            damage = damage*0.5
            print()
            print("It's not very effective.")
            print()
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from Strength!")
        print()
        
def Explosion(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used Explosion!")
        print()
        damage = int(((22*150*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
        if "Rock" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        enemy_active["HP"] = enemy_active["HP"] - damage
        player_active["HP"] = 0
        print(enemy_active["Name"], "took", damage, "damage from Explosion!")
        print()
        print(player_active["Name"], "knocked itself out!")
        print()
    else:
        print(player_active["Name"], "used Explosion!")
        print()
        damage = int(((22*150*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
        player_active["HP"] = player_active["HP"] - damage
        enemy_active["HP"] = 0
        print(player_active["Name"], "took", damage, "damage from Explosion!")
        print()
        print(enemy_active["Name"], "knocked itself out!")
        print()
        
def RockSlide(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used RockSlide!")
        print()
        damage = int(((22*90*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
        if "Rock" in player_active["Type"]:
            damage = damage*1.5    
        if "Rock" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Flying" in enemy_active["Type"]:
            damage = damage*2
            print()
            print("It's Super Effective!")
            print()
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from RockSlide!")
        print()
    else:
        print(enemy_active["Name"], "used RockSlide!")
        print()
        damage = int(((22*90*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
        if "Rock" in enemy_active["Type"]:
            damage = damage*1.5
        if "Rock" in player_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Flying" in player_active["Type"]:
            damage = damage*2
            print()
            print("It's Super Effective!")
            print()
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from RockSlide!")
        print()
        
def Submission(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used Submission!")
        print()
        damage = int(((22*100*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
        if "Fighting" in player_active["Type"]:
            damage = damage*1.5
        if "Psychic" in enemy_active["Type"] or "Flying" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Rock" in enemy_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from Submission!")
        print()
    else:
        print(enemy_active["Name"], "used Submission!")
        print()
        damage = int(((22*100*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
        if "Fighting" in enemy_active["Type"]:
            damage = damage*1.5
        if "Psychic" in player_active["Type"] or "Flying" in player_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Rock" in player_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from Submission!")
        print()
        
def MegaPunch(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used MegaPunch!")
        print()
        damage = int(((22*80*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
        if "Fighting" in player_active["Type"]:
            damage = damage*1.5
        if "Psychic" in enemy_active["Type"] or "Flying" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Rock" in enemy_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from MegaPunch!")
        print()
    else:
        print(enemy_active["Name"], "used MegaPunch!")
        print()
        damage = int(((22*80*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
        if "Fighting" in enemy_active["Type"]:
            damage = damage*1.5
        if "Psychic" in player_active["Type"] or "Flying" in player_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Rock" in player_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from MegaPunch!")
        print()
        
def WingAttack(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used WingAttack!")
        print()
        damage = int(((22*80*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
        if "Flying" in player_active["Type"]:
            damage = damage*1.5
        if "Rock" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Fighting" in enemy_active["Type"] or "Grass" in enemy_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from WingAttack!")
        print()
    else:
        print(enemy_active["Name"], "used WingAttack!")
        print()
        damage = int(((22*80*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
        if "Flying" in enemy_active["Type"]:
            damage = damage*1.5
        if "Rock" in player_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Fighting" in player_active["Type"] or "Grass" in player_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from WingAttack!")
        print()
        
def PoisonJab(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used PoisonJab!")
        print()
        damage = int(((22*80*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
        if "Poison" in player_active["Type"]:
            damage = damage*1.5
        if "Psychic" in enemy_active["Type"] or "Rock" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Grass" in enemy_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from PoisonJab!")
        print()
    else:
        print(enemy_active["Name"], "used PoisonJab!")
        print()
        damage = int(((22*80*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
        if "Poison" in enemy_active["Type"]:
            damage = damage*1.5
        if "Psychic" in player_active["Type"] or "Rock" in player_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Grass" in player_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from PoisonJab!")
        print()
        
def Crunch(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used Crunch!")
        print()
        damage = int(((22*80*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from Crunch!")
        print()
    else:
        print(enemy_active["Name"], "used Crunch!")
        print()
        damage = int(((22*80*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from Crunch!")
        print()
        
def MegaKick(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used MegaKick!")
        print()
        damage = int(((22*80*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
        if "Fighting" in player_active["Type"]:
            damage = damage*1.5
        if "Psychic" in enemy_active["Type"] or "Flying" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Rock" in enemy_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from MegaKick!")
        print()
    else:
        print(enemy_active["Name"], "used MegaKick!")
        print()
        damage = int(((22*80*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
        if "Fighting" in enemy_active["Type"]:
            damage = damage*1.5
        if "Psychic" in player_active["Type"] or "Flying" in player_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Rock" in player_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from MegaKick!")
        print()
        
def JumpKick(player_turn, player_active, enemy_active):
    if player_turn:
        hit_chance = random.randint(1,100)
        if hit_chance >30:
            print(player_active["Name"], "used JumpKick!")
            print()
            damage = int(((22*100*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
            if "Fighting" in player_active["Type"]:
                damage = damage*1.5
            if "Psychic" in enemy_active["Type"] or "Flying" in enemy_active["Type"]:
                print()
                print("It's not very effective.")
                print()
                damage = damage*0.5
            if "Rock" in enemy_active["Type"]:
                print()
                print("It's Super Effective!")
                print()
                damage = damage*2
            enemy_active["HP"] = enemy_active["HP"] - damage
            print(enemy_active["Name"], "took", damage, "damage from JumpKick!")
            print()
        else:
            print(player_active["Name"], "'s kick kept going and missed!")
            print()
            player_active["HP"] = player_active["HP"] - 30
            print(player_active["Name"], "took 30 damage!")
            print()
            
    else:
        hit_chance = random.randint(1,100)
        if hit_chance >30:
            print(enemy_active["Name"], "used JumpKick!")
            print()
            damage = int(((22*100*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
            if "Fighting" in enemy_active["Type"]:
                damage = damage*1.5
            if "Psychic" in player_active["Type"] or "Flying" in player_active["Type"]:
                print()
                print("It's not very effective.")
                print()
                damage = damage*0.5
            if "Rock" in player_active["Type"]:
                print()
                print("It's Super Effective!")
                print()
                damage = damage*2    
            player_active["HP"] = player_active["HP"] - damage
            print(player_active["Name"], "took", damage, "damage from JumpKick!")
            print()
        else:
            print(enemy_active["Name"], "'s kick kept going and missed!")
            print()
            enemy_active["HP"] = enemy_active["HP"] - 30
            print(enemy_active["Name"], "took 30 damage!")
            print()
            
def HiJumpKick(player_turn, player_active, enemy_active):
    if player_turn:
        hit_chance = random.randint(1,100)
        if hit_chance >50:
            print(player_active["Name"], "used HiJumpKick!")
            print()
            damage = int(((22*120*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
            if "Fighting" in player_active["Type"]:
                damage = damage*1.5
            if "Psychic" in enemy_active["Type"] or "Flying" in enemy_active["Type"]:
                print()
                print("It's not very effective.")
                print()
                damage = damage*0.5
            if "Rock" in enemy_active["Type"]:
                print()
                print("It's Super Effective!")
                print()
                damage = damage*2
            enemy_active["HP"] = enemy_active["HP"] - damage
            print(enemy_active["Name"], "took", damage, "damage from HiJumpKick!")
            print()
        else:
            print(player_active["Name"], "'s kick kept going and missed!")
            print()
            player_active["HP"] = player_active["HP"] - 50
            print(player_active["Name"], "took 50 damage!")
            print()
            
    else:
        hit_chance = random.randint(1,100)
        if hit_chance >30:
            print(enemy_active["Name"], "used HiJumpKick!")
            print()
            damage = int(((22*120*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
            if "Fighting" in enemy_active["Type"]:
                damage = damage*1.5
            if "Psychic" in player_active["Type"] or "Flying" in player_active["Type"]:
                print()
                print("It's not very effective.")
                print()
                damage = damage*0.5
            if "Rock" in player_active["Type"]:
                print()
                print("It's Super Effective!")
                print()
                damage = damage*2
            player_active["HP"] = player_active["HP"] - damage
            print(player_active["Name"], "took", damage, "damage from HiJumpKick!")
            print()
        else:
            print(enemy_active["Name"], "'s kick kept going and missed!")
            print()
            enemy_active["HP"] = enemy_active["HP"] - 50
            print(enemy_active["Name"], "took 50 damage!")
            print()



def IcePunch(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used IcePunch!")
        print()
        damage = int(((22*80*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
        if "Water" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Grass" in enemy_active["Type"] or "Flying" in enemy_active["Type"] or"Dragon" in enemy_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from IcePunch!")
        print()
    else:
        print(enemy_active["Name"], "used IcePunch!")
        print()
        damage = int(((22*80*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
        if "Water" in player_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Grass" in player_active["Type"] or "Flying" in player_active["Type"] or"Dragon" in enemy_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from IcePunch!")
        print()
        
def FirePunch(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used FirePunch!")
        print()
        damage = int(((22*80*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
        if "Rock" in enemy_active["Type"] or"Dragon" in enemy_active["Type"]:
            damage = damage*0.5
            print()
            print("It's not very effective.")
            print()
        if "Grass" in enemy_active["Type"] or "Bug" in enemy_active["Type"] or "Ice" in enemy_active["Type"]:
            damage = damage*2
            print()
            print("It's Super Effective!")
            print()
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from FirePunch!")
        print()
    else:
        print(enemy_active["Name"], "used FirePunch!")
        print()
        damage = int(((22*80*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
        if "Rock" in player_active["Type"] or"Dragon" in player_active["Type"]:
            damage = damage*0.5
            print()
            print("It's not very effective.")
            print()
        if "Grass" in player_active["Type"] or "Bug" in player_active["Type"] or "Ice" in player_active["Type"]:
            damage = damage*2
            print()
            print("It's Super Effective!")
            print()
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from FirePunch!")
        print()
        
def ThunderPunch(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used ThunderPunch!")
        print()
        damage = int(((22*80*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
        if "Ground" in enemy_active["Type"] or "Dragon" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Water" in enemy_active["Type"] or "Flying" in enemy_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from ThunderPunch!")
        print()
    else:
        print(enemy_active["Name"], "used ThunderPunch!")
        print()
        damage = int(((22*80*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
        if "Ground" in player_active["Type"] or "Dragon" in player_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Water" in player_active["Type"] or "Flying" in player_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from ThunderPunch!")
        print()

def IceBeam(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used IceBeam!")
        print()
        damage = int(((22*95*player_active["Special"]/enemy_active["Special"])/50)+random.randint(1,6))
        if "Ice" in player_active["Type"]:
            damage = damage*1.5
        if "Water" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Grass" in enemy_active["Type"] or "Flying" in enemy_active["Type"] or"Dragon" in enemy_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from IceBeam!")
        print()
    else:
        print(enemy_active["Name"], "used IceBeam!")
        print()
        damage = int(((22*95*enemy_active["Special"]/player_active["Special"])/50)+random.randint(1,6))
        if "Ice" in enemy_active["Type"]:
            damage = damage*1.5
        if "Water" in player_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Grass" in player_active["Type"] or "Flying" in player_active["Type"] or"Dragon" in enemy_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from IceBeam!")
        print()
        
def SludgeBomb(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used SludgeBomb!")
        print()
        damage = int(((22*95*player_active["Special"]/enemy_active["Special"])/50)+random.randint(1,6))
        if "Poison" in player_active["Type"]:
            damage = damage*1.5
        if "Psychic" in enemy_active["Type"] or "Rock" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Grass" in enemy_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from SludgeBomb!")
        print()
    else:
        print(enemy_active["Name"], "used SludgeBomb!")
        print()
        damage = int(((22*95*enemy_active["Special"]/player_active["Special"])/50)+random.randint(1,6))
        if "Poison" in enemy_active["Type"]:
            damage = damage*1.5
        if "Psychic" in player_active["Type"] or "Rock" in player_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Grass" in player_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from SludgeBomb!")
        print()
        
def BodySlam(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used BodySlam!")
        print()
        damage = int(((22*80*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
        if "Rock" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from BodySlam!")
        print()
    else:
        print(enemy_active["Name"], "used BodySlam!")
        print()
        damage = int(((22*80*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
        if "Rock" in player_active["Type"]:
            damage = damage*0.5
            print()
            print("It's not very effective.")
            print()
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from BodySlam!")
        print()
       
def HyperBeam(player_turn, player_active, enemy_active):
    global hyper_check
    if player_turn:
        print(player_active["Name"], "used HyperBeam!")
        print()
        damage = int(((22*150*player_active["Attack"]/enemy_active["Defense"])/50)+random.randint(1,6))
        if "Rock" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from HyperBeam!")
        print()
        hyper_check = True
    else:
        print(enemy_active["Name"], "used HyperBeam!")
        print()
        damage = int(((22*150*enemy_active["Attack"]/player_active["Defense"])/50)+random.randint(1,6))
        if "Rock" in player_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from HyperBeam!")
        print()
        #global hyper_check 
        hyper_check = True
        
def Blizzard(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used Blizzard!")
        print()
        hit_chance = random.randint(1,100)
        if hit_chance >30:
            damage = int(((22*120*player_active["Special"]/enemy_active["Special"])/50)+random.randint(1,6))
            if "Ice" in player_active["Type"]:
                damage = damage*1.5
            if "Water" in enemy_active["Type"]:
                print()
                print("It's not very effective.")
                print()
                damage = damage*0.5
            if "Grass" in enemy_active["Type"] or "Flying" in enemy_active["Type"] or"Dragon" in enemy_active["Type"]:
                print()
                print("It's Super Effective!")
                print()
                damage = damage*2
            enemy_active["HP"] = enemy_active["HP"] - damage
            print(enemy_active["Name"], "took", damage, "damage from Blizzard!")
            print()
        else:
            print("Uh-oh! Looks like Blizzard missed!")   
            print()
    else:
        print(enemy_active["Name"], "used Blizzard!")
        print()
        hit_chance = random.randint(1,100)
        if hit_chance >30:
            damage = int(((22*120*enemy_active["Special"]/player_active["Special"])/50)+random.randint(1,6))
            if "Ice" in enemy_active["Type"]:
                damage = damage*1.5
            if "Water" in player_active["Type"]:
                print()
                print("It's not very effective.")
                print()
                damage = damage*0.5
            if "Grass" in player_active["Type"] or "Flying" in player_active["Type"] or"Dragon" in enemy_active["Type"]:
                print()
                print("It's Super Effective!")
                print()
                damage = damage*2
            player_active["HP"] = player_active["HP"] - damage
            print(player_active["Name"], "took", damage, "damage from Blizzard!")
            print()
        else:
            print("Uh-oh! Looks like Blizzard missed!")
            print()
            
def HydroPump(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used HydroPump!")
        print()
        hit_chance = random.randint(1,100)
        if hit_chance >30:
            damage = int(((22*120*player_active["Special"]/enemy_active["Special"])/50)+random.randint(1,6))
            if "Water" in player_active["Type"]:
                damage = damage*1.5
            if "Water" in enemy_active["Type"] or "Dragon" in enemy_active["Type"]:
                print()
                print("It's not very effective.")
                print()
                damage = damage*0.5
            if "Fire" in enemy_active["Type"] or "Rock" in enemy_active["Type"]:
                print()
                print("It's Super Effective!")
                print()
                damage = damage*2
            enemy_active["HP"] = enemy_active["HP"] - damage
            print(enemy_active["Name"], "took", damage, "damage from HydroPump!")
            print()
        else:
            print("Uh-oh! Looks like HydroPump missed!")   
            print()
    else:
        print(enemy_active["Name"], "used HydroPump!")
        print()
        hit_chance = random.randint(1,100)
        if hit_chance >30:
            damage = int(((22*120*enemy_active["Special"]/player_active["Special"])/50)+random.randint(1,6))
            if "Water" in enemy_active["Type"]:
                damage = damage*1.5
            if "Water" in player_active["Type"] or "Dragon" in player_active["Type"]:
                print()
                print("It's not very effective.")
                print()
                damage = damage*0.5
            if "Fire" in player_active["Type"] or "Rock" in player_active["Type"]:
                print()
                print("It's Super Effective!")
                print()
                damage = damage*2
            player_active["HP"] = player_active["HP"] - damage
            print(player_active["Name"], "took", damage, "damage from HydroPump!")
            print()
        else:
            print("Uh-oh! Looks like HydroPump missed!")
            print()
            
def Thunder(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used Thunder!")
        print()
        hit_chance = random.randint(1,100)
        if hit_chance >30:
            damage = int(((22*120*player_active["Special"]/enemy_active["Special"])/50)+random.randint(1,6))
            if "Electric" in player_active["Type"]:
                damage = damage*1.5
            if "Ground" in enemy_active["Type"] or "Dragon" in enemy_active["Type"]:
                print()
                print("It's not very effective.")
                print()
                damage = damage*0.5
            if "Water" in enemy_active["Type"] or "Flying" in enemy_active["Type"]:
                print()
                print("It's Super Effective!")
                print()
                damage = damage*2
            enemy_active["HP"] = enemy_active["HP"] - damage
            print(enemy_active["Name"], "took", damage, "damage from Thunder!")
            print()
        else:
            print("Uh-oh! Looks like Thunder missed!")   
            print()
    else:
        print(enemy_active["Name"], "used Thunder!")
        print()
        hit_chance = random.randint(1,100)
        if hit_chance >30:
            damage = int(((22*120*enemy_active["Special"]/player_active["Special"])/50)+random.randint(1,6))
            if "Electric" in enemy_active["Type"]:
                damage = damage*1.5
            if "Ground" in player_active["Type"] or "Dragon" in player_active["Type"]:
                print()
                print("It's not very effective.")
                print()
                damage = damage*0.5
            if "Water" in player_active["Type"] or "Flying" in player_active["Type"]:
                print()
                print("It's Super Effective!")
                print()
                damage = damage*2
            player_active["HP"] = player_active["HP"] - damage
            print(player_active["Name"], "took", damage, "damage from Thunder!")
            print()
        else:
            print("Uh-oh! Looks like Thunder missed!")
            print()
        
def Surf(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used Surf!")
        print()
        damage = int(((22*90*player_active["Special"]/enemy_active["Special"])/50)+random.randint(1,6))
        if "Water" in player_active["Type"]:
            damage = damage*1.5
        if "Water" in enemy_active["Type"] or "Dragon" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Fire" in enemy_active["Type"] or "Rock" in enemy_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from Surf!")
        print()
    else:
        print(enemy_active["Name"], "used Surf!")
        print()
        damage = int(((22*90*enemy_active["Special"]/player_active["Special"])/50)+random.randint(1,6))
        if "Water" in enemy_active["Type"]:
            damage = damage*1.5
        if "Water" in player_active["Type"] or "Dragon" in player_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Fire" in player_active["Type"] or "Rock" in player_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from Surf!")
        print()

def ShadowBall(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used ShadowBall!")
        print()
        damage = int(((22*90*player_active["Special"]/enemy_active["Special"])/50)+random.randint(1,6))
        if "Ghost" in player_active["Type"]:
                damage = damage*1.5
        if "Normal" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Ghost" in enemy_active["Type"] or "Psychic" in enemy_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from ShadowBall!")
        print()
    else:
        print(enemy_active["Name"], "used ShadowBall!")
        print()
        damage = int(((22*90*enemy_active["Special"]/player_active["Special"])/50)+random.randint(1,6))
        if "Ghost" in enemy_active["Type"]:
            damage = damage*1.5
        if "Normal" in player_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Ghost" in player_active["Type"] or "Psychic" in player_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from ShadowBall!") 
        print()
        
def NightShade(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used NightShade!")
        print()
        enemy_active["HP"] = enemy_active["HP"] - 50
        print(enemy_active["Name"], "took 50 damage from NightShade!")
        print()
    else:
        print(enemy_active["Name"], "used NightShade!")
        print()
        player_active["HP"] = player_active["HP"] - 50
        print(player_active["Name"], "took 50 damage from NightShade!") 
        print()
        
def DragonRage(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used DragonRage!")
        print()
        enemy_active["HP"] = enemy_active["HP"] - 40
        print(enemy_active["Name"], "took 40 damage from DragonRage!")
        print()
    else:
        print(enemy_active["Name"], "used DragonRage!")
        print()
        player_active["HP"] = player_active["HP"] - 40
        print(player_active["Name"], "took 40 damage from DragonRage!")
        print()
        
        
def Thunderbolt(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used Thunderbolt!")
        print()
        damage = int(((22*95*player_active["Special"]/enemy_active["Special"])/50)+random.randint(1,6))
        if "Electric" in player_active["Type"]:
            damage = damage*1.5
        if "Ground" in enemy_active["Type"] or "Dragon" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Water" in enemy_active["Type"] or "Flying" in enemy_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from Thunderbolt!")
        print()
    else:
        print(enemy_active["Name"], "used Thunderbolt!")
        print()
        damage = int(((22*95*enemy_active["Special"]/player_active["Special"])/50)+random.randint(1,6))
        if "Electric" in enemy_active["Type"]:
            damage = damage*1.5
        if "Ground" in player_active["Type"] or "Dragon" in player_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Water" in player_active["Type"] or "Flying" in player_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from Thunderbolt!") 
        print()
        
def SolarBeam(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used SolarBeam!")
        print()
        print(player_active["Name"], "absorbed sunlight!")
        print()
        damage = int(((22*100*player_active["Special"]/enemy_active["Special"])/50)+random.randint(1,6))
        if "Grass" in player_active["Type"]:
            damage = damage*1.5
        if "Grass" in enemy_active["Type"] or "Dragon" in enemy_active["Type"] or "Fire" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Water" in enemy_active["Type"] or "Rock" in enemy_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from SolarBeam!")
        print()
    else:
        print(enemy_active["Name"], "used SolarBeam!")
        print()
        print(enemy_active["Name"], "absorbed sunlight!")
        print()
        damage = int(((22*100*enemy_active["Special"]/player_active["Special"])/50)+random.randint(1,6))
        if "Grass" in enemy_active["Type"]:
            damage = damage*1.5
        if "Grass" in player_active["Type"] or "Dragon" in player_active["Type"] or "Fire" in player_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Water" in player_active["Type"] or "Rock" in player_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from SolarBeam!")
        print()
        
def Psychic(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used Psychic!")
        print()
        damage = int(((22*90*player_active["Special"]/enemy_active["Special"])/50)+random.randint(1,6))
        if "Psychic" in player_active["Type"]:
            damage = damage*1.5
        if "Psychic" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Fighting" in enemy_active["Type"] or "Poison" in enemy_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from Psychic!")
        print()
    else:
        print(enemy_active["Name"], "used Psychic!")
        print()
        damage = int(((22*90*enemy_active["Special"]/player_active["Special"])/50)+random.randint(1,6))
        if "Psychic" in enemy_active["Type"]:
            damage = damage*1.5
        if "Psychic" in player_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Fighting" in player_active["Type"] or "Poison" in player_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from Psychic!") 
        print()
        
def Psybeam(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used Psybeam!")
        print()
        damage = int(((22*60*player_active["Special"]/enemy_active["Special"])/50)+random.randint(1,6))
        if "Psychic" in player_active["Type"]:
            damage = damage*1.5
        if "Psychic" in enemy_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Fighting" in enemy_active["Type"] or "Poison" in enemy_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        enemy_active["HP"] = enemy_active["HP"] - damage
        print(enemy_active["Name"], "took", damage, "damage from Psybeam!")
        print()
    else:
        print(enemy_active["Name"], "used Psybeam!")
        print()
        damage = int(((22*60*enemy_active["Special"]/player_active["Special"])/50)+random.randint(1,6))
        if "Psychic" in enemy_active["Type"]:
            damage = damage*1.5
        if "Psychic" in player_active["Type"]:
            print()
            print("It's not very effective.")
            print()
            damage = damage*0.5
        if "Fighting" in player_active["Type"] or "Poison" in player_active["Type"]:
            print()
            print("It's Super Effective!")
            print()
            damage = damage*2
        player_active["HP"] = player_active["HP"] - damage
        print(player_active["Name"], "took", damage, "damage from Psybeam!")
        print()
        
def Reflect(player_turn, player_active, enemy_active):
    if player_turn:
        if player_active["Defense"]>=300:
            print(player_active["Name"], "'s Defense is already too high! No effect!")
            print()
            
        else:
            print(player_active["Name"], "used Reflect!")
            print()
            player_active["Defense"] = player_active["Defense"]*1.5
            print(player_active["Name"], "raised their Defense!")
            print()
            
    else:
        if enemy_active["Defense"]>=300:
            print(enemy_active["Name"], "'s Defense is already too high! No effect!")
            print()
            
        else:
            print(enemy_active["Name"], "used Reflect!")
            print()
            enemy_active["Defense"] = enemy_active["Defense"]*1.5
            print(enemy_active["Name"], "raised their Defense!")
            print()

def Agility(player_turn, player_active, enemy_active):
    if player_turn:
        if player_active["Speed"]>=300:
            print(player_active["Name"], "'s Speed is already too high! No effect!")
            print()
            
        else:
            print(player_active["Name"], "used Agility!")
            print()
            player_active["Speed"] = player_active["Speed"]*1.5
            print(player_active["Name"], "raised their Speed!")
            print()
            
    else:
        if enemy_active["Speed"]>=300:
            print(enemy_active["Name"], "'s Speed is already too high! No effect!")
            print()
            
        else:
            print(enemy_active["Name"], "used Agility!")
            print()
            enemy_active["Speed"] = enemy_active["Speed"]*1.5
            print(enemy_active["Name"], "raised their Speed!")
            print()
            
            
def Screech(player_turn, player_active, enemy_active):
    if player_turn:
        if enemy_active["Defense"]<=15:
            print(enemy_active["Name"], "'s defense is already too low! No effect!")
            print()
            
        else:
            print(player_active["Name"], "used Screech!")
            print()
            enemy_active["Defense"] = enemy_active["Defense"]*0.5
            print(enemy_active["Name"], "'s Defense was lowered!")
            print()
            
    else:
        if player_active["Defense"]<=15:
            print(player_active["Name"], "'s Defense is already too low! No effect!")
            print()
            
        else:
            print(enemy_active["Name"], "used Screech!")
            print()
            player_active["Defense"] = player_active["Defense"]*0.5
            print(player_active["Name"], "'s Defense was lowered!")
            print()
            
            
def Fissure(player_turn, player_active, enemy_active):
    if player_turn:
        print(player_active["Name"], "used Fissure!")
        print()
        hit_chance = random.randint(1,100)
        if hit_chance >30:
            print("Fissure missed!")
            print()
        else:
            print("The Fissure swallowed", enemy_active["Name"], "whole!")
            print()
            enemy_active["HP"] = 0
            
    else:
        print(enemy_active["Name"], "used Fissure!")
        print()
        hit_chance = random.randint(1,100)
        if hit_chance >30:
            print("Fissure missed!")
            print()
        else:
            print("The Fissure swallowed", player_active["Name"], "whole!")
            print()
            player_active["HP"] = 0
            
############################################################
##################### Defining the items   
############################################################  

### Inititally I was going to add in all the items from the game,
### but quite frankly, most of them are useless when you get to this final
### stage. Instead, I only added the best items that people would actually
### choose to purchase anyway if they were experienced with the game.
            
def HyperPotion(Charizard,Alakazam,Blastoise,Venusaur,Jolteon,Lapras_P, hyper_potions):
    print()
    print("Who would you like to use Hyper Potion on? ")
    print()
    lyst = []
    if Charizard["Feint"]==False:
        print(Charizard["Name"], "'s HP = ", Charizard["HP"],'/',Charizard["Max HP"])
        lyst.append("Charizard")
    if Alakazam["Feint"]==False:
        print(Alakazam["Name"], "'s HP = ", Alakazam["HP"],'/',Alakazam["Max HP"])
        lyst.append("Alakazam")
    if Blastoise["Feint"]==False:
        print(Blastoise["Name"], "'s HP = ", Blastoise["HP"],'/',Blastoise["Max HP"])
        lyst.append("Blastoise")
    if Venusaur["Feint"]==False:
        print(Venusaur["Name"], "'s HP = ", Venusaur["HP"],'/',Venusaur["Max HP"])
        lyst.append("Venusaur")
    if Jolteon["Feint"]==False:
        print(Jolteon["Name"], "'s HP = ", Jolteon["HP"],'/',Jolteon["Max HP"])
        lyst.append("Jolteon")
    if Lapras_P["Feint"]==False:
        print(Lapras_P["Name"], "'s HP = ", Lapras_P["HP"],'/',Lapras_P["Max HP"])
        lyst.append("Lapras")
    print()
    hyperp = str(input("Enter the Pokemon to use Hyper Potion on or 'cancel' to cancel: "))
    print()
    z = True
    while z:
        if hyperp == 'cancel' or hyperp == 'Cancel':
            return
        if hyperp in lyst:
            z = False
            return hyperp
        else:
            print("Who would you like to use Hyper Potion on? ")
            print()
            hyperp = str(input("Enter the Pokemon to use Hyper Potion on or 'cancel' to cancel: "))
            print()

        
def Revive(Charizard,Alakazam,Blastoise,Venusaur,Jolteon,Lapras_P, revives):
    lyst = []
    if Charizard["Feint"]==True:
        lyst.append("Charizard")
    if Alakazam["Feint"]==True:
        lyst.append("Alakazam")
    if Blastoise["Feint"]==True:
        lyst.append("Blastoise")
    if Venusaur["Feint"]==True:
        lyst.append("Venusaur")
    if Jolteon["Feint"]==True:
        lyst.append("Jolteon")
    if Lapras_P["Feint"]==True:
        lyst.append("Lapras")
    if len(lyst)==0:
        print()
        return "Failed"
    else:
        print()
        print("Who would you like to revive? ")
        print()
        for i in range(len(lyst)):
            print(lyst[i])
        print()
        revive = str(input("Enter the Pokemon to revive: "))
        print()
        z = True
        while z:
            if revive in lyst:
                z = False
                return revive
            else:
                print("Who would you like to revive? ")
                print()
                revive = str(input("Enter the Pokemon to revive: "))
                print()
        
        
    
    

def main():
    global hyper_check
    
    ## Player's Team
    Moves = {"Flamethrower":Flamethrower, "FireBlast":FireBlast, "Slash":Slash, "Strength":Strength ,"Psychic":Psychic, "Thunderbolt": Thunderbolt,'ShadowBall':ShadowBall, "Reflect":Reflect, "Psybeam":Psybeam, "Blizzard":Blizzard, "IceBeam":IceBeam, "Thunder":Thunder, "SludgeBomb":SludgeBomb, "SolarBeam":SolarBeam, "Surf":Surf, "HydroPump":HydroPump, "BodySlam":BodySlam   }
    Charizard = {"Name":"Charizard", "Type":"FireFlying" , "Max HP":78, "HP":78, "Attack":84, "Defense": 78, "Special":85, "Speed": 100, "Moves":['Flamethrower', 'Strength', 'Slash', "FireBlast"],"Feint":False}
    #Gengar = {"Name":"Gengar", "Type":"GhostPoison" ,"HP":60, "Attack":65, "Defense": 60, "Special":130, "Speed": 110, "Moves":['ShadowBall', 'Psychic', 'Thunderbolt', "BodySlam"]}
    Alakazam = {"Name":"Alakazam", "Type":"Psychic" ,"Max HP":55, "HP":55, "Attack":50, "Defense": 45, "Special":135, "Speed": 120, "Moves":['Reflect', 'Psychic', 'Thunderbolt', "Psybeam"],"Feint":False}
    Blastoise = {"Name":"Blastoise","Type":"Water" ,"Max HP":79, "HP":79, "Attack":83, "Defense": 100, "Special":85, "Speed": 78, "Moves":['HydroPump', 'Strength', 'Surf', "Reflect"],"Feint":False}
    Venusaur = {"Name":"Venusaur","Type":"GrassPoison" ,"Max HP":80, "HP":80, "Attack":82, "Defense": 83, "Special":100, "Speed": 80, "Moves":['SolarBeam', 'SludgeBomb', 'BodySlam', "Reflect"],"Feint":False}
    Jolteon = {"Name":"Jolteon","Type":"Electric" ,"Max HP":65, "HP":65, "Attack":65, "Defense": 60, "Special":110, "Speed": 130, "Moves":['Thunderbolt', 'Reflect', 'Slash', "Thunder"],"Feint":False}
    Lapras_P = {"Name":"Lapras","Type":"WaterIce" ,"Max HP":130, "HP":130, "Attack":85, "Defense": 80, "Special":95, "Speed": 60, "Moves":['IceBeam', 'BodySlam', 'Blizzard', "HydroPump"],"Feint":False}
    
    ## Lorelei's Team
    Dewgong = {"Name":"Dewgong","Type":"WaterIce" ,"HP":90, "Attack":70, "Defense": 80, "Special":95, "Speed": 70, "Moves":['IceBeam', 'BodySlam', 'Blizzard', "Surf"]}
    Cloyster = {"Name":"Cloyster","Type":"WaterIce" ,"HP":50, "Attack":95, "Defense": 180, "Special":85, "Speed": 70, "Moves":['IceBeam', 'BodySlam', 'Reflect', "Surf"]} 
    Slowbro = {"Name":"Slobrow","Type":"WaterPsychic" ,"HP":95, "Attack":75, "Defense": 100, "Special":80, "Speed": 30, "Moves":['Psychic', 'Strength', 'BodySlam', "Surf"]}
    Jinx = {"Name":"Jinx","Type":"PsychicIce" ,"HP":65, "Attack":50, "Defense": 35, "Special":95, "Speed": 95, "Moves":['Slash', 'IceBeam', 'Psychic', "BodySlam"]}
    Lapras_L = {"Name":"Lapras","Type":"WaterIce" ,"HP":130, "Attack":85, "Defense": 80, "Special":95, "Speed": 60, "Moves":['IceBeam', 'BodySlam', 'Blizzard', "HydroPump"]}
    
    ## Bruno's Team
    Onyx = {"Name":"Onyx","Type":"RockGround" ,"HP":35, "Attack":45, "Defense": 130, "Special":30, "Speed": 70, "Moves":['BodySlam', 'RockSlide', 'Reflect', "Strength"]}
    Hitmonchan = {"Name":"Hitmonchan","Type":"Fighting" ,"HP":50, "Attack":104, "Defense": 79, "Special":35, "Speed": 76, "Moves":['MegaPunch', 'IcePunch', 'FirePunch', "ThunderPunch"]}
    Hitmonlee = {"Name":"Hitmonlee","Type":"Fightin" ,"HP":50, "Attack":120, "Defense": 53, "Special":35, "Speed": 87, "Moves":['JumpKick', 'HiJumpKick', 'MegaKick', "Strength"]}
    Golem = {"Name":"Golem","Type":"RockGround" ,"HP":80, "Attack":100, "Defense": 130, "Special":55, "Speed": 45, "Moves":['Explosion', 'RockSlide', 'Reflect', "Strength"]}
    Machamp = {"Name":"Machamp","Type":"Fighting" ,"HP":90, "Attack":130, "Defense": 80, "Special":65, "Speed": 55, "Moves":['Strength', 'Submission', 'BodySlam', "Fissure"]}
    
    ## Agatha's Team
    Gengar_A1 = {"Name":"Gengar", "Type":"GhostPoison" ,"HP":60, "Attack":65, "Defense": 60, "Special":130, "Speed": 110, "Moves":['ShadowBall', 'Psychic', 'Thunderbolt', "BodySlam"]}
    Golbat = {"Name":"Golbat","Type":"PoisonFlying" ,"HP":75, "Attack":80, "Defense": 70, "Special":75, "Speed": 90, "Moves":['BodySlam', 'PoisonJab', 'Reflect', "WingAttack"]}
    Haunter = {"Name":"Haunter","Type":"GhostPoison" ,"HP":45, "Attack":50, "Defense": 450, "Special":115, "Speed": 95, "Moves":['ShadowBall', 'NightShade', 'Fissure', "MegaPunch"]}
    Arbok = {"Name":"Arbok","Type":"Poison" ,"HP":60, "Attack":85, "Defense": 69, "Special":65, "Speed": 80, "Moves":['BodySlam', 'Screech', 'Crunch', "SludgeBomb"]}
    Gengar_A2 = {"Name":"Gengar", "Type":"GhostPoison" ,"HP":60, "Attack":65, "Defense": 60, "Special":130, "Speed": 110, "Moves":['ShadowBall', 'Psychic', 'Thunderbolt', "BodySlam"]}
    
    ## Lance's Team
    Gyarados = {"Name":"Gyarados", "Type":"WaterFlying" ,"HP":95, "Attack":125, "Defense": 79, "Special":100, "Speed": 81, "Moves":['HydroPump', 'Screech', 'DragonRage', "HyperBeam"]}
    Dragonair_L1 = {"Name":"Dragonair", "Type":"Dragon" ,"HP":61, "Attack":84, "Defense": 65, "Special":70, "Speed": 70, "Moves":['BodySlam', 'Agility', 'DragonRage', "HyperBeam"]}
    Dragonair_L2 = {"Name":"Dragonair", "Type":"Dragon" ,"HP":61, "Attack":84, "Defense": 65, "Special":70, "Speed": 70, "Moves":['BodySlam', 'Agility', 'DragonRage', "HyperBeam"]}
    Aerodactyl = {"Name":"Aerodactyl", "Type":"RockFlying" ,"HP":80, "Attack":105, "Defense": 65, "Special":60, "Speed": 130, "Moves":['RockSlide', 'Agility', 'Crunch', "HyperBeam"]}
    Dragonite = {"Name":"Dragonite", "Type":"DragonFlying" ,"HP":91, "Attack":134, "Defense": 95, "Special":100, "Speed": 80, "Moves":['BodySlam', 'Reflect', 'Agility', "HyperBeam"]}
    
    ## Items that can be purchased:
    revives = 0
    hyper_potions = 0
    money = 25500
    
    
    player_team = [True, Charizard, Alakazam, Blastoise, Venusaur, Jolteon, Lapras_P]
    EliteFour = {"Lorelei":["Lorelei",True, Dewgong, Cloyster, Slowbro, Jinx, Lapras_L], "Bruno":["Bruno", True, Onyx, Hitmonchan, Hitmonlee, Golem, Machamp], "Agatha":["Agatha", True, Gengar_A1, Golbat,Haunter,Arbok, Gengar_A2 ], "Lance":["Lance", True, Gyarados, Dragonair_L1, Dragonair_L2, Aerodactyl, Dragonite]}
    enemy_team = EliteFour["Lorelei"]
    current_player = 1
    body_count = 0
    player_active = player_team[current_player]
    current_enemy = 2
    enemy_active = enemy_team[current_enemy]
    
    ### Introduction
    print("Welcome young Pokemon Trainer to the Indigo Plateau!")
    print()
    print("Your long journey has lead you here: to battle the Elite Four!")
    print()
    print("You must defeat all four master trainers in succession.")
    print()
    print("Once you enter, you cannot leave until you emerge victorious or are defeated.")
    print()
    print()
    print("Your team currently is: ")
    print()
    print(" Charizard")
    print(" Alakazam")
    print(" Blastoise")
    print(" Venusaur")
    print(" Jolteon")
    print(" Lapras")
    print()
    print("Thus far in your journey you have collected:", money, "dollars. You now have the chance to spend your hard earned cash!")
    print("I was going to offer you more options, but let's get real! No one buys anything other than Revives and Hyper Potions anyway!")
    print()
    print("Hyper Potions heal your Pokemon if they take damage and Revives will allow them to fight again if they feint.")
    print()
    print()
    
    ## Purchasing Items
    i = True
    while i:
        print()
        print("What would you like to buy?")
        print()
        print(" Revive: $1500")
        print(" Hyper Potion: $1500")
        print()
        print("Remaining Money:", money)
        purchase = str(input("Enter the item you would like to purchase or 'done' to move on: "))
        if purchase == "Revive" or purchase == 'revive':
            print()
            print("How many Revives would you like to buy?")
            print("(Type in a Roman Numeral, please.)")
            print()
            x = True
            while x:
                purchase = str(input("Enter how many Revives would you like to purchase or 'back' to go back: "))
                if purchase == 'back' or purchase == 'Back':
                    x = False
                if purchase != "back" and purchase != "Back":
                    purchase = int(purchase)
                    if purchase *1500<=money:
                        revives = revives + purchase
                        money = money - 1500*purchase
                        print()
                        print("Thanks! You now have:", revives, "Revives and", hyper_potions, "Hyper Potions.")
                        print()
                        print("You have", money, "dollars left. Spend it wisely!")
                        print()
                        x = False
                    else:
                        print()
                        print("You can't afford all that!")
                        print()
                
                
        if purchase == "Hyper Potion" or purchase == 'hyper potion':
            print()
            print("How many Hyper Potions would you like to buy?")
            print("(Type in a Roman Numeral, please.)")
            x = True
            while x:
                purchase = str(input("Enter how many Hyper Potions you would like to purchase or 'back' to go back: "))
                if purchase == 'back' or purchase == 'Back':
                    x = False
                if purchase != "back" and purchase != "Back":
                    purchase = int(purchase)
                    if purchase *1500<=money:
                        hyper_potions = hyper_potions + purchase
                        money = money - 1500*purchase
                        print("Thanks! You now have:", revives, "Revives and", hyper_potions, "Hyper Potions.")
                        print()
                        print("You have", money, "dollars left. Spend it wisely!")
                        print()
                        x = False
                    else:
                        print("You can't afford all that!")
                        print()  
                
                
        if purchase == 'done' or purchase == 'Done':
            i = False
            
    
    ## Introduction Cont.
    print()
    print()
    print()
    print()
    print("You should use these in between battles to keep your team in fighting shape!")
    print()
    print("Prepare yourself trainer! Your first opponent is the icy mistress: Lorelei!")
    print()
    print()
    print()
    print("Lorelei sends out her first Pokemon: Dewgong!")
    print()
    print("You send our your first Pokemon!")
    print()
    print("Charizard! Go!")
    print()
    
    
    ## Battling Lorelei
    while EliteFour["Lorelei"][1] == True:
        while player_active["HP"]>0 and enemy_active["HP"]>0:
            take_turn(player_active, enemy_active, Moves)
        if player_active["HP"]<=0:
            if body_count < 5:
                print()
                print(player_active["Name"], "has feinted!")
                player_active["Feint"]=True
                print("Send in your next Pokemon!")
                print()
                lyst = []
                if Charizard["Feint"]==False:
                    lyst.append("Charizard")
                if Alakazam["Feint"]==False:
                    lyst.append("Alakazam")
                if Blastoise["Feint"]==False:
                    lyst.append("Blastoise")
                if Venusaur["Feint"]==False:
                    lyst.append("Venusaur")
                if Jolteon["Feint"]==False:
                    lyst.append("Jolteon")
                if Lapras_P["Feint"]==False:
                    lyst.append("Lapras")
                print()
                for i in range(len(lyst)):
                    print(lyst[i])
                print()
                print("Who would you like to send in? ")
                print()
                switch = str(input("Enter next Pokemon: "))
                z = True
                while z:
                    if switch in lyst:
                        if switch == "Charizard":
                            current_player = 1
                        if switch == "Alakazam":
                            current_player = 2
                        if switch == "Blastoise":
                            current_player = 3
                        if switch == "Venusaur":
                            current_player = 4
                        if switch == "Jolteon":
                            current_player = 5
                        if switch == "Lapras":
                            current_player = 6
                        z = False
                    else:
                        print("Who would you like to send in? ")
                        print()
                        switch = str(input("Enter next Pokemon: "))
                body_count = body_count + 1 
                player_active = player_team[current_player]
                print()
                print("Go,",player_active["Name"],"!" )
                print()
            else:
                player_team[0] = False
                EliteFour["Lorelei"][1] = False
        if enemy_active["HP"]<=0:
            if current_enemy < len(EliteFour["Lorelei"])-1:
                print()
                print(enemy_active["Name"], "has feinted!")
                print()
                print( "Lorelei will send in her next Pokemon:")
                print()
                current_enemy = current_enemy+1
                enemy_active = enemy_team[current_enemy]
                print(enemy_active["Name"], "!")
                print()
            else:
                print()
                print(enemy_active["Name"], "has feinted!")
                print()
                EliteFour["Lorelei"][1] = False
    if player_team[0] == False:
        print("You have run out of Pokemon!")
        player_team[0] = False
        print()
        print("Better luck next time.")
        return
    if EliteFour["Lorelei"][1] == False:
        print("Lorelei has been defeated!")
        print()
        print()
        enemy_team = EliteFour["Bruno"]
        current_enemy = 2
        enemy_active = enemy_team[current_enemy]
        print()
        print("Now you must face the mighty Bruno!")
        print()
        print("Would you like to use any items?")
        print()
        items = str(input("Enter 'Yes' or 'No': "))
        z = True
        while z:
            if items == 'yes' or items == "Yes":
                print("Which item do you want to use? \n")
                print(" Hyper Potion......x",str(hyper_potions)+"\n","Revive......x",str(revives)+"\n" )
                item = str(input("Enter the item: "))
                print()
                x = True
                while x:
                    if item == "Revive" or item == "revive":
                        revive = Revive(Charizard, Alakazam, Blastoise, Venusaur, Jolteon, Lapras_P, revives)
                        if revive == "Failed":
                            print("None of your Pokemon have fainted!")
                            print()
                        if revive == "Charizard":
                            Charizard["Feint"]=False
                            Charizard["HP"]=Charizard["Max HP"]//2
                            print("Charizard has been revived!")
                            print()
                            revives = revives - 1
                        if revive == "Alakazam":
                            Alakazam["Feint"]=False
                            Alakazam["HP"]=Alakazam["Max HP"]//2
                            print("Alakazam has been revived!")
                            print()
                            revives = revives - 1
                        if revive == "Blastoise":
                            Blastoise["Feint"]=False
                            Blastoise["HP"]=Blastoise["Max HP"]//2
                            print("Blastoise has been revived!")
                            print()
                            revives = revives - 1
                        if revive == "Venusaur":
                            Venusaur["Feint"]=False
                            Venusaur["HP"]=Venusaur["Max HP"]//2
                            print("Venusaur has been revived!")
                            print()
                            revives = revives - 1
                        if revive == "Jolteon":
                            Jolteon["Feint"]=False
                            Jolteon["HP"]=Jolteon["Max HP"]//2
                            print("Jolteon has been revived!")
                            print()
                            revives = revives - 1
                        if revive == "Lapras":
                            Lapras_P["Feint"]=False
                            Lapras_P["HP"]=Lapras_P["Max HP"]//2
                            print("Lapras has been revived!")
                            print()
                            revives = revives - 1
                        x = False
                    elif item == "Hyper Potion" or item == "hyper potion":
                        if Charizard["HP"]==Charizard["Max HP"] and Lapras_P["HP"]==Lapras_P["Max HP"] and Blastoise["HP"]==Blastoise["Max HP"] and Alakazam["HP"]==Alakazam["Max HP"] and Venusaur["HP"]==Venusaur["Max HP"] and Jolteon["HP"]==Jolteon["Max HP"]:
                            print("All of your Pokemon are at full health!")
                            print()
                        else:
                            hyperp = HyperPotion(Charizard, Alakazam, Blastoise, Venusaur, Jolteon, Lapras_P, revives)
                            if hyperp == "Charizard":
                                Charizard["HP"]=Charizard["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Charizard["HP"]>=Charizard["Max HP"]:
                                    Charizard["HP"]=Charizard["Max HP"]
                                    print("Charizard has been fully healed!")
                                    print()
                                
                                else:
                                    print("Charizard has been healed 100 HP!")
                                    print()
                                    print("Charizard's current HP is: ", Charizard["HP"])
                                    print()
                            if hyperp == "Alakazam":
                                Alakazam["HP"]=Alakazam["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Alakazam["HP"]>=Alakazam["Max HP"]:
                                    Alakazam["HP"]=Alakazam["Max HP"]
                                    print("Alakazam has been fully healed!")
                                    print()
                                else:
                                    print("Alakazam has been healed 100 HP!")
                                    print()
                                    print("Alakazam's current HP is: ", Alakazam["HP"])
                                    print()
                            if hyperp == "Blastoise":
                                Blastoise["HP"]=Blastoise["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Blastoise["HP"]>=Blastoise["Max HP"]:
                                    Blastoise["HP"]=Blastoise["Max HP"]
                                    print("Blastoise has been fully healed!")
                                    print()
                                else:
                                    print("Blastoise has been healed 100 HP!")
                                    print()
                                    print("Blastoise's current HP is: ", Blastoise["HP"])
                                    print()
                            if hyperp == "Venusaur":
                                Venusaur["HP"]=Venusaur["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Venusaur["HP"]>=Venusaur["Max HP"]:
                                    Venusaur["HP"]=Venusaur["Max HP"]
                                    print("Venusaur has been fully healed!")
                                    print()
                                else:
                                    print("Venusaur has been healed 100 HP!")
                                    print()
                                    print("Venusaur's current HP is: ", Venusaur["HP"])
                                    print()
                            if hyperp == "Jolteon":
                                Jolteon["HP"]=Jolteon["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Jolteon["HP"]>=Jolteon["Max HP"]:
                                    Jolteon["HP"]=Jolteon["Max HP"]
                                    print("Jolteon has been fully healed!")
                                    print()
                                else:
                                    print("Jolteon has been healed 100 HP!")
                                    print()
                                    print("Jolteon's current HP is: ", Jolteon["HP"])
                                    print()
                            if hyperp == "Lapras":
                                Lapras_P["HP"]=Lapras_P["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Lapras_P["HP"]>=Lapras_P["Max HP"]:
                                    Lapras_P["HP"]=Lapras_P["Max HP"]
                                    print("Lapras has been fully healed!")
                                    print()
                                else:
                                    print("Lapras has been healed 100 HP!")
                                    print()
                                    print("Lapras's current HP is: ", Lapras_P["HP"])
                                    print()
                            
                        x = False
                        
                    else:
                        item = str(input("Enter the item: "))
                        print()
            if items == "No" or items == 'no':
                z = False
            else:
                print()
                items = str(input("Do you want to use an item? "))
                print()
        print("Prepare yourself!")    
        print()
        print()
        print("Bruno sends out his first Pokemon: Onyx!")
        print()
    

       
    ## Battling Bruno
    while EliteFour["Bruno"][1] == True:
        while player_active["HP"]>0 and enemy_active["HP"]>0:
            take_turn(player_active, enemy_active, Moves)
        if player_active["HP"]<=0:
            if body_count < 5:
                print()
                print(player_active["Name"], "has feinted!")
                player_active["Feint"]=True
                print("Send in your next Pokemon!")
                print()
                lyst = []
                if Charizard["Feint"]==False:
                    lyst.append("Charizard")
                if Alakazam["Feint"]==False:
                    lyst.append("Alakazam")
                if Blastoise["Feint"]==False:
                    lyst.append("Blastoise")
                if Venusaur["Feint"]==False:
                    lyst.append("Venusaur")
                if Jolteon["Feint"]==False:
                    lyst.append("Jolteon")
                if Lapras_P["Feint"]==False:
                    lyst.append("Lapras")
                print()
                for i in range(len(lyst)):
                    print(lyst[i])
                print()
                print("Who would you like to send in? ")
                print()
                switch = str(input("Enter next Pokemon: "))
                print()
                z = True
                while z:
                    if switch in lyst:
                        if switch == "Charizard":
                            current_player = 1
                        if switch == "Alakazam":
                            current_player = 2
                        if switch == "Blastoise":
                            current_player = 3
                        if switch == "Venusaur":
                            current_player = 4
                        if switch == "Jolteon":
                            current_player = 5
                        if switch == "Lapras":
                            current_player = 6
                        z = False
                    else:
                        print("Who would you like to send in? ")
                        print()
                        switch = str(input("Enter next Pokemon: "))
                body_count = body_count + 1       
                player_active = player_team[current_player]
                print()
                print("Go,",player_active["Name"],"!" )
                print()
            else:
                player_team[0] = False
                EliteFour["Bruno"][1] = False
        if enemy_active["HP"]<=0:
            if current_enemy < len(EliteFour["Bruno"])-1:
                print()
                print(enemy_active["Name"], "has feinted!")
                print()
                print( "Bruno will send in his next Pokemon:")
                print()
                current_enemy = current_enemy+1
                enemy_active = enemy_team[current_enemy]
                print(enemy_active["Name"], "!")
                print()
            else:
                print()
                print(enemy_active["Name"], "has feinted!")
                print()
                EliteFour["Bruno"][1] = False
    if player_team[0] == False:
        print("You have run out of Pokemon!")
        player_team[0] = False
        print()
        print("Better luck next time.")
        return
    if EliteFour["Bruno"][1] == False:
        print("Bruno has been defeated!")
        print()
        print()
        enemy_team = EliteFour["Agatha"]
        print()
        current_enemy = 2
        enemy_active = enemy_team[current_enemy]
        print("Now you must face the spooky Agatha!")
        print()
        print("Would you like to use any items?")
        print()
        items = str(input("Enter 'Yes' or 'No': "))
        z = True
        while z:
            if items == 'yes' or items == "Yes":
                print("Which item do you want to use? \n")
                print(" Hyper Potion......x",str(hyper_potions)+"\n","Revive......x",str(revives)+"\n" )
                item = str(input("Enter the item: "))
                print()
                x = True
                while x:
                    if item == "Revive":
                        revive = Revive(Charizard, Alakazam, Blastoise, Venusaur, Jolteon, Lapras_P, revives)
                        if revive == "Failed":
                            print("None of your Pokemon have fainted!")
                            print()
                        if revive == "Charizard":
                            Charizard["Feint"]=False
                            Charizard["HP"]=Charizard["Max HP"]//2
                            print("Charizard has been revived!")
                            print()
                            revives = revives - 1
                        if revive == "Alakazam":
                            Alakazam["Feint"]=False
                            Alakazam["HP"]=Alakazam["Max HP"]//2
                            print("Alakazam has been revived!")
                            print()
                            revives = revives - 1
                        if revive == "Blastoise":
                            Blastoise["Feint"]=False
                            Blastoise["HP"]=Blastoise["Max HP"]//2
                            print("Blastoise has been revived!")
                            print()
                            revives = revives - 1
                        if revive == "Venusaur":
                            Venusaur["Feint"]=False
                            Venusaur["HP"]=Venusaur["Max HP"]//2
                            print("Venusaur has been revived!")
                            print()
                            revives = revives - 1
                        if revive == "Jolteon":
                            Jolteon["Feint"]=False
                            Jolteon["HP"]=Jolteon["Max HP"]//2
                            print("Jolteon has been revived!")
                            print()
                            revives = revives - 1
                        if revive == "Lapras":
                            Lapras_P["Feint"]=False
                            Lapras_P["HP"]=Lapras_P["Max HP"]//2
                            print("Lapras has been revived!")
                            print()
                            revives = revives - 1
                        x = False
                    elif item == "Hyper Potion":
                        if Charizard["HP"]==Charizard["Max HP"] and Lapras_P["HP"]==Lapras_P["Max HP"] and Blastoise["HP"]==Blastoise["Max HP"] and Alakazam["HP"]==Alakazam["Max HP"] and Venusaur["HP"]==Venusaur["Max HP"] and Jolteon["HP"]==Jolteon["Max HP"]:
                            print("All of your Pokemon are at full health!")
                            print()
                        else:
                            hyperp = HyperPotion(Charizard, Alakazam, Blastoise, Venusaur, Jolteon, Lapras_P, revives)
                            if hyperp == "Charizard":
                                Charizard["HP"]=Charizard["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Charizard["HP"]>=Charizard["Max HP"]:
                                    Charizard["HP"]=Charizard["Max HP"]
                                    print("Charizard has been fully healed!")
                                    print()
                                
                                else:
                                    print("Charizard has been healed 100 HP!")
                                    print()
                                    print("Charizard's current HP is: ", Charizard["HP"])
                                    print()
                            if hyperp == "Alakazam":
                                Alakazam["HP"]=Alakazam["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Alakazam["HP"]>=Alakazam["Max HP"]:
                                    Alakazam["HP"]=Alakazam["Max HP"]
                                    print("Alakazam has been fully healed!")
                                    print()
                                else:
                                    print("Alakazam has been healed 100 HP!")
                                    print()
                                    print("Alakazam's current HP is: ", Alakazam["HP"])
                                    print()
                            if hyperp == "Blastoise":
                                Blastoise["HP"]=Blastoise["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Blastoise["HP"]>=Blastoise["Max HP"]:
                                    Blastoise["HP"]=Blastoise["Max HP"]
                                    print("Blastoise has been fully healed!")
                                    print()
                                else:
                                    print("Blastoise has been healed 100 HP!")
                                    print()
                                    print("Blastoise's current HP is: ", Blastoise["HP"])
                                    print()
                            if hyperp == "Venusaur":
                                Venusaur["HP"]=Venusaur["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Venusaur["HP"]>=Venusaur["Max HP"]:
                                    Venusaur["HP"]=Venusaur["Max HP"]
                                    print("Venusaur has been fully healed!")
                                    print()
                                else:
                                    print("Venusaur has been healed 100 HP!")
                                    print()
                                    print("Venusaur's current HP is: ", Venusaur["HP"])
                                    print()
                            if hyperp == "Jolteon":
                                Jolteon["HP"]=Jolteon["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Jolteon["HP"]>=Jolteon["Max HP"]:
                                    Jolteon["HP"]=Jolteon["Max HP"]
                                    print("Jolteon has been fully healed!")
                                    print()
                                else:
                                    print("Jolteon has been healed 100 HP!")
                                    print()
                                    print("Jolteon's current HP is: ", Jolteon["HP"])
                                    print()
                            if hyperp == "Lapras":
                                Lapras_P["HP"]=Lapras_P["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Lapras_P["HP"]>=Lapras_P["Max HP"]:
                                    Lapras_P["HP"]=Lapras_P["Max HP"]
                                    print("Lapras has been fully healed!")
                                    print()
                                else:
                                    print("Lapras has been healed 100 HP!")
                                    print()
                                    print("Lapras's current HP is: ", Lapras_P["HP"])
                                    print()
                            
                        x = False
                        
                    else:
                        item = str(input("Enter the item: "))
                        print()
            if items == "No" or items == 'no':
                z = False
            else:
                print()
                items = str(input("Do you want to use an item? "))
                print()
        print("Prepare yourself!")    
        print()
        print()
        print("Agatha sends out her first Pokemon: Gengar!")
        print()
        
    ## Battling Agatha
    while EliteFour["Agatha"][1] == True:
        while player_active["HP"]>0 and enemy_active["HP"]>0:
            take_turn(player_active, enemy_active, Moves)
        if player_active["HP"]<=0:
            if body_count < 5:
                print()
                print(player_active["Name"], "has feinted!")
                player_active["Feint"]=True
                print("Send in your next Pokemon!")
                print()
                lyst = []
                if Charizard["Feint"]==False:
                    lyst.append("Charizard")
                if Alakazam["Feint"]==False:
                    lyst.append("Alakazam")
                if Blastoise["Feint"]==False:
                    lyst.append("Blastoise")
                if Venusaur["Feint"]==False:
                    lyst.append("Venusaur")
                if Jolteon["Feint"]==False:
                    lyst.append("Jolteon")
                if Lapras_P["Feint"]==False:
                    lyst.append("Lapras")
                print()
                for i in range(len(lyst)):
                    print(lyst[i])
                print()
                print("Who would you like to send in? ")
                print()
                switch = str(input("Enter next Pokemon: "))
                z = True
                while z:
                    if switch in lyst:
                        if switch == "Charizard":
                            current_player = 1
                        if switch == "Alakazam":
                            current_player = 2
                        if switch == "Blastoise":
                            current_player = 3
                        if switch == "Venusaur":
                            current_player = 4
                        if switch == "Jolteon":
                            current_player = 5
                        if switch == "Lapras":
                            current_player = 6
                        z = False
                    else:
                        print("Who would you like to send in? ")
                        print()
                        switch = str(input("Enter next Pokemon: "))
                        print()
                body_count = body_count + 1       
                player_active = player_team[current_player]
                print()
                print("Go,",player_active["Name"],"!" )
                print()
            else:
                player_team[0] = False
                EliteFour["Agatha"][1] = False
        if enemy_active["HP"]<=0:
            if current_enemy < len(EliteFour["Agatha"])-1:
                print()
                print(enemy_active["Name"], "has feinted!")
                print()
                print( "Agatha will send in her next Pokemon:")
                print()
                current_enemy = current_enemy+1
                enemy_active = enemy_team[current_enemy]
                print(enemy_active["Name"], "!")
                print()
            else:
                print()
                print(enemy_active["Name"], "has feinted!")
                print()
                EliteFour["Agatha"][1] = False
    if player_team[0] == False:
        print("You have run out of Pokemon!")
        player_team[0] = False
        print()
        print("Better luck next time.")
        return
    if EliteFour["Agatha"][1] == False:
        print("Agatha has been defeated!")
        print()
        print()
        enemy_team = EliteFour["Lance"]
        print()
        current_enemy = 2
        enemy_active = enemy_team[current_enemy]
        print("Now you must face the Dragon Master: Lance!")
        print()
        print("Would you like to use any items?")
        print()
        items = str(input("Enter 'Yes' or 'No': "))
        z = True
        while z:
            if items == 'yes' or items == "Yes":
                print("Which item do you want to use? \n")
                print(" Hyper Potion......x",str(hyper_potions)+"\n","Revive......x",str(revives)+"\n" )
                item = str(input("Enter the item: "))
                print()
                x = True
                while x:
                    if item == "Revive":
                        revive = Revive(Charizard, Alakazam, Blastoise, Venusaur, Jolteon, Lapras_P, revives)
                        if revive == "Failed":
                            print("None of your Pokemon have fainted!")
                            print()
                        if revive == "Charizard":
                            Charizard["Feint"]=False
                            Charizard["HP"]=Charizard["Max HP"]//2
                            print("Charizard has been revived!")
                            print()
                            revives = revives - 1
                        if revive == "Alakazam":
                            Alakazam["Feint"]=False
                            Alakazam["HP"]=Alakazam["Max HP"]//2
                            print("Alakazam has been revived!")
                            print()
                            revives = revives - 1
                        if revive == "Blastoise":
                            Blastoise["Feint"]=False
                            Blastoise["HP"]=Blastoise["Max HP"]//2
                            print("Blastoise has been revived!")
                            print()
                            revives = revives - 1
                        if revive == "Venusaur":
                            Venusaur["Feint"]=False
                            Venusaur["HP"]=Venusaur["Max HP"]//2
                            print("Venusaur has been revived!")
                            print()
                            revives = revives - 1
                        if revive == "Jolteon":
                            Jolteon["Feint"]=False
                            Jolteon["HP"]=Jolteon["Max HP"]//2
                            print("Jolteon has been revived!")
                            print()
                            revives = revives - 1
                        if revive == "Lapras":
                            Lapras_P["Feint"]=False
                            Lapras_P["HP"]=Lapras_P["Max HP"]//2
                            print("Lapras has been revived!")
                            print()
                            revives = revives - 1
                        x = False
                    elif item == "Hyper Potion":
                        if Charizard["HP"]==Charizard["Max HP"] and Lapras_P["HP"]==Lapras_P["Max HP"] and Blastoise["HP"]==Blastoise["Max HP"] and Alakazam["HP"]==Alakazam["Max HP"] and Venusaur["HP"]==Venusaur["Max HP"] and Jolteon["HP"]==Jolteon["Max HP"]:
                            print("All of your Pokemon are at full health!")
                            print()
                        else:
                            hyperp = HyperPotion(Charizard, Alakazam, Blastoise, Venusaur, Jolteon, Lapras_P, revives)
                            if hyperp == "Charizard":
                                Charizard["HP"]=Charizard["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Charizard["HP"]>=Charizard["Max HP"]:
                                    Charizard["HP"]=Charizard["Max HP"]
                                    print("Charizard has been fully healed!")
                                    print()
                                
                                else:
                                    print("Charizard has been healed 100 HP!")
                                    print()
                                    print("Charizard's current HP is: ", Charizard["HP"])
                                    print()
                            if hyperp == "Alakazam":
                                Alakazam["HP"]=Alakazam["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Alakazam["HP"]>=Alakazam["Max HP"]:
                                    Alakazam["HP"]=Alakazam["Max HP"]
                                    print("Alakazam has been fully healed!")
                                    print()
                                else:
                                    print("Alakazam has been healed 100 HP!")
                                    print()
                                    print("Alakazam's current HP is: ", Alakazam["HP"])
                                    print()
                            if hyperp == "Blastoise":
                                Blastoise["HP"]=Blastoise["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Blastoise["HP"]>=Blastoise["Max HP"]:
                                    Blastoise["HP"]=Blastoise["Max HP"]
                                    print("Blastoise has been fully healed!")
                                    print()
                                else:
                                    print("Blastoise has been healed 100 HP!")
                                    print()
                                    print("Blastoise's current HP is: ", Blastoise["HP"])
                                    print()
                            if hyperp == "Venusaur":
                                Venusaur["HP"]=Venusaur["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Venusaur["HP"]>=Venusaur["Max HP"]:
                                    Venusaur["HP"]=Venusaur["Max HP"]
                                    print("Venusaur has been fully healed!")
                                    print()
                                else:
                                    print("Venusaur has been healed 100 HP!")
                                    print()
                                    print("Venusaur's current HP is: ", Venusaur["HP"])
                                    print()
                            if hyperp == "Jolteon":
                                Jolteon["HP"]=Jolteon["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Jolteon["HP"]>=Jolteon["Max HP"]:
                                    Jolteon["HP"]=Jolteon["Max HP"]
                                    print("Jolteon has been fully healed!")
                                    print()
                                else:
                                    print("Jolteon has been healed 100 HP!")
                                    print()
                                    print("Jolteon's current HP is: ", Jolteon["HP"])
                                    print()
                            if hyperp == "Lapras":
                                Lapras_P["HP"]=Lapras_P["HP"]+100
                                hyper_potions = hyper_potions - 1
                                if Lapras_P["HP"]>=Lapras_P["Max HP"]:
                                    Lapras_P["HP"]=Lapras_P["Max HP"]
                                    print("Lapras has been fully healed!")
                                    print()
                                else:
                                    print("Lapras has been healed 100 HP!")
                                    print()
                                    print("Lapras's current HP is: ", Lapras_P["HP"])
                                    print()
                            
                        x = False
                        
                    else:
                        item = str(input("Enter the item: "))
                        print()
            if items == "No" or items == 'no':
                z = False
            else:
                print()
                items = str(input("Do you want to use an item? "))
                print()
        print("Prepare yourself!")    
        print()
        print()
        print("Lance sends out his first Pokemon: Gyarados!")
        print()
        
    ## Battling Lance
    while EliteFour["Lance"][1] == True:
        while player_active["HP"]>0 and enemy_active["HP"]>0:
            take_turn(player_active, enemy_active, Moves)
        if player_active["HP"]<=0:
            if body_count < 5:
                print()
                print(player_active["Name"], "has feinted!")
                player_active["Feint"]=True
                print("Send in your next Pokemon!")
                print()
                lyst = []
                if Charizard["Feint"]==False:
                    lyst.append("Charizard")
                if Alakazam["Feint"]==False:
                    lyst.append("Alakazam")
                if Blastoise["Feint"]==False:
                    lyst.append("Blastoise")
                if Venusaur["Feint"]==False:
                    lyst.append("Venusaur")
                if Jolteon["Feint"]==False:
                    lyst.append("Jolteon")
                if Lapras_P["Feint"]==False:
                    lyst.append("Lapras")
                print()
                for i in range(len(lyst)):
                    print(lyst[i])
                print()
                print("Who would you like to send in? ")
                print()
                switch = str(input("Enter next Pokemon: "))
                z = True
                while z:
                    if switch in lyst:
                        if switch == "Charizard":
                            current_player = 1
                        if switch == "Alakazam":
                            current_player = 2
                        if switch == "Blastoise":
                            current_player = 3
                        if switch == "Venusaur":
                            current_player = 4
                        if switch == "Jolteon":
                            current_player = 5
                        if switch == "Lapras":
                            current_player = 6
                        z = False
                    else:
                        print("Who would you like to send in? ")
                        print()
                        switch = str(input("Enter next Pokemon: "))
                        print()
                body_count = body_count + 1       
                player_active = player_team[current_player]
                print()
                print("Go,",player_active["Name"],"!" )
                print()
            else:
                player_team[0] = False
                EliteFour["Lance"][1] = False
        if enemy_active["HP"]<=0:
            if current_enemy < len(EliteFour["Lance"])-1:
                print()
                print(enemy_active["Name"], "has feinted!")
                hyper_check = False
                print()
                print( "Lance will send in his next Pokemon:")
                print()
                current_enemy = current_enemy+1
                enemy_active = enemy_team[current_enemy]
                print(enemy_active["Name"], "!")
            else:
                print()
                print(enemy_active["Name"], "has feinted!")
                print()
                EliteFour["Lance"][1] = False
    if player_team[0] == False:
        print("You have run out of Pokemon!")
        player_team[0] = False
        print()
        print("Better luck next time.")
        return
    if EliteFour["Lance"][1] == False:
        print("Lance has been defeated!")
        print()
        print()
        print("Congratulations on defeating the Elite Four!")
        print()
        print("Truly, you are a Pokemon Master!")
        print()
        print("Thanks for playing! Challenge us again sometime!")
        
    
if __name__ == "__main__":
    main()
    

