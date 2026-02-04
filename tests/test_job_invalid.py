import pytest
from pages.login_page import LoginPage
from pages.job_upload_page import JobUploadPage

@pytest.mark.parametrize("cv_file", ["./resources/abdul_cv.docx"])
def test_upload_cv(browser, cv_file):
    # Step 1: Navigate to job portal
    login_page = LoginPage(browser)
    #login_page.navigate("https://login.seek.com/login")

    # Step 2: Perform login
    text=login_page.login("abdul.proffj@gmail.com", "Abdul@!proffj")
    print(text)

    # Step 3: Upload CV
    #job_page = JobUploadPage(browser)
    #job_page.upload_cv(cv_file)

    # Optional: Assert success message
    #assert browser.is_visible("text=Upload successful")
