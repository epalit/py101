MONTHS_IN_A_YEAR = 12

def fmt_prompt_msg(msg, err=False, inc_newline=False):
    if err:
        prompt_msg = f"!!! {msg}"
    else:
        prompt_msg = f"-> {msg}"
    if inc_newline:
        prompt_msg += "\n"
    return prompt_msg

def welcome():
    msg = fmt_prompt_msg(
        "Welcome to the loan calculator!\n\n"
        "We'll ask you for three pieces of information one at a time:\n"
        "        - amount\n"
        "        - apr\n"
        "        - duration\n\n"
        "Then we'll display your monthly payment.\n"
    )
    print(msg)

def get_loan_amount():
    msg = fmt_prompt_msg("Please enter your loan amount:", inc_newline=True)
    while True:
        amount = input(msg).strip()
        try:
            amount = float(amount)
        except ValueError:
            msg = fmt_prompt_msg(
                "Please enter a whole number or decimal using a '.'," \
                " no commas",
                err=True,
                inc_newline=True
            )
            continue
        if amount <= 0:
            msg = fmt_prompt_msg(
                "Loan amount must be greater than zero",
                err=True,
                inc_newline=True
            )
            continue
        return amount

def get_apr():
    msg = fmt_prompt_msg("Please enter your apr:", inc_newline=True)
    while True:
        apr = input(msg).strip()
        try:
            apr = float(apr)
        except ValueError:
            msg = fmt_prompt_msg(
                "Please enter a whole number or decimal using a '.', no '%'",
                err=True,
                inc_newline=True
            )
            continue
        if apr < 0:
            msg = fmt_prompt_msg(
                "APR cannot be negative, please enter a value 0 or above",
                err=True,
                inc_newline=True
            )
        else:
            return apr

def get_duration_unit():
    msg = fmt_prompt_msg(
        "Select months or years for your loan duration (m/y):",
        inc_newline=True
    )
    while True:
        unit = input(msg).strip()
        if unit not in ('m', 'y'):
            msg = fmt_prompt_msg(
                "You must select m (for months) or y (for years):",
                err=True,
                inc_newline=True
            )
        else:
            break
    return unit

def get_duration_value():
    msg = fmt_prompt_msg(
        "Please enter your loan duration:",
        inc_newline=True
    )
    while True:
        duration = input(msg).strip()
        try:
            duration = float(duration)
        except ValueError:
            msg = fmt_prompt_msg(
                "Please enter a whole number or decimal using a '.'," \
                " no commas",
                err=True,
                inc_newline=True
            )
            continue
        if duration <= 0:
            msg = fmt_prompt_msg(
                "Duration cannot be negative or 0, " \
                "please enter a value above 0",
                err=True,
                inc_newline=True
            )
        else:
            return duration

def get_duration():
    unit = get_duration_unit()
    duration = get_duration_value()

    if unit == 'y':
        duration = duration * MONTHS_IN_A_YEAR

    return duration

def calc_monthly_payment(
        amount,
        apr,
        duration
    ):
    decimal_apr = apr / 100
    rate = decimal_apr / MONTHS_IN_A_YEAR
    if rate == 0.0:
        monthly_payment = amount / duration
    else:
        monthly_payment = amount * (rate / (1 - (1 + rate) ** (-duration)))
    return monthly_payment

def display_monthly_payment(monthly_payment):
    msg = fmt_prompt_msg(f"Your monthly payment is: ${monthly_payment:.2f}")
    print(msg)

def user_wants_to_continue():
    msg = fmt_prompt_msg(
        "Do you want to perform another calculation? (y or yes to continue)",
        inc_newline=True
    )
    response = input(msg).strip().lower()
    return response in ('y', 'yes')

def run_loan_calculator():
    welcome()
    while True:
        loan_amount = get_loan_amount()
        apr = get_apr()
        duration = get_duration()
        monthly_payment = calc_monthly_payment(loan_amount, apr, duration)
        display_monthly_payment(monthly_payment)
        if not user_wants_to_continue():
            break

run_loan_calculator()