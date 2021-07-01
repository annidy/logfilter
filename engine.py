from log import Log


def like(patten: str, text: str):
    if patten is None:
        return True
    if len(patten) == 0:
        return True
    return text.lower().find(patten.lower()) >= 0


def level_than(level: str, text: str):
    if level == 'E' and (text == 'E'):
        return True
    if level == 'W' and (text == 'E' or text == 'W'):
        return True
    if level == 'I' and (text == 'E' or text == 'W' or text == 'I'):
        return True

    return False


class Filter:
    """过滤器"""
    args = {}

    def __init__(self, args):
        self.tags = args.tags.split(',')
        self.level = args.level
        pass

    def filter(self, log: Log):
        return any(like(tag, log.tag) for tag in self.tags) or level_than(self.level, log.level)
