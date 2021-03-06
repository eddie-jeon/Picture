from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
white = Color(0xE3E3E3, 1.0)
yellow = Color(0xEDF55F, 1.0)
blue = Color(0x0000FF, 1.0)
green = Color(0x84F564, 1.0)
black = Color(0x4D4843, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(400, 200, thinline, green)
ellipse = EllipseAsset(30, 30, thinline, yellow)
ellipse2 = EllipseAsset(70, 40, thinline, blue)
polygon = PolygonAsset([(-85, 100), (25, -75), (100, 125), (-85, 100)], thinline, black)
polygon2 = PolygonAsset([(100, 100), (225, -125), (350, 125), (100, 100)], thinline, black)
# Now display a rectangle
Sprite(rectangle, (100, 200))
Sprite(ellipse, (75, 40))
Sprite(ellipse2, (325, 325))
Sprite(polygon, (150, 150))
Sprite(polygon2, (150, 150))

myapp = App()
myapp.run()