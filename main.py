def calculate_movement(path):
    total = 0
    for i in range(len(path) - 1):
        total += abs(path[i+1] - path[i])
    return total

def run_algorithms(initial_head, requests):
    fcfs_path = [initial_head] + requests
    
    stf_path = [initial_head]
    temp_reqs = list(requests)
    curr = initial_head
    while temp_reqs:
        closest = min(temp_reqs, key=lambda x: abs(x - curr))
        stf_path.append(closest)
        temp_reqs.remove(closest)
        curr = closest

    lower = sorted([r for r in requests if r < initial_head], reverse=True)
    upper = sorted([r for r in requests if r >= initial_head])
    scan_path = [initial_head] + lower + [0] + upper

    c_scan_path = [initial_head] + lower + [0, 300] + sorted(upper, reverse=True)

    c_look_path = [initial_head] + lower + sorted(upper, reverse=True)

    algos = [("FCFS", fcfs_path), ("STF", stf_path), ("SCAN", scan_path), 
             ("C-SCAN", c_scan_path), ("C-LOOK", c_look_path)]
    
    for name, path in algos:
        print(f"{name} Path: {path}")
        print(f"{name} Total Movement: {calculate_movement(path)}\n")

initial_head = 75 
sample_requests = [75, 25, 290, 215, 50, 75, 120, 85, 245, 98]

run_algorithms(initial_head, sample_requests)
