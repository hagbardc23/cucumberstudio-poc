import os
import random
import string
import json
import time

from behave.runner import Context
from playwright.sync_api import Page
from cognito_api import Cognito


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def map_json_to_questions(json_data):
    # Mapping of JSON keys to question strings
    question_mapping = {
        "name": "Wie ist der Name deines Unternehmens?",
        "domain_url": "Hast du bereits eine Website?",
        "branch": "In welcher Branche bist du tätig?",
        "location": "In welcher Region oder Stadt möchtest du Kunden ansprechen?",
        "founded_at": "Wann wurde dein Unternehmen gegründet?",
        "services": "Welche Produkte oder Dienstleistungen bietet dein Unternehmen an?",
        "team_size": "Wie viele Teammitglieder möchtest du auf die Website vorstellen?",
        "target_groups": "Wer ist deine Zielgruppe?",
        "formality": "Wie möchtest du deinen Kunden ansprechen?",
        "values": "Welche drei wichtigsten Eigenschaften repräsentieren die Werte deines Unternehmens?"
    }

    form_questions = []
    for key, question in question_mapping.items():
        if key in json_data:
            value = json_data[key]

            # Check if the value is a list and convert it to a comma-separated string
            if isinstance(value, list):
                value = ', '.join(value)

            # Special handling for the "formality" key
            if key == "formality":
                form_questions.append({
                    "question": question,
                    "positive": "Informal (Du)" if value == "informal" else "Formal (Sie)",
                    "negative": ""
                })
            else:
                form_questions.append({
                    "question": question,
                    "positive": value,
                    "negative": ""
                })

    return form_questions


# prepare testdata for briefing on load
company_briefing = read_json_file(
    '/app/testdata/CompanyBriefing.json')
form_questions = map_json_to_questions(company_briefing)

# currently the json file seems to be incomplete, so we add the missing questions manually
form_questions.append({"question": "Welche drei wichtigsten Eigenschaften repräsentieren die Werte deines Unternehmens?",
                       "positive": "Professionalität, Innovation, Kundenkommunikation", "negative": ""})


def create_cognito_user(email, password):
    """
    Creates a new user in the cognito user pool.
    Parameters:
    username (str): the username to use
    password (str): the password to use
    """
    pool = os.environ.get("COGNITO_POOL", "dev-sma-user-pool")
    print(f"Creating user {email} in cognito user pool {pool}...")
    try:
        cognito = Cognito()
        cognito.create_user(pool, email, password)
    except Exception as e:
        print(f"User already exists: {e}")
# ----------------------------------------------------------------------------------------------------------------------


def input_into_briefing(context, value):
    """
    Inputs the given input into the briefing form.
    Automatically detects the type of input field and fills it accordingly.
    Use comma seperated string for list input with chips.

    Parameters:
    context (behave-context): behave context
    value (str): the input, comma separated for lists
    """

    if context.page.locator('h2.sma-heading').first.inner_text() == ('Hast du bereits eine Website?'):
        # special case, this has two radios an a text input
        print(
            f"Found the question: Hast du bereits eine Website?, filling it with: {value}")
        if value == "Nein":
            context.page.locator("#radio-option-no").click()
        else:
            context.page.locator("#radio-option-yes").click()
            website_form_input = context.page.locator('.sma-input-text')
            website_form_input.fill(value)

    elif context.page.locator('.sma-input-list').count() > 0:
        # Handle list input, needs to be checked before text input
        print(f"Found a list input field")
        items = value.split(', ')
        for item in items:
            print(f"Filling it with: {item}")
            context.page.locator('.sma-input-text').fill(item)
            context.page.locator(
                '.add-button.sma-label-button').click(force=True)
    elif context.page.locator('.sma-input-text').count() > 0:
        # Handle text input
        print(f"Found a text input field, filling it with: {value}")
        context.page.locator('.sma-input-text').fill(value)

    elif context.page.locator('.sma-input-radio').count() > 0:
        # Handle radio input
        print(f"Found a radio input field, filling it with: {value}")
        radio_buttons = context.page.locator('.sma-input-radio')
        for i in range(radio_buttons.count()):
            if radio_buttons.nth(i).inner_text() == value:
                radio_buttons.nth(i).click()
                break
    else:
        raise Exception("No recognized input field found.")


def navigate_to_start(context):
    """
    Navigates to the start of the briefing form by clicking the back button until it is no longer visible.
    Parameters:
    context (behave-context): behave context
    """

    back_button_selector = 'text="Zurück"'
    while context.page.locator(back_button_selector).count() > 0:
        heading = context.page.locator('h2.sma-heading').first.inner_text()
        context.page.locator(back_button_selector).click()
        context.page.wait_for_load_state("networkidle")
        new_heading = context.page.locator('h2.sma-heading').first.inner_text()
        if new_heading == heading:
            print("Reached the start of the stepper.")
            break


def navigate_to_question(context, question):
    """
    Navigates to the given question in the briefing form by clicking the 'Weiter' button until the question is found.
    If it is not found after reaching the end it will go back to the start and try again once.
    Parameters:
    context (behave-context): behave context
    question (str): the question to navigate to
    """

    start_briefing_button = context.page.locator('button', has_text='Start')
    if start_briefing_button.is_visible():
        start_briefing_button.click()
    start_briefing_popup = context.page.locator('button', has_text='Starten')
    if start_briefing_popup.is_visible():
        start_briefing_popup.click()

    # Flag to indicate if we have already navigated to the start of the stepper
    navigated_to_start = False
    # Max iterations set to twice the length of form_questions
    max_iterations = 2 * len(form_questions)
    iteration_count = 0

    while iteration_count < max_iterations:
        iteration_count += 1
        heading = context.page.locator('h2.sma-heading').first.inner_text()

        if heading == question:
            print(f"Found the question: {question}")
            return

        absenden_button = context.page.locator('text="Absenden"')

        if absenden_button.is_visible():
            if not navigated_to_start:
                navigate_to_start(context)
                navigated_to_start = True
                continue
            else:
                raise Exception(
                    f"Could not find the question: {question} after {max_iterations} attempts.")

        for q in form_questions:
            if q["question"] == heading:
                positive_answer = q["positive"]
                print(
                    f"Filling in the default positive value: {positive_answer} for {heading}")
                input_into_briefing(context, positive_answer)
                break

        if not absenden_button.is_visible():
            weiter_button = context.page.locator('text="Weiter"')
            weiter_button.click()
            context.page.wait_for_load_state("networkidle")

    raise Exception(
        f"Reached maximum iterations ({max_iterations}) without finding the question: {question}")


def fill_whole_briefing(context):
    """
    Fills the whole briefing form with valid values.
    It will use the "positive" value of each question in form_questions.
    Parameters:
    context (behave-context): behave context
    """

    for q in form_questions:
        question = q["question"]
        positive_answer = q["positive"]
        print(
            f"Filling in the default positive value: {positive_answer} for {question}")
        navigate_to_question(context, question)
        input_into_briefing(context, positive_answer)
        if context.page.locator('text="Absenden"').is_visible():
            context.page.locator('text="Absenden"').click()
            return


def generate_random_words_list(length):
    """
    Generates a list of random words of the given length.
    Parameters:
    length (int): the length of the list
    Returns:
    list: a list of random words
    """

    words = set()
    while len(words) < length:
        word_length = random.randint(3, 8)
        word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
        words.add(word)
    return list(words)


def page_by_title(context: Context, title: str) -> Page:
    for page in context.browser_context.pages:
        if title in page.title():
            return page
    return None


def login(context, username, password):
    """
    Logs in to the website with the given username and password.
    It will NOT handle possible redirects.
    Parameters:
    context (behave-context): behave context
    username (str): the username to use
    password (str): the password to use
    """
    page = context.page
    login_button = page.locator("button:has-text('Login'):nth-of-type(1)")
    login_button.wait_for(timeout=10000)
    login_button.click()
    page.wait_for_load_state("networkidle")
    page.get_by_role("textbox", name="name@host.com").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="submit").click()
    page.wait_for_load_state("networkidle")


def login_old(context, username, password):
    context.page.goto(context.base_url)
    context.page.get_by_text("Login").click()

    print(f"Logging in as {username}...")
    with context.page.expect_popup() as page1_info:
        context.page.get_by_text("Login").click()
    popup = page1_info.value
    popup.get_by_placeholder("Email Address").fill(username)
    popup.get_by_placeholder("Password").click()
    popup.get_by_placeholder("Password").fill(password)
    popup.get_by_role("button", name="Sign in").click()

    # Wait for the popup to close
    print("Waiting for the login-popup to close...")
    while len(context.browser_context.pages) > 1:
        # Wait for a short period before checking again
        context.page.wait_for_timeout(100)

    # Wait for possible redirect to website editor
    context.page.wait_for_timeout(3000)
