#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    approved_breeds = [
        "Labrador Retriever", "German Shepherd", "Golden Retriever", "French Bulldog", "Bulldog",
        "Poodle", "Beagle", "Rottweiler", "Yorkshire Terrier", "Boxer"
    ]

    def __init__(self, name=None, breed=None, **kwargs):
        if name is not None:
            if (
                not isinstance(name, str)
                or name == ""
                or (isinstance(name, str) and len(name) > 25)
            ):
                print("Name must be string between 1 and 25 characters.")
        self.name = name
        if breed is not None and breed not in Dog.approved_breeds:
            print("Breed must be in list of approved breeds.")
        self.breed = breed
