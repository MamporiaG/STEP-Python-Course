from functools import reduce


def main():

    print("ALLOWANCE TRACKER\n")

    weeks = int(input("How many weeks to track? "))

    weekly_allowances = get_weekly_allowances(weeks)

    bonus = input("Add bonus? (yes/no): ")
    if bonus.lower() == "yes":
        while True:
            bonus_amount = float(input("Bonus amount per week: "))
            if bonus_amount > 0:
                break
            print("Bonus amount shall be more than 0")
    else:
        bonus_amount = 0

    ls_allowances_with_bonus = add_bonuses(weekly_allowances, bonus_amount)

    total_allowances = calculate_total(ls_allowances_with_bonus)

    average_allowance = calculate_average(ls_allowances_with_bonus)

    threshold_value = float(input("Enter the threshold value: "))

    good_weeks = find_good_weeks(ls_allowances_with_bonus, threshold_value)

    if len(good_weeks) > 0:
        best_week = max(good_weeks, key=lambda x: x[1])
    else:
        best_week = (0, 0.0)

    results = display_results(
        weekly_allowances,
        bonus_amount,
        ls_allowances_with_bonus,
        total_allowances,
        average_allowance,
        good_weeks,
        best_week,
    )
    print(results)


def get_weekly_allowances(num_weeks):

    while True:
        if num_weeks > 0:
            break
        print("The number of weeks shall be at least 1")

    allowances_ls = []
    for num in range(1, num_weeks + 1):
        allowances = float(input(f"Enter week {num} allowance amount: "))
        allowances_ls.append(allowances)
    return allowances_ls


def add_bonuses(allowances, bonus):
    """
    Takes list of allowances and bonus amount
    Uses map() to add bonus to each allowance
    Returns list of totals with bonuses (floats)
    Formula: allowance + bonus
    """
    added_bonus = list(map(lambda x: x + bonus, allowances))
    return added_bonus


def calculate_total(amounts):
    """
    Takes list of amounts
    Uses reduce() to calculate total earned
    Returns total as a float
    Formula: sum of all amounts
    """
    total_earned = reduce(lambda x, y: x + y, amounts)
    return float(total_earned)


def calculate_average(amounts):
    """
    Takes list of amounts
    Uses reduce() to sum, then divides by length
    Returns average as a float
    Formula: total ÷ number of weeks
    """
    total = reduce(lambda x, y: x + y, amounts)
    average = total / len(amounts)
    return average


def find_good_weeks(amounts, threshold):
    """
    Takes list of amounts and threshold value
    Uses filter() to find amounts above threshold
    Uses zip() to pair with week numbers
    Returns list of tuples: (week_number, amount)
    Week numbers start at 1

    """
    week_numbers = list(range(1, len(amounts) + 1))
    combined = list(zip(week_numbers, amounts))
    combined_filtered = list(filter(lambda x: x[1] >= threshold, combined))
    return combined_filtered


def display_results(original, bonus, with_bonus, total, average, good_weeks, best_week):
    """
    Takes all calculated data as parameters
    Returns nothing (just prints)
    Displays formatted output as shown in demo
    Format all amounts to 2 decimal places with dollar signs
    """
    print("--- ALLOWANCE SUMMARY ---\n")
    print("Weekly Earnings:\t")

    print("Allowances:", f"${original[0]:.2f}", end="")
    for num in original[1:]:
        print(f", ${num:.2f}", end="")
    print()

    if bonus == 0:
        print(f"Bonus: no")
    else:
        print(f"Bonus: yes, ${bonus:.2f}")

    print("Allowances with bonus:", f"${with_bonus[0]:.2f}", end="")
    for allowances in with_bonus[1:]:
        print(f", ${allowances:.2f}", end="")
    print()

    print(f"Total earned: ${total:.2f}")

    print(f"Average per week: ${average:.2f}")

    print("Good Weeks:")
    if len(good_weeks) == 0:
        print("- No weeks met / exceeded the threshold.")
    if len(good_weeks) == len(with_bonus):
        print("- All weeks are good / above the threshold")
    for week, amount in good_weeks:
        print(f"- Week {week} (${amount:.2f})")

    print(f"Best Week:")
    if best_week[0] == 0:
        print("- No weeks met the threshold")
    else:
        print(f"- Week {best_week[0]} with ${best_week[1]:.2f}")


if __name__ == "__main__":
    main()
