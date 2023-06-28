import pytest
from vision_datasets.common import DatasetTypes
from .coco_adaptor_base import BaseCocoAdaptor
from ..resources.util import coco_database


class TestText2ImageRetrieval(BaseCocoAdaptor):
    TASK = DatasetTypes.TEXT_2_IMAGE_RETRIEVAL

    @pytest.mark.parametrize("coco_dict", coco_database[TASK])
    def test_create_data_manifest(self, coco_dict):
        super().test_create_data_manifest(coco_dict)

    @pytest.mark.parametrize("coco_dict", coco_database[TASK])
    def test_create_data_manifest_with_additional_info(self, coco_dict):
        super().test_create_data_manifest_with_additional_info(coco_dict)
