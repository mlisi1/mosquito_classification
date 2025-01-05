_base_ = [
    '_base_/models/resnet50.py',
    # '../_base_/datasets/cifar100_bs16.py',
    '_base_/schedules/imagenet_bs2048_rsb.py',
    '_base_/default_runtime.py',
    'mosq_dataset.py'
]


backbone=dict(
        type='ResNeSt',
        depth=50,
        num_stages=4,
        out_indices=(3, ),
        style='pytorch',
        norm_cfg=dict(type='SyncBN', requires_grad=True),
        drop_path_rate=0.05,
)

head=dict(
    type='LinearClsHead',
    num_classes=2,
    in_channels=2048,
    loss=dict(
        type='LabelSmoothLoss',
        label_smooth_val=0.1,
        mode='original',
        use_sigmoid=True,
    ),
    topk=(1, 5),
)


data_preprocessor=dict(
        type='ClsDataPreprocessor',
        num_classes=2,  # Number of classes for the dataset
        # mean=[123.675, 116.28, 103.53],  # Adjust to your dataset normalization if needed
        # std=[58.395, 57.12, 57.375],  # Adjust to your dataset normalization if needed
        to_rgb=True,
)

model = dict(
    head=head,
    backbone=backbone,
    train_cfg=dict(augments=[
        dict(type='Mixup', alpha=0.2),
        dict(type='CutMix', alpha=1.0)
    ]),
    data_preprocessor = data_preprocessor,
)

# load_from='https://download.openmmlab.com/mmclassification/v0/resnet/resnet50_8xb256-rsb-a1-600e_in1k_20211228-20e21305.pth'


# schedule settings
optim_wrapper = dict(optimizer=dict(weight_decay=0.0005))

# param_scheduler = dict(
#     type='MultiStepLR',
#     by_epoch=True,
#     milestones=[60, 120, 160],
#     gamma=0.2,
# )

train_cfg = dict(by_epoch=True, max_epochs=200, val_interval=1)
