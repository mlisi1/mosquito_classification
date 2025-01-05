dataset_type = 'CustomDataset'


train_pipeline = [ 
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=(512, 512)),
    dict(type='RandomFlip', prob=0.5, direction='horizontal'),
    # dict(type='RandomRotate', max_angle=360, pad_with_fixed_color=True, prob=0.5),  # Random rotation up to 360°
    dict(type='Rotate', magnitude_range=(0, 180), magnitude_level=100, magnitude_std="inf", pad_val=(0,0,0), interpolation="bicubic", prob=0.5),  # Random rotation up to 360°
    dict(type='Brightness', magnitude=0.25, prob=0.4),     # Random brightness adjustment
    dict(type='Contrast', magnitude=0.25, prob=0.4),       # Random contrast adjustment
    # dict(type='GaussianBlur', radius=[0.2, 2.0], prob=0.4),     # Apply Gaussian blur
    dict(type='ColorTransform', magnitude=0.25, prob=0.4),
    # dict(type='RandomResize', scale=[(512, 512), (480, 480), (400, 400)], prob=0.3),  # Random resizing
    dict(type='PackInputs'),
]

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=(512, 512)),
    dict(type='PackInputs'),
]


train_dataloader = dict(
    batch_size=4,
    num_workers=2,
    dataset=dict(
        type=dataset_type,
        data_prefix='data/mosquitoes_dataset_with_parts/train',
        with_label=True,   # or False for unsupervised tasks
        pipeline=train_pipeline,
        # split='train',
    ),
    sampler=dict(type='DefaultSampler', shuffle=True)
)


val_dataloader = dict(
    batch_size=4,
    num_workers=2,
    dataset=dict(
        type=dataset_type,
        data_root='data/mosquitoes_dataset_with_parts/val',
        # split='val',
        pipeline=test_pipeline),
    sampler=dict(type='DefaultSampler', shuffle=False),
)


test_dataloader = dict(
    batch_size=4,
    num_workers=2,
    dataset=dict(
        type=dataset_type,
        data_root='data/mosquitoes_dataset_with_parts/test',
        # split='test',
        pipeline=test_pipeline),
    sampler=dict(type='DefaultSampler', shuffle=False),
)



val_evaluator = dict(type='Accuracy', topk=(1, ))
test_evaluator = val_evaluator