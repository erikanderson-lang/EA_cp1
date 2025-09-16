#EA_CP1 
print("The crew earned a whole bunch of money on the last outing (an input in dollars), but the captain didn't have time to divvy it all up before release everyone to port. He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares.")

total = int(input(f"What is he total amount they got?: "))
crew = int(input(f"how many crew members are there(excluding capain and first mate): "))
loot = total/(crew+2)
cap_shares = (loot*7)
first_shares = (loot*3)
crewshare = (loot-500)
print(f"crew members {crew}")
print(f"total money {total:.2f}")
print (f"captain got {cap_shares:.2f}") 
print (f"first mate got {first_shares:.2f} ")
print (f"crew got {crewshare:.2f} ")
