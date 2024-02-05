import constants
from utils import download_file, extract_text, fetch_data, logger
import os

# path of the directory
home_folder = os.getcwd()
subfolder = 'file_downloads'
PATH = os.path.join(home_folder, subfolder)

def main():
    try:
        url_list = constants.url
        logger.log_message("Start", 0)
        for url in url_list:
            # get file name from url
            download_file.download_file(url, PATH)
            file_name = url.split('/')[-1]

            #extract text from file
            text = extract_text.read_text(PATH+'/'+file_name, constants.num_pages)
            
            # cin and count(cin)
            cin, count= fetch_data.fetch_cin(text)
            # email
            email = fetch_data.fetch_email(text)
            # phone number
            phone = fetch_data.fetch_phone(text)
            # pan
            pan = fetch_data.fetch_pan(text)
            # website
            website = fetch_data.fetch_websites(text)
            # date
            date = fetch_data.fetch_dates(text)

            with open('output.txt', 'a') as f:
                f.write(f'+++++++++++++{file_name}+++++++++++++\n')
                f.write(f'CIN : {cin}\nCIN-Count: {count}\nContact Number: {phone}\nEmail : {email}\nPhoneNumbers : {None}\nPan : {pan}\nDates : {date}\nWebsite : {website}\n\n')
                f.close()
            logger.log_message(f"File - {file_name} Done", 0)
        logger.log_message("End", 0)
    except Exception as e:
        logger.log_message(f"Error: {e}", 1)
if __name__ == '__main__':
    main()