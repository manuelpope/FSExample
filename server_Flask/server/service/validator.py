from models.Alert import AlertModel


class Validator_Sale():
    def __init__(self):
        pass

    @classmethod
    def validate_condition(cls, nameEntity, field, newValue):
        alerts = AlertModel.find_by_entity(nameEntity)
        field_valuation = [elem for elem in alerts if elem.field == field]
        result = []
        for i in field_valuation:
            eval_func = mapper_condition(i.condition)
            if (eval_func and eval_func(newValue, i.value)):
                result.append(i.id)
        return result


def mapper_condition(condition):
    dictionary = {'greater': greater,
                  "equal": equal,
                  "lesser": lesser

                  }
    return dictionary.get(condition)


def greater(a, b):
    return a > b


def equal(a, b):
    return a == b


def lesser(a, b):
    return a < b
