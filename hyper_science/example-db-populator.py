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
    child_with_parent = [
        ["Biological", None],
        ["Fibres", None],
        ["Surface", None],
        ["Films", "Surface"],
        ["Coated", "Films"],
        ["Electronics", None],
        ["MEMS", "Electronics"],
        ["Nanowires", "Electronics"],
        ["Particles", None],
        ["Patterned", "Surface"],
        ["Sponge", None],
        ["Porous", "Sponge"],
        ["Powder", None],
        ["Tips", None],
        ["other_film", "Coated"],
        ["particle_film", "Coated"],
        ["smooth_film", "Coated"],
        ["3d_edge", "MEMS"],
        ["close_up_line", "MEMS"],
        ["electrode", "MEMS"],
        ["microfluidic", "MEMS"],
        ["waveguide", "MEMS"],
        ["entangled_nanowires", "Nanowires"],
        ["few", "Nanowires"],
        ["individual", "Nanowires"],
        ["Forest", "Nanowires"],
        ["crust", "Forest"],
        ["parallel_aligned", "Forest"],
        ["dispersed", "Particles"],
        ["individal_NP", "Particles"],
        ["other_shape", "Particles"],
        ["small_clusters", "Particles"],
        ["3d_edge_patterned", "Patterned"],
        ["3d_line", "Patterned"],
        ["circle_array", "Patterned"],
        ["line_array", "Patterned"],
        ["rings_spiral", "Patterned"],
        ["square_array", "Patterned"],
        ["triangle_array", "Patterned"],
        ["zigzag", "Patterned"],
        ["Pillars", "Patterned"],
        ["individual_pillar", "Pillars"],
        ["triangular_pillar", "Pillars"],
        ["zoom_in_pillar", "Pillars"],
        ["zoomin_powder", "Powder"],
        ["zoom_out", "Powder"],
        ["tip_on_cantilever", "Tips"],
        ["zoom_in", "Tips"],
        ["zoom_out", "Tips"],
    ]
    for child, parent in child_with_parent:
        db = models.CategoryDefinition.objects.get_or_create(
            name=child,
            parent=models.CategoryDefinition.objects.get(name=parent) if parent else None)

    # create some concepts
    # concept for MEMS
    for concept in [
            "conductivity", "corrosion", "resistance", "hardness", "current load", "weight"
    ]:
        attribute, created = models.AttributeDefinition.objects.get_or_create(
            name=concept, description=concept + " description", value_type="D")
        models.CategoryDictionary.objects.get_or_create(
            attribute=attribute, category=models.CategoryDefinition.objects.get(name="MEMS"))
    # add last attribute to other category
    models.CategoryDictionary.objects.get_or_create(
        attribute=attribute, category=models.CategoryDefinition.objects.get(name="Biological"))

    from explorer.models import Query

    Query.objects.create(
        title='example count',
        sql='select COUNT(*) from images_backend_categorydefinition',
    )

    from django.contrib.auth.models import User
    User.objects.create_user(username='admin', password='admin', is_superuser=True, is_staff=True)

    print("Done!")
    # import pdb
    # pdb.set_trace()
