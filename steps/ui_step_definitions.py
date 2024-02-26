from behave import *
from playwright.sync_api import expect
from helpers.playwright_common_helpers import login, create_cognito_user, fill_whole_briefing, input_into_briefing, navigate_to_question, generate_random_words_list
use_step_matcher("re")


@given("I have an account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    create_cognito_user("ui-test@example.org", "Passwort_01!")


@given("I generate a website")
@when("I generate a website")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    login(context, "sma1@tillmanns.site", "Start123#")

    # Wait for possible redirect to website editor
    context.page.wait_for_timeout(3000)
    if "editor" in context.page.url:  # handle editor
        print("Found the editor page, navigating back to briefing...")
        context.page.get_by_text("Vorschlag regenerieren").click()
        # context.page.get_by_role("button", name="Verwerfen").click()
        context.page.get_by_role("button", name="Weitermachen").click()
        context.page.wait_for_load_state("load")
        context.page.get_by_role("button", name="Starten").click()
    else:
        context.page.locator("p").filter(has_text="Editor").click()
        context.page.get_by_text("Vorschlag regenerieren").click()
        context.page.get_by_role("button", name="Weitermachen").click()
    fill_whole_briefing(context)
    context.page.locator('text="Weiter"').click(timeout=60000)
    # increased timeout for website generation
    context.page.wait_for_url("*/editor", timeout=120000)


@step("I log out of the website")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # default, in briefing
    if context.page.locator(".logout").is_visible():
        context.page.locator(".logout").click()
    # in editor, will probably change in the future
    elif context.page.locator("#router-view").get_by_text("logout").is_visible():
        context.page.locator("#router-view").get_by_text("logout").click()

    # if we continue too fast we wont get logged out correctly
    context.page.wait_for_timeout(2000)
    # we are not redirected anywhere after logout

    # if FE routing is broken add this:
    # if context.page.get_by_role("heading", name="The requested content does").is_visible():
    #    context.page.goto(context.base_url)


@step("I log into the website")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    login(context, "ui-test@example.org", "Passwort_01!")


@then("I should see the generated website")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    expect(context.page.locator(".template-editor")).to_be_visible()


@step("I edit the website")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    template_frame = context.page.frame_locator("iframe[title=\"template-preview\"]")
    template_frame.locator('h1[data-target-name="hero-title"]').hover()
    template_frame.get_by_role("button", name="Edit text").click()
    template_frame.locator('h1[data-target-name="hero-title"]').fill("Neuer Titel")
    template_frame.get_by_role("button", name="Save").click()


@when("I go to the website editor")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.page.locator("p").filter(has_text="Editor").click()


@then("I should see the edited website")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    template_frame = context.page.frame_locator("iframe[title=\"template-preview\"]")
    expect(template_frame.locator('h1[data-target-name="hero-title"]')).to_contain_text("Neuer Titel")



@step("I am not logged on")
@given("I am not logged in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.page.goto(context.base_url)
    if context.page.get_by_text("logout").is_visible():
        context.page.get_by_text("logout").click()


@then("I should see the portal page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    expect(context.page.locator("div.cockpit-wrapper")).to_be_visible()


@step("I am on the website editor page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    expect(context.browser.url).to_equal(f'{context.base_url}/website-editor')
    expect(context.page.locator("#preview-frame")).to_exist()


@then("I should see a placeholder for team picture")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Then I should see a placeholder for team picture')


@given("I have given only 1 service in the briefing")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    login(context, "sma1@tillmanns.site", "Start123#")

    # Wait for possible redirect to website editor
    context.page.wait_for_timeout(3000)
    if "editor" in context.page.url:  # handle editor
        print("Found the editor page, navigating back to briefing...")
        context.page.get_by_text("Vorschlag regenerieren").click()
        # context.page.get_by_role("button", name="Verwerfen").click()
        context.page.get_by_role("button", name="Weitermachen").click()
        context.page.wait_for_load_state("load")
        context.page.get_by_role("button", name="Starten").click()
    else:
        context.page.locator("p").filter(has_text="Editor").click()
        context.page.get_by_text("Vorschlag regenerieren").click()
        context.page.get_by_role("button", name="Weitermachen").click()
    navigate_to_question(context, "Welche Produkte oder Dienstleistungen bietet dein Unternehmen an?")
    input_into_briefing(context, "Geisterjagd")
    fill_whole_briefing(context)


@when("I start the website generation") 
def step_impl(context):
    context.page.locator('text="Weiter"').click(timeout=60000)
    # increased timeout for website generation
    context.page.wait_for_url("*/editor", timeout=120000)

@step("I open the website url")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I open the website url')


@then("I should see the service I entered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I should see the service I entered')


@step("I should see additional services")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I should see additional services')


@given("I have published a website")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I have published a website')


@then("I should see the website")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I should see the website')


@given("I am on the briefing page (?P<question>.+)")
def step_impl(context, question):
    """
    :type context: behave.runner.Context
    :type question: str
    """
    # navigate_to_start(context)
    navigate_to_question(context, question)


@when("I input (?P<value>.+) into the input field")
def step_impl(context, value):
    """
    :type context: behave.runner.Context
    :type value: str
    """
    # Check for the presence of different input types
    input_into_briefing(context, value)


@then("I should not see a validation error")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    expect(context.page.locator('.sma-paragraph.error')).not_to_be_visible()


@step("the next button should be enabled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    next_button = context.page.locator('text=/^(Weiter|Absenden)$/')
    expect(next_button).to_be_enabled()


@then("I should see a validation error")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    expect(context.page.locator('.sma-paragraph.error')).to_be_visible()


@step("the next button should be disabled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    next_button = context.page.locator('text=/^(Weiter|Absenden)$/')
    expect(next_button).to_be_disabled()


@when("I add (?P<number>.+) chips to the input field")
def step_impl(context, number):
    """
    :type context: behave.runner.Context
    :type number: str
    """
    number = int(number)  # Convert the input to an integer
    input = ', '.join(generate_random_words_list(number))
    input_into_briefing(context, input)


@when("I select (?P<input>.+) in the input field")
def step_impl(context, input):
    """
    :type context: behave.runner.Context
    :type input: str
    """
    radio_buttons = context.page.locator('.sma-input-radio')
    for i in range(radio_buttons.count()):
        if radio_buttons.nth(i).inner_text() == input:
            radio_buttons.nth(i).click()
            break


@when("the input field is empty")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Check for the presence of a text input field and clear it if it's not empty
    if context.page.locator('.sma-input-text').count() > 0:
        if context.page.locator('.sma-input-text').input_value() != "":
            context.page.locator('.sma-input-text').fill("")

    # Check for the presence of a list input field and clear it if it's not empty
    elif context.page.locator('.sma-input-list').count() > 0:
        delete_svgs = context.page.locator('.sma-input-list > .tab > svg')
        for svg in delete_svgs:
            svg.click()

    elif context.page.locator('.sma-input-radio:checked').count() > 0:
        raise Exception("Cant deselect radio buttons")
        # if there are any radio buttons present, at least they wont be selected


@step("I know the metadata for the page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I know the metadata for the page')


@when("I edit a section")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I edit a section')


@step("the length of the text is less than the maximum")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: And the length of the text is less than the maximum')


@step("the length of the text is more than the minimum")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: And the length of the text is more than the minimum')


@then("the edit should be accepted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the edit should be accepted')


@step("the edited text should be shown on the website")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: And the edited text should be shown on the website')


@step("the length of the text is exactly the maximum")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: And the length of the text is exactly the maximum')


@step("the length of the text is more than the maximum")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: And the length of the text is more than the maximum')


@then("the edit should be rejected")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the edit should be rejected')


@step("the edited text should not be shown on the website")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: And the edited text should not be shown on the website')


@step("an error message should be shown")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And an error message should be shown')


@step("the length of the text is exactly the minimum")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: And the length of the text is exactly the minimum')


@step("the length of the text is less than the minimum")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: And the length of the text is less than the minimum')


@given("I am on the upload page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I am on the upload page')


@when("I upload an image with the correct dimensions")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: When I upload an image with the correct dimensions')

@then("I should not be able to add more chips")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    chips_selector = ".sma-label-button.light"
    page = context.page

    prior_chips_count = page.locator(chips_selector).count()
    input_into_briefing(context, "longer_than_eight_chars")
    latter_chips_count = page.locator(chips_selector).count()
    print(f"Prior chips count: {prior_chips_count}, Latter chips count: {latter_chips_count}")
    #  using a standard Python assert statement for integer comparison
    assert latter_chips_count == prior_chips_count, "The number of chips should remain the same"

@then("the image should be uploaded")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the image should be uploaded')


@when("I upload an image with the incorrect dimensions")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: When I upload an image with the incorrect dimensions')


@then("I should see an error message")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I should see an error message')


@step("the image should not be uploaded")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the image should not be uploaded')


@when("I upload an image that is too large")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: When I upload an image that is too large')
