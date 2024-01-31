class FieldError:
    def __init__(self, field, error):
        self.field = field
        self.error = error


    def __repr__(self):
        return f"FieldError(field='{self.field}', error='{self.error}')"
