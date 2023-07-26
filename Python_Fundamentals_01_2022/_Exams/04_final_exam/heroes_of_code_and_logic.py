number_of_heroes = int(input())
party = {}
for hero in range(number_of_heroes):
    this_hero = input().split()
    this_name = this_hero[0]
    h_p = int(this_hero[1])
    m_p = int(this_hero[2])
    party[this_name] = [h_p, m_p]

command = input()
while command != "End":
    s_command = command.split(" - ")
    this_command = s_command[0]
    hero_name = s_command[1]
    if this_command == "CastSpell":
        needed_mp = int(s_command[2])
        spell = s_command[3]
        if party[hero_name][1] >= needed_mp:
            party[hero_name][1] -= needed_mp
            print(f"{hero_name} has successfully cast {spell} and now has {party[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell}!")
    elif this_command == "TakeDamage":
        damage = int(s_command[2])
        attacker = s_command[3]
        if party[hero_name][0] > damage:
            party[hero_name][0] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {party[hero_name][0]} HP left!")
        else:
            del party[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
    elif this_command == "Recharge":
        add_mp = int(s_command[2])
        current_mp = party[hero_name][1]
        if (current_mp + add_mp) > 200:
            party[hero_name][1] = 200
            recharge = 200 - current_mp
        else:
            party[hero_name][1] += add_mp
            recharge = add_mp
        print(f"{hero_name} recharged for {recharge} MP!")
    elif this_command == "Heal":
        add_hp = int(s_command[2])
        current_hp = party[hero_name][0]
        if current_hp + add_hp > 100:
            party[hero_name][0] = 100
            recharge = 100 - current_hp
        else:
            party[hero_name][0] += add_hp
            recharge = add_hp
        print(f"{hero_name} healed for {recharge} HP!")
    command = input()

for hero, data in party.items():
    print(f"{hero}")
    print(f"  HP: {data[0]}")
    print(f"  MP: {data[1]}")


