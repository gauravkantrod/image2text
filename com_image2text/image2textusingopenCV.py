from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import pytesseract, pytextractor, os, re, cv2


def get_date_dir():
    config = '-l eng --oem 1 --psm 3'
    dates = {}
    null_dates_lst = []
    files = os.listdir("/Users/gauravkantrod/PycharmProjects/image2text/images")
    for image_file in files:
        im = cv2.imread('/Users/gauravkantrod/PycharmProjects/image2text/images/'+image_file, 1)
        text = pytesseract.image_to_string(im, config=config)
        date = re.findall(r'\d{2}[./-]\d{2}[-./]\d{2,4}|\d{2,4}[-/]\w{3,4}[-/]\d{2,4}|\d{1,2}[/]\d{2,4}|\w{3,9}\s?\d{1,2}[\,]\s?\d{4}|\d{2}[/]\w{3,9}[/]\d{2,4}',text)

        if len(date) == 0:
            dates[file] = 'null'
            null_dates_lst.append('null')
        else:
            dates[file] = date

    efficiency = 100*len(null_dates_lst)/len(dates)
    dates['efficiency']=efficiency

    return dates

get_date_dir()