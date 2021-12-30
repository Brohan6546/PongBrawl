from pbrawl_sp import single
from pbrawl_mp import multi

print("======================================== WELCOME TO PONG BRAWL!!!! ========================================"
        + "\nSingleplayer: Do NOT let the ball touch the floor! Aim for the highest score!"
        + " \nMultiplayer: Go head to head with a friend! Who can keep the ball from"
        + " getting past your racket?! Choose what score to go up to.")
while True:
    gamemode = input("\n\nSelect Gamemode (1 for singleplayer 2 for multiplayer 3 for credits): ")
    if gamemode == "1":
        print("\n-------------------------------------------------------------------------------------------------"
              + "\nWelcome to Singleplayer mode! It's total madness against yourself as you battle a "
                + "progressively quickening ball and prevent it from passing your racket! How long can you prevent it"
              + " from touching the ground? \nChoose between easy medium or hard difficulties which change both the"
              + " starting speed of the ball and how much the speed increased per hit! \nCONTROLS: left"
              + "and right arrow keys to move racket. ENJOY!!"
              + "\n-------------------------------------------------------------------------------------------------")
        single()

        break
    elif gamemode == "2":
        print("\n-------------------------------------------------------------------------------------------------"
                + "\nWelcome to Multiplayer mode! Duke it out with a friend to see who can keep the ball from passing"
                + " their racket! \nBall will get progressively faster as the round goes on (This mode is somewhat"
                + " buggy :) \nCONTROLS: Left and right arrow keys for bottom player, 'a' and 'd' keys for top"
                + "racket. ENJOY!!"
                + "\n-------------------------------------------------------------------------------------------------")
        multi()
        break
    elif gamemode == "3":
        print("\n-------------------------------------------------------------------------------------------------"
                + "\nGame by Ruchit Patel. Special thanks to Professor Eric Pollizi for assigning the project that"
                + " got me started with making this game"\
                + "\n-------------------------------------------------------------------------------------------------")






