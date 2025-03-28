class LoyaltyProgram:
    def __init__(self):
        self.__rewards = {}

    def add_program(self, points_required, reward):
        '''
        This method adds a reward with required points.
        '''
        self.__rewards[points_required] = reward

    def remove_program(self, points_required):
        '''
        This method removed the reward from the loyalty program
        :param points_required:
        :return:
        '''
        if points_required in self.__rewards:
            del self.__rewards[points_required]

    def get_eligible_rewards(self, guest):
        '''
        This method takes in the object of guest and returns the rewards he/she might be eligible for.
        :param guest:
        :return:
        '''
        rewards = ""
        for points, reward in self.__rewards.items():
            if guest.get_loyalty_points() >= points:
                rewards+= (reward + ",")

        return rewards

    def get_rewards(self):
        return self.__rewards
