import math

def solution(fees, records):
    answer = []
    
    basic_time, basic_cost, unit_time, unit_cost = fees
    in_cars, time_check = {}, {}
    for r in records:
        time, car, cmd = r.split()
        if cmd == "IN":
            in_cars[car] = time
        elif cmd == "OUT":
            init_time = in_cars.pop(car)
            if car in time_check:
                time_check[car] += calculate_time_diff(init_time, time)
            else:
                time_check[car] = calculate_time_diff(init_time, time)
    
    for car, init_time in in_cars.items():
        if car in time_check:
            time_check[car] += calculate_time_diff(init_time, "23:59")
        else:
            time_check[car] = calculate_time_diff(init_time, "23:59")
    
    result = sorted([(car, time) for car, time in time_check.items()])
    for car, time in result:
        if time <= basic_time:
            answer.append(basic_cost)
        else:
            answer.append(math.ceil((time - basic_time) / unit_time) * unit_cost + basic_cost)
    
    return answer

def calculate_time_diff(init, end):    
    end_h, end_m = map(int, end.split(":"))
    init_h, init_m = map(int, init.split(":"))
    
    return (end_h - init_h) * 60 + end_m - init_m
    return 0