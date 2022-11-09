#!/usr/bin/env python

from gimpfu import *

def feather_mask(image, drawable, thickness, feather, grow, apply, white):
	active_layer = pdb.gimp_image_get_active_layer(image)
	if grow:
		pdb.gimp_selection_grow(image, thickness)
	else:
		pdb.gimp_selection_shrink(image, thickness)
	pdb.gimp_selection_feather(image, feather)
	if apply:
		foreground_color = pdb.gimp_context_get_foreground()
		mask = pdb.gimp_layer_get_mask(active_layer)
		if white:
			pdb.gimp_context_set_foreground((255, 255, 255))
		else:
			pdb.gimp_context_set_foreground((0, 0, 0))
		pdb.gimp_edit_fill(mask, 0)
		pdb.gimp_context_set_foreground(foreground_color)
	else:
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
		(PF_TOGGLE, "grow", "Grow instead of shrink", 0),
		(PF_TOGGLE, "apply", "Apply color instead of mask", 0),
		(PF_TOGGLE, "white", "Apply white instead of black", 0)
	],
	[],
	feather_mask)
	
main()
