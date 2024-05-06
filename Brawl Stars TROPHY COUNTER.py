brawlers = int(input("How many brawlers do you want to push? "))
trophy_count_push = int(input("How many trophies is your goal? (on each brawler) "))
data_gain = brawlers * trophy_count_push
each_brawler_trophy = input("Enter current trophies for each brawler, separate with comma (,) ")
ohio_final_boss = list(map(int, each_brawler_trophy.split(",")))
total_trophies = sum(ohio_final_boss)
total_trophies = data_gain - total_trophies
leaguetrophy = int(input("How many trophies do you currently have? "))
print("Trophies gained:", total_trophies)
after_push_leaguetrophy = leaguetrophy + total_trophies 
print(f"You are going to have {after_push_leaguetrophy} trophies.")