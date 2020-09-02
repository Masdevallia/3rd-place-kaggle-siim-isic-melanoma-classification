
import sys
import argparse
import pandas as pd
import numpy as np
import os


def get_settings():
    parser = argparse.ArgumentParser(description='Script to ensemble submissions.')
    parser.add_argument('--image_data_path', help='Path to image model submissions.',
        default='./submissions/image_data', type = str)
    parser.add_argument('--metadata_path', help='Path to the metadata model submission.',
        default='./submissions/metadata', type = str)
    parser.add_argument('--metadata_weight', help='Weight assigned to metadata.',
        default=0.2, type = float)
    parser.add_argument('--ensemble_path', help='The desired destination path in which to save the ensemble file.',
        default='./ensemble', type = str)     
    parser.add_argument('--ensemble_filename', help='The desired name for the ensemble file.',
        default='ensemble2', type = str)                    
    args = parser.parse_args()
    return args


def main():
    config = get_settings()
    image_data_path = config.image_data_path
    metadata_path = config.metadata_path
    metadata_weight = config.metadata_weight
    ensemble_path = config.ensemble_path
    ensemble_filename = config.ensemble_filename
    # Image submissions
    image_sub_files = os.listdir(image_data_path)
    image_sub_list = [pd.read_csv(f'{image_data_path}/{e}') for e in image_sub_files]
    target_images = np.mean([e.target for e in image_sub_list], axis=0)
    # Metadata submission
    metadata_sub_files = os.listdir(metadata_path)
    sub_metadata = pd.read_csv(f'{metadata_path}/{metadata_sub_files[0]}')
    # Image + Metadata
    target = ((1-metadata_weight) * target_images) + (metadata_weight * sub_metadata.target)
    # Save ensemble
    sub_ensemble = sub_metadata.copy()
    sub_ensemble.target = target
    sub_ensemble.to_csv(f'{ensemble_path}/{ensemble_filename}.csv', index=False)
    print(f'File {ensemble_filename}.csv saved in {ensemble_path}.')


if __name__=='__main__':
    main()
