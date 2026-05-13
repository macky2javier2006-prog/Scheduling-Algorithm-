# Disk Scheduling Algorithm Simulator

A simple Python program that demonstrates multiple disk scheduling algorithms, including FCFS, SSTF, SCAN, C-SCAN, and C-LOOK.

## Features

- **Multiple Algorithms**: Compares five different scheduling strategies.
- **Path Visualization**: Shows the exact order of track service.
- **Total Movement Calculation**: Calculates total seek distance for each method.

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

## Example Input

```python
initial_head = 75
requests = [75, 25, 290, 215, 50, 75, 120, 85, 245, 98]
```

## Sample Output

```plaintext
FCFS Path: [75, 75, 25, 290, 215, 50, 75, 120, 85, 245, 98]
FCFS Total Movement: 890

SSTF Path: [75, 75, 75, 85, 98, 120, 50, 25, 215, 245, 290]
SSTF Total Movement: 310

SCAN Path: [75, 50, 25, 0, 75, 85, 98, 120, 215, 245, 290]
SCAN Total Movement: 365
```

## Concepts Used

- **Disk Scheduling Algorithms**: FCFS, SSTF, SCAN, C-SCAN, C-LOOK.
- **Python Logic**: Lists, loops, and lambda functions for distance calculation.
- **OS Principles**: Seek time optimization and head movement.

## Authors
- Javier & Masangcay
