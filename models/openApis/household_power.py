from common.mongo_connect import conn_mongodb


class HOUSEHOLD_POWER():
    @staticmethod
    def find(page=1, offset=10):
        col = conn_mongodb().keti_pattern_recognition.household_info
        household_powers_cur = col.find().limit(10)
        household_powers = list()

        for _ in household_powers_cur:
            _['id'] = str(_['_id'])
            del _['_id']

            household_powers.append(_)

        return household_powers
