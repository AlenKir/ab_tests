import random


class Experiment:
    BUTTON_COLORS = ['#FF0000', '#00FF00', '#0000FF']
    PRICES = [10, 20, 50, 5]
    PROBABILITIES = [0.75, 0.1, 0.05, 0.1]

    @staticmethod
    def generate_experiment_data():
        return {
            "button_color": random.choice(Experiment.BUTTON_COLORS),
            "price": random.choices(Experiment.PRICES, Experiment.PROBABILITIES)[0]
        }
