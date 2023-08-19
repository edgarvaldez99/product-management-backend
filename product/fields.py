from drf_extra_fields.fields import Base64ImageField


class HttpBase64ImageField(Base64ImageField):
    def to_internal_value(self, base64_data):
        # Check if this is a base64 string
        if "http://" in base64_data or "https://" in base64_data:
            return None
        return super().to_internal_value(base64_data)
