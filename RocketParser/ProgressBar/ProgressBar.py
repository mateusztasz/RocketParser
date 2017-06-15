import sys


class ProgressBar:
    prefix = 'Progress:'
    suffix = 'Complete'
    length = 50
    decimals = 0
    fill = '█'
    iteration = None
    total = None

    oldpercent = 0

    def setIteration(self, iteration):
        ProgressBar.iteration = iteration

    def setTotal(self, total):
        ProgressBar.total = total

    @staticmethod
    def print():
        percent = ("{0:." + str(ProgressBar.decimals) + "f}").format(100 * (ProgressBar.iteration / float(ProgressBar.total)))

        if percent != ProgressBar.oldpercent:
            filledLength = int(ProgressBar.length * ProgressBar.iteration // ProgressBar.total)+1
            bar = ProgressBar.fill * filledLength + '-' * (ProgressBar.length - filledLength)
            sys.stdout.write('\r%s |%s| %s%% %s' % (ProgressBar.prefix, bar, percent, ProgressBar.suffix))
            sys.stdout.flush()
            ProgressBar.oldpercent = percent

        if ProgressBar.iteration == ProgressBar.total:
            print()
