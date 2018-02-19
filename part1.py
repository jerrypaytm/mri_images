import sys
import csv
import argparse
from multiprocessing import Pool
from parsing import parse_contour_file, parse_dicom_file, poly_to_mask
from os import listdir
from os.path import isfile, join

def process_image(image_filepath, contour_filepath = None) :
    img = parse_dicom_file(image_filepath)
    height, width=img.shape
    if contour_filepath != None :
        coordinates = parse_contour_file(contour_filepath)
        mask = poly_to_mask(coordinates, width, height)
    else :
        mask = None

    return (img, mask)

def load_link_file(link_filepath) :
    f = open(link_filepath, 'rb')
    reader = csv.reader(f)
    next(reader, None)
    link = {}
    for row in reader:
        link[row[0]] = row[1]
    return link

def process_directory(input_directory) :
    linkPath = args.input_directory + '/link.csv'
    link = load_link_file(linkPath)
    result = []
    for patient_id in link.keys():
        img_path = input_directory + '/dicoms/' + patient_id 
        for f in listdir(img_path) :
            full_path = join(img_path, f)
            if isfile(full_path):
                components = f.split('.') 
                img_number = components[0].zfill(4)
                contour_id=link[patient_id]
                contour_path = input_directory + '/contourfiles/' + contour_id + '/i-contours/' + 'IM-0001-' + img_number + '-icontour-manual.txt'
                if isfile(contour_path): 
                    result.append(process_image(full_path, contour_path))
                else :
                    result.append(process_image(full_path))
    return result

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(prog='Parsing DICOM images and contour files')
    arg_parser.add_argument('-i', '--input_directory', required=True, type=str,
    help=
        'the input directory contains 2 subdirectories and a link.csv file.' \
        'The link.csv file contains the mapping between the patient id and its associate contour id.' \
        'The subdirectory contourfiles contains directories that are named according to the contour id' \
        'The subdirectory dicoms contains directories that are named according to the patient id' \
    )
    args = arg_parser.parse_args()
    images = process_directory(args.input_directory)