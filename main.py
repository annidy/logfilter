import argparse
from log import Log
from engine import Filter


parser = argparse.ArgumentParser(description='日志过滤器')
parser.add_argument('file', metavar='file', help='日志文件')
parser.add_argument('--tags',
                    help='tag like')
parser.add_argument('--level',
                    help='level than')

if __name__ == '__main__':
    args = parser.parse_args()

    logf = Filter(args)

    orgFile = open(args.file, "r")
    lines = orgFile.readlines()
    logList = []
    lastLog = None
    for line in lines:
        if lastLog is None:
            lastLog = Log.log_from_tag(line)
        else:
            newLog = Log.log_from_tag(line)
            if newLog is None:
                lastLog.append_contents(line)
            else:
                logList.append(lastLog)
                lastLog = newLog
    if lastLog:
        logList.append(lastLog)

    logList = filter(lambda log: logf.filter(log), logList)
    newFile = open(args.file+".log", "w")
    for log in logList:
        newFile.write(log.__str__())
        newFile.write("\n")

