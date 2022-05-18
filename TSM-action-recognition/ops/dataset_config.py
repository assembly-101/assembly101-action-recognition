# Code for TSM adapted from the original TSM repo:
# https://github.com/mit-han-lab/temporal-shift-module

import os

def return_Assembly101(modality, evaluation_file):
    path_to_data = 'data'
    filename_categories = f'{path_to_data}/category.txt'
    
    # path to frames
    root_data = '/mnt/ssd/fbnus/Assembly101/frames/'
    
    if evaluation_file:
        modality = evaluation_file.split('_')[-1][:-4]
    
    if modality == 'RGB':
        filename_imglist_train = f'{path_to_data}/train_rgb.txt'
        filename_imglist_val = f'{path_to_data}/validation_rgb.txt'
    elif modality == 'mono':
        filename_imglist_train = f'{path_to_data}/train_mono.txt'
        filename_imglist_val = f'{path_to_data}/validation_mono.txt'
    elif modality == 'combined':
        filename_imglist_train = f'{path_to_data}/train_combined.txt'
        filename_imglist_val = f'{path_to_data}/validation_combined.txt'
    else:
        raise NotImplementedError('no such modality:' + modality)

    prefix = '{:010d}.jpg'
    if not evaluation_file == None:
        filename_imglist_val = f'{path_to_data}/{evaluation_file}'
        
    return filename_categories, filename_imglist_train, filename_imglist_val, root_data, prefix


def return_dataset(dataset, modality, evaluation_file=None):
    '''
    Argument evaluation_file: which split do you want to evaluate on
    '''

    dict_single = {'Assembly101': return_Assembly101}
    
    if dataset in dict_single:
        file_categories, file_imglist_train, file_imglist_val, root_data, prefix = dict_single[dataset](modality, evaluation_file)
    else:
        raise ValueError('Unknown dataset '+ dataset)

    if isinstance(file_categories, str):
        with open(file_categories) as f:
            lines = f.readlines()
        categories = [item.rstrip() for item in lines]
    else:
        # number of categories
        categories = [None] * file_categories

    n_class = len(categories)
    print(f'{dataset}: {n_class} classes')
    
    return n_class, file_imglist_train, file_imglist_val, root_data, prefix
