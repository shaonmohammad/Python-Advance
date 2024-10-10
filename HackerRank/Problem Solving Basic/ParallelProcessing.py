def minTime(files, numCores, limit):
    total_time = 0
    parallel = [file for file in files if file % numCores == 0]
    parallel.sort(reverse=True)
    for file in files:
        if (file % numCores != 0):
            total_time += file

    if (len(parallel) > limit or len(parallel) == limit):
        total_time += sum(parallel[limit:])
        for l in range(limit):
            total_time += parallel[l] / numCores
    elif limit > len(parallel):
        for l in range(len(parallel)):
            total_time += parallel[l]/numCores

    return int(total_time)


if __name__ == '__main__':
    n = int(input())
    files = []
    for i in range(n):
        files.append(int(input()))
    numCores = int(input())
    limit = int(input())
    print(minTime(files, numCores, limit))
