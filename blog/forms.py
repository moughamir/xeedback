from django import forms

class PostFrom(forms.Form):
	"""docstring for Post From"""
 	featured_image = froms.ImageField(
 			label = 'Featured Post Image',
 		)
