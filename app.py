from flask import Flask, request, render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_user():
    username = request.form['username']

    # Cấu hình selenium
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Nếu muốn hiện trình duyệt thì xóa dòng này
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Mở trang login
        driver.get("https://hackslot.me/login")

        # Đăng nhập admin
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Tên đăng nhập']").send_keys("toolhu123")
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Mật khẩu']").send_keys("1e123456")
        driver.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(2)

        # Truy cập trang admin tạo user
        driver.get("https://hackslot.me/admin/users")
        time.sleep(2)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Thêm mới')]"))
        ).click()
        time.sleep(2)

        # Nhập thông tin user
        driver.find_element(By.CSS_SELECTOR, 'input[ng-model="user.name"]').send_keys(username)
        driver.find_element(By.CSS_SELECTOR, 'input[ng-model="user.username"]').send_keys(username)
        driver.find_element(By.CSS_SELECTOR, 'input[ng-model="user.phone"]').send_keys(username)
        driver.find_element(By.CSS_SELECTOR, 'input[ng-model="user.password"]').send_keys(username)
        driver.find_element(By.CSS_SELECTOR, 'input[ng-model="user.password_confirmation"]').send_keys(username)

        driver.find_element(By.CSS_SELECTOR, 'button#btnSave').click()
        time.sleep(2)

        return render_template('output.html', username=username)

    except Exception as e:
        return f"Lỗi khi tạo tài khoản: {str(e)}"

    finally:
        driver.quit()

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8000)

