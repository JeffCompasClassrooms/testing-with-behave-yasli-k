from behave import given, when, then
from selenium.webdriver import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

@given("I open the instructables peppers ghost page")
def step_open_page(context):
    context.behave_driver.get("https://www.instructables.com/Peppers-Ghost-Illusion-in-a-Small-Space/")

@then("I expect that there is at least one picture there")
def step_check_for_picture(context):
    images = context.behave_driver.find_elements(By.CSS_SELECTOR, "img") 
    assert images != []

@then('the page title contains "{text}"')
def step_title_contains(context, text):
    title = context.behave_driver.title
    assert text in title, f'Expected title to contain "{text}", got "{title}"'


@then('the heading "{heading_text}" is visible')
def step_heading_visible(context, heading_text):
    heading = context.behave_driver.find_element(
        By.XPATH, f"//h1[contains(text(), '{heading_text}')]"
    )
    assert heading.is_displayed(), f'Heading "{heading_text}" not visible'


@when('I scroll to the bottom of the page')
def step_scroll_bottom(context):
    context.behave_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


@then('I see the "Related Instructables" section')
def step_related_section(context):
    section = context.behave_driver.find_element(
        By.XPATH, "//h2[contains(text(), 'Related Instructables')]"
    )
    assert section.is_displayed()


@when('I click the first step image')
def step_click_first_step_image(context):
    first_img = context.behave_driver.find_element(
        By.CSS_SELECTOR, ".step-image img"
    )
    first_img.click()


@then('a larger image modal opens')
def step_modal_opens(context):
    wait_for(context.behave_driver, lambda d: d.find_element(By.CSS_SELECTOR, ".modal"))
    modal = context.behave_driver.find_element(By.CSS_SELECTOR, ".modal")
    assert modal.is_displayed()


@then('the modal can be closed with the close button')
def step_close_modal(context):
    close_btn = context.behave_driver.find_element(By.CSS_SELECTOR, ".modal .close")
    close_btn.click()
    wait_for(context.behave_driver, lambda d: not d.find_elements(By.CSS_SELECTOR, ".modal"))


@when('I search the page for the word "{word}"')
def step_search_word(context, word):
    # Instructables has a built-in search – we just use the browser find
    context.behave_driver.find_element(By.TAG_NAME, "body").send_keys(
        "\uE01B" + word  # Ctrl+F (or Cmd+F) + word
    )


@then('the word "{word}" is highlighted')
def step_word_highlighted(context, word):
    # The page adds a class "highlight" to matches
    highlighted = context.behave_driver.find_elements(
        By.XPATH, f"//span[contains(@class, 'highlight') and contains(text(), '{word}')]"
    )
    assert highlighted, f'Word "{word}" not highlighted'


@then('the author name is displayed')
def step_author_name(context):
    author = context.behave_driver.find_element(By.CSS_SELECTOR, ".author-name")
    assert author.is_displayed()


@then('the project has at least {n:d} steps')
def step_step_count(context, n):
    steps = context.behave_driver.find_elements(By.CSS_SELECTOR, ".step")
    assert len(steps) >= n, f'Expected >= {n} steps, found {len(steps)}'


@when('I click the "Download PDF" button')
def step_click_download_pdf(context):
    pdf_btn = context.behave_driver.find_element(By.LINK_TEXT, "Download PDF")
    pdf_btn.click()


@then('a new tab with a PDF opens')
def step_pdf_tab(context):
    wait_for(context.behave_driver, lambda d: len(d.window_handles) > 1)
    context.behave_driver.switch_to.window(context.behave_driver.window_handles[-1])
    assert ".pdf" in context.behave_driver.current_url.lower()
    # Close the PDF tab and return
    context.behave_driver.close()
    context.behave_driver.switch_to.window(context.behave_driver.window_handles[0])

