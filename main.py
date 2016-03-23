from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 255, 0, 100 ]
edges = []
transform = new_matrix()

parse_file( 'script_nocurves', edges, transform, screen, color )
