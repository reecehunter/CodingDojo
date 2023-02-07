class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        return self

    def enroll(self):
        if(self.is_rewards_member):
            print("User already a member.")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 20
        return self

    def spend_points(self, amount):
        if(self.gold_card_points - amount >= 0):
            self.gold_card_points -= amount
        else:
            print("Not enough points.")
        return self

user1 = User("Reece", "Hunter", "reece@mail.com", 22)
user2 = User("Kyle", "Wallace", "kyle@mail.com", 80)

user1.display_info().enroll().spend_points(50).display_info()
user2.display_info().enroll().spend_points(50).display_info()