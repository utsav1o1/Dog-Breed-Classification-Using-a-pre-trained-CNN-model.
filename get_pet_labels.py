#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Utsav Karki
# DATE CREATED: 28/07/2022                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    filenames_list = listdir(image_dir)
    print("\nFrom pet_images/ folder printing 10 filenames")
    
    for i in range(0,len(filenames_list)):
        print("{:2d} file: {:>25}".format(i+1, filenames_list[i]))
#     for pet image label
     
    pet_image = filenames_list
#     print(pet_image[1])
    low_pet_image = []
    word_list_pet_image = []
    if in_files[idx][0] != ".":
        for i in range(0,len(filenames_list)): 

            low_pet_image.append(pet_image[i].lower())

        for i in range(0,len(filenames_list)):    
    #         one_pet_image =low_pet_image[i]
    #         word_list_pet_images = one_pet_image.split("_")
            word_list_pet_image.append(low_pet_image[i].split("_",5))




        pet_name = []

        pet_name = [' '.join(i for i in sublist if all(j.isalpha() or j == ' ' for j in i)) for sublist in word_list_pet_image]





    #     for name in pet_name:
    #   pet_names.append(name.strip)
    #     for i in range(0,len(filenames_list)):
    #          print("\nFilename=", pet_image[i], "   Label=", pet_name[i])

        filenames = pet_image
        pet_labels=pet_name
        results_dic = dict()

        items_in_dic = len(results_dic)
    #     print("\nEmpty Dictionary results_dic - n items=", items_in_dic)

    #     filenames = ["beagle_0239.jpg", "Boston_terrier_02259.jpg"]
    #     pet_labels = ["beagle", "boston terrier"]
    #     print(len(filename))
        for idx in range(0,len(filenames)):
            if filenames[idx] not in results_dic:
                results_dic[filenames[idx]] = [pet_labels[idx]]
            else:
                print("** Warning: Key=", filenames[idx],
                      "already exists in results_dic with value =",
                      results_dic[filenames[idx]])

    #     print("\nPrinting all key-value pairs in dictionary results_dic:")
    #     for key in results_dic:
    #         print("Filename=", key, "Pet Label=", results_dic[key][0])
    return results_dic    
 
