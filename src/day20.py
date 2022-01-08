from functools import partial
from itertools import chain

def load_image(image_file):
    with open(image_file, "r") as file:
        pixel_map_encoding = next(file).strip()
        image = InfiniteImage.from_rendering("".join((line for line in file)).strip())

    enhance_partial = partial(enhance, list(map(decode, pixel_map_encoding)))

    return (image, enhance_partial)

def enhance(pixel_map, image):
    enhance_value = lambda box: pixel_map[int("".join(chain.from_iterable(box)), base = 2)]

    padded_values = image.get_values(padding = 2)

    values = []
    for j in range(1, len(padded_values) - 1):
        values.append([])
        for i in range(1, len(padded_values[j]) - 1):
            value_box = list((r[(i - 1):(i + 2)] for r in padded_values[(j - 1):(j + 2)]))
            values[-1].append(enhance_value(value_box))

    default_value = enhance_value([[image.default_value] * 3] * 3)

    return InfiniteImage(values, default_value)

def decode(pixel):
    return { "#": "1", ".": "0" }[pixel]

def encode(value):
    return { "0": ".", "1": "#" }[value]

class Enhancer:
    def __init__(self, pixel_map_encoding):
        self._pixel_map = list(map(decode, pixel_map_encoding))

    def _enhance_value(self, value_box):
        return self._pixel_map[int("".join(chain.from_iterable(value_box)), base = 2)]

    def enhance(self, image):
        padded_values = image.get_values(padding = 2)

        values = []
        for j in range(1, len(padded_values) - 1):
            values.append([])
            for i in range(1, len(padded_values[j]) - 1):
                value_box = list((r[(i - 1):(i + 2)] for r in padded_values[(j - 1):(j + 2)]))
                values[-1].append(self._enhance_value(value_box))

        default_value = self._enhance_value([[image.default_value] * 3] * 3)

        return InfiniteImage(values, default_value)

class InfiniteImage:

    def __init__(self, values, default_value = "0"):
        self._default_value = default_value
        self._values = values

    @staticmethod
    def from_rendering(rendering, default_pixel = "."):
        values = list(map(lambda row: [decode(p) for p in row], rendering.split("\n")))
        return InfiniteImage(
            values,
            default_value = decode(default_pixel)
        )

    @property
    def default_value(self):
        return self._default_value

    def get_values(self, padding = 0):
        finite_width = len(self._values[0])

        return list(chain(
            ([self._default_value] * (finite_width + 2 * padding) for _ in range(padding)),
            ([self._default_value] * padding + row + [self._default_value] * padding for row in self._values),
            ([self._default_value] * (finite_width + 2 * padding) for _ in range(padding)),
        ))

    def render(self, padding = 0):

        return "\n".join(("".join(map(encode, row)) for row in self.get_values(padding)))
