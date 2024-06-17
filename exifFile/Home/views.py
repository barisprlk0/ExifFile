from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from PIL import Image
from PIL.ExifTags import TAGS
import os
def get_exif_data(image_path, exif_key):
    # Resmi aç ve EXIF verilerini al
    image = Image.open(image_path)
    exif_data = image._getexif()
    if not exif_data:
        return None

    # Her bir EXIF etiketi ve değeri için döngü yap
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        if tag_name == exif_key:
            return value
    return None

def index(request):
    form = ImageUploadForm()  
    image_full_path = None  
    width_value = None
    lenght_value = None
    reso_value = None
    wb_value = None
    flash_value = None
    date_value = None
    make_value= None
    model_value= None
    software_value= None
    fnumber_value= None
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()
            image_full_path = image_instance.image.path 

            # EXIF verisini almak için yardımcı fonksiyonu çağır
            width_key = 'ImageWidth'  # Aramak istediğiniz EXIF anahtarı
            lenght_key = 'ImageLength'  # Aramak istediğiniz EXIF anahtarı
            reso_key = 'ResolutionUnit'  # Aramak istediğiniz EXIF anahtarı
            wb_key = 'WhiteBalance'  # Aramak istediğiniz EXIF anahtarı
            flash_key = 'Flash'  # Aramak istediğiniz EXIF anahtarı
            date_key = 'DateTime'  # Aramak istediğiniz EXIF anahtarı

            width_value = get_exif_data(image_full_path, width_key)
            lenght_value = get_exif_data(image_full_path, lenght_key)
            reso_value = get_exif_data(image_full_path, reso_key)
            wb_value = get_exif_data(image_full_path, wb_key)
            flash_value = get_exif_data(image_full_path, flash_key)
            date_value = get_exif_data(image_full_path, date_key)

            make_key = 'Make'  # Aramak istediğiniz EXIF anahtarı
            model_key = "Model"
            software_key = "Software"
            fnumber_key= "Number"
            
            make_value = get_exif_data(image_full_path, make_key)
            model_value = get_exif_data(image_full_path, model_key)
            software_value = get_exif_data(image_full_path, software_key)
            fnumber_value = get_exif_data(image_full_path, fnumber_key)

            os.remove(image_full_path)

    else:
        form = ImageUploadForm()

    return render(request, 'home/index.html', {
        'form': form,
        'image_full_path': image_full_path,
        'width_value': width_value,
        'lenght_value': lenght_value,
        'reso_value': reso_value,
        'wb_value': wb_value,
        'flash_value': flash_value,
        'date_value': date_value,
        
        'make_value':make_value,
        'model_value':model_value,
        'software_value':software_value,
        'fnumber_value':fnumber_value,  
    })
