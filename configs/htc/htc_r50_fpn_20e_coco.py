#_base_ = './htc_r50_fpn_1x_coco.py'
_base_ = './htc_without_semantic_r50_fpn_1x_coco'
# learning policy
lr_config = dict(step=[16, 19])
total_epochs = 20
