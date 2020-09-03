
import sys
import argparse
import pandas as pd
import numpy as np
import os


def get_settings():
    parser = argparse.ArgumentParser(description='Script to ensemble submissions.')
    parser.add_argument('--include_external', help='whether to include external data (1) or not (0).',
        default=0, type = int)
    parser.add_argument('--metadata_weight', help='Weight assigned to metadata (0-1).',
        default=0.2, type = float)
    parser.add_argument('--ensemble_filename', help='The desired name for the ensemble file.',
        default='ensemble', type = str)                
    args = parser.parse_args()
    return args


def main():
    
    config = get_settings()
    include_external = config.include_external
    metadata_weight = config.metadata_weight
    ensemble_filename = config.ensemble_filename

    # Image submissions
    image_sub_files = os.listdir('./submissions/image_data')
    image_sub_list = [pd.read_csv(f'./submissions/image_data/{e}') for e in image_sub_files]

    if include_external == 1:
        ext_image_sub_files = os.listdir('./submissions/external_image_data')
        ext_image_sub_list = [pd.read_csv(f'./submissions/external_image_data/{e}') for e in ext_image_sub_files]
        image_sub_list = image_sub_list + ext_image_sub_list

    target_images = np.mean([e.target for e in image_sub_list], axis=0)

    # Metadata submission
    metadata_sub_files = os.listdir('./submissions/metadata')
    sub_metadata = pd.read_csv(f'./submissions/metadata/{metadata_sub_files[0]}')

    # Image + Metadata
    target = ((1-metadata_weight) * target_images) + (metadata_weight * sub_metadata.target)

    # Save ensemble
    sub_ensemble = sub_metadata.copy()
    sub_ensemble.target = target
    sub_ensemble.to_csv(f'./ensemble/{ensemble_filename}.csv', index=False)
    print(f'File {ensemble_filename}.csv saved in ./ensemble.')

if __name__=='__main__':
    main()
