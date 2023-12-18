from io import BytesIO

from PIL import Image
from django.core.exceptions import ValidationError


def validate_allowed_file_extensions(value):
    allowed_extensions = ["png", "gif", "jpg", "jpeg", "txt"]
    if not any(value.name.lower().endswith(ext) for ext in allowed_extensions):
        raise ValidationError(
            "Invalid file format. Allowed formats are .png, .gif, .jpg, .jpeg, .txt."
        )


def validate_file_field(value):
    max_txt_file_size = 100 * 1024

    validate_allowed_file_extensions(value)

    if value.name.lower().endswith(".txt"):
        if value.size > max_txt_file_size:
            raise ValidationError("Text file size exceeds 100 kB.")
    else:
        pass


def compress_image(image):
    valid_extensions = ["png", "gif", "jpg", "jpeg"]
    extension = image.name.lower().split(".")[-1]
    if extension in valid_extensions:
        extension = extension.upper()
        if extension == "JPG":
            extension = "JPEG"
        img = Image.open(image)
        max_width = 320
        max_height = 240
        img.thumbnail((max_width, max_height))
        image_io = BytesIO()
        img.save(image_io, format=f"{extension}")

        image_io.seek(0)
        image.file = image_io
