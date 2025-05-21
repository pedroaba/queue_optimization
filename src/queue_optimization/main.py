import pprint

from models.mm1k import MM1KModel


if __name__ == "__main__":
    model = MM1KModel()
    result = model.queue_mm1k(0.3, 0.5, 2, 1, 1)
    pprint.pprint(result)
