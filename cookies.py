from selenium import webdriver

# Set the path to your webdriver executable
webdriver_path = '/path/to/chromedriver'  # Replace with the actual path

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=webdriver_path)

# Open the URL
url = "https://www.saucedemo.com"
driver.get(url)

try:
    # Display cookies before login
    cookies_before_login = driver.get_cookies()
    print("Cookies before login:", cookies_before_login)

    # Login
    username_input = driver.find_element_by_id("user-name")
    password_input = driver.find_element_by_id("password")
    login_button = driver.find_element_by_id("login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    # Check if cookies are present after login
    cookies_after_login = driver.get_cookies()
    print("Cookies after login:", cookies_after_login)

    if cookies_after_login:
        print("Login successful - Cookies generated during the login process.")
    else:
        print("Login failed - Cookies not generated.")

    # Navigate to the dashboard (Assuming successful login redirects to the dashboard)
    # Your actual navigation code may vary based on the website structure

    # Perform Logout
    logout_button = driver.find_element_by_id("logout_sidebar_link")  # Replace with actual logout button identifier
    logout_button.click()

    # Display cookies after logout
    cookies_after_logout = driver.get_cookies()
    print("Cookies after logout:", cookies_after_logout)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser after completion
    driver.quit()
