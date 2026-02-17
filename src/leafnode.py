from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("invalid HTML: no value")
        if not self.tag:
            return self.value
        else:
            res = (f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>")
            return res

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"