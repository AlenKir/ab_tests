
def get_mongo():
    from app import mongo
    return mongo



class StatisticsService:
    @staticmethod
    def get_statistics():
        stats = {}

        for experiment in ['button_color', 'price']:
            options_count = {}

            assignments = get_mongo().experiment_assignments.find()

            for assignment in assignments:
                value = assignment["experiments"].get(experiment)
                if value:
                    options_count[value] = options_count.get(value, 0) + 1

            stats[experiment] = options_count

        return stats
