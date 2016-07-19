from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xF2527B, 0.7)
darkred = Color(0xFF0000, 0.3)
yellow = Color(0xEDF55F, 0.7)
blue = Color(0x0000FF, 1.0)
green = Color(0x84F564, 1.0)
black = Color(0x000000, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(50, 50, thinline, red)
rectangle2 = RectangleAsset(50, 50, thinline, green)
rectangle3 = RectangleAsset(50, 50, thinline, yellow)
ellipse = EllipseAsset(27, 27, thinline, blue)
polygon = PolygonAsset([(0, 100), (300, 100), (100, 275), (0, 100)], thinline, darkred)

# Now display a rectangle
Sprite(rectangle, (210, 160))
Sprite(rectangle2, (225, 180))
Sprite(rectangle3, (235, 150))
Sprite(ellipse, (300, 300))
Sprite(polygon, (150, 150))

myapp = App()
myapp.run()
