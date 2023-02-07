class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)

    def enroll(self):
        if(self.is_rewards_member):
            print("User already a member.")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 20

    def spend_points(self, amount):
        if(self.gold_card_points - amount >= 0):
            self.gold_card_points -= amount
        else:
            print("Not enough points.")