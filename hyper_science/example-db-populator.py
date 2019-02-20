#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import django

if __name__ == "__main__":
    # Needed to import django apps below.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hyper_science.settings')
    django.setup()

    from images_backend import models

    # Creathe some default categories.
    # category, created = models.CategoryDefinition.objects.get_or_create()
    child_with_parent = {
        "Biological": None,
        "Fibres": None,
        "Films_Coated_Surface": None,
        "MEMS_devices_and_electrodes": None,
        "Nanowires": None,
        "Particles": None,
        "Patterned_surface": None,
        "Porous_Sponge": None,
        "Powder": None,
        "Tips": None,
        "other_film": "Films_Coated_Surface",
        "particle_film": "Films_Coated_Surface",
        "smooth_film": "Films_Coated_Surface",
        "3d_edge": "MEMS_devices_and_electrodes",
        "close_up_line": "MEMS_devices_and_electrodes",
        "electrode": "MEMS_devices_and_electrodes",
        "microfluidic": "MEMS_devices_and_electrodes",
        "waveguide": "MEMS_devices_and_electrodes",
        "entangled_nanowires": "Nanowires",
        "few": "Nanowires",
        "individual": "Nanowires",
        "Forest": "Nanowires",
        "crust": "Forest",
        "parallel_aligned": "Forest",
        "dispersed": "Particles",
        "individal_NP": "Particles",
        "other_shape": "Particles",
        "small_clusters": "Particles",
        "3d_edge_patterned": "Patterned_surface",
        "3d_line": "Patterned_surface",
        "circle_array": "Patterned_surface",
        "line_array": "Patterned_surface",
        "rings_spiral": "Patterned_surface",
        "square_array": "Patterned_surface",
        "triangle_array": "Patterned_surface",
        "zigzag": "Patterned_surface",
        "Pillars": "Patterned_surface",
        "individual_pillar": "Pillars",
        "triangular_pillar": "Pillars",
        "zoom_in_pillar": "Pillars",
        "zoomin_powder": "Powder",
        "zoom_out": "Powder",
        "tip_on_cantilever": "Tips",
        "zoom_in": "Tips",
        "zoom_out": "Tips",
    }
    for child, parent in child_with_parent.items():
        db = models.CategoryDefinition.objects.get_or_create(
            name=child,
            parent=models.CategoryDefinition.objects.get(name=parent) if parent else None)

    print("Done!")
    # import pdb
    # pdb.set_trace()
