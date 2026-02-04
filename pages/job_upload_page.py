from pages.base_page import BasePage

class JobUploadPage(BasePage):
    def upload_cv(self, file_path: str):
        self.page.set_input_files("#cvUpload", file_path)
        self.click("#submitBtn")
