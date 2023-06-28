

from ..common import ImageLabelWithCategoryManifest


class ImageObjectDetectionLabelManifest(ImageLabelWithCategoryManifest):
    """
    [c_id, left, top, right, bottom], ...] (absolute coordinates);
    """

    @property
    def category_id(self):
        return self.label_data[0]

    @category_id.setter
    def category_id(self, value):
        self._category_id_check(value)
        self.label_data[0] = value

    def _read_label_data(self):
        raise NotImplementedError

    def _check_label(self, label_data):
        if not label_data or len(label_data) != 5:
            raise ValueError
