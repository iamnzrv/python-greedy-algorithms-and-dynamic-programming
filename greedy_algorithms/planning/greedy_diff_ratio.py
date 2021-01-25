class Job(object):
    def __init__(self, length, weight):
        self.length = length
        self.weight = weight

    def __str__(self):
        return str(self.length) + " " + str(self.weight)


def print_sum_end_time(jobs, comparator):
    jobs.sort(key=comparator, reverse=True)  # greedy ratio
    end_time = 0
    sum_end_time = 0
    for job in jobs:
        end_time += job.length
        sum_end_time += job.weight * end_time
    print(sum_end_time)


def main():
    read_jobs = []
    f = open("../../challenge13.4.txt", "r")
    numOfCases = int(f.readline())
    for i in range(0, numOfCases):
        line = f.readline()
        job_data = list(map(lambda x: int(x), line.rstrip().split(" ")))
        read_jobs.append(Job(job_data[0], job_data[1]))

    print_sum_end_time(read_jobs, lambda x: x.weight - x.length)  # greedy diff
    print_sum_end_time(read_jobs, lambda x: x.weight / x.length)  # greedy ratio


main()
