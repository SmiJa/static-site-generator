class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError
  
  def props_to_html(self):
    prop_string_list = []
    for prop in self.props:
      prop_string_list.append(f'{prop}="{self.props[prop]}"')
    prop_string = " ".join(prop_string_list)
    return prop_string
  
  def __eq__(self, other):
    if isinstance(other, HTMLNode):
      return (self.tag == other.tag and
              self.value == other.value and
              self.children == other.children and
              self.props == other.props)
    return False
  
  def __repr__(self):
    print(f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}")