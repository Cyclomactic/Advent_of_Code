from utils import timer


file_v = 'text'
file = '2024/Day2/input/' + file_v + '.txt'


@timer
def main():
    # general test for initial criteria
    def test(report, safe_report):
        if sorted(report) == report or sorted(report, reverse=True) == report:
            safe = True
            report_index = 0
            while report_index < (len(report)-1):
                diff = abs(report[report_index+1] - report[report_index])
                if diff > 0 and diff < 4:
                    report_index += 1
                    safe = True
                else:
                    safe = False
                    break
            return safe, safe_report
        else:
            safe = False
            return safe, safe_report

    # function for Part 2 testing
    def try_remove(report, safe, safe_report):
        length = len(report)
        report_copy = report.copy()
        index = 0
        while safe is False:
            if index > (length - 1):
                break
            report_copy = report.copy()
            report_copy.pop(index)
            copy_test = test(report_copy, safe_report)
            safe = copy_test[0]
            safe_report = copy_test[1]
            index += 1
        if safe is True:
            check_safe_report = safe_report.count(report)
            if check_safe_report is not None:
                safe_report.append(report)
        return safe, safe_report

    def part1(report, safe_report):
        report_test = test(report, safe_report)
        safe = report_test[0]
        if safe is True:
            safe_report.append(report)
        return safe_report

    def part2(report, safe_report):
        report_test = test(report, safe_report)
        safe = report_test[0]
        if safe is False:
            trial = try_remove(report, safe, safe_report)
            safe = trial[0]
            safe_report = trial[1]
        else:
            check_safe_report = safe_report.count(report)
            if check_safe_report is not None:
                safe_report.append(report)
        return safe_report

    # parse data
    with open(file, 'r') as text:
        p1_safe_reports = []
        p2_safe_reports = []
        for line in text:
            report = []
            split_line = line.split()
            for nums in split_line:
                report.append(int(nums))
            part1(report, p1_safe_reports)
            part2(report, p2_safe_reports)
        print(f' part 1 safe reports: {len(p1_safe_reports)}')
        print(f' part 2 safe reports: {len(p2_safe_reports)}')


main()
