class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
    
    def __repr__(self):
        return f"<{self.tag} {self.props_to_html()} {"value='"+self.value+"'" if self.value is not None else ""}'>{self.children}</{self.tag}>"