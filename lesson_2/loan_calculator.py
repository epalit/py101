# TODO: loan amount:
#   ensure input is valid
#   handle input formats (like , or .)
#   exception handling
# TODO: apr:
#   ensure input is valid
#   handle input formats (like % or .)
#   exception handling
# TODO: duration:
#   ensure input is valid
#   ask months or years
#   exception handling
# TODO:
#   Ask if user wants to do another calculation
#   Add more instructions to welcome message
#   Handle no-interest loans

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
        """ Welcome to the loan calculator!
            We'll ask you for three pieces of information one at a time:
                     - apr
                     - duration
                     - amount
            Then we'll display your monthly payment.
        """)
    print(msg)

def get_loan_amount():
    msg = fmt_prompt_msg("Please enter your loan amount:", inc_newline=True)
    return int(input(msg))

def get_apr():
    msg = fmt_prompt_msg("Please enter your apr:", inc_newline=True)
    return int(input(msg))

def get_duration():
    msg = fmt_prompt_msg("Please enter the loan duration:", inc_newline=True)
    return int(input(msg))

def calc_monthly_payment(
        amount,
        apr,
        duration
    ):
    rate = apr/12
    monthly_payment = amount * (rate / (1 - (1 + rate) ** (-duration)))
    return monthly_payment

def display_monthly_payment(monthly_payment):
    msg = fmt_prompt_msg(f"Your monthly payment is: ${monthly_payment}")
    print(msg)

def run_loan_calculator():
    welcome()
    loan_amount = get_loan_amount()
    apr = get_apr()
    duration = get_duration()
    monthly_payment = calc_monthly_payment(loan_amount, duration, apr)
    display_monthly_payment(monthly_payment)

run_loan_calculator()

