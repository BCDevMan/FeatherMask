#!/usr/bin/env python

from gimpfu import *

def feather_mask(image, drawable, thickness, feather):
	active_layer = pdb.gimp_image_get_active_layer(image)
	pdb.gimp_selection_shrink(image, thickness)
	pdb.gimp_selection_feather(image, feather)
	new_mask = pdb.gimp_layer_create_mask(active_layer, 4)
	pdb.gimp_layer_add_mask(active_layer, new_mask)
	return

register(
	"FeatherMask",
	"Create mask by shrinking then feathering selection",
	"Create mask by shrinking then feathering selection",
	"Bartholmew Black",
	"Bartholmew Black",
	"2022",
	"<Image>/Filters/Decor/FeatherMask...",
	"*",
	[
		(PF_INT, "thickness", "Thickness", 1),
		(PF_FLOAT, "feather", "Feather Amount", 1),
	],
	[],
	feather_mask)
	
main()
