class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name, self.last_name, self.email, self.age, self.is_rewards_member, self.gold_card_points)

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

        if self.is_rewards_member:
            print("user already a member")
            return self

    def spend_point(self, amount):
        self.gold_card_points -= amount


my_user = User("Balaki", "Douglas", "balaki@gmail.com", 55)

user2 = User("Rose", "Marc", "rose@codingdojo.com", 29)

user3 = User("Jeff", "Bezos", "jeff@codingdojo.com", 32)


my_user.display_info()
my_user.enroll()  
my_user.display_info()
user2.enroll()
user2.spend_point (80)
my_user.display_info()
user2.display_info()
user2.spend_point(80)
user3.display_info()



# user1.display_info().enroll().spend_points(50).display_info()
# user2.enroll().spend_points(80).display_info()
