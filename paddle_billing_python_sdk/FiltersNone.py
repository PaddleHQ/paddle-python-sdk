class FiltersNone:
    def filter_none(self, values):  # noqa PEP-484
        """
        This method filters out values that are None from the given list
        """
        return [value for value in values if not None]

