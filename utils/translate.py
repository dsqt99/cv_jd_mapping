from googletrans import Translator

def transtext(text):
    translator = Translator(service_urls=['translate.google.com'])
    try:
        translated = translator.translate(text, src='auto', dest='vi')
        return translated.text
    except:
        return text
    
def transdata(cv):
    cv_translated = {}
    for key in cv.keys():
        if key in ['full_name', 'tel', 'phone', 'mail', 'date_of_birth']:
            cv_translated[key] = cv[key]
        elif key == 'gender':
            if transtext(cv[key]).lower() in ['đàn bà', 'nữ', 'phụ nữ', 'con gái', 'nữ giới']:
                cv_translated[key] = 'Nữ'
            else:
                cv_translated[key] = 'Nam'
        else:
            cv_translated[key] = transtext(cv[key])
    return cv_translated