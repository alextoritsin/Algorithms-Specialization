# Uses python3

def count_refils(stops, m):
    last_station = -1
    refils = last_refil =  0
    while last_station + 1 != len(stops):
        if stops[last_station + 1] - last_refil > m:
            return -1

        while stops[last_station + 1] - last_refil <= m:
            if last_station + 1 == len(stops) - 1:
                return refils

            last_station += 1

        refils += 1
        last_refil = stops[last_station]
    
    return refils

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, input().split()))
    stops.append(d)
    print(count_refils(stops, m))