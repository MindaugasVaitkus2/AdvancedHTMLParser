# Copyright (c) 2015, 2017 Tim Savannah under LGPLv3. 
#  See LICENSE (https://gnu.org/licenses/lgpl-3.0.txt) for more information.
#   Constants in AdvancedHTMLParser

from .conversions import convertToIntOrNegativeOneIfUnset

# These tags are always self-closing, whether given that way or not.
IMPLICIT_SELF_CLOSING_TAGS = set(['meta', 'link', 'input', 'img', 'hr', 'br'])

# These tags have preformatted content and will not be modified at all
PREFORMATTED_TAGS = set(['pre', 'code'])

# These tags will not have content modified, except for first-and-last line indentation
PRESERVE_CONTENTS_TAGS = set(['script', 'pre', 'code', 'style'])

# Tag name for a "transparent" root node. Used if there are multiple nodes at root level as an internal placeholder.
#  I.E. an inomplete page, or an ajax request. @see Parser.AdvancedHTMLParser.getRootNodes
INVISIBLE_ROOT_TAG = 'xxxblank'

# Start tag used on invisible root tag
INVISIBLE_ROOT_TAG_START = '<%s>' %(INVISIBLE_ROOT_TAG,)
# End tag used on invisible root tag
INVISIBLE_ROOT_TAG_END = '</%s>' %(INVISIBLE_ROOT_TAG,)

# Tag names with attributes that are not common to all, but exist on certain elements
TAG_NAMES_TO_ADDITIONAL_ATTRIBUTES = { 
    'input' : {'checked', 'onsearch', 'onchange', 'oncontextmenu', 'oninput', 'oninvalid', 'onreset', 'onselect'},
    'option': {'selected', },
    'body'  : {'bgcolor', 'background', 'vlink', 'alink', 'link', 'onafterprint', 'onbeforeprint', 'onbeforeunload', 'onerror', 'onhashchange', 'onload', 'onmessage', \
                'onoffline', 'ononline', 'onpagehide', 'onpageshow', 'onpopstate', 'onresize', 'onstorage', 'onunload'},
    'form'  : {'onblur', 'onchange', 'oncontextmenu', 'onfocus', 'oninput', 'oninvalid', 'onreset', 'onsearch', 'onselect', 'onsubmit'},
    'menu'  : {'onshow', },
    'a'     : {'href', 'target', },
    'details' : {'ontoggle', },
    'img'   : {'src', 'height', 'width'}
}

# These all inherit the special attributes from input
for otherInputName in ('button', 'select', 'option'):
    if otherInputName not in TAG_NAMES_TO_ADDITIONAL_ATTRIBUTES:
        TAG_NAMES_TO_ADDITIONAL_ATTRIBUTES[otherInputName] = TAG_NAMES_TO_ADDITIONAL_ATTRIBUTES['input']
    else:
        TAG_NAMES_TO_ADDITIONAL_ATTRIBUTES[otherInputName].update(TAG_NAMES_TO_ADDITIONAL_ATTRIBUTES['input'])

# Inherits special attributes from input plus onsubmit
TAG_NAMES_TO_ADDITIONAL_ATTRIBUTES['submit'] = TAG_NAMES_TO_ADDITIONAL_ATTRIBUTES['input'].union('onsubmit')

# Javascript attributes common to all elements
COMMON_JAVASCRIPT_ATTRIBUTES = { 'onkeydown', 'onkeyup', 'onkeypress', 'onfocus', 'onblur', 'onselect', 'oncontextmenu', \
                                    'onclick', 'ondblclick', 'onmousedown', 'onmousemove', 'onmouseout', 'onmouseover', \
                                    'onmouseup', 'onmousewheel', 'onwheel', 'oncopy', 'onpaste', 'oncut', \
                                    'ondrag', 'ondragend', 'ondragenter', 'ondragleave', 'ondragover', 'ondragstop', 'ondrop', 'onscroll',
                                    'onchange', 
}

# All javascript attributes known by AdvancedHTMLParser
ALL_JAVASCRIPT_EVENT_ATTRIBUTES = COMMON_JAVASCRIPT_ATTRIBUTES.union( 
    set([value for values in TAG_NAMES_TO_ADDITIONAL_ATTRIBUTES.values() for value in values if value.startswith('on')]) 
)

# object-access that link directly to an attribute on the tag
TAG_ITEM_ATTRIBUTE_LINKS = { 'id', 'name', 'title', 'dir', 'align', 'tabIndex', 'value', 'className', 
    'hidden', 'spellcheck' }

# Add all javascript event attributes
TAG_ITEM_ATTRIBUTE_LINKS.update(COMMON_JAVASCRIPT_ATTRIBUTES)

# These attributes have a different object-access than their name
TAG_ITEM_CHANGE_NAME_FROM_ITEM = {
    'tabIndex' : 'tabindex',
    'className' : 'class',
}

# These attributes are binary (only accept true/false)
TAG_ITEM_BINARY_ATTRIBUTES = { 'hidden', 'checked', 'selected', }

# These attributes are binary for dot-access, but have the value "true" or "false" in the HTML representation
TAG_ITEM_BINARY_ATTRIBUTES_STRING_ATTR = { 'spellcheck', }

# The opposite of TAG_ITEM_CHANGE_NAME_FROM_ITEM, for going from the attribute name to the object-access name
TAG_ITEM_CHANGE_NAME_FROM_ATTR = { val : key for key, val in TAG_ITEM_CHANGE_NAME_FROM_ITEM.items() }

# These attributes can have a special value
TAG_ITEM_ATTRIBUTES_SPECIAL_VALUES = {
    'tabIndex' : lambda em : convertToIntOrNegativeOneIfUnset(em.getAttribute('tabindex', None)),
}

