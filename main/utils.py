from django.core.exceptions import ValidationError


def validate_allowed_file_extensions(value):
    allowed_extensions = ['.png', '.gif', '.jpg', '.jpeg', '.txt']
    if not any(value.name.lower().endswith(ext) for ext in allowed_extensions):
        raise ValidationError('Invalid file format. Allowed formats are .png, .gif, .jpg, .jpeg, .txt.')


def validate_file_field(value):
    max_txt_file_size = 100 * 1024

    validate_allowed_file_extensions(value)

    if value.name.lower().endswith('.txt'):
        if value.size > max_txt_file_size:
            raise ValidationError('Text file size exceeds 100 kB.')
    else:
        pass
