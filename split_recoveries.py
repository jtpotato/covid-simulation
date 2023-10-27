def split(case_numbers):
    daily_recoveries = case_numbers // 14
    recoveries = [daily_recoveries] * 14
    remainder = case_numbers % 14
    for i in range(remainder):
        recoveries[i] += 1

    return recoveries