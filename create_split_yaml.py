def create_split_yaml(base_dir="/content/SeljukDetection"):
    data_yaml = {
        'train': f'{base_dir}/train/images',
        'val':   f'{base_dir}/val/images',
        'test':  f'{base_dir}/test/images',
        'nc': 1,
        'names': ['seljuk_shape']
    }

    yaml_path = f"{base_dir}/seljuk_data_split.yaml"

    with open(yaml_path, 'w') as f:
        yaml.dump(data_yaml, f)

    print(f" YAML for training created: {yaml_path}")
    return yaml_path
