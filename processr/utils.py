import os
import pickle
from sklearn.naive_bayes import GaussianNB

# define the class encodings and reverse encodings
classes = {0: "Adelie", 1: "Chinstrap", 2: "Gentoo"}
r_classes = {y: x for x, y in classes.items()}

# function to process data and return it in correct format
def process_data(data):
    processed = [
        {
            "bill_length_mm": d.bill_length_mm,
            "bill_depth_mm": d.bill_depth_mm,
            "flipper_length_mm": d.flipper_length_mm,
            "body_mass_g": d.body_mass_g,
            "species_class": d.species_class,
        }
        for d in data
    ]

    return processed
