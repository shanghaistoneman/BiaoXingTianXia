import random
import math

class Caravan:
    def __init__(self, destination, distance_factor, cargo_value):
        self.destination = destination
        self.distance_factor = distance_factor
        self.cargo_value = cargo_value
        self.escort_fee = int(cargo_value * 0.05 * distance_factor)

    def __str__(self):
        return f"押运任务：目的地{self.destination}，货物价值{self.cargo_value}两，押运费{self.escort_fee}两"

def main():
    silver = 10000
    strength = 10
    popularity = 10
    level = 1

    destinations = [
        ("金陵", 1),
        ("钱塘", 2),
        ("荆州", 4),
        ("洛阳", 5),
        ("广州", 8),
        ("长安", 10),
        ("太原", 10),
        ("幽州", 13),
        ("成都", 18)
    ]

    print("欢迎扬州威远镖局总镖头回家，目前镖局业务刚刚起步，资产只有白银1万两，声望和武力都还比较低，被评为等级最低的1级镖局。", end="\n\n")
    print("有几个客户已经发来了走镖任务，赶紧看看吧，不过距离越远路上意外越多，走镖失败可是要按货物价值赔偿的，切记量力而行", end="\n\n")
    print(f"镖局当前资产：{silver}两，镖局武力：{strength}，镖局声望：{popularity}")

    while silver >= 0 and popularity >= 0 and ( silver < 1000000 or popularity < 1000 ) :
        choice = input("现在先招募镖师，还是发个宣传广告，或是直接开始走镖？(输入1招募镖师，输入2发布广告，输入3开始走镖)：")

        if choice == "1":
            recruit_cost = int(input("这次招募镖师要花费多少招募费用（招募费用为1000两的整数倍）？："))
            if recruit_cost % 1000 != 0 or recruit_cost < 1000:
                print("招募费用必须是1000两的整数倍，且最少1000两。", end="\n\n")
            elif silver >= recruit_cost:
                silver -= recruit_cost
                old_strength = strength
                strength += random.randint(1, recruit_cost*recruit_cost // 1000000)
                if strength - old_strength < 5 :
                    print(f"花费招募费用{recruit_cost}两，招到一名普通趟子手，镖局武力增长{strength - old_strength}", end="\n\n")
                elif strength - old_strength < 15 :
                    print(f"花费招募费用{recruit_cost}两，招到一名资深镖师，镖局武力增长{strength - old_strength}", end="\n\n")
                elif strength - old_strength < 45 :
                    print(f"花费招募费用{recruit_cost}两，招到一名武林名宿，镖局武力增长{strength - old_strength}", end="\n\n")
                else :
                    print(f"花费招募费用{recruit_cost}两，招到一名绝世高手，镖局武力增长{strength - old_strength}", end="\n\n")
                print(f"镖局当前资产：{silver}两，镖局武力：{strength}，镖局声望：{popularity}")
            else:
                print("资金不足，无法招募镖师。", end="\n\n")
        if choice == "2":
            advertising_cost = int(input("这次发布广告要花费多少招募费用（招募费用为10000两的整数倍）？："))
            if advertising_cost % 10000 != 0 or advertising_cost < 10000:
                print("招募费用必须是10000两的整数倍，且最少10000两。", end="\n\n")
            elif silver >= advertising_cost:
                silver -= advertising_cost
                old_popularity = popularity
                popularity += random.randint(1, advertising_cost*advertising_cost // 100000000)
                if popularity - old_popularity < 5 :
                    print(f"花费广告费用{advertising_cost}两，宣传效果平平，镖局声望提升{popularity - old_popularity}", end="\n\n")
                elif popularity - old_popularity < 15 :
                    print(f"花费广告费用{advertising_cost}两，宣传有点效果，引来几家新客户，镖局声望提升{popularity - old_popularity}", end="\n\n")
                elif popularity - old_popularity < 45 :
                    print(f"花费广告费用{advertising_cost}两，镖局名号传的满城皆知，镖局声望提升{popularity - old_popularity}", end="\n\n")
                else :
                    print(f"花费广告费用{advertising_cost}两，镖局一时声名大噪，周边城市的商家都慕名而来，镖局声望提升{popularity - old_popularity}", end="\n\n")
                print(f"镖局当前资产：{silver}两，镖局武力：{strength}，镖局声望：{popularity}")
            else:
                print("资金不足，无法发布广告。", end="\n\n")
        elif choice == "3":
            selected_destinations = random.sample(destinations, 3)
            caravans = [
                Caravan(destination, distance_factor, random.randint(1000, 10000 * level))
                for destination, distance_factor in selected_destinations
            ]
            print("可选的走镖任务如下：")
            for i, caravan in enumerate(caravans):
                print(f"{i + 1}. {caravan}")
            print("4. 这些镖风险太大，全都放弃吧(损失定金1000两)")
            task_choice = int(input("请选择一个走镖任务（输入任务编号）：")) - 1
            if task_choice == 3 :
                silver -= 1000
                print(f"镖局当前资产：{silver}两，镖局武力：{strength}，镖局声望：{popularity}")
            elif task_choice == 0 or task_choice == 1 or task_choice == 2 :
                caravan = caravans[task_choice]
                success_chance = random.uniform(0.1, strength / caravan.distance_factor)

                event = random.randint(1, 6)
                if event == 1:
                    silver -= int(caravan.cargo_value * 0.05)
                    print(f"遇到绿林拦路，缴纳过路费，损失财产{int(caravan.cargo_value * 0.05)}", end="\n\n")
                elif event == 2:
                    strength += int(strength * 0.1)
                    print(f"迷路误入秘境，捡到武功秘籍，镖局武力提升{int(strength * 0.1)}", end="\n\n")
                elif event == 3:
                    strength -= int(strength * 0.05)
                    print(f"迷路误入山崖，镖师摔伤，镖局武力下降{int(strength * 0.05)}", end="\n\n")
                elif event == 4:
                    silver -= int(caravan.cargo_value * 0.1)
                    print(f"遇到山贼，一番激战后逃脱，损失财产{int(caravan.cargo_value * 0.1)}", end="\n\n")
                elif event == 5:
                    silver += strength * 200
                    print(f"遇到山贼，一番激战后成功剿灭，从山贼巢穴获得财宝，镖局资产增加{strength * 200}", end="\n\n")
                elif event == 6:
                    popularity += level
                    print(f"救助晕倒路边的陌生人，醒来原来是一名朝廷命官，镖局声望提升{level}", end="\n\n")
                elif event == 7:
                    popularity -= level
                    print(f"遇到恶人碰瓷，招来百姓围观，却百口莫辩，镖局声望下降{level}", end="\n\n")

                if success_chance >= 0.5:
                    silver += caravan.escort_fee
                    popularity += int(caravan.escort_fee / 100)
                    print("顺利抵达，走镖成功，皆大欢喜！")
                    print(f"获得押运费{caravan.escort_fee}两，镖局声望提升{int(caravan.escort_fee / 100)}", end="\n\n")
                    print(f"镖局当前资产：{silver}两，镖局武力：{strength}，镖局声望：{popularity}")
                    if popularity > ( level + 1) * (level + 1) * 10 :
                       level = int(math.sqrt(popularity / 10))
                       print(f"随着声望提升，镖局等级升级为{level}级,可以接到货物价值更高的走镖任务了！")
                else:
                    silver -= caravan.cargo_value
                    strength -= int(strength * 0.2)
                    popularity -= int(caravan.escort_fee / 100)
                    print("路遇强大匪徒，货物全部被劫，镖师多人伤亡，走镖失败，损失惨重！")
                    print(f"镖局资产损失{caravan.cargo_value}两，镖局武力下降{int(strength * 0.2)}，镖局声望降低{int(caravan.escort_fee / 100)}", end="\n\n")
                    print(f"镖局当前资产：{silver}两，镖局武力：{strength}，镖局声望：{popularity}")
                    if popularity < level * level * 10 and popularity > 0 :
                       level = int(math.sqrt(popularity / 10))
                       print(f"随着声望降低，镖局等级下降为{level}级,货物价值很高的走镖任务不找我们做了！")

    if silver >= 1000000 and popularity >= 1000:
        print("结局：镖局运营成功，威震天下，富甲一方")
    else:
        print("结局：镖局运营凄惨，身败名裂，倒闭破产")
    a = input("任意输入结束游戏...")
	
if __name__ == "__main__":
    main()