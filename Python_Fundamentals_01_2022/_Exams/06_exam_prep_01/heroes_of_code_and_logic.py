number_of_heroes = int(input())
heroes = {}
for hero in range(number_of_heroes):
    hero_data = input().split()
    hero_name = hero_data[0]
    hero_hp = int(hero_data[1])
    hero_mp = int(hero_data[2])
    heroes[hero_name] = [hero_hp, hero_mp]

command = input()
while command != "End":
    current_command = command.split(" - ")
    this_command = current_command[0]
    name = current_command[1]
    if this_command == "CastSpell":
        mp_needed = int(current_command[2])
        spell_name = current_command[3]
        if heroes[name][1] >= mp_needed:
            heroes[name][1] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    elif this_command == "TakeDamage":
        damage = int(current_command[2])
        attacker = current_command[3]
        heroes[name][0] -= damage
        if heroes[name][0] <= 0:
            del heroes[name]
            print(f"{name} has been killed by {attacker}!")
        else:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!")
    elif this_command == "Recharge":
        amount = int(current_command[2])
        old_mp = heroes[name][1]
        heroes[name][1] += amount
        if heroes[name][1] > 200:
            heroes[name][1] = 200
        recharge = heroes[name][1] - old_mp
        print(f"{name} recharged for {recharge} MP!")
    elif this_command == "Heal":
        heal_amount = int(current_command[2])
        old_hp = heroes[name][0]
        heroes[name][0] += heal_amount
        if heroes[name][0] > 100:
            heroes[name][0] = 100
        heal_recharge = heroes[name][0] - old_hp
        print(f"{name} healed for {heal_recharge} HP!")
    command = input()
for name, data in heroes.items():
    print(f"{name}")
    print(f"  HP: {data[0]}")
    print(f"  MP: {data[1]}")