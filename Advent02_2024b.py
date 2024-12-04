
def is_safe(levels):
    increasing = all(1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))
    return increasing or decreasing

def is_safe_with_removal(levels):
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        if is_safe(modified_levels):
            return True
    return False

def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe(report) or is_safe_with_removal(report):
            safe_count += 1
    return safe_count

def read_reports_from_file(file_path):
    reports = []
    with open(file_path, 'r') as file:
        for line in file:
            reports.append(list(map(int, line.strip().split())))
    return reports

file_path = 'Advent02_2024.txt'
reports = read_reports_from_file(file_path)
print(f"Number of safe reports: {count_safe_reports(reports)}")