checkpoint_config = dict(interval=5)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        dict(type='TensorboardLoggerHook')
    ])
# yapf:enable
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
#'/content/mmdetection/htc_r50_fpn_1x_coco_20200317-7332cf16.pth'
resume_from = None
workflow = [('train', 1)]
work_dir='/content/gdrive/My Drive/k-fashion/model/htc_without_semantic_r50_fpn_1x/'
