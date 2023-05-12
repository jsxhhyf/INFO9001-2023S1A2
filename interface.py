"""
Write your solution for the class Interface here.
This is your answer for Question 8.4.

Author:
SID:
Unikey:
"""
from cshop import CheeseShop
from hunter import Hunter
from mouse import Mouse
from trap import Trap


class Interface:
    def __init__(self, player: Hunter = Hunter()):
        self.menu = {"1": "Exit game", "2": "Join the Hunt", "3": "The Cheese Shop", "4": "Change Cheese"}
        self.player = player

    def set_player(self, player: Hunter) -> None:
        if not isinstance(player, Hunter):
            print("Invalid argument!\nThe argument player should be a Hunter object.")
            return
        self.player = player

    def get_menu(self):
        ret = [
            f"What do ye want to do now, Hunter {self.player.get_name()}?",
            f"1. - {self.menu['1']}",
            f"2. - {self.menu['2']}",
            f"3. - {self.menu['3']}",
            f"4. - {self.menu['4']}",
        ]
        return "\n".join(ret)

    def change_cheese(self) -> None:
        print(f"Hunter {self.player.get_name()}, you currently have:")
        print(self.player.get_cheese())

        while True:
            pl_cheese_choice_input = input("Type cheese name to arm trap: ").strip().lower()
            if pl_cheese_choice_input == "back":
                return
            elif pl_cheese_choice_input == "cheddar":
                if self.player.have_cheese("Cheddar") > 0:
                    if self.player.get_trap().get_one_time_enchantment():
                        print(
                            f"Your One-time Enchanted {self.player.get_trap().get_trap_name()} has a one-time enchantment granting +25 points drop by Brown mouse."
                        )
                    pl_confirm_change_input = input("Do you want to arm your trap with Cheddar? ").strip().lower()
                    if pl_confirm_change_input == "yes":
                        self.player.arm_trap("Cheddar")
                        print(f"{self.player.get_trap().get_trap_name()} is now armed with Cheddar!")
                        return
                    elif pl_confirm_change_input == "back":
                        print("")
                        return
                    else:
                        print("")
                else:
                    print("Out of cheese!")
                    continue
            elif pl_cheese_choice_input == "marble":
                if self.player.have_cheese("Marble") > 0:
                    if self.player.get_trap().get_one_time_enchantment():
                        print(
                            f"Your One-time Enchanted {self.player.get_trap().get_trap_name()} has a one-time enchantment granting +25 gold drop by Brown mouse."
                        )
                    pl_confirm_change_input = input("Do you want to arm your trap with Marble? ").strip().lower()
                    if pl_confirm_change_input == "yes":
                        self.player.arm_trap("Marble")
                        print(f"{self.player.get_trap().get_trap_name()} is now armed with Marble!")
                        return
                    elif pl_confirm_change_input == "back":
                        print("")
                        return
                    else:
                        print("")
                    self.player.arm_trap("Marble")
                else:
                    print("Out of cheese!")
                    continue
            elif pl_cheese_choice_input == "swiss":
                if self.player.have_cheese("Swiss") > 0:
                    if self.player.get_trap().get_one_time_enchantment():
                        print(
                            f"Your One-time Enchanted {self.player.get_trap().get_trap_name()} has a one-time enchantment granting +0.25 attraction rate to Tiny mouse."
                        )
                    pl_confirm_change_input = input("Do you want to arm your trap with Swiss? ").strip().lower()
                    if pl_confirm_change_input == "yes":
                        self.player.arm_trap("Swiss")
                        print(f"{self.player.get_trap().get_trap_name()} is now armed with Swiss!")
                        return
                    elif pl_confirm_change_input == "back":
                        print("")
                        return
                    else:
                        print("")
                    self.player.arm_trap("Swiss")
                else:
                    print("Out of cheese!")
                    continue
            else:
                print("No such cheese!")
                continue

    def cheese_shop(self) -> None:
        cheese_shop = CheeseShop()
        print(cheese_shop.greet())
        cheese_shop.move_to(self.player)

    def hunt(self) -> None:
        num_fails = 0
        while True:
            if num_fails == 5:
                pl_continue = input("Do you want to continue the hunt? ").strip().lower()
                if pl_continue != "yes":
                    break
                else:
                    num_fails = 0
            print("Sound the horn to call for the mouse...")
            pl_horn_input = input('Sound the horn by typing "yes": ').strip().lower()
            print("")

            if pl_horn_input == "yes":
                self.player.get_trap().set_one_time_enchantment(False)
                if self.player.have_cheese(self.player.get_trap().get_trap_cheese()) == 0:
                    print("Nothing happens. You are out of cheese!")
                    num_fails += 1
                else:
                    self.player.consume_cheese(self.player.get_trap().get_trap_cheese())
                    caught_mouse = Mouse(
                        self.player.get_trap().get_trap_cheese(), self.player.get_trap().get_one_time_enchantment()
                    )
                    if caught_mouse.get_name() is None:
                        num_fails += 1
                        print("Nothing happens.", end=" ")
                        if self.player.have_cheese(self.player.get_trap().get_trap_cheese()) == 0:
                            print("You are out of cheese!")
                        else:
                            print("")
                    else:
                        num_fails = 0
                        print(f"Caught a {caught_mouse.get_name()} mouse!")
                        print(caught_mouse.get_coat())
                        # check the enchantment benefit
                        if self.player.get_trap().get_one_time_enchantment():
                            value, reward, mouse = Trap.get_benefit(self.player.get_trap().get_trap_cheese())
                            if (
                                self.player.get_trap().get_trap_cheese() == "Cheddar"
                                and caught_mouse.get_name() == "Brown"
                            ):
                                self.player.update_gold(caught_mouse.get_gold())
                                self.player.update_points(caught_mouse.get_points() + 25)
                            elif (
                                self.player.get_trap().get_trap_cheese() == "Marble"
                                and caught_mouse.get_name() == "Brown"
                            ):
                                self.player.update_gold(caught_mouse.get_gold() + 25)
                                self.player.update_points(caught_mouse.get_points())
                        else:
                            self.player.update_gold(caught_mouse.get_gold())
                            self.player.update_points(caught_mouse.get_points())

                        if self.player.have_cheese(self.player.get_trap().get_trap_cheese()) == 0:
                            print("You are out of cheese!")
                        else:
                            print("")
            elif pl_horn_input == "stop hunt":
                break
            else:
                num_fails += 1
                print("Do nothing.")

            print(f"My gold: {self.player.get_gold()}, My points: {self.player.get_points()}")

    def move_to(self, choice: int) -> int:
        if not isinstance(choice, int):
            print("Invalid input. Try again!")
            return -1
        if choice == 1:
            return 0
        elif choice == 2:
            self.hunt()
        elif choice == 3:
            self.cheese_shop()
        elif choice == 4:
            self.change_cheese()
            # TODO when trap is armed with None cheese
        elif choice < 1 or choice > 4:
            print("Must be between 1 and 4.")
            return -1

        return 1
