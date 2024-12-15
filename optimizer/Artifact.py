import itertools 
import string

class Artifact:
    def __init__(self, name, set_name, artifact_type, main_stat, sub_stats):
        self.name = name                      # ชื่อของ Artifact
        self.set_name = set_name              # ชื่อของเซ็ต Artifact
        self.artifact_type = artifact_type    # ประเภทของ Artifact
        self.main_stat = main_stat            # ค่าพลังหลัก
        self.sub_stats = sub_stats            # ค่าพลังรอง (List of dicts)

    def __repr__(self):
        return f"Artifact(name={self.name}, set={self.set_name}, type={self.artifact_type})"

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Set: {self.set_name}")
        print(f"Type: {self.artifact_type}")
        print(f"Main Stat: {self.main_stat['name']} +{self.main_stat['value']}")
        print(f"Sub Stats:")
        for sub_stat in self.sub_stats:
            print(f"  - {sub_stat['name']} +{sub_stat['value']}")




def example_usage():
    print("Example Usage")


    # Example Usage
    artifact_1 = Artifact(
        name="Flower of Life1",
        set_name="Gladiator's Finale",
        artifact_type="Flower",
        main_stat={"name": "HP", "value": 4780},
        sub_stats=[
            {"name": "ATK%", "value": 5.8},
            {"name": "CRIT Rate%", "value": 3.1},
            {"name": "Energy Recharge%", "value": 4.5},
            {"name": "DEF", "value": 19}
        ]
    )

    artifact_2 = Artifact(
        name="Flower of Life2",
        set_name="Gladiator's Finale",
        artifact_type="Flower",
        main_stat={"name": "HP", "value": 4780},
        sub_stats=[
            {"name": "ATK%", "value": 10.8},
            {"name": "CRIT Rate%", "value": 20.5},
            {"name": "CRIT DMG", "value": 20},
            {"name": "Energy Recharge%", "value": 4.5}
        ]
    )

    artifact_3 = Artifact(
        name="Flower of Life3",
        set_name="Gladiator's Finale",
        artifact_type="Flower",
        main_stat={"name": "HP", "value": 4780},
        sub_stats=[
            {"name": "ATK%", "value": 2},
            {"name": "CRIT Rate%", "value": 3},
            {"name": "DEF", "value": 1},
            {"name": "Energy Recharge%", "value": 4.5}
        ]
    )

    artifact_4 = Artifact(
        name="Flower of Life44444",
        set_name="Gladiator's Finale",
        artifact_type="Flower",
        main_stat={"name": "HP", "value": 4780},
        sub_stats=[
            {"name": "ATK%", "value": 99},
            {"name": "CRIT Rate%", "value": 99},
            {"name": "DEF", "value": 99},
            {"name": "Energy Recharge%", "value": 99}
        ]
    )



    # artifact_1.display_info()

    sum_atkP = 0
    sum_Er = 0
    sum_criR = 0
    sum_criD = 0

    #####qc
    box = [artifact_1, artifact_2]
    for artifact in box:
        for substat in artifact.sub_stats:
            if "ATK%" in substat['name']:
                sum_atkP += int(substat['value'])
            elif "CRIT Rate%" in substat['name']:
                sum_criR += int(substat['value'])
            elif "CRIT DMG" in substat['name']:
                sum_criD += int(substat['value'])

    print(f"ATK%: {sum_atkP}")
    print(f"Cri rate:  {sum_criR}")
    print(f"Cri dmg:  {sum_criD}")
    #####qc






def allPossible(mixer_box):
    print('from allPossible() mixer_box')
    # print(mixer_box)
    #Remove empty lists from mixer_box
    filtered_mixer_box = [box for box in mixer_box if box]


    # Flower_1 = Artifact(
    #     name="Flower1",
    #     set_name="Gladiator's Finale",
    #     artifact_type="Flower",
    #     main_stat={"name": "HP", "value": 4780},
    #     sub_stats=[
    #         {"name": "ATK%", "value": 5.8},
    #         {"name": "CRIT Rate%", "value": 3.1},
    #         {"name": "Energy Recharge%", "value": 4.5},
    #         {"name": "DEF", "value": 19}
    #     ]
    # )

    # Flower_2 = Artifact(
    #     name="Flower2",
    #     set_name="Gladiator's Finale",
    #     artifact_type="Flower",
    #     main_stat={"name": "HP", "value": 4780},
    #     sub_stats=[
    #         {"name": "ATK%", "value": 5.8},
    #         {"name": "CRIT Rate%", "value": 3.1},
    #         {"name": "Energy Recharge%", "value": 4.5},
    #         {"name": "DEF", "value": 19}
    #     ]
    # )

    # Feather_1 = Artifact(
    #     name="Feather1",
    #     set_name="Gladiator's Finale",
    #     artifact_type="Feather",
    #     main_stat={"name": "HP", "value": 4780},
    #     sub_stats=[
    #         {"name": "ATK%", "value": 5.8},
    #         {"name": "CRIT Rate%", "value": 3.1},
    #         {"name": "Energy Recharge%", "value": 4.5},
    #         {"name": "DEF", "value": 19}
    #     ]
    # )

    # Feather_2 = Artifact(
    #     name="Feather2",
    #     set_name="Gladiator's Finale",
    #     artifact_type="Feather",
    #     main_stat={"name": "HP", "value": 4780},
    #     sub_stats=[
    #         {"name": "ATK%", "value": 5.8},
    #         {"name": "CRIT Rate%", "value": 99},
    #         {"name": "Energy Recharge%", "value": 4.5},
    #         {"name": "DEF", "value": 19}
    #     ]
    # )

    # Sand_1 = Artifact(
    #     name="Sand1",
    #     set_name="Gladiator's Finale",
    #     artifact_type="Sand",
    #     main_stat={"name": "HP", "value": 4780},
    #     sub_stats=[
    #         {"name": "ATK%", "value": 5.8},
    #         {"name": "CRIT Rate%", "value": 3.1},
    #         {"name": "Energy Recharge%", "value": 4.5},
    #         {"name": "DEF", "value": 19}
    #     ]
    # )

    # flower_box =[Flower_1,Flower_2]
    # feather_box = [Feather_1,Feather_2]
    # sand_box = [Sand_1]
    # mixer_box = [flower_box, feather_box, sand_box]

    for combination in itertools.product(*filtered_mixer_box):
        sum_hp_plat = 0  #hp
        sum_hp_per = 0   #hp%
        sum_atk_plat = 0 #atk
        sum_atk_per = 0  #atk%
        sum_def_plat = 0 #def
        sum_def_per = 0 #def%
        sum_em = 0      #em
        sum_Er = 0      #ER
        sum_criR = 0    #cri rate
        sum_criD = 0    #cri dmg
        # print(f"all possible= {len(combination)}")
        for arti in combination:
            # print(arti.name)
            # print(arti.sub_stats)
            for substat in arti.sub_stats:
                if "HP" == substat['name']:
                    sum_hp_plat += int(substat['value'])
                elif "HP%" == substat['name']:
                    sum_hp_per += int(substat['value'])
                elif "DEF" == substat['name']:
                    sum_def_plat += int(substat['value'])
                elif "DEF%" == substat['name']:
                    sum_def_per += int(substat['value'])
                elif "ATK" == substat['name']:
                    sum_atk_plat += int(substat['value'])
                elif "ATK%" == substat['name']:
                    sum_atk_per += int(substat['value'])
                elif "EM" in substat['name']:
                    sum_em += int(substat['value'])
                elif "ER" in substat['name']:
                    sum_Er += int(substat['value'])
                elif "CR" in substat['name']:
                    sum_criR += int(substat['value'])
                elif "CD" in substat['name']:
                    sum_criD += int(substat['value'])

        if sum_hp_plat != 0:print(f"HP: {sum_hp_plat}")
        if sum_hp_per != 0:print(f"HP%: {sum_hp_per }")
        if sum_atk_plat != 0:print(f"ATK: {sum_atk_plat }")
        if sum_atk_per != 0:print(f"ATK%: {sum_atk_per }")
        if sum_def_plat != 0:print(f"DEF: {sum_def_plat }")
        if sum_def_per != 0:print(f"DEF%: {sum_def_per }")
        if sum_em != 0:print(f"EM: {sum_em}")
        if sum_Er != 0:print(f"ER: {sum_Er}")
        if sum_criR != 0:print(f"Cri Rate: {sum_criR }")
        if sum_criD != 0:print(f"Cri Damage: {sum_criD }")
        
        print('---')


def bfpw():
    txt = 'abc'
    passwd = 'admin555'
    stringgs = string.ascii_lowercase + string.ascii_uppercase + string.digits

    # for combination in itertools.product(stringgs,repeat=8):
    #     print(combination)
    #     comp = ''
        # for ele in combination:
        #     comp = comp + ele
        #     print(comp)
        # if passwd == comp:
        #     print(comp)
        #     break

if __name__ =='__main__':
    # allPossible()
    bfpw()



