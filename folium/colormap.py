# -*- coding: utf-8 -*-
"""
Colormap
-------

Utility module for dealing with colormaps.

"""
from jinja2 import Template
from folium.six import text_type, binary_type

_cnames = {
    'aliceblue':            '#F0F8FF',
    'antiquewhite':         '#FAEBD7',
    'aqua':                 '#00FFFF',
    'aquamarine':           '#7FFFD4',
    'azure':                '#F0FFFF',
    'beige':                '#F5F5DC',
    'bisque':               '#FFE4C4',
    'black':                '#000000',
    'blanchedalmond':       '#FFEBCD',
    'blue':                 '#0000FF',
    'blueviolet':           '#8A2BE2',
    'brown':                '#A52A2A',
    'burlywood':            '#DEB887',
    'cadetblue':            '#5F9EA0',
    'chartreuse':           '#7FFF00',
    'chocolate':            '#D2691E',
    'coral':                '#FF7F50',
    'cornflowerblue':       '#6495ED',
    'cornsilk':             '#FFF8DC',
    'crimson':              '#DC143C',
    'cyan':                 '#00FFFF',
    'darkblue':             '#00008B',
    'darkcyan':             '#008B8B',
    'darkgoldenrod':        '#B8860B',
    'darkgray':             '#A9A9A9',
    'darkgreen':            '#006400',
    'darkkhaki':            '#BDB76B',
    'darkmagenta':          '#8B008B',
    'darkolivegreen':       '#556B2F',
    'darkorange':           '#FF8C00',
    'darkorchid':           '#9932CC',
    'darkred':              '#8B0000',
    'darksage':             '#598556',
    'darksalmon':           '#E9967A',
    'darkseagreen':         '#8FBC8F',
    'darkslateblue':        '#483D8B',
    'darkslategray':        '#2F4F4F',
    'darkturquoise':        '#00CED1',
    'darkviolet':           '#9400D3',
    'deeppink':             '#FF1493',
    'deepskyblue':          '#00BFFF',
    'dimgray':              '#696969',
    'dodgerblue':           '#1E90FF',
    'firebrick':            '#B22222',
    'floralwhite':          '#FFFAF0',
    'forestgreen':          '#228B22',
    'fuchsia':              '#FF00FF',
    'gainsboro':            '#DCDCDC',
    'ghostwhite':           '#F8F8FF',
    'gold':                 '#FFD700',
    'goldenrod':            '#DAA520',
    'gray':                 '#808080',
    'green':                '#008000',
    'greenyellow':          '#ADFF2F',
    'honeydew':             '#F0FFF0',
    'hotpink':              '#FF69B4',
    'indianred':            '#CD5C5C',
    'indigo':               '#4B0082',
    'ivory':                '#FFFFF0',
    'khaki':                '#F0E68C',
    'lavender':             '#E6E6FA',
    'lavenderblush':        '#FFF0F5',
    'lawngreen':            '#7CFC00',
    'lemonchiffon':         '#FFFACD',
    'lightblue':            '#ADD8E6',
    'lightcoral':           '#F08080',
    'lightcyan':            '#E0FFFF',
    'lightgoldenrodyellow': '#FAFAD2',
    'lightgreen':           '#90EE90',
    'lightgray':            '#D3D3D3',
    'lightpink':            '#FFB6C1',
    'lightsage':            '#BCECAC',
    'lightsalmon':          '#FFA07A',
    'lightseagreen':        '#20B2AA',
    'lightskyblue':         '#87CEFA',
    'lightslategray':       '#778899',
    'lightsteelblue':       '#B0C4DE',
    'lightyellow':          '#FFFFE0',
    'lime':                 '#00FF00',
    'limegreen':            '#32CD32',
    'linen':                '#FAF0E6',
    'magenta':              '#FF00FF',
    'maroon':               '#800000',
    'mediumaquamarine':     '#66CDAA',
    'mediumblue':           '#0000CD',
    'mediumorchid':         '#BA55D3',
    'mediumpurple':         '#9370DB',
    'mediumseagreen':       '#3CB371',
    'mediumslateblue':      '#7B68EE',
    'mediumspringgreen':    '#00FA9A',
    'mediumturquoise':      '#48D1CC',
    'mediumvioletred':      '#C71585',
    'midnightblue':         '#191970',
    'mintcream':            '#F5FFFA',
    'mistyrose':            '#FFE4E1',
    'moccasin':             '#FFE4B5',
    'navajowhite':          '#FFDEAD',
    'navy':                 '#000080',
    'oldlace':              '#FDF5E6',
    'olive':                '#808000',
    'olivedrab':            '#6B8E23',
    'orange':               '#FFA500',
    'orangered':            '#FF4500',
    'orchid':               '#DA70D6',
    'palegoldenrod':        '#EEE8AA',
    'palegreen':            '#98FB98',
    'paleturquoise':        '#AFEEEE',
    'palevioletred':        '#DB7093',
    'papayawhip':           '#FFEFD5',
    'peachpuff':            '#FFDAB9',
    'peru':                 '#CD853F',
    'pink':                 '#FFC0CB',
    'plum':                 '#DDA0DD',
    'powderblue':           '#B0E0E6',
    'purple':               '#800080',
    'red':                  '#FF0000',
    'rosybrown':            '#BC8F8F',
    'royalblue':            '#4169E1',
    'saddlebrown':          '#8B4513',
    'salmon':               '#FA8072',
    'sage':                 '#87AE73',
    'sandybrown':           '#FAA460',
    'seagreen':             '#2E8B57',
    'seashell':             '#FFF5EE',
    'sienna':               '#A0522D',
    'silver':               '#C0C0C0',
    'skyblue':              '#87CEEB',
    'slateblue':            '#6A5ACD',
    'slategray':            '#708090',
    'snow':                 '#FFFAFA',
    'springgreen':          '#00FF7F',
    'steelblue':            '#4682B4',
    'tan':                  '#D2B48C',
    'teal':                 '#008080',
    'thistle':              '#D8BFD8',
    'tomato':               '#FF6347',
    'turquoise':            '#40E0D0',
    'violet':               '#EE82EE',
    'wheat':                '#F5DEB3',
    'white':                '#FFFFFF',
    'whitesmoke':           '#F5F5F5',
    'yellow':               '#FFFF00',
    'yellowgreen':          '#9ACD32',
    'r':                    '#FF0000',
    'g':                    '#008000',
    'b':                    '#0000FF',
    'c':                    '#00FFFF',
    'm':                    '#FF00FF',
    'y':                    '#FFFF00',
    'w':                    '#FFFFFF',
    'k':                    '#000000',
    }

_schemes = {'BuGn': ['#EDF8FB', '#CCECE6', '#CCECE6',
                    '#66C2A4', '#41AE76', '#238B45', '#005824'],
           'BuPu': ['#EDF8FB', '#BFD3E6', '#9EBCDA',
                    '#8C96C6', '#8C6BB1', '#88419D', '#6E016B'],
           'GnBu': ['#F0F9E8', '#CCEBC5', '#A8DDB5',
                    '#7BCCC4', '#4EB3D3', '#2B8CBE', '#08589E'],
           'OrRd': ['#FEF0D9', '#FDD49E', '#FDBB84',
                    '#FC8D59', '#EF6548', '#D7301F', '#990000'],
           'PuBu': ['#F1EEF6', '#D0D1E6', '#A6BDDB',
                    '#74A9CF', '#3690C0', '#0570B0', '#034E7B'],
           'PuBuGn': ['#F6EFF7', '#D0D1E6', '#A6BDDB',
                      '#67A9CF', '#3690C0', '#02818A', '#016450'],
           'PuRd': ['#F1EEF6', '#D4B9DA', '#C994C7',
                    '#DF65B0', '#E7298A', '#CE1256', '#91003F'],
           'RdPu': ['#FEEBE2', '#FCC5C0', '#FA9FB5',
                    '#F768A1', '#DD3497', '#AE017E', '#7A0177'],
           'YlGn': ['#FFFFCC', '#D9F0A3', '#ADDD8E',
                    '#78C679', '#41AB5D', '#238443', '#005A32'],
           'YlGnBu': ['#FFFFCC', '#C7E9B4', '#7FCDBB',
                      '#41B6C4', '#1D91C0', '#225EA8', '#0C2C84'],
           'YlOrBr': ['#FFFFD4', '#FEE391', '#FEC44F',
                      '#FE9929', '#EC7014', '#CC4C02', '#8C2D04'],
           'YlOrRd': ['#FFFFB2', '#FED976', '#FEB24C',
                      '#FD8D3C', '#FC4E2A', '#E31A1C', '#B10026'],
           'BrBg': ['#8c510a', '#d8b365', '#f6e8c3',
                    '#c7eae5', '#5ab4ac', '#01665e'],
           'PiYG': ['#c51b7d', '#e9a3c9', '#fde0ef',
                    '#e6f5d0', '#a1d76a', '#4d9221'],
           'PRGn': ['#762a83', '#af8dc3', '#e7d4e8',
                    '#d9f0d3', '#7fbf7b', '#1b7837'],
           'PuOr': ['#b35806', '#f1a340', '#fee0b6',
                    '#d8daeb', '#998ec3', '#542788'],
           'RdBu': ['#b2182b', '#ef8a62', '#fddbc7',
                    '#d1e5f0', '#67a9cf', '#2166ac'],
           'RdGy': ['#b2182b', '#ef8a62', '#fddbc7',
                    '#e0e0e0', '#999999', '#4d4d4d'],
           'RdYlBu': ['#d73027', '#fc8d59', '#fee090',
                      '#e0f3f8', '#91bfdb', '#4575b4'],
           'RdYlGn': ['#d73027', '#fc8d59', '#fee08b',
                      '#d9ef8b', '#91cf60', '#1a9850'],
           'Spectral': ['#d53e4f', '#fc8d59', '#fee08b',
                        '#e6f598', '#99d594', '#3288bd'],
           'Accent': ['#7fc97f', '#beaed4', '#fdc086',
                      '#ffff99', '#386cb0', '#f0027f'],
           'Dark2': ['#1b9e77', '#d95f02', '#7570b3',
                     '#e7298a', '#66a61e', '#e6ab02'],
           'Paired': ['#a6cee3', '#1f78b4', '#b2df8a',
                      '#33a02c', '#fb9a99', '#e31a1c'],
           'Pastel1': ['#fbb4ae', '#b3cde3', '#ccebc5',
                       '#decbe4', '#fed9a6', '#ffffcc'],
           'Pastel2': ['#b3e2cd', '#fdcdac', '#cbd5e8',
                       '#f4cae4', '#e6f5c9', '#fff2ae'],
           'Set1': ['#e41a1c', '#377eb8', '#4daf4a',
                    '#984ea3', '#ff7f00', '#ffff33'],
           'Set2': ['#66c2a5', '#fc8d62', '#8da0cb',
                    '#e78ac3', '#a6d854', '#ffd92f'],
           'Set3': ['#8dd3c7', '#ffffb3', '#bebada',
                    '#fb8072', '#80b1d3', '#fdb462'],
          }

def _parse_color(x):
    """
    """
    if isinstance(x, tuple) or isinstance(x, list):
        color_tuple = tuple(x)[:4]
    elif isinstance(x, text_type) or isinstance(x, binary_type):
        if x[0]=="#" and len(x)==7:
            # Color of the for #RRGGBB
            color_tuple = (int(x[1:3],16), int(x[3:5],16), int(x[5:7],16))
        else:
            color_code = _cnames.get(x.lower(),None)
            if color_code is None:
                raise ValueError('Unknown color.')
            color_tuple = (int(color_code[1:3],16), int(color_code[3:5],16), int(color_code[5:7],16))
    if max(color_tuple)>1.:
        color_tuple = tuple(u/255. for u in color_tuple)
    return tuple(map(float,(color_tuple+(1.,))[:4]))

class ColorMap(object):
    """A generic class for creating colormaps."""

    def __init__(self, min=0., max=1.):
        self.min = min
        self.max = max

    def _rgba_floats_tuple(self, x):
        """This class has to be implemented for each class inheriting from Colormap.
        This has to be a function of the form float -> (float,float,float,float)
        Describing for each input float x, the output color in RGBA format ;
        each output value being between 0 and 1.
        """
        raise NotImplementedError

    def rgba_floats_tuple(self, x):
        """Provides the color corresponding to value `x` in the
        form of a tuple (R,G,B,A) with float values between 0. and 1.
        """
        return self._rgba_floats_tuple(x)

    def rgba_bytes_tuple(self, x):
        """Provides the color corresponding to value `x` in the
        form of a tuple (R,G,B,A) with int values between 0 and 255.
        """
        return tuple(int(u*255.9999) for u in self.rgba_floats_tuple(x))

    def rgb_bytes_tuple(self, x):
        """Provides the color corresponding to value `x` in the
        form of a tuple (R,G,B) with int values between 0 and 255.
        """
        return self.rgba_bytes_tuple(x)[:3]

    def rgb_hex_str(self, x):
        """Provides the color corresponding to value `x` in the
        form of a string of hewadecimal values "#RRGGBB".
        """
        return "#%02x%02x%02x" % self.rgb_bytes_tuple(x)

    def __call__(self, x):
        """Provides the color corresponding to value `x` in the
        form of a string of hewadecimal values "#RRGGBB".
        """
        return self.rgb_hex_str(x)

    def _repr_html_(self):
        return (
            '<svg height="50" width="500">'
            + ''.join(
                [(
                    '<line x1="{i}" y1="0" x2="{i}" '
                    'y2="20" style="stroke:{color};stroke-width:3;" />'
                    ).format(
                        i=i*1,
                        color = self.rgb_hex_str(self.min + (self.max-self.min)*i/499.))
                    for i in range(500)
                    ])
            + '<text x="0" y="35">{}</text>'.format(self.min)
            + '<text x="500" y="35" style="text-anchor:end;">{}</text>'.format(self.max)
            + '</svg>')

class LinearColormap(ColorMap):
    def __init__(self, colors, index=None, min=0., max=1.):
        """Creates a ColorMap based on linear interpolation of a set of colors
        over a given index.
        
        Parameters
        ----------
        colors : list-like object
            The set of colors to be used for interpolation.
            Colors can be provided in the form:
            * tuples of int between 0 and 255 (e.g: `(255,255,0)` or `(255,255,0,255)`)
            * tuples of floats between 0. and 1. (e.g: `(1.,1.,0.)` or `(1.,1.,0.,1.)`)
            * HTML-like string (e.g: `"#ffff00`)
            * a color name or shortcut (e.g: `"y"` or `"yellow"`)
        index : list of floats, default None
            The values corresponding to each color.
            It has to be sorted, and have the same length as `colors`.
            If None, a regular grid between `min` and `max` is created.
        min : float, default 0.
            The minimal value for the colormap.
            Values lower than `min` will be bound directly to `colors[0]`.
        max : float, default 1.
            The maximal value for the colormap.
            Values higher than `max` will be bound directly to `colors[-1]`.
        """
        n = len(colors)
        if n<2:
            raise ValueError('You must provide at least 2 colors.')
        if index is None:
            self.index = [min + (max-min)*i*1./(n-1) for i in range(n)]
        else:
            self.index = list(index).copy()
        self.colors = [_parse_color(x) for x in colors]
        self.min = min
        self.max = max

    def _rgba_floats_tuple(self, x):
        """Provides the color corresponding to value `x` in the
        form of a tuple (R,G,B,A) with float values between 0. and 1.
        """
        if x<= self.index[0]:
            return self.colors[0]
        if x>= self.index[-1]:
            return self.colors[-1]

        i = len([u for u in self.index if u<x]) # 0 < i < n
        if self.index[i-1] < self.index[i]:
            p = (x - self.index[i-1])*1./(self.index[i]-self.index[i-1])
        elif self.index[i-1] == self.index[i]:
            p = 1.
        else:
            raise ValueError('Thresholds are not sorted.')
        
        return tuple((1.-p) * self.colors[i-1][j] + p*self.colors[i][j] for j in range(4))

    def to_step(self, n=None, index=None):
        """Splits the LinearColormap into a StepColormap.

        Parameters
        ----------
        n : int, default None
            The number of expected colors in the ouput StepColormap.
            This will be ignored if `index` is provided.
        index : list of floats, default None
            The values corresponding to each color bounds.
            It has to be sorted.
            If None, a regular grid between `min` and `max` is created.

        Return
        ------
        A StepColormap with `n=len(index)-1` colors.
        """
        if index is None:
            if n is None:
                raise ValueError('You must specify either `index` or `n`')
            index = [self.min + (self.max-self.min)*i*1./n for i in range(1+n)]

        n = len(index)-1

        colors = [self._rgba_floats_tuple(index[i]*(1.-i/(n-1.))+index[i+1]*i/(n-1.)) for i in range(n)]

        return StepColormap(colors, index=index, min=self.min, max=self.max)

    def scale(self, min=0., max=1.):
        """Transforms the colorscale so that the minimal and maximal values
        fit the given parameters.
        """
        return LinearColormap(
            self.colors,
            index = [min + (max-min)*(x-self.min)*1./(self.max-self.min) for x in self.index],
            min = min,
            max = max,
            )

class StepColormap(ColorMap):
    def __init__(self, colors, index=None, min=0., max=1.):
        """Creates a ColorMap based on stepwise constant colorfunction.

        Parameters
        ----------
        colors : list-like object
            The set of colors to be used.
            Colors can be provided in the form:
            * tuples of int between 0 and 255 (e.g: `(255,255,0)` or `(255,255,0,255)`)
            * tuples of floats between 0. and 1. (e.g: `(1.,1.,0.)` or `(1.,1.,0.,1.)`)
            * HTML-like string (e.g: `"#ffff00`)
            * a color name or shortcut (e.g: `"y"` or `"yellow"`)
        index : list of floats, default None
            The values corresponding to each color.
            It has to be sorted, and its length must be equal to `len(colors)+1`.
            If None, a regular grid between `min` and `max` is created.
        min : float, default 0.
            The minimal value for the colormap.
            Values lower than `min` will be bound directly to `colors[0]`.
        max : float, default 1.
            The maximal value for the colormap.
            Values higher than `max` will be bound directly to `colors[-1]`.
        """
        n = len(colors)
        if n<1:
            raise ValueError('You must provide at least 1 colors.')
        if index is None:
            self.index = [min + (max-min)*i*1./n for i in range(n+1)]
        else:
            self.index = list(index).copy()
        self.colors = [_parse_color(x) for x in colors]
        self.min = min
        self.max = max

    def _rgba_floats_tuple(self, x):
        """Provides the color corresponding to value `x` in the
        form of a tuple (R,G,B,A) with float values between 0. and 1.
        """
        if x<= self.index[0]:
            return self.colors[0]
        if x>= self.index[-1]:
            return self.colors[-1]

        i = len([u for u in self.index if u<x]) # 0 < i < n
        return tuple(self.colors[i-1])

    def to_linear(self, index=None):
        """Transforms the StepColormap into a LinearColormap.

        Parameters
        ----------
        index : list of floats, default None
                The values corresponding to each color in the output colormap.
                It has to be sorted.
                If None, a regular grid between `min` and `max` is created.
        """
        if index is None:
            n = len(self.index)-1
            index = [self.index[i]*(1.-i/(n-1.))+self.index[i+1]*i/(n-1.) for i in range(n)]

        colors = [self._rgba_floats_tuple(x) for x in index]
        return LinearColormap(colors, index=index, min=self.min, max=self.max)

    def scale(self, min=0., max=1.):
        """Transforms the colorscale so that the minimal and maximal values
        fit the given parameters.
        """
        return StepColormap(
            self.colors,
            index = [min + (max-min)*(x-self.min)*1./(self.max-self.min) for x in self.index],
            min = min,
            max = max,
            )

class _LinearColormaps(object):
    """A class for hosting the list of built-in linear colormaps.
    """
    def __init__(self):
        self._schemes = _schemes.copy()
        self._colormaps = {key : LinearColormap(val) for key,val in _schemes.items()}
        for key,val in _schemes.items():
            setattr(self,key, LinearColormap(val))
    def _repr_html_(self):
        return Template("""
        <table>
        {% for key,val in this._colormaps.items() %}
        <tr><td>{{key}}</td><td>{{val._repr_html_()}}</td></tr>
        {% endfor %}</table>
        """).render(this=self)

linear = _LinearColormaps()
