class Log:
    """日志"""
    timestamp = None  # 时间
    thread = None  # 线程
    level = None  # 等级
    tag = None  #
    method = None  #
    contents = ""  # 内容（多行）

    @classmethod
    def log_from_tag(cls, line: str):
        if len(line) < 10:
            return None

        def tag_generator(stat: str, pos: int):
            if len(stat) - pos < 3:
                raise GeneratorExit
            if stat[pos] != '[':
                raise GeneratorExit
            end = stat.find(']', pos)
            if end < 0:
                raise GeneratorExit
            return stat[pos + 1:end], end + 1

        try:
            log = Log()
            log.timestamp, pos = tag_generator(line, 0)
            log.thread, pos = tag_generator(line, pos)
            log.level, pos = tag_generator(line, pos)
            log.tag, pos = tag_generator(line, pos)
            log.method, pos = tag_generator(line, pos)
            log.contents = line[pos + 1:-1]
            return log
        except GeneratorExit:
            return None

    def append_contents(self, line):
        self.contents = self.contents + line

    def __repr__(self):
        return "[{timestamp}][{thread}][{level}][{tag}][{method}]{contents}".format_map(self.__dict__)
