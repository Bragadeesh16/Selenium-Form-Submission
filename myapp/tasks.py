from celery import shared_task
from django.core.mail import send_mail,EmailMessage
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

@shared_task
def FormSubmiting():
    website = ' https://forms.gle/WT68aV5UnPajeoSc8'
    chromedriver_path = "/home/bragadeesh/Documents/chromedriver-linux64"
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.binary_location = chromedriver_path
    driver = webdriver.Chrome(options=options)
    driver.get(website)


    name = 'bragadeeshwaran'
    phone = 6383030862
    email_id = 'bragadeesh03294@gmail.com'
    address = 'maniyakara street Kalavai , Ranipet , TamilNadu'
    pincode = 632506
    dob = '01/16/2004'
    Gender = 'male'
    code = 'GNFPYC'

    time.sleep(2)

    input_fields = driver.find_elements(By.XPATH,'//input[@type = "text"]')
    date_field = driver.find_elements(By.XPATH,'//input[@type = "date"]')
    address_field = driver.find_element(By.TAG_NAME,'textarea')

    input_fields[0].send_keys(name)
    input_fields[1].send_keys(phone)
    input_fields[2].send_keys(email_id)
    address_field.send_keys(address)
    input_fields[3].send_keys(pincode)
    input_fields[4].send_keys(Gender)
    input_fields[5].send_keys(code)
    date_field[0].send_keys(dob)
    submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
    submit_button.click()

    photo_path = '/home/bragadeesh/Desktop/form submition/env/myproject/static/conformation.png'
    photo = driver.save_screenshot(photo_path)
    print(photo)
    

    time.sleep(40)

@shared_task
def Emailsending():
        
        photo_path = '/home/bragadeesh/Desktop/form submition/env/myproject/static/conformation.png' 

        if os.path.exists(photo_path):
            with open(photo_path, 'rb') as f:
                photo_content = f.read()

            from_email = 'bragadeesh03294@gmail.com'
            subject = 'Photo Attachment'
            message = 'confirmation page photo'
            recipient_list = ['tech@themedius.ai','hr@themedius.ai']
            # recipient_list = ['bragadeesh03294@gmail.com','kara80499@gmail.com']

            email = EmailMessage(subject, message, from_email, to=recipient_list)
            email.attach(os.path.basename(photo_path), photo_content, 'image/jpeg')
            email.send()
